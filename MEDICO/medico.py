import re
from excepciones import MatriculaInvalidaError, NombreInvalidoError
from ESPECIALIDAD.especialidad import Especialidad

class Medico:
    def __init__(self, nombre: str, matricula: str, especialidades: list[Especialidad] = None):
        self.nombre = self._validar_nombre(nombre)
        self.matricula = self._validar_matricula(matricula)
        self.especialidades = especialidades or []

    def _validar_nombre(self, valor):
        if not valor or not valor.replace(" ", "").isalpha():
            raise NombreInvalidoError(valor)
        return valor.strip().title()
    

    def _validar_matricula(self, valor):
        if not re.match(r"^\d{4,7}$", valor): 
            raise MatriculaInvalidaError(valor)
        return valor

    def agregar_especialidad(self, especialidad: Especialidad):
        for esp in self.especialidades:
            if (esp.obtener_especialidad().lower() == especialidad.obtener_especialidad().lower()
                and set(esp.dias) == set(especialidad.dias)):
                print("\u26a0\ufe0f Ya existe esa especialidad con los mismos días. No se agregó.")
                return
        self.especialidades.append(especialidad)
        print("\u2705 Especialidad agregada correctamente.")


    def obtener_matricula(self) -> str:
        return self.matricula

    def obtener_especialidad_para_dia(self, dia: str) -> str | None:
        for esp in self.especialidades:
            if esp.atiende_el_dia(dia):
                return esp.nombre
        return None
    
    def obtener_nombre(self) -> str:
        return self.nombre
    
    def __str__(self):
        especialidades_str = ",\n  ".join(str(e) for e in self.especialidades)
        return f"{self.nombre},\n{self.matricula},\n[\n  {especialidades_str}\n]"

