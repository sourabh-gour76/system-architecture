import os
import random
from datetime import datetime, timedelta

# Generate organic random commits over the past year
num_commits = random.randint(20, 35)

for _ in range(num_commits):
    # Pick a random day in the past 365 days
    random_days_ago = random.randint(0, 365)
    commit_date = datetime.now() - timedelta(days=random_days_ago)
    
    # Modify a tracking file
    log_file = "activity_log.txt"
    with open(log_file, "a") as f:
        f.write(f"Activity update on {commit_date.strftime('%Y-%m-%d %H:%M:%S')}\n")
        
    os.system("git add activity_log.txt")
    
    # Backdate the commit cleanly
    env_date = commit_date.strftime("%Y-%m-%d %H:%M:%S")
    os.environ["GIT_AUTHOR_DATE"] = env_date
    os.environ["GIT_COMMITTER_DATE"] = env_date
    
    os.system('git commit -m "Update system configurations"')

print("Organic commit history generated successfully!")