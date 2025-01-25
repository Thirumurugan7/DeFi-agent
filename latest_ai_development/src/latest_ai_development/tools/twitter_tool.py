from crewai.tools import BaseTool
import tweepy
import re
from typing import Optional, List, Dict, Any, Type
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

load_dotenv()

class TwitterTool(BaseTool):
    name: str = "Twitter ETH Address Monitor"
    description: str = "Monitors Twitter mentions for ETH addresses"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._initialize_client()

    def _initialize_client(self):
        """Initialize Twitter API client"""
        try:
            print("Initializing Twitter client...")
            self._client = tweepy.Client(
                bearer_token=os.getenv('TWITTER_BEARER_TOKEN'),
                consumer_key=os.getenv('TWITTER_API_KEY'),
                consumer_secret=os.getenv('TWITTER_API_SECRET'),
                access_token=os.getenv('TWITTER_ACCESS_TOKEN'),
                access_token_secret=os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
            )
            print("Twitter client initialized successfully")
        except Exception as e:
            print(f"Error initializing Twitter client: {str(e)}")
            raise

    @property
    def client(self):
        """Getter for Twitter client"""
        if not hasattr(self, '_client'):
            self._initialize_client()
        return self._client

    def _get_user_id(self, username: str) -> Optional[str]:
        """Get Twitter user ID from username."""
        try:
            if username.startswith('@'):
                username = username[1:]
            print(f"Getting user ID for {username}")
            user = self.client.get_user(username=username)
            return user.data.id if user.data else None
        except Exception as e:
            print(f"Error getting user ID: {str(e)}")
            return None

    def _extract_eth_addresses(self, text: str) -> List[str]:
        """Extract all ETH addresses from text."""
        pattern = r'0x[a-fA-F0-9]{40}'
        addresses = re.findall(pattern, text)
        print(f"Found {len(addresses)} ETH addresses in text")
        return addresses

    def _run(self, target_account: str = None, hours_ago: int = 24) -> List[dict]:
        """Run the tool with parameters."""
        try:
            print(f"Processing mentions for {target_account} from last {hours_ago} hours")

            if not target_account:
                return {"error": "Target account is required"}

            # Get target account ID
            account_id = self._get_user_id(target_account)
            if not account_id:
                return {"error": f"Account {target_account} not found"}

            print(f"Found account ID: {account_id}")

            # Calculate start time
            start_time = datetime.utcnow() - timedelta(hours=hours_ago)

            # Search for tweets mentioning the account
            print("Searching for mentions...")
            query = f"@{target_account.replace('@', '')}"
            mentions = self.client.search_recent_tweets(
                query=query,
                start_time=start_time,
                max_results=100,
                tweet_fields=['author_id', 'created_at', 'text']
            )

            results = []
            if mentions and mentions.data:
                print(f"Found {len(mentions.data)} mentions")
                for tweet in mentions.data:
                    addresses = self._extract_eth_addresses(tweet.text)
                    if addresses:
                        results.append({
                            'tweet_id': tweet.id,
                            'author_id': tweet.author_id,
                            'text': tweet.text,
                            'eth_addresses': addresses,
                            'created_at': tweet.created_at
                        })
                print(f"Found {len(results)} tweets with ETH addresses")
            else:
                print("No mentions found")

            return results if results else {"error": "No ETH addresses found in mentions"}

        except Exception as e:
            print(f"Error in TwitterTool._run: {str(e)}")
            return {"error": str(e)} 