from fastapi import HTTPException
from api.routers.patients import delete_patient_endpoint
from api.routers.professionals import delete_professional_endpoint
from api.routers.professional_patients import delete_professional_patient_endpoint
from api.routers.health_centers import delete_health_center_endpoint


def prompt_input(prompt_text: str) -> str:
    val = input(prompt_text).strip()
    if val == ".":
        raise KeyboardInterrupt
    return val


def delete_patient():
    print("\n--- Eliminar Paciente (Escribe '.' para salir) ---")
    try:
        patient_id = prompt_input("Patient ID (UUID): ")
        delete_patient_endpoint(patient_id)
        print(f"[SUCCESS] Patient successfully deleted.")

    except HTTPException as e:
        print(f"[ERROR] {e.detail}")
    except KeyboardInterrupt:
        print("\n[INFO] Cancelled patient deletion.")


def delete_professional():
    print("\n--- Eliminar Profesional (Escribe '.' para salir) ---")
    try:
        professional_id = prompt_input("Professional ID (UUID): ")
        delete_professional_endpoint(professional_id)
        print(f"[SUCCESS] Professional successfully deleted.")

    except HTTPException as e:
        print(f"[ERROR] {e.detail}")
    except KeyboardInterrupt:
        print("\n[INFO] Cancelled professional deletion.")


def delete_professionalPatient():
    print("\n--- Eliminar Asignación Paciente-Profesional (Escribe '.' para salir) ---")
    try:
        professional_id = prompt_input("Professional ID (UUID): ")
        patient_id = prompt_input("Patient ID (UUID): ")

        delete_professional_patient_endpoint(professional_id, patient_id)
        print(f"[SUCCESS] Assignment successfully deleted.")

    except HTTPException as e:
        print(f"[ERROR] {e.detail}")
    except KeyboardInterrupt:
        print("\n[INFO] Cancelled assignment deletion.")


def delete_healthCenter():
    print("\n--- Eliminar Centro de Salud (Escribe '.' para salir) ---")
    try:
        health_center_id = prompt_input("Health Center ID (UUID): ")
        delete_health_center_endpoint(health_center_id)
        print(f"[SUCCESS] Health Center successfully deleted.")

    except HTTPException as e:
        print(f"[ERROR] {e.detail}")
    except KeyboardInterrupt:
        print("\n[INFO] Cancelled health center deletion.")