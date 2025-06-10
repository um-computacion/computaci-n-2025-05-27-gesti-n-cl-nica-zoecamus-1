import re
import datetime
from PACIENTE.paciente import Paciente
from MEDICO.medico import Medico
from excepciones import TurnoOcupadoError, TurnoDuplicadoError, TurnoNoEncontradoError, TurnoError

class Turno:
    def __init__(self, medico: Medico, paciente: Paciente, especialidad: str, fecha_hora):
        if isinstance(fecha_hora, str):
            fecha_hora = datetime.datetime.strptime(fecha_hora, "%Y-%m-%d %H:%M")
        self.__medico = medico
        self.__paciente = paciente
        self.__especialidad = especialidad
        self.__fecha_hora = fecha_hora

    def obtener_medico(self) -> Medico:
        return self.__medico

    def obtener_paciente(self) -> Paciente:
        return self.__paciente

    def obtener_fecha_hora(self) -> datetime.datetime:
        return self.__fecha_hora

    def __str__(self) -> str:
        return (f"Paciente: {self.__paciente.obtener_nombre()}, "
                f"Médico: {self.__medico.obtener_nombre()}, "
                f"Especialidad: {self.__especialidad}, "
                f"Fecha y hora: {self.__fecha_hora.strftime('%Y-%m-%d %H:%M')}")

    def __eq__(self, otro):
        return (self.__paciente == otro.__paciente and
                self.__medico == otro.__medico and
                self.__especialidad == otro.__especialidad and
                self.__fecha_hora == otro.__fecha_hora)

    def __hash__(self):
        return hash((self.__paciente, self.__medico, self.__especialidad, self.__fecha_hora))

    @staticmethod
    def validar_fecha_hora(fecha_hora: datetime.datetime):
        if fecha_hora < datetime.datetime.now():
            raise TurnoOcupadoError(fecha_hora)



    def validar_fecha_hora_unica(self, turnos_existentes: list):
        for turno in turnos_existentes:
            if (
                turno._Turno__fecha_hora == self.__fecha_hora and
                turno._Turno__medico == self.__medico and
                turno._Turno__paciente == self.__paciente and
                turno._Turno__especialidad == self.__especialidad
            ):
                raise TurnoDuplicadoError("El turno ya existe.")
    
    @staticmethod
    def validar_turno_ocupado(turnos: list["Turno"], fecha_hora: str):
        for turno in turnos:
            if turno.obtener_fecha_hora().strftime("%Y-%m-%d %H:%M") == fecha_hora:
                raise TurnoOcupadoError(fecha_hora)

    @staticmethod
    def validar_existe_turno(turnos: list["Turno"], fecha_hora: str):
        for turno in turnos:
            if turno.obtener_fecha_hora().strftime("%Y-%m-%d %H:%M") == fecha_hora:
                return
        raise TurnoNoEncontradoError(fecha_hora)

    @staticmethod
    def validar_especialidad(medico, especialidad: str):
        dias = ["lunes", "martes", "miércoles", "jueves", "viernes"]
        for dia in dias:
            if medico.obtener_especialidad_para_dia(dia) == especialidad:
                return
        raise TurnoError("El médico no atiende esa especialidad.")

    @staticmethod
    def validar_dia_semana(fecha_hora: datetime.datetime):
        dia = fecha_hora.strftime("%A").lower()
        if dia not in ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado"]:
            raise TurnoError(f"Día de la semana inválido: {dia}")

    @staticmethod
    def validar_turno(medico, especialidad, fecha_hora):
        if not medico:
            raise ValueError("El médico no puede estar vacío")
        if not especialidad:
            raise ValueError("La especialidad no puede estar vacía")
