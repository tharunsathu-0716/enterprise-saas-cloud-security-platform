from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from db.database import get_db
from models.organization import Organization
from schemas.organization import OrganizationCreate

router = APIRouter(
    prefix="/organizations",
    tags=["Organizations"]
)


@router.post("/")
def create_organization(
    organization: OrganizationCreate,
    db: Session = Depends(get_db)
):

    existing_org = (
        db.query(Organization)
        .filter(
            Organization.name == organization.name
        )
        .first()
    )

    if existing_org:
        raise HTTPException(
            status_code=400,
            detail="Organization already exists"
        )

    new_org = Organization(
        name=organization.name
    )

    db.add(new_org)
    db.commit()
    db.refresh(new_org)

    return {
        "id": new_org.id,
        "name": new_org.name
    }