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
print("uvicorn main:app --host 0.0.0.0 --port 5050")
# Misc array of Variables and Class Instances
app = FastAPI()
cache = redis.Redis(host='0.0.0.0', port=6379)
templates = Jinja2Templates(directory='static/')
# Actual Backend Logic 
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

# Fake User DB 
fake_users_db = {
    "tycherms": {
        "username": "tycherms",
        "full_name": "Ty Chermsirivatana",
        "email": "professornitro@gmail.com",
        "hashed_password": "fakehashedorion12",
        "disabled": False,
    },
    "jimmybob": {
        "username": "jimmybob",
        "full_name": "Jimmy Boberson",
        "email": "jimmybob5@gmail.com",
        "hashed_password": "fakehashedjimmybob24",
        "disabled": False,
    },
}
# Authentication Functions and Code  
def fake_hash_password(password: str):
    return "fakehashed" + password


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


class UserInDB(User):
    hashed_password: str


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(fake_users_db, token)
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user 

# FastAPI Authentication Endpoints
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}


@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

# FastAPI General Endpoint functions 
@app.get('/')
def main(request: Request): # This code makes no sense don't worry. This is some experimental stuff for importing markdown into FastAPI
    with open("README.md", "r", encoding="utf-8") as input_file:
        text = input_file.read()
    html = markdown.markdown(text)
    return templates.TemplateResponse("main.html", {"request": request})

@app.get('/hits') # Main Function
def hello():
    count = add_redis('hits')
    hits = '{"hitCounter":%d}' % (count)
    return Response(content=hits, media_type="application/json") 

@app.get('/kfc') 
def kfc():
    kfc = get_redis('kfc')
    return Response(content=kfc, media_type="application/json") 




