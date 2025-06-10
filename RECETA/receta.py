import datetime
from PACIENTE.paciente import Paciente
from MEDICO.medico import Medico
from excepciones import RecetaNoEncontradaError, TurnoError

class Receta:
    def __init__(self, paciente: Paciente, medico: Medico, medicamentos: list[str]):
        self.__paciente = paciente
        self.__medico = medico
        self.__medicamentos = medicamentos
        self.__fecha = datetime.datetime.now()

    def __str__(self):
        medicamentos_str = ", ".join(self.__medicamentos)
        return (f"Paciente: {self.__paciente.obtener_nombre()}, "
                f"Médico: {self.__medico.obtener_nombre()}, "
                f"Especialidad: {self.__medico.obtener_especialidad_para_dia(self.__fecha.strftime('%A').lower())}, "
                f"Medicamentos: {medicamentos_str}, "
                f"Fecha: {self.__fecha.strftime('%Y-%m-%d %H:%M')}")

    def __eq__(self, otro):
        return (self.__paciente == otro.__paciente and
                self.__medico == otro.__medico and
                self.__medicamentos == otro.__medicamentos and
                self.__fecha == otro.__fecha)

    def __hash__(self):
        return hash((self.__paciente, self.__medico, tuple(self.__medicamentos), self.__fecha))

    def obtener_paciente(self) -> Paciente:
        return self.__paciente

    def obtener_medico(self) -> Medico:
        return self.__medico

    def obtener_medicamentos(self) -> list[str]:
        return self.__medicamentos

    def obtener_fecha(self) -> datetime.datetime:
        return self.__fecha

    @staticmethod
    def validar_existe_receta(recetas: list["Receta"], dni: str):
        for receta in recetas:
            if receta.obtener_paciente().obtener_dni() == dni:
                return
        raise RecetaNoEncontradaError(dni)

    @staticmethod
    def validar_especialidad(medico: Medico, especialidad: str):
        dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        for dia in dias:
            if medico.obtener_especialidad_para_dia(dia) == especialidad:
                return
        raise TurnoError("El médico no atiende esa especialidad.")
