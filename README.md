# Coding Agent

A production-ready AI coding agent that scrapes documentation, writes code, solves GitHub issues, and creates pull requests - all controlled via Slack.

## Overview

This agent combines Claude AI, LangChain, and GitHub API to provide an autonomous coding assistant that can:
- Scrape and analyze technical documentation
- Generate production-ready code from requirements
- Solve GitHub issues autonomously
- Create pull requests with code changes
- Interact via Slack commands for seamless workflow integration

## Features

- **AI-Powered Code Generation**: Uses Claude 3.5 Sonnet for intelligent code generation
- **Documentation Scraping**: Automatically scrapes and understands documentation using Firecrawl or BeautifulSoup
- **Issue Resolution**: Analyzes and solves GitHub issues with working solutions
- **PR Creation**: Automatically creates branches, commits code, and raises pull requests
- **Slack Integration**: Control everything via Slack commands for team collaboration
- **Fallback Mechanisms**: BeautifulSoup fallback when Firecrawl is unavailable

## Architecture

```
┌─────────────────┐
│  Slack Commands │
│  /scrape        │
│  /generate      │
│  /solve         │
└────────┬────────┘
         │
         v
┌─────────────────┐
│   Slack Bot     │
│  (slack_bot.py) │
└────────┬────────┘
         │
         v
┌─────────────────┐       ┌──────────────────┐
│  Coding Agent   │◄──────┤  Doc Scraper     │
│ (coding_agent)  │       │  (doc_scraper)   │
└────────┬────────┘       └──────────────────┘
         │
         v
┌─────────────────┐
│ GitHub Manager  │
│ (github_manager)│
└─────────────────┘
         │
         v
┌─────────────────┐
│  GitHub API     │
│  (Issues, PRs)  │
└─────────────────┘
```

## Tech Stack

- **LLM**: Anthropic Claude 3.5 Sonnet
- **Agent Framework**: LangChain
- **Slack**: Slack Bolt SDK (Socket Mode)
- **GitHub**: PyGithub
- **Web Scraping**: Firecrawl API / BeautifulSoup4
- **Language**: Python 3.12+

## Prerequisites

Before you begin, ensure you have:

