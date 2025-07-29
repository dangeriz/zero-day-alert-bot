from fetcher import fetch_articles
from notifier import notify_all
from scheduler import run_scheduler

if __name__ == "__main__":
    run_scheduler(fetch_articles, notify_all)