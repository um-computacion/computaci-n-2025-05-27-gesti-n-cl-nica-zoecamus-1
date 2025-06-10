import unittest
from MEDICO.medico import Medico
from ESPECIALIDAD.especialidad import Especialidad
from excepciones import MatriculaInvalidaError, NombreInvalidoError

class TestMedico(unittest.TestCase):

    def setUp(self):
        self.pediatria = Especialidad("Pediatría", ["lunes", "miércoles", "viernes"])
        self.cardiologia = Especialidad("Cardiología", ["martes", "jueves"])
        self.cirugia = Especialidad("Cirugía", ["lunes"])
        self.neurologia = Especialidad("Neurología", ["martes"])

        self.medico = Medico("Zoe Camus", "0001", [
        self.pediatria,
        self.cardiologia,])
        self.medico = Medico("Daniel Morales", "0002", [
        self.cirugia,
        self.neurologia])

    def test_crear_medico_y_obtener_datos(self):
        m = Medico("Zoe Camus", "0001", [self.pediatria])
        m.agregar_especialidad(self.cardiologia)

        self.assertEqual(m.obtener_matricula(), "0001")
        self.assertEqual(m.obtener_especialidad_para_dia("lunes"), "Pediatría")
        self.assertEqual(m.obtener_especialidad_para_dia("martes"), "Cardiología")
        self.assertIsNone(m.obtener_especialidad_para_dia("domingo"))

    def test_str_medico(self):
        m = Medico("Zoe Camus", "0001", [self.pediatria, self.cardiologia])
        salida = str(m)
        self.assertIn("Pediatría", salida)
        self.assertIn("Cardiología", salida)
        self.assertIn("lunes", salida)

if __name__ == "__main__":
    unittest.main()