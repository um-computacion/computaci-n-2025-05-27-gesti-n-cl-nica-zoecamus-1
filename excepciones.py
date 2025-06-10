#PACIENTE
class PacienteError(Exception):
    """Excepción base para errores relacionados con pacientes."""
    pass

class DniInvalidoError(PacienteError):
    def __init__(self, dni):
        super().__init__(f"DNI inválido: {dni}")

class NombreInvalidoError(PacienteError):
    def __init__(self, nombre):
        super().__init__(f"Nombre inválido: {nombre}")

class FechaNacimientoInvalidaError(Exception):
    def __init__(self, fecha):
        super().__init__(f"Fecha de nacimiento inválida: {fecha}")


#MEDICO
class MedicoError(Exception):
    """Excepción base para errores relacionados con médicos."""
    pass

class MatriculaInvalidaError(MedicoError):
    def __init__(self, matricula):
        super().__init__(f"Matricula inválida: {matricula}")

class EspecialidadInvalidaError(MedicoError):
    def __init__(self, especialidad):
        super().__init__(f"Especialidad inválida: {especialidad}")

#ESPECIALIDAD
class EspecialidadInvalidaError(MedicoError):
    def __init__(self, especialidad):
        super().__init__(f"Especialidad inválida: {especialidad}")

#TURNO
class TurnoOcupadoError(MedicoError):
    def __init__(self, fecha_hora):
        super().__init__(f"Turno ocupado: {fecha_hora}")

class TurnoError(Exception):
    """Excepción base para errores relacionados con turnos."""
    pass

class TurnoDuplicadoError(TurnoError):
    def __init__(self, fecha_hora):
        super().__init__(f"Turno duplicado: {fecha_hora}")

class TurnoNoEncontradoError(TurnoError):
    def __init__(self, fecha_hora):
        super().__init__(f"Turno no encontrado: {fecha_hora}")

#RECETA
class RecetaError(Exception):
    """Excepción base para errores relacionados con recetas."""
    pass

class RecetaInvalidaError(RecetaError):
    def __init__(self, receta):
        super().__init__(f"Receta inválida: {receta}")

class RecetaNoEncontradaError(RecetaError):
    def __init__(self, dni):
        super().__init__(f"Receta no encontrada para el paciente con DNI: {dni}")

#HISTORIA_CLINICA
class HistoriaClinicaError(Exception):
    """Excepción base para errores relacionados con la historia clínica."""
    pass
class HistoriaClinicaInvalidaError(HistoriaClinicaError):
    def __init__(self, historia_clinica):
        super().__init__(f"Historia clínica inválida: {historia_clinica}")

class HistoriaClinicaNoEncontradaError(HistoriaClinicaError):
    def __init__(self, dni):
        super().__init__(f"Historia clínica no encontrada para el paciente con DNI: {dni}")

#CLINICA
class ClinicaError(Exception):
    """Excepción base para errores relacionados con la clinica."""
    pass

class ClinicaInvalidaError(ClinicaError):
    def __init__(self, clinica):
        super().__init__(f"Clínica inválida: {clinica}")

class ClinicaNoEncontradaError(ClinicaError):
    def __init__(self, dni):
        super().__init__(f"Clínica no encontrada para el paciente con DNI: {dni}")