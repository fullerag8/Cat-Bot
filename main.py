from fastapi import FastAPI, Body
from cat_logic import *
import requests 
import os
import uvicorn


app = FastAPI()


@app.post('/', status_code=200)
def handle_groupme_message(text: str = Body(), sender_type: str = Body()):
    if 'cat' in text and sender_type == 'user':
        post_groupme_message(get_cat_pic())
        return 

def post_groupme_message(link):
    url = 'https://api.groupme.com/v3/bots/post'
    groupme_parameters = {
        'bot_id': os.getenv('BOT_ID'), 
        'text': link
    }
    requests.post(url, json = groupme_parameters)

uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('PORT')))

@app.get('/live', status_code=200)
def run_live():
    return "live"
