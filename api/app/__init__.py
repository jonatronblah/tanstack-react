from fastapi import FastAPI

from app.api.main import router as api_router

app = FastAPI(root_path="/api/v1")
app.include_router(api_router)


@app.get("/hello", include_in_schema=False)
async def root():
    return {"message": "Hello World"}


@app.get("/goodbye", include_in_schema=False)
async def root2():
    return {"message": "goodbye!"}
