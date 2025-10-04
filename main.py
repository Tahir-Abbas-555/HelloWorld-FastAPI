from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Name(BaseModel):
    firstname: str
    lastname: str

@app.get("/{text}")
def read_root(text: str):
    return 'Hello ' + text.capitalize()

@app.post("/postname")
def create_name(name: Name):
    return f"Hello {name.firstname.capitalize()} {name.lastname.capitalize()}"