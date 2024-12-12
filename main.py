from fastapi import FastAPI
from common.middleware import custom_response_middleware
from contextlib import asynccontextmanager
from database import connect_to_mongo, close_mongo_connect
from routes import user

@asynccontextmanager
async def lifespan(app: FastAPI):
    # start the database connection
    await connect_to_mongo(app)
    yield
    # Close database connection
    await close_mongo_connect(app)

app = FastAPI(lifespan=lifespan)

app.middleware('http')(custom_response_middleware)

app.include_router(user.router, prefix="/users", tags=["users"])

@app.get('/')
def read_root():
    return {"Hello World"}
