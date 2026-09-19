from fastapi import FastAPI

from app.api.chat import router as chat_router


app = FastAPI(
    title="AI Engineering Copilot",
    version="0.1.0",
)


app.include_router(chat_router)


@app.get("/")
def root():
    return {
        "message": "AI Engineering Copilot is running",
        "version": "0.1.0",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }