from pydantic import BaseModel

class ProfessionalPatient(BaseModel):
    professional_id: str
    patient_id: str

class CreateProfessionalPatient(BaseModel):
    professional_id: str
    patient_id: str