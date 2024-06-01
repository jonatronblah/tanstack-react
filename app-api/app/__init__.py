from fastapi import FastAPI

app = FastAPI(root_path='/api/v1')


@app.get("/hello")
async def root():
    return {"message": "Hello World"}
