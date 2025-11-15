from flask import Flask, request, jsonify, session, redirect
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv
import secrets

load_dotenv()

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

# Get frontend URL from environment or use default
FRONTEND_URL = os.getenv('FRONTEND_URL', 'http://localhost:3000')
CORS(app, supports_credentials=True, origins=[FRONTEND_URL, 'https://vamp-zeta.vercel.app'])

# Discord OAuth2 Config
CLIENT_ID = os.getenv('DISCORD_CLIENT_ID')
CLIENT_SECRET = os.getenv('DISCORD_CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI', 'http://localhost:5000/api/auth/callback')
DISCORD_API_URL = 'https://discord.com/api/v10'

@app.route('/api/auth/login')
def login():
    return jsonify({
        'url': f'https://discord.com/api/oauth2/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code&scope=identify%20guilds'
    })

@app.route('/api/auth/callback')
def callback():
    code = request.args.get('code')
    if not code:
        return redirect(f'{FRONTEND_URL}?error=no_code')
    
    # Exchange code for access token
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI
    }
    
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    
    response = requests.post(f'{DISCORD_API_URL}/oauth2/token', data=data, headers=headers)
    
    if response.status_code != 200:
        return redirect(f'{FRONTEND_URL}?error=token_exchange_failed')
    
    credentials = response.json()
    access_token = credentials['access_token']
    
    # Get user info
    headers = {'Authorization': f'Bearer {access_token}'}
    user_response = requests.get(f'{DISCORD_API_URL}/users/@me', headers=headers)
    user = user_response.json()
    
    # Get user's guilds
    guilds_response = requests.get(f'{DISCORD_API_URL}/users/@me/guilds', headers=headers)
    guilds = guilds_response.json()
    
    # Check if user has admin perms in any guild
    has_admin = False
    for guild in guilds:
        permissions = int(guild.get('permissions', 0))
        # Check for ADMINISTRATOR permission (0x8)
        if permissions & 0x8:
            has_admin = True
            break
    
    if not has_admin:
        return redirect(f'{FRONTEND_URL}?error=no_admin_perms')
    
    # Store user session
    session['user'] = {
        'id': user['id'],
        'username': user['username'],
        'discriminator': user.get('discriminator', '0'),
        'avatar': user['avatar'],
        'access_token': access_token
    }
    
    return redirect(f'{FRONTEND_URL}/dashboard')

@app.route('/api/auth/user')
def get_user():
    user = session.get('user')
    if not user:
        return jsonify({'authenticated': False}), 401
    
    return jsonify({
        'authenticated': True,
        'user': {
            'id': user['id'],
            'username': user['username'],
            'discriminator': user['discriminator'],
            'avatar': f"https://cdn.discordapp.com/avatars/{user['id']}/{user['avatar']}.png"
        }
    })

@app.route('/api/auth/logout')
def logout():
    session.clear()
    return jsonify({'success': True})

@app.route('/api/stats')
def get_stats():
    user = session.get('user')
    if not user:
        return jsonify({'error': 'Unauthorized'}), 401
    
    # Mock stats - replace with real bot data
    return jsonify({
        'servers': 1,
        'users': 847,
        'commands': 1234,
        'uptime': '99.9%'
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
