from fastapi import APIRouter, HTTPException, status
from schemas.conversation import (
    Conversation,
    CreateConversation,
)
from repositories.conversations import (
    get_conversation,
    create_conversation,
    delete_conversation,
    list_conversations
)

router = APIRouter(prefix="/conversations", tags=["conversations"])


@router.get("/{conversation_id}", response_model=Conversation)
def get_conversation_endpoint(conversation_id: str):
    conv = get_conversation(conversation_id)
    if conv is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conversation not found",
        )
    return conv

@router.get("", response_model=list[Conversation])
def list_conversations_endpoint():
    return list_conversations()

@router.post("", response_model=Conversation, status_code=status.HTTP_201_CREATED)
def create_conversation_endpoint(conversation: CreateConversation):
    return create_conversation(created_at=conversation.created_at)


@router.delete("/{conversation_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_conversation_endpoint(conversation_id: str):
    deleted = delete_conversation(conversation_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conversation not found",
        )
    return None

