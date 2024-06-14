from fastapi import FastAPI

from app.tasks import process

app = FastAPI(root_path='/api/v1')


@app.get("/hello")
async def root():
    return {"message": "Hello World"}


@app.get("/goodbye")
async def root2():
    return {"message": "goodbye!"}
