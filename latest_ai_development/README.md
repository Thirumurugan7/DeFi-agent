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

A sophisticated AI-powered Ethereum transfer system built with CrewAI that enables secure and validated ETH transfers on the Sepolia testnet.

## Overview

This application uses a multi-agent system to handle Ethereum transfers with built-in validation and security checks. It consists of two specialized AI agents:

1. **Validator Agent**: Performs pre-transfer validation checks including:
   - Address validation
   - Amount reasonability
   - Balance verification
   - Security compliance

2. **Transfer Agent**: Executes the validated transfers with:
   - Secure transaction signing
   - Gas optimization
   - Transaction monitoring
   - Detailed reporting

## Features

- 🔒 Secure ETH transfers on Sepolia testnet
- ✅ Multi-step validation process
- 💡 Intelligent transfer amount verification
- 📊 Detailed transaction reporting
- ⚡ Gas optimization
- 🔍 Comprehensive error handling

## Prerequisites

- Python >=3.10, <3.13
- Sepolia testnet ETH
- Alchemy API key
- Ethereum wallet private key

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
SEPOLIA_RPC_URL=https://sepolia.infura.io/v3/YOUR_INFURA_PROJECT_ID
PRIVATE_KEY=0x...
```


## Usage

1. Configure transfer details in `main.py`:

```bash
python main.py
```

inputs = {
'amount': 0.01, # Amount in ETH
'recipient': '0x...' # Recipient address
}



2. Run the crew:

```bash
crewai run
```



## System Architecture

### Components

1. **CrewAI Framework**
   - Manages agent interactions
   - Handles task sequencing
   - Provides tool integration

2. **Blockchain Utils**
   - Web3 integration
   - Transaction management
   - Address validation

3. **Transfer Tool**
   - Transaction execution
   - Error handling
   - Result formatting

### Workflow

1. User initiates transfer request
2. Validator agent performs checks
3. Transfer agent executes validated transaction
4. System provides detailed transaction report

## Security Features

- Private key safety through environment variables
- Address validation
- Balance checks
- Transaction amount validation
- Sepolia testnet support for safe testing

## Configuration

### Agents (`config/agents.yaml`)
- Validator agent configuration
- Transfer agent configuration

### Tasks (`config/tasks.yaml`)
- Transfer validation task
- Transfer execution task

## Error Handling

The system includes comprehensive error handling for:
- Invalid addresses
- Insufficient balances
- Network issues
- Transaction failures
- Invalid inputs

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

