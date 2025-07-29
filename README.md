# 🛡️ Zero-Day Vulnerability Alert Bot

Fetches articles about zero-day vulnerabilities and sends alerts via email and Discord.

## ✅ Features
- Pulls from 5 trusted sources
- Filters for "zero-day" keywords
- Avoids duplicate notifications using SQLite
- Notifies via Email + Discord

## 🚀 Deploy

### On Render
1. Push this repo to GitHub
2. Create new Cron Job at [Render.com](https://render.com)
3. Connect your GitHub repo
4. Add `DISCORD_WEBHOOK_URL`, `SMTP_USER`, etc. to Render’s environment tab
5. Done! It will run every 4 hours

### On EC2
```bash
sudo apt update && sudo apt install python3-pip sqlite3
pip3 install -r requirements.txt
cp .env.example .env  # and fill in secrets
python3 main.py
```

## 🔧 Customize Sources
Edit `RSS_FEEDS` in `fetcher.py` to add or remove feeds.