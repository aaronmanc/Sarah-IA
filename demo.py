from datetime import date
from fastapi import HTTPException

from demo.insert import (insert_patient, insert_healthCenter, insert_professional, assign_patientProfessional)
from demo.delete import (delete_patient, delete_professional, delete_professionalPatient, delete_healthCenter)
from demo.list import (list_patients, list_professionals, list_patient_professionals, list_health_centers)
from demo.management import management_menu

def main_menu():
    while True:
        print("\n==============================")
        print("   SARAH DATA TERMINAL APP    ")
        print("==============================")
        print("1. Insertar")
        print("2. Eliminar")
        print("3. Listar")
        print("4. Gestión")
        print("0. Salir")
        
        choice = input("\nSeleccione una opción: ").strip()

        if choice == "0":
            print("Saliendo de la aplicación...")
            break

        elif choice == "1":
            while True:
                print("\n--- MENÚ DE INSERCIÓN ---")
                print("1. Insertar Paciente")
                print("2. Insertar Profesional")
                print("3. Asignar Paciente-Profesional")
                print("4. Insertar Centro de salud")
                print("0. Volver al menú principal")

                sub_choice = input("\nSeleccione una opción: ").strip()

                if sub_choice == "0":
                    break
                elif sub_choice == "1":
                    insert_patient()
                elif sub_choice == "2":
                    insert_professional()
                elif sub_choice == "3":
                    assign_patientProfessional()
                elif sub_choice == "4":
                    insert_healthCenter()
                else:
                    print("[ERROR] Opción no válida.")

        elif choice == "2":
            while True:
                print("\n--- MENÚ DE ELIMINACIÓN ---")
                print("1. Eliminar Paciente")
                print("2. Eliminar Profesional")
                print("3. Eliminar Asignación Paciente-Profesional")
                print("4. Eliminar Centro de salud")
                print("0. Volver al menú principal")

                sub_choice = input("\nSeleccione una opción: ").strip()

                if sub_choice == "0":
                    break
                elif sub_choice == "1":
                    delete_patient()
                elif sub_choice == "2":
                    delete_professional()
                elif sub_choice == "3":
                    delete_professionalPatient()
                elif sub_choice == "4":
                    delete_healthCenter()
                else:
                    print("[ERROR] Opción no válida.")

        elif choice == "3":
            while True:
                print("\n--- MENÚ DE LISTADO ---")
                print("1. Listar Pacientes")
                print("2. Listar Profesionales")
                print("3. Listar Asignaciones Paciente-Profesional")
                print("4. Listar Centros de salud")
                print("0. Volver al menú principal")

                sub_choice = input("\nSeleccione una opción: ").strip()

                if sub_choice == "0":
                    break
                elif sub_choice == "1":
                    list_patients()
                elif sub_choice == "2":
                    list_professionals()
                elif sub_choice == "3":
                    list_patient_professionals()
                elif sub_choice == "4":
                    list_health_centers()
                else:
                    print("[ERROR] Opción no válida.")

        elif choice == "4":
            management_menu()

        else:
            print("[ERROR] Opción no válida.")


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n¡Hasta luego!")