import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get environment variables
email = os.getenv("EMAIL")
api_key = os.getenv("API_KEY")
jira_domain = os.getenv("JIRA_DOMAIN")
project_key = os.getenv("JIRA_PROJECT_KEY")

# Construct the URL
url = f"https://{jira_domain}.atlassian.net/rest/api/2/issue"
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}
auth = (email, api_key)

# Function to create a Jira ticket
def create_ticket(summary, description, issue_type="Task"):
    payload = json.dumps({
        "fields": {
            "project": {
                "key": project_key
            },
            "summary": summary,
            "description": description,
            "issuetype": {
                "name": issue_type
            }
        }
    })

    response = requests.post(url, headers=headers, data=payload, auth=auth)
    return response.json()

# Example usage
if __name__ == "__main__":
    summary = "Test1"
    description = "Testing the Jira Rest API"
    response = create_ticket(summary, description)
    print(response)
