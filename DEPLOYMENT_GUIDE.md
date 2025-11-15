# VAMP Discord Bot - Complete Deployment Guide

## 🎯 Overview
This guide will help you deploy:
- **Frontend (Vercel)**: https://vamp-zeta.vercel.app/ ✅ Already deployed
- **Backend (Railway)**: Flask API with Discord OAuth2
- **Discord OAuth**: Connect everything together

---

## 📋 Part 1: Get Discord OAuth Credentials

### Step 1.1: Access Discord Developer Portal
1. Go to https://discord.com/developers/applications
2. Log in with your Discord account
3. Click on your **VAMP** application (the bot you created)

### Step 1.2: Get Client ID and Secret
1. In the left sidebar, click **OAuth2** → **General**
2. You'll see:
   - **CLIENT ID**: A long number (e.g., `1439220485257822359`)
   - **CLIENT SECRET**: Click "Reset Secret" or "Copy" to reveal it
3. **IMPORTANT**: Copy both values and save them temporarily in a notepad

### Step 1.3: Set Redirect URI (We'll add this after Railway deployment)
- You'll need your Railway backend URL first
- Come back to this after Part 2

---

## 📋 Part 2: Deploy Backend to Railway

### Step 2.1: Create Railway Account
1. Go to https://railway.app
2. Click **Login with GitHub**
3. Authorize Railway to access your GitHub account

