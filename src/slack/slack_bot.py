"""Slack bot integration."""
import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

class SlackBot:
    def __init__(self, agent, github_manager, doc_scraper):
        self.bot_token = os.getenv("SLACK_BOT_TOKEN")
        self.app_token = os.getenv("SLACK_APP_TOKEN")
        
        if not self.bot_token or not self.app_token:
            raise ValueError("SLACK_BOT_TOKEN and SLACK_APP_TOKEN required")
        
        self.app = App(token=self.bot_token)
        self.agent = agent
        self.github = github_manager
        self.scraper = doc_scraper
        
        self._register_commands()
    
    def _register_commands(self):
        """Register Slack commands."""
        
        @self.app.command("/scrape")
        def handle_scrape(ack, command, say):
            ack()
            url = command['text']
            say(f"🔍 Scraping documentation from {url}...")
            
            try:
                docs = self.scraper.scrape(url)
                say(f"✅ Scraped {len(docs)} characters from {url}")
            except Exception as e:
                say(f"❌ Error: {str(e)}")
        
        @self.app.command("/generate")
        def handle_generate(ack, command, say):
            ack()
            requirements = command['text']
            say(f"🤖 Generating code...")
            
            try:
                code = self.agent.generate_code(requirements)
                say(f"```\n{code}\n```")
            except Exception as e:
                say(f"❌ Error: {str(e)}")
        
        @self.app.command("/solve")
        def handle_solve(ack, command, say):
            ack()
            issue_number = int(command['text'])
            say(f"🔧 Solving issue #{issue_number}...")
            
            try:
                issue = self.github.get_issue(issue_number)
                solution = self.agent.solve_issue(issue.title, issue.body)
                say(f"✅ Solution:\n```\n{solution['solution']}\n```")
            except Exception as e:
                say(f"❌ Error: {str(e)}")
        
        @self.app.message("hello")
        def handle_hello(message, say):
            say(f"Hi <@{message['user']}>! I'm your coding agent. Use /scrape, /generate, or /solve commands.")
    
    def start(self):
        """Start the Slack bot."""
        handler = SocketModeHandler(self.app, self.app_token)
        print("⚡ Slack bot is running!")
        handler.start()
