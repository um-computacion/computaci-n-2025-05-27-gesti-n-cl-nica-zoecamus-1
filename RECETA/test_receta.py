import unittest
from datetime import datetime
from RECETA.receta import Receta
from PACIENTE.paciente import Paciente
from MEDICO.medico import Medico
from ESPECIALIDAD.especialidad import Especialidad
from excepciones import RecetaNoEncontradaError, TurnoError

class TestReceta(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Juan Pérez", "12345678", "12/12/2000")
        especialidad = Especialidad("Pediatría", ["miércoles"])
        self.medico = Medico("Zoe Camus", "0001", [especialidad])
        self.medicamentos = ["Ibuprofeno", "Paracetamol"]
        self.receta = Receta(self.paciente, self.medico, self.medicamentos)

    def test_str(self):
        resultado = str(self.receta)
        self.assertIn("Paciente: Juan Pérez", resultado)
        self.assertIn("Médico: Zoe Camus", resultado)
        self.assertIn("Ibuprofeno", resultado)

    def test_validar_existe_receta_valido(self):
        recetas = [self.receta]
        try:
            Receta.validar_existe_receta(recetas, "12345678")
        except RecetaNoEncontradaError:
            self.fail("RecetaNoEncontradaError fue lanzado incorrectamente.")

    def test_validar_existe_receta_invalido(self):
        recetas = [self.receta]
        with self.assertRaises(RecetaNoEncontradaError):
            Receta.validar_existe_receta(recetas, "00000000")

    def test_validar_especialidad_valida(self):
        try:
            Receta.validar_especialidad(self.medico, "Pediatría")
        except TurnoError:
            self.fail("TurnoError fue lanzado incorrectamente.")

    def test_validar_especialidad_invalida(self):
        with self.assertRaises(TurnoError):
            Receta.validar_especialidad(self.medico, "Cardiología")

if __name__ == "__main__":
    unittest.main()
