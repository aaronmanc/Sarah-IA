from datetime import date
from fastapi import HTTPException

from api.routers.patients import create_patient_endpoint
from api.routers.professionals import create_professional_endpoint
from api.routers.professional_patients import create_professional_patient_endpoint
from api.routers.health_centers import create_health_center_endpoint

from schemas.patient import CreatePatient
from schemas.professional import CreateProfessional
from schemas.professional_patient import CreateProfessionalPatient
from schemas.health_center import CreateHealthCenter

def prompt_input(prompt_text: str) -> str:
    val = input(prompt_text).strip()
    if val == ".":
        raise KeyboardInterrupt
    return val


def insert_patient():
    print("\n--- Insertar Paciente (Escribe '.' para salir) ---")
    try:
        first_name = prompt_input("First Name: ")
        last_name = prompt_input("Last Name: ")
        rut = prompt_input("RUT: ")
        birth_date_str = prompt_input("Birth Date (YYYY-MM-DD): ")
        birth_date = date.fromisoformat(birth_date_str)
        sex = prompt_input("Sex (M/F): ")
        email = prompt_input("Email: ")
        phone = prompt_input("Phone: ")
        current_height = float(prompt_input("Current Height (e.g. 1.75): "))
        current_weight = float(prompt_input("Current Weight (e.g. 70.5): "))
        lives_alone_str = prompt_input("Lives Alone (True/False): ")
        lives_alone = lives_alone_str.lower() in ("true", "1", "y", "yes")
        bmi = float(prompt_input("BMI (e.g. 23.0): "))
        context = prompt_input("Context: ")
        psychological_profile = prompt_input("Psychological Profile: ")

        payload = CreatePatient(
            first_name=first_name,
            last_name=last_name,
            rut=rut,
            birth_date=birth_date,
            sex=sex,
            email=email,
            phone=phone,
            current_height=current_height,
            current_weight=current_weight,
            lives_alone=lives_alone,
            bmi=bmi,
            context=context,
            psychological_profile=psychological_profile,
        )

        result = create_patient_endpoint(payload)
        print(f"[SUCCESS] Patient created with ID: {result.id}")

    except HTTPException as e:
        print(f"[ERROR] {e.detail}")
    except ValueError as e:
        print(f"[ERROR] Invalid input format: {e}")
    except KeyboardInterrupt:
        print("\n[INFO] Cancelled patient creation.")


def insert_professional():
    print("\n--- Insertar Profesional (Escribe '.' para salir) ---")
    try:
        first_name = prompt_input("First Name: ")
        last_name = prompt_input("Last Name: ")
        specialty = prompt_input("Specialty: ")
        email = prompt_input("Email: ")
        phone = prompt_input("Phone: ")
        health_center_id = prompt_input("Health Center ID (UUID): ")

        payload = CreateProfessional(
            first_name=first_name,
            last_name=last_name,
            specialty=specialty,
            email=email,
            phone=phone,
            health_center_id=health_center_id,
        )

        result = create_professional_endpoint(payload)
        print(f"[SUCCESS] Professional created with ID: {result.id}")

    except HTTPException as e:
        print(f"[ERROR] {e.detail}")
    except KeyboardInterrupt:
        print("\n[INFO] Cancelled professional creation.")


def assign_patientProfessional():
    print("\n--- Asignar Paciente-Profesional (Escribe '.' para salir) ---")
    try:
        professional_id = prompt_input("Professional ID (UUID): ")
        patient_id = prompt_input("Patient ID (UUID): ")

        payload = CreateProfessionalPatient(
            professional_id=professional_id,
            patient_id=patient_id,
        )

        create_professional_patient_endpoint(payload)
        print(f"[SUCCESS] Professional successfully linked to Patient!")

    except HTTPException as e:
        print(f"[ERROR] {e.detail}")
    except KeyboardInterrupt:
        print("\n[INFO] Cancelled assignment.")


def insert_healthCenter():
    print("\n--- Insertar Centro de Salud (Escribe '.' para salir) ---")
    try:
        name = prompt_input("Health Center Name: ")
        city = prompt_input("City: ")

        payload = CreateHealthCenter(
            name=name,
            city=city,
        )

        result = create_health_center_endpoint(payload)
        print(f"[SUCCESS] Health Center created with ID: {result.id}")

    except HTTPException as e:
        print(f"[ERROR] {e.detail}")
    except KeyboardInterrupt:
        print("\n[INFO] Cancelled health center creation.")

