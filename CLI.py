from CLINICA.clinica import Clinica
from PACIENTE.paciente import Paciente
from MEDICO.medico import Medico
from ESPECIALIDAD.especialidad import Especialidad
from excepciones import *
from datetime import datetime

class CLI:
    def __init__(self):
            self.clinica = Clinica()

    def ejecutar(self):
        while True:
            print("""
--- Menú Clínica ---
1) Agregar paciente
2) Agregar médico
3) Agendar turno
4) Agregar especialidad a médico
5) Emitir receta
6) Ver historia clínica
7) Ver todos los turnos
8) Ver todos los pacientes
9) Ver todos los médicos
0) Salir
""")
            opcion = input("Seleccione una opción: ")

            try:
                if opcion == "1":
                    self.agregar_paciente()
                elif opcion == "2":
                    self.agregar_medico()
                elif opcion == "3":
                    self.agendar_turno()
                elif opcion == "4":
                    self.agregar_especialidad()
                elif opcion == "5":
                    self.emitir_receta()
                elif opcion == "6":
                    self.ver_historia_clinica()
                elif opcion == "7":
                    self.ver_turnos()
                elif opcion == "8":
                    self.ver_pacientes()
                elif opcion == "9":
                    self.ver_medicos()
                elif opcion == "0":
                    print("Saliendo del sistema. Hasta luego.")
                    break
                else:
                    print("Opción inválida.")
            except Exception as e:
                print(f"Error: {e}")

    def agregar_paciente(self):
        nombre = input("Nombre completo: ")
        dni = input("DNI: ")
        fecha_nac = input("Fecha de nacimiento (dd/mm/aaaa): ")
        paciente = Paciente(nombre, dni, fecha_nac)
        self.clinica.agregar_paciente(paciente)
        print("Paciente registrado correctamente.")

    def agregar_medico(self):
        nombre = input("Nombre completo: ")
        matricula = input("Matrícula: ")
        medico = Medico(nombre, matricula)
        self.clinica.agregar_medico(medico)
        print("Médico registrado correctamente.")

    def agregar_especialidad(self):
        matricula = input("Matrícula del médico: ")
        tipo = input("Especialidad: ")
        dias = input("Días de atención (separados por coma): ").lower().split(",")
        especialidad = Especialidad(tipo, [dia.strip() for dia in dias])
        medico = self.clinica.obtener_medico_por_matricula(matricula)
        medico.agregar_especialidad(especialidad)
        print("Especialidad agregada correctamente.")

    def agendar_turno(self):
        dni = input("DNI del paciente: ")
        matricula = input("Matrícula del médico: ")
        especialidad = input("Especialidad: ")
        fecha = input("Fecha y hora (yyyy-mm-dd HH:MM): ")
        fecha_dt = datetime.strptime(fecha, "%Y-%m-%d %H:%M")
        self.clinica.agendar_turno(dni, matricula, especialidad, fecha_dt)
        print("Turno agendado correctamente.")

    def emitir_receta(self):
        dni = input("DNI del paciente: ")
        matricula = input("Matrícula del médico: ")
        medicamentos = input("Medicamentos (separados por coma): ").split(",")
        receta = self.clinica.emitir_receta(dni, matricula, [m.strip() for m in medicamentos])
        print("Receta emitida:\n", receta)

    def ver_historia_clinica(self):
        dni = input("DNI del paciente: ")
        historia = self.clinica.obtener_historia_clinica_por_dni(dni)
        print(historia)

    def ver_turnos(self):
        for turno in self.clinica.obtener_turnos():
            print(turno)

    def ver_pacientes(self):
        for paciente in self.clinica.obtener_pacientes():
            print(paciente)

    def ver_medicos(self):
        for medico in self.clinica.obtener_medicos():
            print(medico)

if __name__ == "__main__":
    CLI().ejecutar()
