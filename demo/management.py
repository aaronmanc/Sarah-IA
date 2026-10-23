from datetime import datetime, date
from fastapi import HTTPException

from api.routers.patients import (list_patients_endpoint, update_patient_endpoint)
from api.routers.professionals import (list_professionals_endpoint, list_patients_by_professional_endpoint, update_professional_endpoint)
from api.routers.professional_patients import (create_professional_patient_endpoint)

from api.routers.weight_records import (create_weight_record_endpoint, list_weight_records_endpoint, update_weight_record_endpoint, delete_weight_record_endpoint)
from api.routers.food_records import (create_food_record_endpoint, list_food_records_endpoint, update_food_record_endpoint, delete_food_record_endpoint)
from api.routers.emotional_records import (create_emotional_record_endpoint, list_emotional_records_endpoint, update_emotional_record_endpoint, delete_emotional_record_endpoint) 
from api.routers.physical_records import (create_physical_record_endpoint, list_physical_records_endpoint, update_physical_record_endpoint, delete_physical_record_endpoint)

from .message import (send_message)

from schemas.patient import UpdatePatient
from schemas.professional import UpdateProfessional
from schemas.professional_patient import CreateProfessionalPatient
from schemas.weight_record import CreateWeightRecord, UpdateWeightRecord
from schemas.food_record import CreateFoodRecord, UpdateFoodRecord
from schemas.emotional_record import CreateEmotionalRecord, UpdateEmotionalRecord
from schemas.physical_record import CreatePhysicalActivityRecord, UpdatePhysicalActivityRecord


def prompt_input(prompt_text: str) -> str:
    val = input(prompt_text).strip()
    if val == ".":
        raise KeyboardInterrupt
    return val


def select_item_by_index(items, display_attr_func):
    if not items:
        print("[INFO] No hay elementos disponibles.")
        return None

    print("\nSeleccione un elemento por número:")
    for idx, item in enumerate(items, start=1):
        print(f"{idx}. {display_attr_func(item)}")
    print("0. Cancelar")

    choice = input("\nNúmero de opción: ").strip()
    if choice == "0" or choice == ".":
        return None

    try:
        index = int(choice) - 1
        if 0 <= index < len(items):
            return items[index]
        else:
            print("[ERROR] Número fuera de rango.")
            return None
    except ValueError:
        print("[ERROR] Entrada inválida. Debe ser un número.")
        return None


def management_menu():
    while True:
        print("\n==============================")
        print("      MENÚ DE GESTIÓN         ")
        print("==============================")
        print("1. Gestionar Pacientes")
        print("2. Gestionar Profesionales")
        print("0. Volver al menú principal")

        choice = input("\nSeleccione una opción: ").strip()

        if choice == "0":
            break
        elif choice == "1":
            manage_patients_flow()
        elif choice == "2":
            manage_professionals_flow()
        else:
            print("[ERROR] Opción no válida.")


def manage_patients_flow():
    patients = list_patients_endpoint()
    selected_patient = select_item_by_index(
        patients, 
        lambda p: f"{p.first_name} {p.last_name} (RUT: {p.rut})"
    )
    if not selected_patient:
        return

    while True:
        print(f"\n-- GESTIONANDO PACIENTE: {selected_patient.first_name} {selected_patient.last_name} --")
        print("1. Actualizar información del paciente")
        print("2. Gestionar registros médicos")
        print("3. Enviar Mensaje a Sarah IA")
        print("0. Volver")

        choice = input("\nSeleccione una opción: ").strip()
        if choice == "0":
            break
        elif choice == "1":
            update_patient_info(selected_patient.id)
        elif choice == "2":
            manage_records_flow(selected_patient.id)
        elif choice == "3":
            send_message(selected_patient.id)
        else:
            print("[ERROR] Opción no válida.")


