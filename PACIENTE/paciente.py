import re
from datetime import datetime
from excepciones import DniInvalidoError, NombreInvalidoError, FechaNacimientoInvalidaError

class Paciente:
    def __init__(self, nombre, dni, fecha_nacimiento):
        self.nombre = nombre
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.historia_clinica = []

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or not valor.replace(" ", "").isalpha():
            raise NombreInvalidoError(valor)
        self._nombre = valor.strip().title()

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, valor):
        if not re.fullmatch(r"\d{7,8}", valor):
            raise DniInvalidoError(valor)
        self._dni = valor

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, valor):
        try:
            datetime.strptime(valor, "%d/%m/%Y")
            self._fecha_nacimiento = valor
        except ValueError:
            raise FechaNacimientoInvalidaError(valor)

    def obtener_nombre(self) -> str:
        return self.nombre

    def obtener_dni(self) -> str:
        return self.dni

    def agregar_historia(self, entrada):
        self.historia_clinica.append(entrada)

    def __str__(self):
        return f"{self.nombre}, {self.dni}, {self.fecha_nacimiento}"
