from fastapi import APIRouter, HTTPException, status, Query
from typing import List, Optional
from sqlalchemy.exc import IntegrityError
from schemas.food_record import FoodRecord, CreateFoodRecord, UpdateFoodRecord
from repositories.food_records import (
    get_food_record,
    list_food_records,
    create_food_record,
    update_food_record,
    delete_food_record,
)

router = APIRouter(prefix="/food-records", tags=["food_records"])


@router.get("/{record_id}", response_model=FoodRecord)
def get_food_record_endpoint(record_id: str):
    record = get_food_record(record_id)
    if record is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Food record not found",
        )
    return record

@router.get("/food", response_model=list[FoodRecord])
def list_food_records_endpoint(patient_id: str | None = None):
    records = list_food_records(patient_id=patient_id)
    return records

@router.post("", response_model=FoodRecord, status_code=status.HTTP_201_CREATED)
def create_food_record_endpoint(record: CreateFoodRecord):
    try:
        created = create_food_record(
            description=record.description,
            patient_id=record.patient_id,
            recorded_at=record.recorded_at,
        )
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid patient ID reference",
        )
    return created


@router.put("/{record_id}", response_model=FoodRecord)
def update_food_record_endpoint(record_id: str, record: UpdateFoodRecord):
    updated = update_food_record(
        record_id=record_id,
        description=record.description,
        recorded_at=record.recorded_at,
    )
    if updated is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Food record not found",
        )
    return updated


@router.delete("/{record_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_food_record_endpoint(record_id: str):
    deleted = delete_food_record(record_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Food record not found",
        )
    return None

