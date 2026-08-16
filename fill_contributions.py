import os
import random
from datetime import datetime, timedelta

# List of your local repository directories or current repo path
repo_path = os.getcwd()

# Generate random commits spread across random dates in the past year
num_commits = random.randint(25, 50)

for _ in range(num_commits):
    # Pick completely random days across the entire year (0 to 365 days ago)
    random_days_ago = random.randint(0, 365)
    commit_date = datetime.now() - timedelta(days=random_days_ago)
    
    # Modify the tracking file
    log_file = "activity_log.txt"
    with open(log_file, "a") as f:
        f.write(f"Random activity update at {commit_date.strftime('%Y-%m-%d %H:%M:%S')}\n")
        
    os.system("git add activity_log.txt")
    
    # Apply the backdated timestamp for author and committer
    env_date = commit_date.strftime("%Y-%m-%d %H:%M:%S")
    os.environ["GIT_AUTHOR_DATE"] = env_date
    os.environ["GIT_COMMITTER_DATE"] = env_date
    
    os.system('git commit -m "Refactor internal components"')

print("Organic random contribution history generated successfully!")