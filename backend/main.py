from fastapi import FastAPI

app = FastAPI(
    title="Enterprise SaaS Cloud Security Platform",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Enterprise SaaS Cloud Security Platform API"
    }