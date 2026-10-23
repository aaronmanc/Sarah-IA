from fastapi import APIRouter, HTTPException, status
from sqlalchemy.exc import IntegrityError
from schemas.health_center import HealthCenter, CreateHealthCenter, UpdateHealthCenter
from repositories.health_centers import (get_health_center, list_health_centers, create_health_center, update_health_center, delete_health_center)

router = APIRouter(prefix="/health-centers", tags=["health_centers"])

@router.get("/{health_center_id}", response_model=HealthCenter)
def get_health_center_endpoint(health_center_id: str):
    hc = get_health_center(health_center_id)
    if hc is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Health center not found")
    return hc

@router.get("", response_model=list[HealthCenter])
def list_health_centers_endpoint():
    return list_health_centers()

@router.post("", response_model=HealthCenter, status_code=status.HTTP_201_CREATED)
def create_health_center_endpoint(health_center: CreateHealthCenter):
    try:
        created = create_health_center(name=health_center.name, city=health_center.city)
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Health center already exists")
    return created

@router.put("/{health_center_id}", response_model=HealthCenter)
def update_health_center_endpoint(health_center_id: str, health_center: UpdateHealthCenter):
    updated = update_health_center(health_center_id, name=health_center.name, city=health_center.city)
    if updated is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Health center not found")
    return updated

@router.delete("/{health_center_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_health_center_endpoint(health_center_id: str):
    deleted = delete_health_center(health_center_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Health center not found")
    return None

