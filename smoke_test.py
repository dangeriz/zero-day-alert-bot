# smoke_test.py
import os
from datetime import datetime
from fetcher import fetch_articles
from notifier import notify_all

LOG_PATH = "notifications.log"

def append_smoke_log(status: str):
    timestamp = datetime.utcnow().isoformat()
    with open(LOG_PATH, "a") as f:
        f.write(f"[SMOKE TEST] {timestamp} — {status}\n")

def run_smoke_test():
    try:
        articles = fetch_articles()
        if articles:
            msg = f"[Smoke Test] Fetched {len(articles)} article(s)."
        else:
            msg = "[Smoke Test] No new articles found."

        notify_all(msg)
        append_smoke_log("Success")
        print("✅ Smoke test succeeded")
    except Exception as e:
        append_smoke_log(f"Failure: {e}")
        print(f"❌ Smoke test failed: {e}")
        raise

if __name__ == "__main__":
    run_smoke_test()
