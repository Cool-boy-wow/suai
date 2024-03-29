from fastapi import FastAPI, Request
import logging
from github3 import GitHub

app = FastAPI()

logging.basicConfig(filename='events.log', level=logging.INFO)

@app.post("/webhook")
async def webhook(request: Request):
    body = await request.json()
    event_type = request.headers.get('X-GitHub-Event')
    if event_type == 'push':
        logging.info(f"Push event detected: {body}")
    elif event_type == 'merge':
        logging.info(f"Merge event detected: {body}")
    return {"status": "ok"}
    