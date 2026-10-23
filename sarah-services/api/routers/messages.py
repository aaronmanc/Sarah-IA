from fastapi import APIRouter, HTTPException, status
from sqlalchemy.exc import IntegrityError
from schemas.message import Message, CreateMessage, UpdateMessage
from repositories.messages import (
    get_message,
    create_message,
    update_message,
    list_messages
)

router = APIRouter(prefix="/messages", tags=["messages"])


@router.get("/{message_id}", response_model=Message)
def get_message_endpoint(message_id: str):
    msg = get_message(message_id)
    if msg is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Message not found"
        )
    return msg

@router.get("", response_model=list[Message])
def list_messages_endpoint():
    return list_messages()

@router.post("", response_model=Message, status_code=status.HTTP_201_CREATED)
def create_message_endpoint(message: CreateMessage):
    try:
        created = create_message(
            conversation_id=message.conversation_id,
            sender_type=message.sender_type,
            sender_id=message.sender_id,
            content=message.content,
            created_at=message.created_at,
            image_id=message.image_id,
            patient_id=message.patient_id,
            professional_id=message.professional_id,
            sarah_version_id=message.sarah_version_id,
        )
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid foreign key reference in message data",
        )
    return created


@router.put("/{message_id}", response_model=Message)
def update_message_endpoint(message_id: str, message: UpdateMessage):
    updated = update_message(
        message_id=message_id,
        content=message.content,
        sender_type=message.sender_type,
        sender_id=message.sender_id,
        image_id=message.image_id,
    )
    if updated is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Message not found"
        )
    return updated


@router.delete("/{message_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_message_endpoint(message_id: str):
    deleted = delete_message(message_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Message not found"
        )
    return None

