from fastapi import APIRouter, HTTPException, status
from sqlalchemy.exc import IntegrityError
from schemas.emotional_record import (
    EmotionalRecord,
    CreateEmotionalRecord,
    UpdateEmotionalRecord,
)
from repositories.emotional_records import (
    get_emotional_record,
    create_emotional_record,
    update_emotional_record,
    delete_emotional_record,
)

router = APIRouter(prefix="/emotional-records", tags=["emotional_records"])


@router.get("/{record_id}", response_model=EmotionalRecord)
def get_emotional_record_endpoint(record_id: str):
    record = get_emotional_record(record_id)
    if record is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Emotional record not found",
        )
    return record


@router.post("", response_model=EmotionalRecord, status_code=status.HTTP_201_CREATED)
def create_emotional_record_endpoint(record: CreateEmotionalRecord):
    try:
        created = create_emotional_record(
            emotional_state=record.emotional_state,
            patient_id=record.patient_id,
            recorded_at=record.recorded_at,
        )
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid patient ID reference",
        )
    return created


@router.put("/{record_id}", response_model=EmotionalRecord)
def update_emotional_record_endpoint(
    record_id: str, record: UpdateEmotionalRecord
):
    updated = update_emotional_record(
        record_id=record_id,
        emotional_state=record.emotional_state,
        recorded_at=record.recorded_at,
    )
    if updated is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Emotional record not found",
        )
    return updated


@router.delete("/{record_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_emotional_record_endpoint(record_id: str):
    deleted = delete_emotional_record(record_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Emotional record not found",
        )
    return None

