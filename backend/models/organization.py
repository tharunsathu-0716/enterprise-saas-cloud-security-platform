import uuid

from sqlalchemy import Column
from sqlalchemy import String

from db.database import Base


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    name = Column(
        String,
        unique=True,
        nullable=False
    )