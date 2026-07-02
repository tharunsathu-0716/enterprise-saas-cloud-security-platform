from fastapi import FastAPI

from db.database import Base
from db.database import engine
from api.auth import router as auth_router

import models.user

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Enterprise SaaS Cloud Security Platform",
    version="1.0.0"
)

app.include_router(auth_router)

@app.get("/")
def root():
    return {
        "message": "Enterprise SaaS Cloud Security Platform API"
    }