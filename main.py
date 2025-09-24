from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Meu Pipeline CI/CD Funciona!"}