1. **Python 3.12 or higher**
2. **Anthropic API key** - Get from [Anthropic Console](https://console.anthropic.com/)
3. **Slack workspace** with admin access
4. **GitHub personal access token** with repo permissions
5. **(Optional) Firecrawl API key** - Get from [Firecrawl](https://firecrawl.dev/)

## Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd coding-agent
```

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy the example environment file and fill in your credentials:

```bash
cp .env.example .env
```

Edit `.env` with your API keys:

```bash
# Required
ANTHROPIC_API_KEY=your_claude_api_key_here
SLACK_BOT_TOKEN=xoxb-your-bot-token
SLACK_APP_TOKEN=xapp-your-app-token
GITHUB_TOKEN=ghp_your_github_token
GITHUB_REPO_OWNER=your_github_username
GITHUB_REPO_NAME=your_repo_name

# Optional
FIRECRAWL_API_KEY=your_firecrawl_key
```

## Configuration

### Setting up Slack App

1. Go to [Slack API](https://api.slack.com/apps) and create a new app
2. Enable **Socket Mode** under Settings > Socket Mode
3. Create an **App-Level Token** with `connections:write` scope (this is your `SLACK_APP_TOKEN`)
4. Under **OAuth & Permissions**, add these Bot Token Scopes:
   - `chat:write`
   - `commands`
   - `app_mentions:read`
5. Install the app to your workspace (this generates your `SLACK_BOT_TOKEN`)
6. Under **Slash Commands**, create these commands:
   - `/scrape` - Description: "Scrape documentation from URL"
   - `/generate` - Description: "Generate code from requirements"
   - `/solve` - Description: "Solve a GitHub issue by number"

### Setting up GitHub Token

1. Go to GitHub Settings > Developer settings > Personal access tokens > Tokens (classic)
2. Generate new token with these scopes:
   - `repo` (Full control of private repositories)
   - `workflow` (Update GitHub Action workflows)
3. Copy the token to `GITHUB_TOKEN` in `.env`

### Setting up Anthropic API

1. Sign up at [Anthropic Console](https://console.anthropic.com/)
2. Create an API key
3. Copy to `ANTHROPIC_API_KEY` in `.env`

## Usage

### Running the Agent

Start the agent with:

```bash
python src/main.py
```

You should see:

```
Starting Coding Agent...
Coding agent initialized
GitHub manager initialized
Doc scraper initialized
Slack bot initialized
Slack bot is running!
```

### Slack Commands

Once running, use these commands in Slack:

#### 1. Scrape Documentation

```
/scrape https://docs.python.org/3/library/asyncio.html
```

Scrapes and stores documentation for later use.

#### 2. Generate Code

```
/generate Create a FastAPI endpoint that accepts JSON and returns processed data
```

Generates production-ready code based on your requirements.

#### 3. Solve GitHub Issue

```
/solve 42
```

Analyzes issue #42 in your configured repository and provides a solution.

### Testing Without Slack

Test the agent locally without Slack:

```bash
python test_agent.py
```

This will:
- Initialize the agent
- Test code generation
- Test documentation scraping

## Project Structure

```
coding-agent/
├── src/
│   ├── __init__.py
│   ├── main.py                 # Entry point
│   ├── agent/
│   │   ├── __init__.py
│   │   └── coding_agent.py     # Core AI agent logic
│   ├── slack/
│   │   ├── __init__.py
│   │   └── slack_bot.py        # Slack integration
│   ├── github/
│   │   ├── __init__.py
│   │   └── github_manager.py   # GitHub API wrapper
│   └── scraper/
│       ├── __init__.py
│       └── doc_scraper.py      # Documentation scraper
├── tests/                       # Unit tests
├── docs/                        # Additional documentation
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment template
├── .gitignore
├── test_agent.py               # Local testing script
└── README.md
```

## Module Documentation

### CodingAgent (`src/agent/coding_agent.py`)

Main AI agent using Claude 3.5 Sonnet.

**Methods:**
- `analyze_docs(docs: str, query: str) -> str`: Analyze documentation and answer queries
- `generate_code(requirements: str, context: Optional[str]) -> str`: Generate code from requirements
- `solve_issue(title: str, body: str, context: Optional[str]) -> dict`: Solve GitHub issues

### DocScraper (`src/scraper/doc_scraper.py`)

Documentation scraping with Firecrawl and BeautifulSoup fallback.

**Methods:**
- `scrape(url: str) -> str`: Scrape documentation from URL

### GitHubManager (`src/github/github_manager.py`)

GitHub API integration for repository operations.

**Methods:**
- `get_repo(owner, name)`: Get repository object
- `get_issue(issue_number)`: Get issue by number
- `create_pr(title, body, head_branch, base_branch)`: Create pull request
- `create_branch(branch_name, from_branch)`: Create new branch
- `update_file(file_path, content, message, branch)`: Update or create file

### SlackBot (`src/slack/slack_bot.py`)

Slack integration using Socket Mode.

**Commands:**
- `/scrape <url>`: Scrape documentation
- `/generate <requirements>`: Generate code
- `/solve <issue_number>`: Solve GitHub issue

## Deployment

### Option 1: AWS Lambda (Recommended for production)

1. Package the application:
```bash
pip install -t package -r requirements.txt
cd package && zip -r ../deployment.zip . && cd ..
zip -g deployment.zip src/ -r
```

2. Create Lambda function with Python 3.12 runtime
3. Upload `deployment.zip`
4. Set environment variables in Lambda configuration
5. Configure API Gateway or EventBridge for triggers

### Option 2: Railway

1. Install Railway CLI:
```bash
npm install -g @railway/cli
```

2. Login and deploy:
```bash
railway login
railway init
railway up
```

3. Set environment variables in Railway dashboard

### Option 3: Docker

```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ ./src/
COPY .env .

CMD ["python", "src/main.py"]
```

Build and run:
```bash
docker build -t coding-agent .
docker run --env-file .env coding-agent
```

## Troubleshooting

### Common Issues

**1. "ANTHROPIC_API_KEY not found"**
- Ensure `.env` file exists and contains valid API key
- Check that `python-dotenv` is installed

**2. "Slack bot not responding"**
- Verify Socket Mode is enabled in Slack app settings
- Check that both `SLACK_BOT_TOKEN` and `SLACK_APP_TOKEN` are set
- Ensure slash commands are registered in Slack app

**3. "GitHub authentication failed"**
- Verify GitHub token has correct permissions (`repo` scope)
- Check that `GITHUB_REPO_OWNER` and `GITHUB_REPO_NAME` are correct

**4. "Firecrawl API error"**
- Firecrawl is optional; agent will fallback to BeautifulSoup
- If you have a key, verify it's correct in `.env`

### Debug Mode

Enable verbose logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Development

### Running Tests

```bash
pytest tests/
```

### Code Style

Format code with:
```bash
black src/
```

Lint with:
```bash
pylint src/
```

## Limitations

- Slack Socket Mode requires persistent connection (not suitable for serverless without modifications)
- Claude API has rate limits (check Anthropic documentation)
- GitHub API has rate limits (5000 requests/hour for authenticated requests)
- Firecrawl free tier has usage limits

## Future Enhancements

- [ ] Add support for multiple repositories
- [ ] Implement code review capabilities
- [ ] Add unit test generation
- [ ] Support for more LLM providers (OpenAI, etc.)
- [ ] Web UI for non-Slack users
- [ ] Persistent conversation memory
- [ ] Multi-file code generation
- [ ] Automated PR reviews

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

MIT License - see LICENSE file for details

## Acknowledgments

- Built with [Anthropic Claude](https://www.anthropic.com/)
- Powered by [LangChain](https://www.langchain.com/)
- Slack integration via [Bolt SDK](https://slack.dev/bolt-python/)
- GitHub API via [PyGithub](https://github.com/PyGithub/PyGithub)

## Support

For issues and questions:
- Open an issue on GitHub
- Check existing issues for solutions
- Review troubleshooting section above

---

**Note**: This agent makes API calls that may incur costs. Monitor your usage on respective platforms (Anthropic, Firecrawl, etc.).
