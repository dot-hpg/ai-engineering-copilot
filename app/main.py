from fastapi import FastAPI

app = FastAPI(
    title="AI Engineering Copilot",
    version="0.1.0",
)


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