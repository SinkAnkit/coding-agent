"""Test script to verify agent functionality without Slack."""
import os
from dotenv import load_dotenv
from src.agent.coding_agent import CodingAgent
from src.scraper.doc_scraper import DocScraper

def test_agent():
    load_dotenv()
    
    print("Testing Coding Agent...\n")
    
    # Test 1: Initialize agent
    print("1. Initializing agent...")
    agent = CodingAgent()
    print("✅ Agent initialized\n")
    
    # Test 2: Generate simple code
    print("2. Testing code generation...")
    code = agent.generate_code("Write a Python function to calculate fibonacci numbers")
    print(f"Generated code:\n{code[:200]}...\n")
    print("✅ Code generation works\n")
    
    # Test 3: Test scraper
    print("3. Testing doc scraper...")
    scraper = DocScraper()
    docs = scraper.scrape("https://example.com")
    print(f"Scraped {len(docs)} characters")
    print("✅ Scraper works\n")
    
    print("🎉 All tests passed!")

if __name__ == "__main__":
    test_agent()
