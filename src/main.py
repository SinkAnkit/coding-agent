"""Main entry point for the coding agent."""
import os
from dotenv import load_dotenv
from src.agent.coding_agent import CodingAgent
from src.github.github_manager import GitHubManager
from src.scraper.doc_scraper import DocScraper
from src.slack.slack_bot import SlackBot

def main():
    # Load environment variables
    load_dotenv()
    
    print("🚀 Starting Coding Agent...")
    
    # Initialize components
    try:
        agent = CodingAgent()
        print("✅ Coding agent initialized")
        
        github = GitHubManager()
        print("✅ GitHub manager initialized")
        
        scraper = DocScraper()
        print("✅ Doc scraper initialized")
        
        bot = SlackBot(agent, github, scraper)
        print("✅ Slack bot initialized")
        
        # Start the bot
        bot.start()
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        raise

if __name__ == "__main__":
    main()
