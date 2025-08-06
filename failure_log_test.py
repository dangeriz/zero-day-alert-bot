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
    """Trigger a GitHub commit & push for the updated log."""
    github_repo = os.getenv("GITHUB_REPO")
    github_token = os.getenv("GITHUB_TOKEN")

    if not github_repo or not github_token:
        print("Skipping GitHub push trigger — GITHUB_REPO or GITHUB_TOKEN not set.")
        return

    # Git identity from env vars (with defaults)
    git_name = os.getenv("GIT_COMMIT_NAME", "Render Bot")
    git_email = os.getenv("GIT_COMMIT_EMAIL", "render@users.noreply.github.com")

    os.system(f'git config user.name "{git_name}"')
    os.system(f'git config user.email "{git_email}"')

    os.system("git add notifications.log")
    os.system(
        f"git commit -m 'chore: append test entry from Render at {datetime.utcnow().isoformat()}' || echo 'No changes to commit'"
    )
    os.system(f"git push https://{github_token}@github.com/{github_repo}.git HEAD:main")

if __name__ == "__main__":
    append_test_entry()
    trigger_github_push()
