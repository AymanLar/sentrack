# Deployment Guide

This guide explains how to deploy the Sentrack Flask app using GitHub Actions and various platforms.

## GitHub Actions Setup

### 1. Repository Setup
- Push your code to a GitHub repository
- Ensure your main branch is named `main` or `master`

### 2. Required Secrets
You need to set up the following secrets in your GitHub repository:

#### For Vercel Deployment:
1. Go to your GitHub repository → Settings → Secrets and variables → Actions
2. Add the following secrets:
   - `VERCEL_TOKEN`: Your Vercel API token
   - `VERCEL_ORG_ID`: Your Vercel organization ID
   - `VERCEL_PROJECT_ID`: Your Vercel project ID

#### How to get Vercel credentials:
1. Install Vercel CLI: `npm i -g vercel`
2. Run `vercel login`
3. Run `vercel link` in your project directory
4. Check `.vercel/project.json` for your project ID
5. Get your token from [Vercel Dashboard → Settings → Tokens](https://vercel.com/account/tokens)

### 3. Environment Variables
Make sure to set up your environment variables in Vercel:
- `GENIUS_API_KEY`: Your Genius API key

## Alternative Deployment Platforms

### Railway
1. Connect your GitHub repository to Railway
2. Add environment variables in Railway dashboard
3. Railway will automatically deploy on pushes to main branch

### Render
1. Connect your GitHub repository to Render
2. Create a new Web Service
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `python app.py`
5. Add environment variables

### Heroku
1. Install Heroku CLI
2. Create a new Heroku app
3. Add your GitHub repository
4. Set up environment variables in Heroku dashboard

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export GENIUS_API_KEY="your_api_key_here"

# Run the app
python app.py
```

## Troubleshooting

### Common Issues:
1. **Missing environment variables**: Ensure all required environment variables are set
2. **Python version mismatch**: The app requires Python 3.11+
3. **Dependencies not found**: Make sure all packages in requirements.txt are compatible

### Testing Locally:
```bash
# Test imports
python -c "import app; print('App imports successfully')"
python -c "import helpers; print('Helpers imports successfully')"
```

## File Structure
```
sentrack/
├── .github/workflows/deploy.yml  # GitHub Actions workflow
├── app.py                        # Main Flask application
├── helpers.py                    # Helper functions
├── requirements.txt              # Python dependencies
├── vercel.json                  # Vercel configuration
├── Procfile                     # For Heroku/Railway
├── runtime.txt                  # Python version specification
└── templates/                   # HTML templates
    └── index.html
``` 