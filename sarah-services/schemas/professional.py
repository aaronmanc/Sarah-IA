from pydantic import BaseModel

class Professional(BaseModel):
    id:str
    first_name:str
    last_name:str
    specialty:str
    email:str
    phone:str
    health_center_id:str

class CreateProfessional(BaseModel):
    first_name:str
    last_name:str
    specialty:str
    email:str
    phone:str
    health_center_id:str

class UpdateProfessional(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    specialty: str | None = None
    email: str | None = None
    phone: str | None = None
    health_center_id: str | None = None