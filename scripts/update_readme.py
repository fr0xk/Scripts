import subprocess
import datetime

def get_git_stats():
    try:
        last_commit = subprocess.check_output(['git', 'log', '-1', '--pretty=format:%H']).decode('utf-8').strip()
        num_commits = int(subprocess.check_output(['git', 'rev-list', '--count', 'HEAD']).decode('utf-8').strip())
        last_updated = datetime.datetime.now().strftime("%Y-%m-%d")
        return f"Last commit: {last_commit}\nNumber of commits: {num_commits}\nLast updated: {last_updated}"
    except subprocess.CalledProcessError as e:
        print(f"Error getting git stats: {e}")
        return "Error fetching git stats"

if __name__ == "__main__":
    print(get_git_stats())
