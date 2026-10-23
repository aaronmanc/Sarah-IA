from fastapi import APIRouter, HTTPException, status
from sqlalchemy.exc import IntegrityError
from schemas.professional_patient import ProfessionalPatient, CreateProfessionalPatient
from repositories.professional_patients import (
    get_professional_patient,
    list_professional_patients,
    create_professional_patient,
    delete_professional_patient,
)

router = APIRouter(prefix="/professional-patients", tags=["professional_patients"])


@router.get("", response_model=ProfessionalPatient)
def get_professional_patient_endpoint(professional_id: str, patient_id: str):
    rel = get_professional_patient(professional_id, patient_id)
    if rel is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Association not found",
        )
    return rel

@router.get("", response_model=list[ProfessionalPatient])
def list_professional_patients_endpoint():
    return list_professional_patients()

@router.post("", response_model=ProfessionalPatient, status_code=status.HTTP_201_CREATED)
def create_professional_patient_endpoint(data: CreateProfessionalPatient):
    try:
        created = create_professional_patient(
            professional_id=data.professional_id,
            patient_id=data.patient_id,
        )
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid professional or patient ID reference",
        )
    return created


@router.delete("", status_code=status.HTTP_204_NO_CONTENT)
def delete_professional_patient_endpoint(professional_id: str, patient_id: str):
    deleted = delete_professional_patient(professional_id, patient_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Association not found",
        )
    return None

