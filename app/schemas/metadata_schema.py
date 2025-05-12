from typing import Optional

from pydantic import BaseModel


class MetadataBase(BaseModel):
    name: str
    description: str


class MetadataCreate(MetadataBase):
    pass


class MetadataUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class MetadataResponse(MetadataBase):
    id: int

    class Config:
        orm_mode = True
