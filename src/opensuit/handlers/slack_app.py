import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


def start_slack_connector(agent):
    print("OpenSuit Slack Connector is starting...")

    app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

    @app.event("app_mention")
    def handle_mentions(event, say):
        user_id = event["user"]
        text = event["text"]
        response = agent.process_request(text)
        say(f"{response}")

    print("OpenSuit Slack Connector is starting with Agent Brain...")
    handler = SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN"))
    handler.start()
