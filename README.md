# Coding Agent

A production-ready AI coding agent that scrapes documentation, writes code, solves GitHub issues, and creates pull requests - all controlled via Slack.

## Features

- 🤖 **AI-Powered Code Generation**: Uses Claude AI to write production-ready code
- 📚 **Documentation Scraping**: Automatically scrapes and understands documentation
- 🐛 **Issue Resolution**: Solves GitHub issues autonomously
- 🔀 **PR Creation**: Automatically creates and raises pull requests
- 💬 **Slack Integration**: Control everything via Slack commands

## Architecture

```
┌─────────────┐
│   Slack     │
│   Commands  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Agent     │◄──────┐
│   Core      │       │
└──────┬──────┘       │
       │              │
       ├──────────────┤
       │              │
       ▼              ▼
┌─────────────┐ ┌─────────────┐
│  Doc        │ │  GitHub     │
│  Scraper    │ │  API        │
└─────────────┘ └─────────────┘
```

## Tech Stack

- **LLM**: Anthropic Claude
- **Agent Framework**: LangChain
- **Slack**: Slack Bolt SDK
- **GitHub**: PyGithub
- **Web Scraping**: Firecrawl / BeautifulSoup

## Setup

### Prerequisites

- Python 3.12+
- Anthropic API key
- Slack workspace with bot permissions
- GitHub personal access token

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd coding-agent
```

2. Create virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys
```

### Configuration

Edit `.env` file with your credentials:

- `ANTHROPIC_API_KEY`: Your Claude API key
- `SLACK_BOT_TOKEN`: Slack bot token (starts with `xoxb-`)
- `SLACK_APP_TOKEN`: Slack app token (starts with `xapp-`)
- `GITHUB_TOKEN`: GitHub personal access token
- `FIRECRAWL_API_KEY`: Firecrawl API key (optional)

## Usage

### Running the Agent

```bash
python src/main.py
```

### Slack Commands

- `/code-agent scrape <url>` - Scrape documentation from URL
- `/code-agent solve <issue-number>` - Solve a GitHub issue
- `/code-agent generate <description>` - Generate code from description

## Development

### Project Structure

```
coding-agent/
├── src/
│   ├── agent/          # Core agent logic
│   ├── slack/          # Slack integration
│   ├── github/         # GitHub API integration
│   └── scraper/        # Documentation scraper
├── tests/              # Unit tests
├── docs/               # Documentation
├── requirements.txt    # Python dependencies
└── README.md
```

### Running Tests

```bash
pytest tests/
```

## Deployment

(Deployment instructions will be added after implementation)

## License

MIT

## Contributing

Contributions welcome! Please open an issue or PR.
