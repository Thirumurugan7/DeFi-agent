import time
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import os
from dotenv import load_dotenv

load_dotenv()

def create_session():
    """Create a requests session with retries"""
    session = requests.Session()
    retries = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=[500, 502, 503, 504]
    )
    session.mount('http://', HTTPAdapter(max_retries=retries))
    return session

def monitor_mentions(interval_minutes=15):
    """
    Continuously monitor mentions and process transfers
    """
    session = create_session()
    
    while True:
        try:
            print("\nChecking for new mentions...")
            response = session.post(
                "http://localhost:8000/monitor/mentions",
                json={
                    "target_account": os.getenv('MONITOR_ACCOUNT'),
                    "hours_ago": 1,  # Check last hour
                    "amount_per_address": float(os.getenv('TRANSFER_AMOUNT'))
                },
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                print(f"Processed {len(result['transfers'])} transfers")
                for transfer in result['transfers']:
                    print(f"Transfer to {transfer['address']}: {transfer['status']}")
            else:
                print(f"Error response: {response.status_code} - {response.text}")
            
        except requests.exceptions.ConnectionError:
            print("Connection error. Waiting for API server to be available...")
            time.sleep(5)
            continue
        except Exception as e:
            print(f"Error in monitoring: {e}")
        
        print(f"Waiting {interval_minutes} minutes before next check...")
        time.sleep(interval_minutes * 60)

if __name__ == "__main__":
    monitor_mentions() 