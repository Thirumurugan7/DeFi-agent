# LatestAiDevelopment Crew

Welcome to the LatestAiDevelopment Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/latest_ai_development/config/agents.yaml` to define your agents
- Modify `src/latest_ai_development/config/tasks.yaml` to define your tasks
- Modify `src/latest_ai_development/crew.py` to add your own logic, tools and specific args
- Modify `src/latest_ai_development/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the latest-ai-development Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The latest-ai-development Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the LatestAiDevelopment Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.



# Ethereum Transfer Agent System

A sophisticated AI-powered Ethereum transfer system built with CrewAI that enables secure and validated ETH transfers on the Sepolia testnet, with Twitter integration for automated transfers to addresses mentioned in tweets.

## Overview

This application uses a multi-agent system to handle Ethereum transfers with built-in validation and security checks, plus Twitter monitoring capabilities. It consists of:

1. **Validator Agent**: Performs pre-transfer validation checks
   - Address validation
   - Amount reasonability
   - Balance verification
   - Security compliance

2. **Transfer Agent**: Executes the validated transfers
   - Secure transaction signing
   - Gas optimization
   - Transaction monitoring
   - Detailed reporting

3. **Twitter Monitor**: Monitors Twitter for ETH addresses
   - Tracks mentions of specified account
   - Extracts ETH addresses from tweets
   - Triggers automatic transfers

## Features

- 🔒 Secure ETH transfers on Sepolia testnet
- ✅ Multi-step validation process
- 💡 Intelligent transfer amount verification
- 📊 Detailed transaction reporting
- 🐦 Twitter integration for automated transfers
- ⚡ Gas optimization
- 🔍 Comprehensive error handling

## Prerequisites

- Python >=3.10, <3.13
- Sepolia testnet ETH
- Alchemy/Infura API key
- Ethereum wallet private key
- Twitter API credentials

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd latest_ai_development
```

2. Install dependencies:
```bash
pip install -e .
```

3. Configure environment variables in `.env`:
```bash
# Blockchain Configuration
SEPOLIA_RPC_URL=https://sepolia.infura.io/v3/YOUR_INFURA_PROJECT_ID
PRIVATE_KEY=0x...

# Twitter API Configuration
TWITTER_API_KEY=your-twitter-api-key
TWITTER_API_SECRET=your-twitter-api-secret
TWITTER_BEARER_TOKEN=your-twitter-bearer-token
TWITTER_ACCESS_TOKEN=your-twitter-access-token
TWITTER_ACCESS_TOKEN_SECRET=your-twitter-access-token-secret

# Monitoring Configuration
MONITOR_ACCOUNT=@YourTwitterHandle
TRANSFER_AMOUNT=0.01
MONITOR_INTERVAL_MINUTES=15
```

## Usage

### Direct Transfer

1. Configure transfer details in `main.py`:
```python
inputs = {
    'amount': 0.01,  # Amount in ETH
    'recipient': '0x...'  # Recipient address
}
```

2. Run the transfer:
```bash
python main.py
```

### Twitter Monitoring Service

Run the monitoring service that automatically processes transfers from Twitter mentions:

```bash
# Run the complete service (API + Monitor)
python -m latest_ai_development.scripts.run_service
```

Or run components separately:

```bash
# Run just the API server
uvicorn latest_ai_development.api.server:app --reload --host 0.0.0.0 --port 8000

# Run just the monitor in another terminal
python -m latest_ai_development.scripts.monitor
```

### API Endpoints

Test the API directly:

```bash
# Monitor mentions and process transfers
curl -X POST "http://localhost:8000/monitor/mentions" \
     -H "Content-Type: application/json" \
     -d '{
           "target_account": "@YourTwitterHandle",
           "hours_ago": 24,
           "amount_per_address": 0.01
         }'

# Check specific tweet
curl "http://localhost:8000/check/tweet/1234567890"
```

## Twitter Integration

The system monitors mentions of your Twitter account and processes ETH transfers automatically:

1. Users mention your account with an ETH address
2. System detects the mention and extracts the address
3. Validates the address and initiates transfer
4. Reports transfer status

Example tweet that triggers a transfer:
```
@YourTwitterHandle Here's my ETH address: 0x742d35Cc6634C0532925a3b844Bc454e4438f44e
```

## Development

To extend or modify the system:

1. Add new agents in `config/agents.yaml`
2. Define new tasks in `config/tasks.yaml`
3. Implement new tools in `tools/`
4. Modify blockchain utils in `utils/blockchain.py`

## Testing

Run on Sepolia testnet first:
1. Get test ETH from Sepolia faucet
2. Use test addresses for initial transfers
3. Verify transaction success on Sepolia block explorer

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Create a Pull Request

