import uuid

from sqlalchemy import Column
from sqlalchemy import String

from db.database import Base


class SecurityEvent(Base):

    __tablename__ = "security_events"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    event_type = Column(String)

    user_email = Column(String)

    description = Column(String)