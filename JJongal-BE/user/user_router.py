
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from database import get_db

from datetime import datetime
from datetime import timedelta
from jose import jwt

from fastapi import APIRouter, Depends, status, HTTPException, Response, Request
from fastapi.security import OAuth2PasswordRequestForm

#from user import user_schema
#from user import user_schema, user_crud

import os
from dotenv import load_dotenv
""" 
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = float(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

 """
 # user 경로 맞잖아 왜 안 되는데 짜정나게 흥흥흥
app = APIRouter(
    prefix="/user"
)

@app.get(path="/test")
async def user_test():
    return {"message": "User test successful"}

@app.get(path="/logout")
async def logout(response: Response, request: Request):
    access_token = request.cookies.get("access_token")

    # 쿠키 삭제
    response.delete_cookie(key="access_token")

    response_body = {"message": "Logout successful"}
    return JSONResponse(status_code=status.HTTP_200_OK, content=response_body)

""" @app.post(path="/signup")
async def signup (new_user: user_schema.NewUserForm, db: Session = Depends(get_db)):
    return new_user """