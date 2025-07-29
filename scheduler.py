import time
import schedule

def run_scheduler(fetch_func, notify_func):
    def job():
        articles = fetch_func()
        notify_func(articles)
    schedule.every(4).hours.do(job)
    job()  # Run once at startup
    while True:
        schedule.run_pending()
        time.sleep(60)