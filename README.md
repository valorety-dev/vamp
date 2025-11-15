# 🦇 VAMP - Discord Pinterest Bot

A cool Discord bot that pulls and sends images from Pinterest based on keywords!

## Features

- 🔍 Search Pinterest with simple commands
- 🖼️ Fetches multiple images per search
- 🎨 Beautiful embed formatting
- ⚡ Fast and responsive
- 🦇 Cool vampire theme

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- A Discord account
- Discord Developer Portal access

### Step 1: Create a Discord Bot

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name (e.g., "VAMP")
3. Go to the "Bot" tab and click "Add Bot"
4. Under "Privileged Gateway Intents", enable:
   - ✅ Message Content Intent
5. Click "Reset Token" and copy your bot token (keep this secret!)

### Step 2: Install Dependencies

```powershell
# Create a virtual environment (recommended)
python -m venv venv

# Activate the virtual environment
.\venv\Scripts\Activate.ps1

# Install required packages
pip install -r requirements.txt
```

### Step 3: Configure the Bot

1. Copy `.env.example` to `.env`:
   ```powershell
   Copy-Item .env.example .env
   ```

2. Edit `.env` and add your Discord bot token:
   ```
   DISCORD_TOKEN=your_actual_token_here
   ```

### Step 4: Invite Bot to Your Server

1. Go back to Discord Developer Portal
2. Navigate to "OAuth2" → "URL Generator"
3. Select scopes:
   - ✅ bot
4. Select bot permissions:
   - ✅ Send Messages
   - ✅ Embed Links
   - ✅ Attach Files
   - ✅ Read Message History
5. Copy the generated URL and open it in your browser
6. Select your server and authorize the bot

### Step 5: Run the Bot

```powershell
python bot.py
```

You should see: `VAMP has connected to Discord!`

## Commands

| Command | Description | Example |
|---------|-------------|---------|
| `!vamp <keyword>` | Search and display Pinterest images | `!vamp aesthetic sunset` |
| `!vamphelp` | Show help information | `!vamphelp` |

## Usage Examples

```
!vamp cute cats
!vamp aesthetic wallpaper
!vamp vintage fashion
!vamp nature photography
```

## Troubleshooting

### Bot doesn't respond
- Make sure Message Content Intent is enabled in Discord Developer Portal
- Check that your bot token is correct in `.env`
- Verify the bot has permissions to send messages in the channel

### No images found
- Pinterest may be blocking automated requests
- Try different keywords
- The scraper relies on web scraping, which may need updates if Pinterest changes their site structure

### Rate limiting
- If you get rate limited, wait a few minutes before trying again
- Consider adding delays between multiple searches

## Notes

⚠️ **Important**: This bot uses web scraping to fetch images from Pinterest. This method:
- Does not require a Pinterest API key
- May break if Pinterest updates their website structure
- Should be used responsibly to avoid rate limiting
- Is for educational/personal use

For production use, consider using the official Pinterest API if available.

## Project Structure

```
VAMP/
├── bot.py                  # Main Discord bot file
├── pinterest_scraper.py    # Pinterest scraping module
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
├── .env                   # Your actual config (not in git)
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## License

Free to use for personal projects. Have fun! 🦇

## Contributing

Feel free to fork and improve! Some ideas:
- Add more image sources
- Implement caching
- Add reaction-based navigation
- Support for GIFs
- Custom embed colors per server

---

Made with 🦇 by the VAMP team
