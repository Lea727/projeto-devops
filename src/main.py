from fastapi import FastAPI

app = FastAPI()

@app.get("/helloworld")
async def root():
    return {"message": "Hello World"}

@app.get("/status")
async def get_status():
    return {"status": "online"}

def funcaoteste():
    return {"resultado": "sucesso"}

def soma(a, b):
    return a + b