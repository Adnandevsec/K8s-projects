from fastapi import FastAPI
import os

app = FastAPI()


APP_TITLE = os.getenv("APP_TITLE", "Default Title")
DB_PASSWORD = os.getenv("DB_PASSWORD", "default-secret")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

@app.get("/")
def read_root():
    return {
        "message": f"Welcome to {APP_TITLE}!",
        "secret_loaded": f"Password length is {len(DB_PASSWORD)} characters",
        "environment": f"current env is {ENVIRONMENT}"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}