from fastapi import FastAPI

app = FastAPI(
    title="Nexora",
    description="AI-powered WhatsApp accounting assistant",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "Nexora API",
        "status": "running",
    }