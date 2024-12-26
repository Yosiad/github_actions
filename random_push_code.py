import os
import random
import string
import subprocess
from datetime import datetime 

# GitHub authentication details
GITHUB_USER = 'your_github_username'
GITHUB_REPO = 'your_github_repo'
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')  # Use GitHub Actions secret

# Generate random code
def generate_random_code():
    length = random.randint(20, 100)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Commit and push changes
def commit_and_push_changes():
    random_code = generate_random_code()
    file_path = 'random_code.txt'

    # Append the random code to a file
    with open(file_path, 'a') as file:
        file.write(f"{datetime.now()} - {random_code}\n")

    # Git commands to commit and push
    subprocess.run(['git', 'add', '.'], check=True)
    subprocess.run(['git', 'commit', '-m', f'Random commit {datetime.now()}'], check=True)
    subprocess.run(['git', 'push', f'https://{GITHUB_USER}:{GITHUB_TOKEN}@github.com/{GITHUB_USER}/{GITHUB_REPO}.git', 'main'], check=True)
    print(f"Changes pushed at {datetime.now()}")

# Run the function to commit and push 
if __name__ == '__main__':
    commit_and_push_changes() 
