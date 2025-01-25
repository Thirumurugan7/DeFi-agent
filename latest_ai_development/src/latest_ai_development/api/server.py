from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from ..crew import TokenTransferCrew
from ..tools.twitter_tool import TwitterTool

app = FastAPI()

class MonitorRequest(BaseModel):
    target_account: str
    hours_ago: int = 24
    amount_per_address: float

class TransferResponse(BaseModel):
    status: str
    message: str
    transfers: List[dict] = []

@app.post("/monitor/mentions", response_model=TransferResponse)
async def process_mentions(request: MonitorRequest):
    try:
        # Get mentions with ETH addresses
        twitter_tool = TwitterTool()
        mentions = twitter_tool._run(
            target_account=request.target_account,
            hours_ago=request.hours_ago
        )

        if isinstance(mentions, dict) and 'error' in mentions:
            raise HTTPException(status_code=400, detail=mentions['error'])

        if not mentions:
            return TransferResponse(
                status="success",
                message="No new mentions with ETH addresses found",
                transfers=[]
            )

        # Process transfers
        transfers = []
        for mention in mentions:
            for address in mention['eth_addresses']:
                try:
                    # Initialize transfer crew with inputs
                    inputs = {
                        'amount': request.amount_per_address,
                        'recipient': address
                    }
                    
                    # Execute transfer
                    result = TokenTransferCrew().crew().kickoff(inputs=inputs)
                    
                    transfers.append({
                        'tweet_id': mention['tweet_id'],
                        'address': address,
                        'amount': request.amount_per_address,
                        'status': 'success',
                        'transaction_hash': result.get('transaction_hash')
                    })
                except Exception as e:
                    transfers.append({
                        'tweet_id': mention['tweet_id'],
                        'address': address,
                        'amount': request.amount_per_address,
                        'status': 'failed',
                        'error': str(e)
                    })

        return TransferResponse(
            status="success",
            message=f"Processed {len(transfers)} transfers",
            transfers=transfers
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Optional: Add endpoint to check specific tweet
@app.get("/check/tweet/{tweet_id}")
async def check_tweet(tweet_id: str):
    twitter_tool = TwitterTool()
    tweet = twitter_tool.client.get_tweet(tweet_id)
    addresses = twitter_tool._extract_eth_addresses(tweet.data.text)
    return {"addresses": addresses} 