from datetime import datetime
from fastapi import HTTPException

from api.routers.conversations import create_conversation_endpoint, list_conversations_endpoint
from api.routers.messages import create_message_endpoint, list_messages_endpoint
from schemas.conversation import CreateConversation
from schemas.message import CreateMessage


def get_patient_conversations(patient_id: str):
    """Retrieves all distinct conversations associated with the given patient."""
    try:
        all_messages = list_messages_endpoint()
        
        # Collect unique conversation IDs for this patient
        patient_conv_ids = set()
        for msg in all_messages:
            if msg.patient_id == patient_id:
                patient_conv_ids.add(msg.conversation_id)

        # Get the corresponding conversation objects
        all_conversations = list_conversations_endpoint()
        patient_conversations = [c for c in all_conversations if c.id in patient_conv_ids]
        
        return patient_conversations
    except Exception as e:
        print(f"[ERROR] No se pudieron cargar las conversaciones: {e}")
        return []


def get_conversation_history(conversation_id: str):
    """Gets and chronologically sorts all messages within a specific conversation."""
    try:
        all_messages = list_messages_endpoint()
        conv_msgs = [m for m in all_messages if m.conversation_id == conversation_id]
        conv_msgs.sort(key=lambda m: m.created_at)
        return conv_msgs
    except Exception as e:
        print(f"[ERROR] No se pudo cargar el historial: {e}")
        return []


def send_message(patient_id: str):
    print("\n--- CHAT / MENSAJERÍA CON SARAH AI ---")

    sarah_version_id = input("Ingrese ID de versión de Sarah (Enter para 'v1.0'): ").strip() or "v1.0"

    existing_conversations = get_patient_conversations(patient_id)
    selected_conv_id = None

    if not existing_conversations:
        print("\n[INFO] No hay conversaciones previas. Creando una nueva conversación...")
        conv_payload = CreateConversation(created_at=datetime.now())
        new_conv = create_conversation_endpoint(conv_payload)
        selected_conv_id = new_conv.id
    else:
        print("\nConversaciones disponibles para este paciente:")
        for idx, conv in enumerate(existing_conversations, start=1):
            print(f"{idx}. Conversación ID: {conv.id} (Creada: {conv.created_at})")
        print(f"{len(existing_conversations) + 1}. Crear NUEVA conversación")
        print("0. Cancelar / Volver")

        choice = input("\nSeleccione una opción: ").strip()
        if choice == "0" or choice == ".":
            return

        try:
            choice_num = int(choice)
            if 1 <= choice_num <= len(existing_conversations):
                selected_conv_id = existing_conversations[choice_num - 1].id
            elif choice_num == len(existing_conversations) + 1:
                conv_payload = CreateConversation(created_at=datetime.now())
                new_conv = create_conversation_endpoint(conv_payload)
                selected_conv_id = new_conv.id
            else:
                print("[ERROR] Opción inválida.")
                return
        except ValueError:
            print("[ERROR] Entrada inválida. Debe ser un número.")
            return

    # Display conversation history
    print(f"\n=================== CHAT (ID: {selected_conv_id}) ===================")
    print("Escriba '.' para finalizar y volver al menú.")

    history = get_conversation_history(selected_conv_id)
    if history:
        print("\n--- Historial de Mensajes ---")
        for msg in history:
            sender_label = "Paciente" if msg.sender_type == "patient" else "Sarah AI"
            print(f"[{sender_label}]: {msg.content}")
        print("-----------------------------\n")

    # Interactive Messaging Loop
    try:
        while True:
            content = input("Paciente > ").strip()
            if content == ".":
                print("[INFO] Conversación finalizada.")
                break

            if not content:
                continue

            # Save Patient Message
            user_msg_payload = CreateMessage(
                conversation_id=selected_conv_id,
                sender_type="patient",
                sender_id=patient_id,
                content=content,
                created_at=datetime.now(),
                patient_id=patient_id,
                sarah_version_id=sarah_version_id,
                image_id=None,
                professional_id=None,
            )
            create_message_endpoint(user_msg_payload)

            # Generate & Save Simulated AI Response
            ai_simulated_response = (
                "Hola! Soy Sarah. He recibido tu mensaje y estoy procesando tus "
                "registros médicos para brindarte el mejor seguimiento."
            )

            ai_msg_payload = CreateMessage(
                conversation_id=selected_conv_id,
                sender_type="sarah",
                sender_id="sarah-ai-bot",
                content=ai_simulated_response,
                created_at=datetime.now(),
                patient_id=patient_id,
                sarah_version_id=sarah_version_id,
                image_id=None,
                professional_id=None,
            )
            create_message_endpoint(ai_msg_payload)

            print(f"Sarah AI  > {ai_simulated_response}")

    except HTTPException as e:
        print(f"[ERROR] Ocurrió un error en la mensajería: {e.detail}")
    except KeyboardInterrupt:
        print("\n[INFO] Conversación terminada.")