def update_patient_info(patient_id: str):
    print("\n-- Actualizar Paciente (Presione Enter para mantener valor actual) --")
    try:
        first_name = input("Nuevo First Name: ").strip() or None
        last_name = input("Nuevo Last Name: ").strip() or None
        rut = input("Nuevo RUT: ").strip() or None
        
        birth_date_str = input("Nueva Fecha de Nacimiento (YYYY-MM-DD): ").strip()
        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date() if birth_date_str else None

        sex = input("Nuevo Sexo: ").strip() or None
        email = input("Nuevo Email: ").strip() or None
        phone = input("Nuevo Teléfono: ").strip() or None

        current_height_str = input("Nueva Altura (m): ").strip()
        current_height = float(current_height_str) if current_height_str else None

        current_weight_str = input("Nuevo Peso (kg): ").strip()
        current_weight = float(current_weight_str) if current_weight_str else None

        lives_alone_str = input("¿Vive solo? (s/n): ").strip().lower()
        lives_alone = None
        if lives_alone_str in ("s", "si", "y", "yes", "true", "1"):
            lives_alone = True
        elif lives_alone_str in ("n", "no", "false", "0"):
            lives_alone = False

        bmi_str = input("Nuevo BMI: ").strip()
        bmi = float(bmi_str) if bmi_str else None

        context = input("Nuevo Contexto: ").strip() or None
        psychological_profile = input("Nuevo Perfil Psicológico: ").strip() or None

        payload = UpdatePatient(
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
        
        updated = update_patient_endpoint(patient_id, payload)
        print(f"[SUCCESS] Paciente actualizado correctamente.")
        
    except HTTPException as e:
        print(f"[ERROR] {e.detail}")
    except ValueError:
        print("[ERROR] Formato de dato inválido (verifique números o el formato de fecha YYYY-MM-DD).")
    except KeyboardInterrupt:
        print("\n[INFO] Actualización cancelada.")


def manage_records_flow(patient_id: str):
    while True:
        print("\n-- GESTIÓN DE REGISTROS DEL PACIENTE --")
        print("1. Registro de Peso (Weight Record)")
        print("2. Registro de Comida (Food Record)")
        print("3. Registro Emocional (Emotional Record)")
        print("4. Registro de Actividad Física (Physical Activity Record)")
        print("0. Volver")

        choice = input("\nSeleccione tipo de registro: ").strip()
        if choice == "0":
            break
        elif choice == "1":
            handle_record_crud("weight", patient_id)
        elif choice == "2":
            handle_record_crud("food", patient_id)
        elif choice == "3":
            handle_record_crud("emotional", patient_id)
        elif choice == "4":
            handle_record_crud("physical", patient_id)
        else:
            print("[ERROR] Opción no válida.")


def handle_record_crud(record_type: str, patient_id: str):
    while True:
        print(f"\n-- CRUD {record_type.upper()} RECORDS --")
        print("1. Insertar")
        print("2. Actualizar")
        print("3. Eliminar")
        print("4. Listar")
        print("0. Volver")

        action = input("\nSeleccione acción: ").strip()
        if action == "0":
            break
        elif action == "1":
            try:
                if record_type == "weight":
                    weight = float(prompt_input("Peso (kg): "))
                    create_weight_record_endpoint(CreateWeightRecord(weight=weight, patient_id=patient_id))
                elif record_type == "food":
                    desc = prompt_input("Descripción de comida: ")
                    create_food_record_endpoint(CreateFoodRecord(description=desc, patient_id=patient_id))
                elif record_type == "emotional":
                    state = prompt_input("Estado emocional: ")
                    create_emotional_record_endpoint(CreateEmotionalRecord(emotional_state=state, patient_id=patient_id))
                elif record_type == "physical":
                    act = prompt_input("Tipo de actividad: ")
                    dur = float(prompt_input("Duración (minutos/horas): "))
                    create_physical_record_endpoint(CreatePhysicalActivityRecord(activity_type=act, duration=dur, patient_id=patient_id))
                print(f"[SUCCESS] Registro de {record_type} creado exitosamente.")
            except HTTPException as e:
                print(f"[ERROR] {e.detail}")
            except KeyboardInterrupt:
                print("\n[INFO] Operación cancelada.")
        elif action == "2":
            record_id = prompt_input("ID del registro a actualizar (UUID): ")
            try:
                if record_type == "weight":
                    w = float(prompt_input("Nuevo peso: "))
                    update_weight_record_endpoint(record_id, UpdateWeightRecord(weight=w))
                elif record_type == "food":
                    d = prompt_input("Nueva descripción: ")
                    update_food_record_endpoint(record_id, UpdateFoodRecord(description=d))
                elif record_type == "emotional":
                    s = prompt_input("Nuevo estado emocional: ")
                    update_emotional_record_endpoint(record_id, UpdateEmotionalRecord(emotional_state=s))
                elif record_type == "physical":
                    a = prompt_input("Nuevo tipo de actividad: ")
                    update_physical_record_endpoint(record_id, UpdatePhysicalActivityRecord(activity_type=a))
                print(f"[SUCCESS] Registro actualizado.")
            except HTTPException as e:
                print(f"[ERROR] {e.detail}")
            except KeyboardInterrupt:
                print("\n[INFO] Operación cancelada.")
        elif action == "3":
            record_id = prompt_input("ID del registro a eliminar (UUID): ")
            try:
                if record_type == "weight":
                    delete_weight_record_endpoint(record_id)
                elif record_type == "food":
                    delete_food_record_endpoint(record_id)
                elif record_type == "emotional":
                    delete_emotional_record_endpoint(record_id)
                elif record_type == "physical":
                    delete_physical_record_endpoint(record_id)
                print(f"[SUCCESS] Registro eliminado.")
            except HTTPException as e:
                print(f"[ERROR] {e.detail}")
            except KeyboardInterrupt:
                print("\n[INFO] Operación cancelada.")
        elif action == "4":
            try:
                print(f"\n--- Listado de Registros ({record_type}) ---")
                if record_type == "weight":
                    records = list_weight_records_endpoint(patient_id=patient_id)
                    for r in records:
                        print(f"ID: {r.id} | Peso: {r.weight}kg")
                elif record_type == "food":
                    records = list_food_records_endpoint(patient_id=patient_id)
                    for r in records:
                        print(f"ID: {r.id} | Descripción: {r.description}")
                elif record_type == "emotional":
                    records = list_emotional_records_endpoint(patient_id=patient_id)
                    for r in records:
                        print(f"ID: {r.id} | Estado: {r.emotional_state}")
                elif record_type == "physical":
                    records = list_physical_records_endpoint(patient_id=patient_id)
                    for r in records:
                        print(f"ID: {r.id} | Actividad: {r.activity_type} | Duración: {r.duration}")
                
                if not records:
                    print("[INFO] No se encontraron registros para este paciente.")
            except HTTPException as e:
                print(f"[ERROR] {e.detail}")
            except KeyboardInterrupt:
                print("\n[INFO] Operación cancelada.")
        else:
            print("[ERROR] Opción no válida.")






def manage_professionals_flow():
    professionals = list_professionals_endpoint()
    selected_prof = select_item_by_index(
        professionals, 
        lambda p: f"{p.first_name} {p.last_name} - Especialidad: {p.specialty}"
    )
    if not selected_prof:
        return

    while True:
        print(f"\n--- GESTIONANDO PROFESIONAL: {selected_prof.first_name} {selected_prof.last_name} ---")
        print("1. Actualizar información del profesional")
        print("2. Asignar este profesional a un paciente")
        print("3. Ver pacientes asignados")
        print("0. Volver")

        choice = input("\nSeleccione una opción: ").strip()
        if choice == "0":
            break
        elif choice == "1":
            update_professional_info(selected_prof.id)
        elif choice == "2":
            assign_prof_to_patient(selected_prof.id)
        elif choice == "3":
            show_assigned_patients(selected_prof.id, f"{selected_prof.first_name} {selected_prof.last_name}")   
        else:
            print("[ERROR] Opción no válida.")


def update_professional_info(professional_id: str):
    print("\n--- Actualizar Profesional (Presione Enter para mantener valor actual) ---")
    try:
        first_name = input("Nuevo First Name: ").strip() or None
        last_name = input("Nuevo Last Name: ").strip() or None
        specialty = input("Nueva Especialidad: ").strip() or None
        email = input("Nuevo Email: ").strip() or None
        phone = input("Nuevo Phone: ").strip() or None
        health_center_id = input("Nuevo Health Center ID (UUID): ").strip() or None

        payload = UpdateProfessional(
            first_name=first_name,
            last_name=last_name,
            specialty=specialty,
            email=email,
            phone=phone,
            health_center_id=health_center_id
        )
        update_professional_endpoint(professional_id, payload)
        print(f"[SUCCESS] Profesional actualizado correctamente.")
    except HTTPException as e:
        print(f"[ERROR] {e.detail}")
    except KeyboardInterrupt:
        print("\n[INFO] Actualización cancelada.")


def assign_prof_to_patient(professional_id: str):
    print("\n--- Asignar Profesional a Paciente ---")
    
    all_patients = list_patients_endpoint()
    assigned_patients = list_patients_by_professional_endpoint(professional_id)
    assigned_patient_ids = {p.id for p in assigned_patients}
    
    available_patients = [
        p for p in all_patients 
        if p.id not in assigned_patient_ids
    ]
    
    if not available_patients:
        print("[INFO] Todos los pacientes ya están asignados a este profesional.")
        return

    selected_patient = select_item_by_index(
        available_patients, 
        lambda p: f"{p.first_name} {p.last_name} (RUT: {p.rut})"
    )
    
    if not selected_patient:
        return

    try:
        payload = CreateProfessionalPatient(
            professional_id=professional_id,
            patient_id=selected_patient.id
        )
        create_professional_patient_endpoint(payload)
        print(f"[SUCCESS] Profesional asignado exitosamente al paciente {selected_patient.first_name} {selected_patient.last_name}.")
    except HTTPException as e:
        print(f"[ERROR] {e.detail}")


def show_assigned_patients(professional_id: str, prof_name: str):
    print(f"\n-- Pacientes Asignados a {prof_name} --")
    assigned_patients = list_patients_by_professional_endpoint(professional_id)
    
    if not assigned_patients:
        print("[INFO] Este profesional no tiene pacientes asignados.")
        return

    for index, patient in enumerate(assigned_patients, 1):
        print(f"{index}. {patient.first_name} {patient.last_name} | RUT: {patient.rut} | Email: {patient.email}")
