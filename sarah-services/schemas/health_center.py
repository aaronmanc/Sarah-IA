from pydantic import BaseModel

class HealthCenter(BaseModel):
    id: str
    name: str
    city: str

class CreateHealthCenter(BaseModel):
    name: str
    city: str

class UpdateHealthCenter(BaseModel):
    name: str | None = None
    city: str | None = None