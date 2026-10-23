from pydantic import BaseModel

class Image(BaseModel):
    id: str
    file_reference: str
    image_type: str
    description: str

class CreateImage(BaseModel):
    file_reference: str
    image_type: str
    description: str