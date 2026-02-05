# Quick Start: Deploy to Railway

## What You Need

Before deploying, you need these API keys:

1. **Anthropic API Key** - Get from: https://console.anthropic.com/
2. **Slack Bot Token** - Get from: https://api.slack.com/apps (starts with `xoxb-`)
3. **Slack App Token** - Get from: https://api.slack.com/apps (starts with `xapp-`)
4. **GitHub Token** - Get from: https://github.com/settings/tokens
5. (Optional) **Firecrawl API Key** - Get from: https://firecrawl.dev/

## Deploy Now (3 Steps)

### Step 1: Login to Railway

```bash
cd coding-agent
railway login
```

This will open your browser. Sign up/login with GitHub.

### Step 2: Create Project

```bash
railway init
```

Choose "Empty Project" and give it a name (e.g., "coding-agent").

### Step 3: Set Environment Variables

```bash
railway variables set ANTHROPIC_API_KEY="your_key_here"
railway variables set SLACK_BOT_TOKEN="xoxb-your-token"
railway variables set SLACK_APP_TOKEN="xapp-your-token"
railway variables set GITHUB_TOKEN="ghp_your-token"
railway variables set GITHUB_REPO_OWNER="your_github_username"
railway variables set GITHUB_REPO_NAME="your_repo_name"
```

### Step 4: Deploy

```bash
railway up
```

Wait for deployment to complete (1-2 minutes).

### Step 5: Check Logs

```bash
railway logs
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

## Test It

Go to Slack and try:
```
/generate Write a Python function to reverse a string
```

## Done!

Your agent is now running 24/7 on Railway.

## Useful Commands

- `railway logs` - View logs
- `railway status` - Check service status
- `railway open` - Open Railway dashboard
- `railway down` - Stop service
- `railway up` - Redeploy

## Troubleshooting

**Problem: "No project found"**
```bash
railway link
```

**Problem: Service keeps restarting**
- Check logs: `railway logs`
- Verify environment variables: `railway variables`

**Problem: Slack bot not responding**
- Ensure Socket Mode is enabled in Slack app settings
- Verify SLACK_APP_TOKEN is set correctly

## Cost

- Railway Free Tier: $5 credit/month
- This project uses ~$2-3/month
- More than enough for testing!

## Next Steps

1. Test all Slack commands
2. Monitor logs for any errors
3. Set up GitHub repository for the agent to work with
4. Enjoy your automated coding assistant!
