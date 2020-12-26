from typing import Optional
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse
import redis 
import time
import markdown
import jinja2
import aiofiles

app = FastAPI()
cache = redis.Redis(host='0.0.0.0', port=6379)
templates = Jinja2Templates(directory='static/')

def get_hit_count(): # Hit Counter for Visit. Stored in Redis. Should Revamp Hit-Counter as Retries should be exponential.
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.get('/')
def main(request: Request): # This code makes no sense don't worry. This is some experimental stuff for importing markdown into FastAPI
    with open("README.md", "r", encoding="utf-8") as input_file:
        text = input_file.read()
    html = markdown.markdown(text)
    return templates.TemplateResponse("main.html", {"request": request})

@app.get('/hits') # Main Function
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.'.format(count)



