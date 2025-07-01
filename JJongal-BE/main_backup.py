from fastapi import FastAPI
from enum import Enum

from fastapi.responses import FileResponse

import models
from database import engine
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

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
    return FileResponse('user_list.html')