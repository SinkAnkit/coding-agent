# Railway Deployment Guide

## Prerequisites

1. Create a Railway account at https://railway.app
2. Install Railway CLI (optional but recommended)

## Deployment Steps

### Option 1: Deploy via GitHub (Recommended)

1. **Push your code to GitHub:**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/coding-agent.git
   git push -u origin main
   ```

2. **Connect to Railway:**
   - Go to https://railway.app/new
   - Click "Deploy from GitHub repo"
   - Select your `coding-agent` repository
   - Click "Deploy Now"

3. **Set Environment Variables:**
   - In Railway dashboard, go to your project
   - Click on "Variables" tab
   - Add these variables:
     ```
     ANTHROPIC_API_KEY=your_claude_api_key
     SLACK_BOT_TOKEN=xoxb-your-token
     SLACK_APP_TOKEN=xapp-your-token
     GITHUB_TOKEN=ghp_your_token
     GITHUB_REPO_OWNER=your_username
     GITHUB_REPO_NAME=your_repo
     FIRECRAWL_API_KEY=your_key (optional)
     ```

4. **Deploy:**
   - Railway will automatically deploy
   - Check logs to ensure it's running

### Option 2: Deploy via Railway CLI

1. **Install Railway CLI:**
   ```bash
   npm install -g @railway/cli
   ```

2. **Login:**
   ```bash
   railway login
   ```

3. **Initialize project:**
   ```bash
   railway init
   ```

4. **Link to project:**
   ```bash
   railway link
   ```

5. **Set environment variables:**
   ```bash
   railway variables set ANTHROPIC_API_KEY=your_key
   railway variables set SLACK_BOT_TOKEN=xoxb-your-token
   railway variables set SLACK_APP_TOKEN=xapp-your-token
   railway variables set GITHUB_TOKEN=ghp_your-token
   railway variables set GITHUB_REPO_OWNER=your_username
   railway variables set GITHUB_REPO_NAME=your_repo
   ```

6. **Deploy:**
   ```bash
   railway up
   ```

### Option 3: One-Click Deploy

Click this button to deploy directly:

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/YOUR_USERNAME/coding-agent)

## Verify Deployment

1. Check Railway logs:
   ```bash
   railway logs
   ```

2. You should see:
   ```
   Starting Coding Agent...
   Coding agent initialized
   GitHub manager initialized
   Doc scraper initialized
   Slack bot initialized
   Slack bot is running!
   ```

3. Test in Slack:
   ```
   /generate Write a hello world function
   ```

## Monitoring

- **View Logs:** Railway dashboard > Deployments > Logs
- **Check Status:** Railway dashboard shows service status
- **Resource Usage:** Monitor your $5/month credit usage

## Troubleshooting

### Service keeps restarting
- Check logs for errors
- Verify all environment variables are set
- Ensure Slack tokens are valid

### "Out of credits" error
- Railway free tier: $5/month
- Upgrade to hobby plan ($5/month) for more credits
- Optimize resource usage

### Slack bot not responding
- Verify service is running in Railway dashboard
- Check that Socket Mode is enabled in Slack app
- Ensure SLACK_APP_TOKEN is set correctly

## Updating Deployment

### Via GitHub:
```bash
git add .
git commit -m "Update feature"
git push origin main
```
Railway auto-deploys on push.

### Via CLI:
```bash
railway up
```

## Cost Estimation

Railway Free Tier:
- $5 credit/month
- This project uses ~$2-3/month (running 24/7)
- Sufficient for development/testing

## Alternative: Fly.io

If Railway credits run out, deploy to Fly.io (also free):

```bash
# Install flyctl
curl -L https://fly.io/install.sh | sh

# Login
flyctl auth login

# Deploy
flyctl launch
flyctl deploy
```

## Support

For Railway-specific issues:
- Railway Docs: https://docs.railway.app
- Railway Discord: https://discord.gg/railway
