from fastapi import FastAPI

from db.database import Base
from db.database import engine

import models.user

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Enterprise SaaS Cloud Security Platform",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Enterprise SaaS Cloud Security Platform API"
    }