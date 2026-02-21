from dotenv import load_dotenv

from opensuit.agent import Agent
from opensuit.handlers.slack_app import start_slack_connector


def run():
    load_dotenv()
    agent = Agent()
    start_slack_connector(agent)
