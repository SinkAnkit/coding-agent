"""Documentation scraper using Firecrawl and BeautifulSoup."""
import os
from typing import Optional
import requests
from bs4 import BeautifulSoup

class DocScraper:
    def __init__(self):
        self.firecrawl_api_key = os.getenv("FIRECRAWL_API_KEY")
    
    def scrape(self, url: str) -> str:
        """Scrape documentation from URL."""
        if self.firecrawl_api_key:
            return self._scrape_with_firecrawl(url)
        return self._scrape_with_bs4(url)
    
    def _scrape_with_firecrawl(self, url: str) -> str:
        """Scrape using Firecrawl API."""
        try:
            from firecrawl import FirecrawlApp
            app = FirecrawlApp(api_key=self.firecrawl_api_key)
            result = app.scrape_url(url, params={'formats': ['markdown']})
            return result.get('markdown', '')
        except Exception as e:
            print(f"Firecrawl failed: {e}, falling back to BeautifulSoup")
            return self._scrape_with_bs4(url)
    
    def _scrape_with_bs4(self, url: str) -> str:
        """Fallback scraper using BeautifulSoup."""
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
            
            text = soup.get_text()
            lines = (line.strip() for line in text.splitlines())
            return '\n'.join(line for line in lines if line)
        except Exception as e:
            return f"Error scraping {url}: {str(e)}"
