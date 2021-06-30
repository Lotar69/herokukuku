from fastapi import FastAPI
import uvicorn
import pandas as pd


app = FastAPI()



@app.get("/")
async def root():
    return {"message": "ONLINE"}



@app.get("/test/{key_word}")
async def test(key_word):
    return f" le keyword est {key_word}"























if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


