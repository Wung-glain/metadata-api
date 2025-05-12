from sqlalchemy.orm import Session

from app.db import models
from app.schemas import metadata_schema


def get_all_metadata(db: Session):
    return db.query(models.Metadata).all()


def get_metadata_by_id(db: Session, metadata_id: int):
    return db.query(models.Metadata).filter(models.Metadata.id == metadata_id).first()


def create_metadata(db: Session, metadata: metadata_schema.MetadataCreate):
    db_metadata = models.Metadata(**metadata.dict())
    db.add(db_metadata)
    db.commit()
    db.refresh(db_metadata)
    return db_metadata


def update_metadata(
    db: Session, metadata_id: int, metadata_in: metadata_schema.MetadataUpdate
):
    db_metadata = get_metadata_by_id(db, metadata_id)
    if not db_metadata:
        return None

    for field, value in metadata_in.dict(exclude_unset=True).items():
        setattr(db_metadata, field, value)

    db.commit()
    db.refresh(db_metadata)
    return db_metadata


def delete_metadata(db: Session, metadata_id: int):
    db_metadata = get_metadata_by_id(db, metadata_id)
    if not db_metadata:
        return None
    db.delete(db_metadata)
    db.commit()
    return db_metadata
