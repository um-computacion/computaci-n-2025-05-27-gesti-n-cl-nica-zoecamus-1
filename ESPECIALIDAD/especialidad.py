import re
from excepciones import EspecialidadInvalidaError

class Especialidad:
    def __init__(self, nombre: str, dias: list[str]):
        if not nombre or not re.match(r"^[A-Za-záéíóúÁÉÍÓÚñÑ ]+$", nombre):
            raise EspecialidadInvalidaError(f"Nombre de especialidad inválido: '{nombre}'")

        dias_validos = {"lunes", "martes", "miércoles", "jueves", "viernes"}
        dias_normalizados = [d.strip().lower() for d in dias]

        for dia in dias_normalizados:
            if dia not in dias_validos:
                raise EspecialidadInvalidaError(f"Día inválido: '{dia}'. Solo se permite lunes a viernes.")
        
        self.nombre = nombre.strip().title()
        self.dias = dias_normalizados

    def atiende_el_dia(self, dia: str) -> bool:
        return dia.lower() in self.dias

    def __str__(self):
        dias_str = ", ".join(self.dias)
        return f"{self.nombre} (Días: {dias_str})"

    def obtener_especialidad(self) -> str:
        return self.nombre
