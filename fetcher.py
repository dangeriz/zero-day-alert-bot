import feedparser
import sqlite3
from datetime import datetime, timezone 

RSS_FEEDS = {
    "Bleeping Computer": "https://www.bleepingcomputer.com/feed/",
    "Hacker News": "https://feeds.feedburner.com/TheHackersNews",
    "Rapid7": "https://www.rapid7.com/blog/rss/",
    "SecurityWeek": "https://feeds.feedburner.com/securityweek",
    "Dark Reading": "https://www.darkreading.com/rss.xml"
}

DB = "storage.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS articles (link TEXT PRIMARY KEY)''')
    conn.commit()
    conn.close()

def is_new_article(link):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT 1 FROM articles WHERE link = ?", (link,))
    exists = c.fetchone()
    if not exists:
        c.execute("INSERT INTO articles (link) VALUES (?)", (link,))
        conn.commit()
        conn.close()
        return True
    conn.close()
    return False

def fetch_articles():
    init_db()
    new_articles = []
    for source, url in RSS_FEEDS.items():
        feed = feedparser.parse(url)
        for entry in feed.entries:
            if "zero-day" in entry.title.lower() or "zero day" in entry.summary.lower():
                if is_new_article(entry.link):
                    new_articles.append({
                        "source": source,
                        "title": entry.title,
                        "link": entry.link,
                        "published": entry.get("published", datetime.now(timezone.utc).isoformat())
                    })
    return new_articles