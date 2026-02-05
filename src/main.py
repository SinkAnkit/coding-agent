"""Main entry point for the coding agent."""
import os
import sys
from dotenv import load_dotenv

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent.coding_agent import CodingAgent
from gh_integration.github_manager import GitHubManager
from scraper.doc_scraper import DocScraper
from slack.slack_bot import SlackBot

def main():
    # Load environment variables
    load_dotenv()
    
    print("Starting Coding Agent...", flush=True)
    
    # Initialize components
    try:
        agent = CodingAgent()
        print("Coding agent initialized", flush=True)
        
        github = GitHubManager()
        print("GitHub manager initialized", flush=True)
        
        scraper = DocScraper()
        print("Doc scraper initialized", flush=True)
        
        bot = SlackBot(agent, github, scraper)
        print("Slack bot initialized", flush=True)
        
        # Start the bot
        print("Starting Slack bot...", flush=True)
        bot.start()
        
    except Exception as e:
        print(f"ERROR: {str(e)}", flush=True)
        import traceback
        traceback.print_exc()
        raise

if __name__ == "__main__":
    main()
