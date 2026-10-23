from fastapi import HTTPException
from api.routers.patients import list_patients_endpoint
from api.routers.professionals import list_professionals_endpoint
from api.routers.professional_patients import list_professional_patients_endpoint
from api.routers.health_centers import list_health_centers_endpoint


def list_patients():
    try:
        patients = list_patients_endpoint()
        print("\n--- LISTA DE PACIENTES ---")
        if not patients:
            print("No hay pacientes registrados.")
            return
        for p in patients:
            print(f"ID: {p.id} | Nombre: {p.first_name} {p.last_name} | RUT: {p.rut} | Email: {p.email}")
    except HTTPException as e:
        print(f"[ERROR] {e.detail}")


def list_professionals():
    try:
        professionals = list_professionals_endpoint()
        print("\n--- LISTA DE PROFESIONALES ---")
        if not professionals:
            print("No hay profesionales registrados.")
            return
        for prof in professionals:
            print(f"ID: {prof.id} | Nombre: {prof.first_name} {prof.last_name} | Especialidad: {prof.specialty} | Centro ID: {prof.health_center_id}")
    except HTTPException as e:
        print(f"[ERROR] {e.detail}")


def list_patient_professionals():
    try:
        relations = list_professional_patients_endpoint()
        print("\n--- LISTA DE ASIGNACIONES PACIENTE-PROFESIONAL ---")
        if not relations:
            print("No hay asignaciones registradas.")
            return
        for rel in relations:
            print(f"Profesional ID: {rel.professional_id} <---> Paciente ID: {rel.patient_id}")
    except HTTPException as e:
        print(f"[ERROR] {e.detail}")


def list_health_centers():
    try:
        hcs = list_health_centers_endpoint()
        print("\n--- LISTA DE CENTROS DE SALUD ---")
        if not hcs:
            print("No hay centros de salud registrados.")
            return
        for hc in hcs:
            print(f"ID: {hc.id} | Nombre: {hc.name} | Ciudad: {hc.city}")
    except HTTPException as e:
        print(f"[ERROR] {e.detail}")