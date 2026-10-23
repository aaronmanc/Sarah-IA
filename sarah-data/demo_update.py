from datetime import date, datetime

from repositories.patients import (create_patient, update_patient, delete_patient)
from repositories.health_centers import (create_health_center, update_health_center, delete_health_center)
from repositories.professionals import (create_professional, update_professional, delete_professional)
from repositories.sarah_versions import (create_sarah_version, update_sarah_version, delete_sarah_version)
from repositories.conversations import (create_conversation, delete_conversation)
from repositories.messages import (create_message, update_message)
from repositories.images import (create_image, delete_image)
from repositories.weight_records import (create_weight_record, update_weight_record, delete_weight_record)
from repositories.food_records import (create_food_record, update_food_record, delete_food_record)
from repositories.emotional_records import (create_emotional_record, update_emotional_record, delete_emotional_record)
from repositories.physical_records import (create_physical_activity_record, update_physical_activity_record, delete_physical_activity_record)
from repositories.professional_patients import (create_professional_patient, delete_professional_patient)

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

# Conversations & Media
conversation = create_conversation()

image = create_image(
    description="X-Ray result",
    image_type="png",
    file_reference="/files/xray.png",
)

message = create_message(
    conversation_id=conversation.id,
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
# UPDATE
#################################

updated_hc = update_health_center(health_center.id, name="Hospital Regional")
updated_sv = update_sarah_version(sarah_ver.id, description="Updated stable version with bug fixes")
updated_patient = update_patient(patient.id, current_weight=71.0, bmi=23.2)
updated_prof = update_professional(professional.id, specialty="Cardiology & Vascular")

updated_weight = update_weight_record(weight_rec.id, weight=71.0)
updated_food = update_food_record(food_rec.id, description="Grilled chicken and quinoa salad")
updated_emotional = update_emotional_record(emotional_rec.id, emotional_state="Energetic")
updated_activity = update_physical_activity_record(activity_rec.id, duration=45.0)

updated_msg = update_message(message.id, content="Hello Sarah, updated message content!")

print("[SUCCESS] All records updated successfully!")


#################################
# DELETE
#################################

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