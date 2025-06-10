import unittest
from PACIENTE.paciente import Paciente
from excepciones import DniInvalidoError, NombreInvalidoError


class TestPaciente(unittest.TestCase):

    def test_crear_paciente(self):
        p = Paciente("Juan Pérez", "12345678", "12/12/2000")
        self.assertEqual(p.nombre, "Juan Pérez")
        self.assertEqual(p.obtener_dni(), "12345678")
        self.assertEqual(p.fecha_nacimiento, "12/12/2000")
        self.assertEqual(str(p), "Juan Pérez, 12345678, 12/12/2000")

    def test_nombre_invalido_vacio(self):
        with self.assertRaises(NombreInvalidoError):
            Paciente("", "12345678", "12/12/2000")

    def test_nombre_invalido_con_numeros(self):
        with self.assertRaises(NombreInvalidoError):
            Paciente("Juan123", "12345678", "12/12/2000")

    def test_dni_invalido_corto(self):
        with self.assertRaises(DniInvalidoError):
            Paciente("Juan Pérez", "1234", "12/12/2000")

    def test_dni_invalido_con_letras(self):
        with self.assertRaises(DniInvalidoError):
            Paciente("Juan Pérez", "1234ABCD", "12/12/2000")

if __name__ == "__main__":
    unittest.main()
