from typing import Optional
from fastapi import Depends, FastAPI, Request, Form, HTTPException, status, Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from starlette.responses import FileResponse
import redis 
import time
import markdown
import jinja2
import aiofiles

# Use this command to start the application: uvicorn main:app --host 0.0.0.0 --port 5050
print("uvicorn main:app --port 5050")
# Misc array of Variables and Class Instances
app = FastAPI(root_path="/api")
cache = redis.Redis(host='0.0.0.0', port=6379)
templates = Jinja2Templates(directory='static/')
# Actual Backend Logic for Redis Functions 
is_redis_available(cache)
def is_redis_available(r):
    try:
        r.ping()
        print("Redis is loaded on port 6379!")
    except (redis.exceptions.ConnectionError, ConnectionRefusedError):
        print("Redis is not loaded on port 6379! Switching to alternative listening of port 6000")
        return redis.Redis(host='0.0.0.0', port=6000)
    return True

if is_redis_available(r):
    cache = redis.Redis(host='0.0.0.0', port=6379) 
else:
    cache = redis.Redis(host='0.0.0.0', port=6000)
    


def add_redis(obj): # General increase or adding values to Redis objects and values. Must be a str.
    retries = 10
    while True:
        try:
            return cache.incr(obj)
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

def get_redis(obj): # General retriever function for getting Redis Objects and Values. Must be a str.
    retries = 10
    while True:
        try:
            return cache.get(obj)
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5) 

def set_redis(obj): # General setting function for getting Redis Objects and Values. Can be any value or variable type
    retries = 10
    while True:
        try:
            return cache.get(obj)
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5) 

# Base User Model 
class User(BaseModel):
    username: str
    email: Optional[str] = None
    disabled: Optional[bool] = None 

# Authentication code 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def fake_decode_token(token): 
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user

# FastAPI Authentication Functions
@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
# FastAPI General Endpoint Functions 
@app.get('/')
async def main(request: Request): # This code makes no sense don't worry. This is some experimental stuff for importing markdown into FastAPI
    with open("README.md", "r", encoding="utf-8") as input_file:
        text = input_file.read()
    html = markdown.markdown(text)
    return templates.TemplateResponse("main.html", {"request": request})

@app.get('/hits') # Main Function
async def hello():
    count = add_redis('hits')
    hits = '{"hitCounter":%d}' % (count)
    return Response(content=hits, media_type="application/json") 

@app.get('/kfc') 
async def kfc():
    kfc = get_redis('kfc')
    return Response(content=kfc, media_type="application/json") 




