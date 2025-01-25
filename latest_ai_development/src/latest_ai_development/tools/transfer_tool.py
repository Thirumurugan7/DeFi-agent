from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from ..utils.blockchain import EVMBlockchain

class TransferToolInput(BaseModel):
    """Input schema for TransferTool."""
    recipient: str = Field(..., description="Recipient address for the transfer")
    amount: float = Field(..., description="Amount of ETH to transfer")

class TransferTool(BaseTool):
    name: str = "ETH Transfer Tool"
    description: str = (
        "A tool for executing ETH transfers on Sepolia network to specified recipients"
    )
    args_schema: Type[BaseModel] = TransferToolInput

    def _run(self, argument: str = None, recipient: str = None, amount: float = None) -> str:
        """Execute the transfer with proper error handling"""
        try:
            blockchain = EVMBlockchain()
            
            # Parse arguments if provided as JSON string
            if argument and not (recipient and amount):
                import json
                try:
                    params = json.loads(argument)
                    recipient = params.get('recipient')
                    amount = float(params.get('amount'))
                except json.JSONDecodeError:
                    return "Transfer failed: Invalid JSON input format"
                except ValueError:
                    return "Transfer failed: Invalid amount format"

            # Validate inputs
            if not recipient or not amount:
                return "Transfer failed: Missing recipient address or amount"

            # Validate recipient address
            if not blockchain.validate_address(recipient):
                return "Transfer failed: Invalid recipient address"

            # Validate sender has sufficient balance
            sender_balance = blockchain.get_balance(blockchain.account.address)
            if sender_balance < amount:
                return f"Transfer failed: Insufficient balance. Available: {sender_balance} ETH"

            # Execute transfer
            result = blockchain.transfer_eth(recipient, amount)
            
            if result['status'] == 'success':
                return (
                    f"Transfer successful!\n"
                    f"Transaction Hash: {result['transaction_hash']}\n"
                    f"Amount: {result['amount']} ETH\n"
                    f"From: {result['from']}\n"
                    f"To: {result['to']}\n"
                    f"Block Number: {result['block_number']}"
                )
            else:
                return f"Transfer failed: {result['error']}"
                
        except Exception as e:
            return f"Transfer failed: {str(e)}"