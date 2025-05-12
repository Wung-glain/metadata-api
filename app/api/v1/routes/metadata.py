from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import models
from app.db.deps import get_db
from app.schemas import metadata_schema
from app.services import metadata_service

router = APIRouter()
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.schemas import metadata_schema
from app.services import metadata_service

router = APIRouter()


# READ all
@router.get("/metadata", response_model=list[metadata_schema.MetadataResponse])
def read_metadata(db: Session = Depends(get_db)):
    return metadata_service.get_all_metadata(db)


# CREATE
@router.post(
    "/metadata",
    response_model=metadata_schema.MetadataResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_metadata(
    metadata: metadata_schema.MetadataCreate, db: Session = Depends(get_db)
):
    return metadata_service.create_metadata(db, metadata)


# UPDATE  (full/partial)
@router.patch(
    "/metadata/{metadata_id}",
    response_model=metadata_schema.MetadataResponse,
)
def update_metadata(
    metadata_id: int,
    metadata_in: metadata_schema.MetadataUpdate,
    db: Session = Depends(get_db),
):
    updated = metadata_service.update_metadata(db, metadata_id, metadata_in)
    if not updated:
        raise HTTPException(status_code=404, detail="Metadata not found")
    return updated


# DELETE
@router.delete(
    "/metadata/{metadata_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_metadata(metadata_id: int, db: Session = Depends(get_db)):
    deleted = metadata_service.delete_metadata(db, metadata_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Metadata not found")


@router.get("/metadata", response_model=list[metadata_schema.MetadataResponse])
def read_metadata(db: Session = Depends(get_db)):
    return metadata_service.get_all_metadata(db)


@router.post("/metadata", response_model=metadata_schema.MetadataResponse)
def create_metadata(
    metadata: metadata_schema.MetadataCreate, db: Session = Depends(get_db)
):
    return metadata_service.create_metadata(db, metadata)
