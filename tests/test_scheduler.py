import schedule
from scheduler import run_scheduler

def test_schedule_job(monkeypatch):
    called = []

    def fake_fetch():
        called.append("fetch")

    def fake_notify(articles):
        called.append("notify")

    def run_once(fetch, notify):
        fetch()
        notify(["dummy article"])
        return called

    monkeypatch.setattr(schedule, 'every', lambda *args, **kwargs: schedule.Job(interval=0))
    results = run_once(fake_fetch, fake_notify)

    assert "fetch" in results
    assert "notify" in results