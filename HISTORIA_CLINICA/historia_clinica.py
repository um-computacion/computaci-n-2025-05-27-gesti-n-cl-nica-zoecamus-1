import re
from datetime import datetime
from excepciones import HistoriaClinicaInvalidaError, HistoriaClinicaNoEncontradaError
from TURNO.turno import Turno
from RECETA.receta import Receta
from PACIENTE.paciente import Paciente
from MEDICO.medico import Medico
from ESPECIALIDAD.especialidad import Especialidad
class HistoriaClinica:
    def __init__(self, paciente: Paciente):
        self.__paciente = paciente
        self.__turnos = []
        self.__recetas = []

    def __str__(self):
        turnos_str = ",\n  ".join(str(t) for t in self.__turnos)
        recetas_str = ",\n  ".join(str(r) for r in self.__recetas)
        return f"{self.__paciente.obtener_nombre()},\n{turnos_str},\n{recetas_str}"

    def __eq__(self, otro):
        return (self.__paciente == otro.__paciente and
                self.__turnos == otro.__turnos and
                self.__recetas == otro.__recetas)

    def __hash__(self):
        return hash((self.__paciente, tuple(self.__turnos), tuple(self.__recetas)))

    def obtener_paciente(self) -> Paciente:
        return self.__paciente

    def obtener_turnos(self) -> list[Turno]:
        return self.__turnos

    def obtener_recetas(self) -> list[Receta]:
        return self.__recetas

    @staticmethod
    def validar_existe_historia_clinica(historias_clinicas: list, dni: str):
        for historia_clinica in historias_clinicas:
            if historia_clinica.obtener_paciente().obtener_dni() == dni:
                return
        raise HistoriaClinicaNoEncontradaError(dni)


    def agregar_turno(self, medico: Medico, especialidad: Especialidad, fecha_hora: datetime):
        Turno.validar_turno_ocupado(self.obtener_turnos(), fecha_hora)
        Turno.validar_turno(medico, especialidad, fecha_hora)
        self.obtener_turnos().append(Turno(medico, self.obtener_paciente(), especialidad, fecha_hora))


    def agregar_receta(self, medico: Medico, medicamentos: list[str]):
        self.__recetas.append(Receta(self.__paciente, medico, medicamentos))



