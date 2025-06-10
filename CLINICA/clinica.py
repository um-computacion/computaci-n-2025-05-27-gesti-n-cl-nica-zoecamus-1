import re
from datetime import datetime
from typing import List
from MEDICO.medico import Medico
from PACIENTE.paciente import Paciente
from RECETA.receta import Receta
from TURNO.turno import Turno
from HISTORIA_CLINICA.historia_clinica import HistoriaClinica
from excepciones import PacienteError, MedicoError, TurnoDuplicadoError

class Clinica:
    def __init__(self):
        self.__pacientes: dict[str, Paciente] = {}
        self.__medicos: dict[str, Medico] = {}
        self.__turnos: List[Turno] = []
        self.__historias_clinicas: dict[str, HistoriaClinica] = {}

    def agregar_paciente(self, paciente: Paciente):
        dni = paciente.obtener_dni()
        if dni not in self.__pacientes:
            self.__pacientes[dni] = paciente
            self.__historias_clinicas[dni] = HistoriaClinica(paciente)

    def agregar_medico(self, medico: Medico):
        matricula = medico.obtener_matricula()
        if matricula not in self.__medicos:
            self.__medicos[matricula] = medico

    def agendar_turno(self, dni: str, matricula: str, especialidad: str, fecha_hora: datetime):
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)
        self.validar_turno_no_duplicado(matricula, fecha_hora)

        Turno.validar_fecha_hora(fecha_hora)  
        
        Turno.validar_turno(medico, especialidad, fecha_hora)  
        Turno.validar_fecha_hora(fecha_hora)
        self.validar_turno_no_duplicado(matricula, fecha_hora)



        medico = self.__medicos[matricula]
        paciente = self.__pacientes[dni]
        historia = self.__historias_clinicas[dni]

        Turno.validar_turno(medico, especialidad, fecha_hora)
        turno = Turno(medico, paciente, especialidad, fecha_hora)
        self.__turnos.append(turno)
        historia.agregar_turno(medico, especialidad, fecha_hora)

    def emitir_receta(self, dni: str, matricula: str, medicamentos: List[str]) -> Receta:
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)

        if not medicamentos or all(m.strip() == "" for m in medicamentos):
            raise ValueError("Debe ingresar al menos un medicamento.")

        paciente = self.__pacientes[dni]
        medico = self.__medicos[matricula]
        receta = Receta(paciente, medico, medicamentos)

   
        self.__historias_clinicas[dni].agregar_receta(medico, medicamentos)

        return receta

    def obtener_pacientes(self) -> List[Paciente]:
        return list(self.__pacientes.values())

    def obtener_medicos(self) -> List[Medico]:
        return list(self.__medicos.values())

    def obtener_medico_por_matricula(self, matricula: str) -> Medico:
        self.validar_existencia_medico(matricula)
        return self.__medicos[matricula]

    def obtener_turnos(self) -> List[Turno]:
        return self.__turnos

    def obtener_historia_clinica_por_dni(self, dni: str) -> HistoriaClinica:
        self.validar_existencia_paciente(dni)
        return self.__historias_clinicas[dni]

    def validar_existencia_paciente(self, dni: str):
        if dni not in self.__pacientes:
            raise PacienteError(dni)

    def validar_existencia_medico(self, matricula: str):
        if matricula not in self.__medicos:
            raise MedicoError(matricula)
        
    def validar_turno_no_duplicado(self, matricula: str, fecha_hora: datetime):
        for turno in self.obtener_turnos():
            medico = turno.obtener_medico()
            if medico.obtener_matricula() == matricula and turno.obtener_fecha_hora() == fecha_hora:
                raise TurnoDuplicadoError(f"El turno con médico {matricula} ya está reservado para esa fecha.")

    @staticmethod
    def obtener_dia_semana_en_espanol(fecha_hora: datetime) -> str | None:
        dias = {
            0: "lunes",
            1: "martes",
            2: "miércoles",
            3: "jueves",
            4: "viernes",
        }
        return dias.get(fecha_hora.weekday())