import os
import smtplib
import requests
from email.message import EmailMessage

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
EMAIL_TO = os.getenv("EMAIL_TO")

def send_email(articles):
    if not SMTP_USER or not EMAIL_TO:
        return
    msg = EmailMessage()
    msg["Subject"] = f"[Zero-Day Alert] {len(articles)} New Articles"
    msg["From"] = SMTP_USER
    msg["To"] = EMAIL_TO
    content = ""
    for a in articles:
        content += f"{a['title']} ({a['source']})\n{a['link']}\n\n"
    msg.set_content(content)
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)

def send_discord(articles):
    if not DISCORD_WEBHOOK_URL:
        return
    for a in articles:
        data = {
            "content": f"🛡️ **{a['title']}**\n🔗 {a['link']}\n📡 Source: {a['source']}"
        }
        requests.post(DISCORD_WEBHOOK_URL, json=data)

def notify_all(articles):
    if not articles:
        return
    send_email(articles)
    send_discord(articles)