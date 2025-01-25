from web3 import Web3
from eth_account import Account
import os
from dotenv import load_dotenv
from eth_account.signers.local import LocalAccount
from web3.middleware import construct_sign_and_send_raw_middleware

load_dotenv()

class EVMBlockchain:
    def __init__(self):
        # Initialize Web3
        self.w3 = Web3(Web3.HTTPProvider(os.getenv('SEPOLIA_RPC_URL')))
        
        # Set up account
        self.private_key = os.getenv('PRIVATE_KEY')
        if not self.private_key.startswith('0x'):
            self.private_key = '0x' + self.private_key
            
        self.account: LocalAccount = Account.from_key(self.private_key)
        
        # Add middleware
        self.w3.middleware_onion.add(construct_sign_and_send_raw_middleware(self.account))
        
        # Print debug info
        print(f"Connected to network: {self.w3.is_connected()}")
        print(f"Account address: {self.account.address}")
        
    def validate_address(self, address: str) -> bool:
        """Validate if the address is a valid Ethereum address"""
        return self.w3.is_address(address)
    
    def get_balance(self, address: str) -> float:
        """Get balance of an address in ETH"""
        balance_wei = self.w3.eth.get_balance(address)
        return float(self.w3.from_wei(balance_wei, 'ether'))
    
    def transfer_eth(self, to_address: str, amount_eth: float) -> dict:
        """
        Transfer ETH to specified address
        Returns transaction details
        """
        try:
            # Convert ETH to Wei
            amount_wei = self.w3.to_wei(amount_eth, 'ether')
            
            # Build transaction
            transaction = {
                'from': self.account.address,
                'to': to_address,
                'value': amount_wei,
                'nonce': self.w3.eth.get_transaction_count(self.account.address),
                'gas': 21000,
                'gasPrice': self.w3.eth.gas_price,
                'chainId': 11155111
            }
            
            # Estimate gas
            try:
                estimated_gas = self.w3.eth.estimate_gas(transaction)
                transaction['gas'] = estimated_gas
            except Exception as e:
                print(f"Gas estimation failed: {e}")
                # Keep default gas if estimation fails
            
            print(f"Sending transaction: {transaction}")
            
            # Sign and send transaction
            signed = self.account.sign_transaction(transaction)
            tx_hash = self.w3.eth.send_raw_transaction(signed.rawTransaction)
            print(f"Transaction sent: {tx_hash.hex()}")
            
            # Wait for receipt
            tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
            print(f"Transaction receipt: {tx_receipt}")
            
            return {
                'status': 'success',
                'transaction_hash': tx_receipt['transactionHash'].hex(),
                'from': tx_receipt['from'],
                'to': tx_receipt['to'],
                'amount': amount_eth,
                'block_number': tx_receipt['blockNumber']
            }
            
        except Exception as e:
            print(f"Transfer error: {str(e)}")
            return {
                'status': 'failed',
                'error': str(e)
            } 