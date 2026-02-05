"""Core coding agent using Claude and LangChain."""
import os
from typing import Optional
from anthropic import Anthropic
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, SystemMessage

class CodingAgent:
    def __init__(self):
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment")
        
        self.llm = ChatAnthropic(
            model="claude-3-5-sonnet-20241022",
            api_key=self.api_key,
            temperature=0
        )
        
        self.system_prompt = """You are an expert coding agent. Your role is to:
1. Analyze documentation and understand context
2. Write clean, production-ready code
3. Solve GitHub issues with working solutions
4. Follow best practices and coding standards

Always provide complete, working code with minimal explanations."""
    
    def analyze_docs(self, docs: str, query: str) -> str:
        """Analyze documentation and answer query."""
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=f"Documentation:\n{docs}\n\nQuery: {query}")
        ]
        response = self.llm.invoke(messages)
        return response.content
    
    def generate_code(self, requirements: str, context: Optional[str] = None) -> str:
        """Generate code based on requirements."""
        prompt = f"Requirements:\n{requirements}"
        if context:
            prompt = f"Context:\n{context}\n\n{prompt}"
        
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=prompt)
        ]
        response = self.llm.invoke(messages)
        return response.content
    
    def solve_issue(self, issue_title: str, issue_body: str, repo_context: Optional[str] = None) -> dict:
        """Solve a GitHub issue and return solution."""
        prompt = f"""GitHub Issue:
Title: {issue_title}
Body: {issue_body}
"""
        if repo_context:
            prompt += f"\nRepository Context:\n{repo_context}"
        
        prompt += "\n\nProvide a complete solution with code changes needed."
        
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=prompt)
        ]
        response = self.llm.invoke(messages)
        
        return {
            "solution": response.content,
            "issue_title": issue_title
        }
