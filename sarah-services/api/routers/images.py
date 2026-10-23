from fastapi import APIRouter, HTTPException, status
from schemas.image import Image, CreateImage
from repositories.images import (
    get_image,
    create_image,
    delete_image,
)

router = APIRouter(prefix="/images", tags=["images"])


@router.get("/{image_id}", response_model=Image)
def get_image_endpoint(image_id: str):
    img = get_image(image_id)
    if img is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Image not found"
        )
    return img


@router.post("", response_model=Image, status_code=status.HTTP_201_CREATED)
def create_image_endpoint(image: CreateImage):
    return create_image(
        file_reference=image.file_reference,
        image_type=image.image_type,
        description=image.description,
    )



@router.delete("/{image_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_image_endpoint(image_id: str):
    deleted = delete_image(image_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Image not found"
        )
    return None

