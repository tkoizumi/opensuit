import os

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from mangum import Mangum
from slack_bolt import App as SlackApp
from slack_bolt.adapter.fastapi import SlackRequestHandler

from opensuit.core.agent import Agent

load_dotenv()
app = FastAPI(title="OpenSuit API")
agent = Agent()

slack_app = SlackApp(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
    process_before_response=True,
)
slack_handler = SlackRequestHandler(slack_app)


@slack_app.event("app_mention")
def handle_app_mentions(event, say):
    raw_text = event.get("text", "")
    clean_query = raw_text.split(">")[-1].strip()

    response = agent.process_request(clean_query)
    say(f"Agent Response: {response}")


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
