import unittest
from ESPECIALIDAD.especialidad import Especialidad
from excepciones import EspecialidadInvalidaError

class TestEspecialidad(unittest.TestCase):

    def test_creacion_valida(self):
        esp = Especialidad("Pediatría", ["lunes", "miércoles"])
        self.assertEqual(esp.obtener_especialidad(), "Pediatría")
        self.assertTrue(esp.atiende_el_dia("lunes"))
        self.assertTrue(esp.atiende_el_dia("Miércoles"))
        self.assertFalse(esp.atiende_el_dia("domingo"))

    def test_str(self):
        esp = Especialidad("Cardiología", ["martes", "jueves"])
        self.assertEqual(str(esp), "Cardiología (Días: martes, jueves)")

    def test_nombre_invalido_vacio(self):
        with self.assertRaises(EspecialidadInvalidaError):
            Especialidad("", ["lunes"])

    def test_nombre_invalido_caracteres(self):
        with self.assertRaises(EspecialidadInvalidaError):
            Especialidad("Cardiología123", ["martes"])

        with self.assertRaises(EspecialidadInvalidaError):
            Especialidad("Pediatría!", ["miércoles"])

if __name__ == "__main__":
    unittest.main()