### Step 2.2: Create New Project
1. On Railway dashboard, click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Find and select **`valorety-dev/vamp`**
4. Railway will start deploying (it might fail initially - that's okay!)

### Step 2.3: Configure Root Directory
1. Click on your deployment card
2. Click **"Settings"** tab
3. Scroll to **"Root Directory"**
4. Click **"Configure"** or the edit icon
5. Enter: `api`
6. Click **"Update"**

### Step 2.4: Set Start Command
1. Still in **Settings** tab
2. Find **"Start Command"**
3. Enter: `python app.py`
4. Click **"Update"**

### Step 2.5: Add Environment Variables
1. Click the **"Variables"** tab
2. Click **"+ New Variable"**
3. Add these **4 variables** one by one:

**Variable 1:**
```
Name: DISCORD_CLIENT_ID
Value: [Paste the CLIENT ID from Step 1.2]
```

**Variable 2:**
```
Name: DISCORD_CLIENT_SECRET
Value: [Paste the CLIENT SECRET from Step 1.2]
```

**Variable 3:**
```
Name: DISCORD_TOKEN
Value: [Your Discord bot token from .env file]
```

**Variable 4:**
```
Name: REDIRECT_URI
Value: https://YOUR-RAILWAY-URL.railway.app/api/auth/callback
```
⚠️ **For Variable 4**: You need to get your Railway URL first (next step), then come back and add this

### Step 2.6: Get Your Railway URL
1. Click the **"Settings"** tab
2. Scroll to **"Networking"** section
3. Click **"Generate Domain"**
4. Railway will give you a URL like: `https://vamp-production-abcd.up.railway.app`
5. **COPY THIS URL** - you'll need it multiple times

### Step 2.7: Update REDIRECT_URI Variable
1. Go back to **"Variables"** tab
2. Click on the **REDIRECT_URI** variable
3. Update it to: `https://your-actual-railway-url.railway.app/api/auth/callback`
4. Example: `https://vamp-production-abcd.up.railway.app/api/auth/callback`

### Step 2.8: Redeploy
1. Click **"Deployments"** tab
2. Click the three dots **"···"** on the latest deployment
3. Click **"Redeploy"**
4. Wait for the green **"SUCCESS"** status

---

## 📋 Part 3: Complete Discord OAuth Setup

### Step 3.1: Add Redirect URI to Discord
1. Go back to https://discord.com/developers/applications
2. Select your **VAMP** application
3. Go to **OAuth2** → **General**
4. Scroll to **"Redirects"** section
5. Click **"Add Redirect"**
6. Paste: `https://your-railway-url.railway.app/api/auth/callback`
   - Example: `https://vamp-production-abcd.up.railway.app/api/auth/callback`
7. Click **"Save Changes"**

---

## 📋 Part 4: Connect Frontend to Backend

### Step 4.1: Add API URL to Vercel
1. Go to https://vercel.com/dashboard
2. Click on your **vamp** project
3. Click **"Settings"** tab
4. Click **"Environment Variables"** in the left sidebar
5. Click **"Add New"**
6. Enter:
   ```
   Name: REACT_APP_API_URL
   Value: https://your-railway-url.railway.app
   ```
   - Example: `https://vamp-production-abcd.up.railway.app`
   - ⚠️ **NO trailing slash!**
7. Select: **Production**, **Preview**, **Development** (all three)
8. Click **"Save"**

### Step 4.2: Redeploy Frontend
1. Click **"Deployments"** tab
2. Click the three dots **"···"** on the latest deployment
3. Click **"Redeploy"**
4. Wait for deployment to complete

---

## 📋 Part 5: Test Authentication

### Step 5.1: Test the Login Flow
1. Go to https://vamp-zeta.vercel.app/
2. You should see the login page with geometric lines
3. Click **"Authenticate with Discord"** button
4. You should be redirected to Discord OAuth page
5. Click **"Authorize"**
6. If you have **ADMINISTRATOR** permission in any server with the bot:
   - ✅ You'll be redirected to the dashboard
7. If you DON'T have admin permissions:
   - ❌ You'll see an error message

### Step 5.2: Verify Backend is Running
1. Open in browser: `https://your-railway-url.railway.app/api/auth/login`
2. You should see JSON with a Discord OAuth URL
3. If you see an error, check Railway logs:
   - Railway dashboard → Your project → **"Logs"** tab

---

## 🐛 Troubleshooting

### Problem: "Failed to fetch" error when clicking login
**Solution:**
- Check that `REACT_APP_API_URL` is set correctly in Vercel
- Make sure Railway backend is running (check Logs tab)
- Verify no trailing slash in API URL

### Problem: "Redirect URI mismatch" error from Discord
**Solution:**
- Make sure the redirect URI in Discord Developer Portal exactly matches:
  `https://your-railway-url.railway.app/api/auth/callback`
- No extra spaces or trailing slashes
- Protocol must be `https://`

### Problem: "No admin permissions" error
**Solution:**
- Make sure you have ADMINISTRATOR permission in at least one Discord server where VAMP bot is installed
- The bot must be in the server
- Your Discord account must have the Administrator role

### Problem: Railway deployment failed
**Solution:**
1. Check Railway logs for errors
2. Make sure all 4 environment variables are set
3. Verify `Root Directory` is set to `api`
4. Verify `Start Command` is `python app.py`

### Problem: Frontend shows blank page
**Solution:**
- Check browser console (F12) for errors
- Verify Vercel deployment succeeded
- Check that `Root Directory` in Vercel is set to `dashboard`

---

## 📝 Quick Reference - URLs and Settings

### Discord Developer Portal
- Application: https://discord.com/developers/applications
- Redirect URI: `https://YOUR-RAILWAY-URL.railway.app/api/auth/callback`

### Railway (Backend)
- Dashboard: https://railway.app
- Root Directory: `api`
- Start Command: `python app.py`
- Environment Variables: 4 total (CLIENT_ID, CLIENT_SECRET, TOKEN, REDIRECT_URI)

### Vercel (Frontend)
- Dashboard: https://vercel.com/dashboard
- Root Directory: `dashboard`
- Live URL: https://vamp-zeta.vercel.app/
- Environment Variable: `REACT_APP_API_URL` = Your Railway URL

---

## ✅ Success Checklist

Before testing, make sure:
- [ ] Discord CLIENT_ID and CLIENT_SECRET copied
- [ ] Railway project deployed with `api` root directory
- [ ] All 4 Railway environment variables set
- [ ] Railway domain generated and copied
- [ ] Discord redirect URI added with Railway URL
- [ ] Vercel environment variable `REACT_APP_API_URL` added
- [ ] Both Railway and Vercel redeployed
- [ ] You have Administrator permission in a server with the bot

---

## 🎉 You're Done!

Your VAMP dashboard should now be fully functional with Discord OAuth2 authentication!

**Test URL:** https://vamp-zeta.vercel.app/

If you encounter any issues, check the Troubleshooting section above or review the Railway/Vercel logs for specific error messages.
