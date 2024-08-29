import requests


def generate_report(branch):
    token = "your_github_token"
    headers = {'Authorization': f'token {token}'}
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/code-scanning/alerts?ref={branch}"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        alerts = response.json()
        # Process the alerts and create a report
        with open(f"report_{branch}.txt", "w") as report_file:
            for alert in alerts:
                report_file.write(
                    f"{alert['rule']['description']}: {alert['most_recent_instance']['location']['path']}\n")
    else:
        print(f"Failed to retrieve alerts for branch {branch}: {response.status_code}")


if __name__ == "__main__":
    import sys

    branch = sys.argv[1]
    generate_report(branch)
