from pydantic import BaseModel

class SarahVersion(BaseModel):
    id: str
    nombre: str
    description: str

class CreateSarahVersion(BaseModel):
    nombre: str
    description: str

class UpdateSarahVersion(BaseModel):
    nombre: str | None = None
    description: str | None = None