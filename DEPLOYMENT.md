# VAMP Bot Dashboard

Premium Discord moderation bot with OAuth2 authentication.

## Deployment

### Frontend (Vercel)
1. Push code to GitHub
2. Import project to Vercel
3. Deploy from `dashboard` folder
4. Add environment variable: `REACT_APP_API_URL` (your backend URL)

### Backend (Vercel Serverless or Railway)

**Option 1: Railway (Recommended for Flask)**
1. Create Railway account
2. Deploy from `api` folder
3. Add environment variables:
   - `DISCORD_CLIENT_ID`
   - `DISCORD_CLIENT_SECRET`
   - Update `REDIRECT_URI` to your Railway URL

**Option 2: Vercel Serverless**
1. Convert Flask to serverless functions
2. Deploy from `api` folder

## Discord OAuth2 Setup
1. Go to https://discord.com/developers/applications
2. Select VAMP application → OAuth2
3. Add redirect URI: `https://your-backend-url.com/api/auth/callback`
4. Copy CLIENT_ID and CLIENT_SECRET
5. Update environment variables

## Local Development
```bash
# Frontend
cd dashboard
npm install
npm start

# Backend
cd api
pip install -r requirements.txt
python app.py
```
