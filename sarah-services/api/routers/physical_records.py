from fastapi import APIRouter, HTTPException, status
from sqlalchemy.exc import IntegrityError
from schemas.physical_record import (
    PhysicalActivityRecord,
    CreatePhysicalActivityRecord,
    UpdatePhysicalActivityRecord,
)
from repositories.physical_records import (
    get_physical_activity_record,
    create_physical_activity_record,
    update_physical_activity_record,
    delete_physical_activity_record,
)

router = APIRouter(prefix="/physical-records", tags=["physical_records"])

@router.get("/{record_id}", response_model=PhysicalActivityRecord)
def get_physical_record_endpoint(record_id: str):
    record = get_physical_activity_record(record_id)
    if record is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Physical activity record not found",
        )
    return record


@router.post("", response_model=PhysicalActivityRecord, status_code=status.HTTP_201_CREATED)
def create_physical_record_endpoint(record: CreatePhysicalActivityRecord):
    try:
        created = create_physical_activity_record(
            activity_type=record.activity_type,
            duration=record.duration,
            patient_id=record.patient_id,
            recorded_at=record.recorded_at,
        )
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid patient ID reference",
        )
    return created


@router.put("/{record_id}", response_model=PhysicalActivityRecord)
def update_physical_record_endpoint(record_id: str, record: UpdatePhysicalActivityRecord):
    updated = update_physical_activity_record(
        record_id=record_id,
        activity_type=record.activity_type,
        duration=record.duration,
        recorded_at=record.recorded_at,
    )
    if updated is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Physical activity record not found",
        )
    return updated


@router.delete("/{record_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_physical_record_endpoint(record_id: str):
    deleted = delete_physical_activity_record(record_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Physical activity record not found",
        )
    return None

