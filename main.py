from fastapi import FastAPI, Body
from cat_logic import *
import requests 
import os
import uvicorn


app = FastAPI()

# Handle GroupMe messages, return 200 status(success)
@app.post('/', status_code=200)
def handle_groupme_message(text: str = Body(), sender_type: str = Body()):
    if 'cat' in text.lower() and sender_type == 'user':
        post_groupme_message(get_cat_pic())
        return

def post_groupme_message(link):
    # GroupMe's Bot API Endpoint
    url = 'https://api.groupme.com/v3/bots/post'
    # Bot message data
    groupme_parameters = {
        'bot_id': os.getenv('BOT_ID'), 
        'text': link
    }
    # Post message
    requests.post(url, json = groupme_parameters)

# Check app liveness
@app.get('/live', status_code=200)
def run_live():
    return "live"

# Used by GroupMe url validation
@app.head('/', status_code=200)
def run_head():
    return

uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('PORT')))