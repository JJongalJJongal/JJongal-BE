from fastapi import FastAPI
from enum import Enum

from fastapi.responses import FileResponse

from board import board_router
from user import user_router

import models
from database import engine
models.Base.metadata.create_all(bind=engine)

app = FastAPI(tags=["회원가입"])

app.include_router(board_router.app, tags=["[CCB] 회원가입 CRUD"])
app.include_router(user_router.app, tags=["[CCB] Test"])

#get_db()

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/items/{item}")
async def read_item(item):
    return {"item": item}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/")
def read_root():
    return FileResponse('user_list.html', tags=["회원가입"])