from fastapi import FastAPI
from pydantic import BaseModel

class Password(BaseModel):
    password: str


app = FastAPI()

@app.post("/check")
def read_root(password: Password):
    return {"message": password}