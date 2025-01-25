#!/usr/bin/env python
# src/latest_ai_development/main.py
import sys
from latest_ai_development.crew import TokenTransferCrew

def run():
  """
  Run the transfer crew.
  """
  inputs = {
    'amount': 0.01,  # Amount in ETH
    'recipient': '0xcBAee4793486f3Df37dbb584F5a3610ff581A614'  # Recipient address
  }
  TokenTransferCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()
