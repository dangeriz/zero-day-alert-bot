# failure_log_test.py
import os
from datetime import datetime

LOG_PATH = "notifications.log"

def append_test_entry():
    """Append a test entry to notifications.log."""
    timestamp = datetime.utcnow().isoformat()
    entry = f"[TEST ENTRY] Zero-day alert test at {timestamp}\n"
    with open(LOG_PATH, "a") as log_file:
        log_file.write(entry)
    print(f"Appended test entry to {LOG_PATH}")

def trigger_github_push():
    """Optionally trigger GitHub Action push-failure-log.yml."""
    github_repo = os.getenv("GITHUB_REPO")
    github_token = os.getenv("GITHUB_TOKEN")

    if not github_repo or not github_token:
        print("Skipping GitHub push trigger — GITHUB_REPO or GITHUB_TOKEN not set.")
        return

    # Create a commit with the updated log file
    os.system("git config user.name 'Render Bot'")
    os.system("git config user.email 'render@users.noreply.github.com'")
    os.system("git add notifications.log")
    os.system(f"git commit -m 'chore: append test entry from Render at {datetime.utcnow().isoformat()}' || echo 'No changes to commit'")
    os.system(f"git push https://{github_token}@github.com/{github_repo}.git HEAD:main")

if __name__ == "__main__":
    append_test_entry()
    trigger_github_push()
