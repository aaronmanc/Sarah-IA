from fastapi import APIRouter, HTTPException, status
from sqlalchemy.exc import IntegrityError
from schemas.weight_record import (
    WeightRecord,
    CreateWeightRecord,
    UpdateWeightRecord,
)
from repositories.weight_records import (
    get_weight_record,
    list_weight_records,
    create_weight_record,
    update_weight_record,
    delete_weight_record,
)

router = APIRouter(prefix="/weight-records", tags=["weight_records"])


@router.get("/{record_id}", response_model=WeightRecord)
def get_weight_record_endpoint(record_id: str):
    record = get_weight_record(record_id)
    if record is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Weight record not found",
        )
    return record

@router.get("/weight", response_model=list[WeightRecord])
def list_weight_records_endpoint(patient_id: str | None = None):
    records = list_weight_records(patient_id=patient_id)
    return records


@router.post("", response_model=WeightRecord, status_code=status.HTTP_201_CREATED)
def create_weight_record_endpoint(record: CreateWeightRecord):
    try:
        created = create_weight_record(
            weight=record.weight,
            patient_id=record.patient_id,
            recorded_at=record.recorded_at,
        )
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid patient ID reference",
        )
    return created


@router.put("/{record_id}", response_model=WeightRecord)
def update_weight_record_endpoint(record_id: str, record: UpdateWeightRecord):
    updated = update_weight_record(
        record_id=record_id,
        weight=record.weight,
        recorded_at=record.recorded_at,
    )
    if updated is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Weight record not found",
        )
    return updated


@router.delete("/{record_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_weight_record_endpoint(record_id: str):
    deleted = delete_weight_record(record_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Weight record not found",
        )
    return None

