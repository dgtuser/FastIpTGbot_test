from fastapi import FastAPI
from weather import getForecast
import uvicorn
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello"}

@app.get("/weather")
async def weather(q: str, days: int):
    return getForecast(q, days)

# if __name__ == '__main__':
#     uvicorn.run(app, host='0.0.0.0', port=8080)
