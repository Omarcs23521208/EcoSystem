
from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.modules.drop_and_go.schemas import (
    DropAndGoCreateInput,
    DropAndGoResponse,
)
from app.modules.drop_and_go.repository import DropAndGoRepository


router = APIRouter(
    prefix="/drop-and-go",
    tags=["Solicitudes Drop & Go (HU-003 / HU-011)"],
)


@router.post(
    "/requests",
    response_model=DropAndGoResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_drop_and_go_request(
    payload: DropAndGoCreateInput,
    db: Session = Depends(get_db),
):
    repo = DropAndGoRepository(db)
    return repo.create(payload)


@router.get(
    "/requests/citizen/{citizen_id}",
    response_model=List[DropAndGoResponse],
)
def get_citizen_requests(
    citizen_id: int,
    db: Session = Depends(get_db),
):
    repo = DropAndGoRepository(db)
    return repo.get_by_citizen(citizen_id)
