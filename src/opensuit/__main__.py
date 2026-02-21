import os

# Set SSL certificate path for Slack API requests
import certifi
os.environ['SSL_CERT_FILE'] = certifi.where()

from dotenv import load_dotenv

from opensuit.main import Agent
from opensuit.slack_app import start_slack_connector


def run():
    load_dotenv()
    agent = Agent()
    start_slack_connector(agent)


if __name__ == "__main__":
    run()
