import unittest
from datetime import datetime
from PACIENTE.paciente import Paciente
from MEDICO.medico import Medico
from ESPECIALIDAD.especialidad import Especialidad
from HISTORIA_CLINICA.historia_clinica import HistoriaClinica
from TURNO.turno import Turno
from excepciones import HistoriaClinicaNoEncontradaError

class TestHistoriaClinica(unittest.TestCase):

    def setUp(self):
        especialidad = Especialidad("Pediatría", ["lunes", "miércoles"])
        self.medico = Medico("Zoe Camus", "0001", [especialidad])
        self.paciente = Paciente("Juan Pérez", "12345678", "12/12/2000")
        self.historia = HistoriaClinica(self.paciente)

    def test_creacion_historia_clinica(self):
        self.assertEqual(self.historia.obtener_paciente(), self.paciente)
        self.assertEqual(self.historia.obtener_turnos(), [])
        self.assertEqual(self.historia.obtener_recetas(), [])

    def test_validar_existe_historia_clinica(self):
        historias = [self.historia]
        try:
            HistoriaClinica.validar_existe_historia_clinica(historias, "12345678")
        except HistoriaClinicaNoEncontradaError:
            self.fail("HistoriaClinicaNoEncontradaError fue lanzado incorrectamente")

    def test_validar_existe_historia_clinica_error(self):
        historias = [self.historia]
        with self.assertRaises(HistoriaClinicaNoEncontradaError):
            HistoriaClinica.validar_existe_historia_clinica(historias, "999")

    def test_agregar_turno(self):
        fecha = "2025-06-10 10:00"
        fecha_dt = datetime.strptime(fecha, "%Y-%m-%d %H:%M")  

        HistoriaClinica.agregar_turno(self.historia, self.medico, "Pediatría", fecha)
        self.assertEqual(len(self.historia.obtener_turnos()), 1)
        self.assertEqual(self.historia.obtener_turnos()[0].obtener_fecha_hora(), fecha_dt)
        self.assertEqual(self.historia.obtener_turnos()[0].obtener_paciente(), self.paciente)


if __name__ == '__main__':
    unittest.main()
