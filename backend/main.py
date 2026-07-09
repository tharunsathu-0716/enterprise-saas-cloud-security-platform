from fastapi import FastAPI

from db.database import Base
from db.database import engine

from api.auth import router as auth_router
from api.organizations import router as organization_router
from api.security_events import router as security_event_router

import models.user
import models.organization
import models.security_event


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Enterprise SaaS Cloud Security Platform",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(organization_router)
app.include_router(security_event_router)

@app.get("/")
def root():
    return {
        "message": "Enterprise SaaS Cloud Security Platform API"
    }