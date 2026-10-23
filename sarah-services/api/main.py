from fastapi import FastAPI
from api.routers import patients

app = FastAPI(
    title = "Sarah Services",
    description = "API de servicios de sistema Sarah",
    version = "1.0.0",
)

@app.get("/")
def root ():
    return {
        "message": "Sarah Services funcionando"
    }

app.include_router(patients.router)