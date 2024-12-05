from fastapi import FastAPI

from common.middleware import custom_response_middleware

app = FastAPI()

app.middleware('http')(custom_response_middleware)

# Dummy 데이터
dummy_data = [
    {"id": 1, "name": "Alice", "age": 25},
    {"id": 2, "name": "Bob", "age": 30},
    {"id": 3, "name": "Charlie", "age": 35},
]


@app.get('/users')
async def root():
    return dummy_data