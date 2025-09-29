from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Testando a pipeline novamente!!"}