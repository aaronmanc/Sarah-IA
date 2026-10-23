from fastapi import APIRouter, HTTPException, status
from sqlalchemy.exc import IntegrityError
from schemas.professional import Professional, CreateProfessional, UpdateProfessional
from repositories.professionals import (get_professional, list_professionals, create_professional, update_professional, delete_professional)

router = APIRouter(prefix="/professionals", tags=["professionals"])

@router.get("/{professional_id}", response_model=Professional)
def get_professional_endpoint(professional_id: str):
    prof = get_professional(professional_id)
    if prof is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Professional not found")
    return prof

@router.get("", response_model = list[Professional])
def list_professionals_endpoint():
    return list_professionals()

@router.post("", response_model=Professional, status_code=status.HTTP_201_CREATED)
def create_professional_endpoint(professional: CreateProfessional):
    try:
        created = create_professional(
            first_name=professional.first_name,
            last_name=professional.last_name,
            specialty=professional.specialty,
            email=professional.email,
            phone=professional.phone,
            health_center_id=professional.health_center_id,
        )
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid health center reference or duplicate email")
    return created

@router.put("/{professional_id}", response_model=Professional)
def update_professional_endpoint(professional_id: str, professional: UpdateProfessional):
    updated = update_professional(
        professional_id=professional_id,
        first_name=professional.first_name,
        last_name=professional.last_name,
        specialty=professional.specialty,
        email=professional.email,
        phone=professional.phone,
        health_center_id=professional.health_center_id,
    )
    if updated is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Professional not found")
    return updated

@router.delete("/{professional_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_professional_endpoint(professional_id: str):
    deleted = delete_professional(professional_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Professional not found")
    return None

