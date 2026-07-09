from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from db.database import get_db
from models.security_event import SecurityEvent

router = APIRouter(
    prefix="/security-events",
    tags=["Security Events"]
)


@router.get("/")
def get_security_events(
    db: Session = Depends(get_db)
):

    events = db.query(
        SecurityEvent
    ).all() 

    return events