import unittest
from src.jira.jira_api import create_ticket
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class TestTicketCreation(unittest.TestCase):
    def test_create_ticket(self):
        summary = "Test1"
        description = "Testing the Jira Rest API"
        response = create_ticket(summary, description)
        self.assertIn("id", response, msg="Ticket creation failed, 'id' not found in response")
        print(response)

if __name__ == "__main__":
    unittest.main()
