import unittest
from datetime import datetime
from MEDICO.medico import Medico
from PACIENTE.paciente import Paciente
from ESPECIALIDAD.especialidad import Especialidad
from TURNO.turno import Turno
from excepciones import TurnoError, TurnoOcupadoError, TurnoNoEncontradoError

class TestTurno(unittest.TestCase):
    def setUp(self):
 
        self.fecha_lunes = datetime.strptime("2025-06-09 10:00", "%Y-%m-%d %H:%M")     
        self.fecha_martes = datetime.strptime("2025-06-10 10:00", "%Y-%m-%d %H:%M")    
        self.fecha_jueves = datetime.strptime("2025-06-12 10:00", "%Y-%m-%d %H:%M")    

  
        self.pediatria = Especialidad("Pediatría", ["lunes", "miércoles", "viernes"])
        self.cardiologia = Especialidad("Cardiología", ["martes", "jueves"])
        self.cirugia = Especialidad("Cirugía", ["lunes"])
        self.neurologia = Especialidad("Neurología", ["martes"])

   
        self.medico_zoe = Medico("Zoe Camus", "0001", [self.pediatria, self.cardiologia])
        self.medico_daniel = Medico("Daniel Morales", "0002", [self.cirugia, self.neurologia])

 
        self.paciente_juan = Paciente("Juan Pérez", "12345678", "01/01/1980")
        self.paciente_laura = Paciente("Laura", "87654321", "15/03/1995")

        self.turno = Turno(self.medico_zoe, self.paciente_juan, "Pediatría", self.fecha_lunes)

    def test_turno_ocupado(self):
        with self.assertRaises(TurnoOcupadoError):
            Turno.validar_turno_ocupado([self.turno], "2025-06-09 10:00")

    def test_turno_no_encontrado(self):
        with self.assertRaises(TurnoNoEncontradoError):
            Turno.validar_existe_turno([self.turno], "2025-06-15 10:00")

    def test_turno(self):
        self.assertEqual(self.turno.obtener_medico(), self.medico_zoe)
        self.assertEqual(self.turno.obtener_paciente(), self.paciente_juan)
        self.assertEqual(self.turno.obtener_fecha_hora(), self.fecha_lunes)


    def test_turno_especialidad_valida(self):
        Turno.validar_especialidad(self.medico_daniel, "Cirugía")  

    def test_turno_especialidad_invalida(self):
        with self.assertRaises(TurnoError):
            Turno.validar_especialidad(self.medico_daniel, "Cardiología")  

    def test_str(self):
        texto = str(self.turno)
        self.assertIn("Juan Pérez", texto)
        self.assertIn("Zoe Camus", texto)
        self.assertIn("Pediatría", texto)

if __name__ == "__main__":
    unittest.main()
