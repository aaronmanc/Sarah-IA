from datetime import date, datetime

from repositories.patients import (create_patient, get_patient, delete_patient)
from repositories.health_centers import (create_health_center, get_health_center, delete_health_center)
from repositories.professionals import (create_professional, get_professional, delete_professional)
from repositories.sarah_versions import (create_sarah_version, get_sarah_version, delete_sarah_version)
from repositories.conversations import (create_conversation, get_conversation, delete_conversation)
from repositories.messages import (create_message, get_message)
from repositories.images import (create_image, get_image, delete_image)
from repositories.weight_records import (create_weight_record, get_weight_record, delete_weight_record)
from repositories.food_records import (create_food_record, get_food_record, delete_food_record)
from repositories.emotional_records import (create_emotional_record, get_emotional_record, delete_emotional_record)
from repositories.physical_records import (create_physical_activity_record, get_physical_activity_record, delete_physical_activity_record)
from repositories.professional_patients import (create_professional_patient, get_professional_patient, delete_professional_patient)

#################################
# INSERT
#################################

# Patients & Professionals
health_center = create_health_center(name="Hospital Central", city="Valdivia")
sarah_ver = create_sarah_version(nombre="v1.0", description="Initial stable version")

patient = create_patient(
    first_name="Juan",
    last_name="Pérez",
    rut="12345678-9",
    birth_date=date(1990, 5, 15),
    sex="M",
    email="juan.perez@example.com",
    phone="+56912345678",
    current_height=1.75,
    current_weight=70.5,
    lives_alone=False,
    bmi=23.0,
    context="None",
    psychological_profile="Stable",
)

professional = create_professional(
    first_name="Maria",
    last_name="Gomez",
    specialty="Cardiology",
    email="maria.gomez@example.com",
    phone="+56987654321",
    health_center_id=health_center.id,
)

create_professional_patient(professional_id=professional.id, patient_id=patient.id)

# Records
weight_rec = create_weight_record(weight=70.5, patient_id=patient.id)
food_rec = create_food_record(description="Salad and chicken", patient_id=patient.id)
emotional_rec = create_emotional_record(emotional_state="Happy", patient_id=patient.id)
activity_rec = create_physical_activity_record(activity_type="Running", duration=30.0, patient_id=patient.id)

# Conversations
conversation = create_conversation()

image = create_image(
    description="X-Ray result",
    image_type="png",
    file_reference="/files/xray.png",
)


message = create_message(
    conversation_id=conversation.id ,
    sender_type="patient",
    sender_id=patient.id,
    content="Hello Sarah, how are you?",
    created_at=datetime.now(),
    image_id=image.id,
    patient_id=patient.id,
    professional_id=professional.id,
    sarah_version_id=sarah_ver.id,
)
print("[SUCCESS] All test records inserted successfully!")


#################################
# GET
#################################

fetched_hc = get_health_center(health_center.id)
fetched_sv = get_sarah_version(sarah_ver.id)
fetched_patient = get_patient(patient.id)
fetched_prof = get_professional(professional.id)
fetched_rel = get_professional_patient(professional.id, patient.id)
fetched_weight = get_weight_record(weight_rec.id)
fetched_food = get_food_record(food_rec.id)
fetched_emotional = get_emotional_record(emotional_rec.id)
fetched_activity = get_physical_activity_record(activity_rec.id)
fetched_conv = get_conversation(conversation.id)
fetched_msg = get_message(message.id)
fetched_img = get_image(image.id)

print("[SUCCESS] All records retrieved successfully!")


#################################
# DELETE
#################################


# Leafs first
delete_conversation(conversation.id)
delete_image(image.id)

delete_weight_record(weight_rec.id)
delete_food_record(food_rec.id)
delete_emotional_record(emotional_rec.id)
delete_physical_activity_record(activity_rec.id)

delete_professional_patient(professional.id, patient.id)
delete_professional(professional.id)
delete_patient(patient.id)
delete_sarah_version(sarah_ver.id)
delete_health_center(health_center.id)

print("[SUCCESS] All test records deleted successfully!")