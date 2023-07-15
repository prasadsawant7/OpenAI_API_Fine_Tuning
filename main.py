from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import json
from chatbot import get_completion

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Data(BaseModel):
    prompt: str


@app.get("/")
def index():
    response = {"Message": "Successfully Connected!"}
    return response


@app.post("/chat")
def send_message(data: Data):
    try:
        completion = get_completion(data.prompt)
        response = {"status": "ok", "completion": completion}
        return response
    except Error as e:
        response = {"status": "Something went wrong"}
        return response
