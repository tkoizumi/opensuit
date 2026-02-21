import os
from pathlib import Path

import certifi
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from mangum import Mangum
from slack_bolt import App as SlackApp
from slack_bolt.adapter.fastapi import SlackRequestHandler
from slack_bolt.oauth.oauth_settings import OAuthSettings
from slack_sdk.oauth.installation_store import FileInstallationStore

from opensuit.core.agent import Agent

BASE_DIR = Path(__file__).resolve().parent.parent.parent
env_path = BASE_DIR / ".env"
load_dotenv(dotenv_path=env_path)

oauth_settings = OAuthSettings(
    client_id=os.environ.get("SLACK_CLIENT_ID"),
    client_secret=os.environ.get("SLACK_CLIENT_SECRET"),
    scopes=["app_mentions:read", "chat:write"],  # Add any other scopes you need
    installation_store=FileInstallationStore(base_dir="./data"),
)

os.environ["SSL_CERT_FILE"] = certifi.where()

app = FastAPI(title="OpenSuit API")
agent = Agent()

slack_app = SlackApp(
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
    oauth_settings=oauth_settings,
    process_before_response=True,
)
slack_handler = SlackRequestHandler(slack_app)


@slack_app.event("app_mention")
def handle_app_mentions(event, say):
    raw_text = event.get("text", "")
    clean_query = raw_text.split(">")[-1].strip()

    response = agent.process_request(clean_query)
    say(f"Agent Response: {response}")


@app.get("/slack/install")
async def install(req: Request):
    return await slack_handler.handle(req)


@app.get("/slack/oauth_redirect")
async def oauth_redirect(req: Request):
    return await slack_handler.handle(req)


@app.post("/slack/events")
async def slack_events_endpoint(req: Request):
    return await slack_handler.handle(req)


@app.get("/health")
async def health_check():
    return {"status": "online", "service": "opensuit"}


handler = Mangum(app)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
