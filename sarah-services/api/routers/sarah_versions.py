from fastapi import APIRouter, HTTPException, status
from schemas.sarah_version import SarahVersion, CreateSarahVersion, UpdateSarahVersion
from repositories.sarah_versions import (get_sarah_version, create_sarah_version, update_sarah_version, delete_sarah_version)

router = APIRouter(prefix="/sarah-versions", tags=["sarah_versions"])

@router.get("/{version_id}", response_model=SarahVersion)
def get_sarah_version_endpoint(version_id: str):
    ver = get_sarah_version(version_id)
    if ver is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sarah version not found")
    return ver

@router.post("", response_model=SarahVersion, status_code=status.HTTP_201_CREATED)
def create_sarah_version_endpoint(version: CreateSarahVersion):
    return create_sarah_version(nombre=version.nombre, description=version.description)

@router.put("/{version_id}", response_model=SarahVersion)
def update_sarah_version_endpoint(version_id: str, version: UpdateSarahVersion):
    updated = update_sarah_version(version_id, nombre=version.nombre, description=version.description)
    if updated is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sarah version not found")
    return updated

@router.delete("/{version_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sarah_version_endpoint(version_id: str):
    deleted = delete_sarah_version(version_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sarah version not found")
    return None

