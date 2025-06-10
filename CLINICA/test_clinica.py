import unittest
from datetime import datetime
from CLINICA.clinica import Clinica
from PACIENTE.paciente import Paciente
from MEDICO.medico import Medico
from ESPECIALIDAD.especialidad import Especialidad
from excepciones import (
    PacienteError,
    MedicoError,
    TurnoDuplicadoError
)

class TestClinica(unittest.TestCase):
    fecha = datetime.strptime("2025-06-07 15:00", "%Y-%m-%d %H:%M")

    def setUp(self):
        self.paciente = Paciente("Jose Pérez","12345678" ,"12/12/2000")
        self.medico = Medico("Zoe Camus", "0001", [Especialidad("Pediatría", ["lunes", "martes"]),
        Especialidad("Cardiología", ["miércoles", "jueves"])])
        self.clinica = Clinica()

        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)

    def test_agregar_paciente(self):
        nuevo = Paciente("Laura Gonzalez", "87654321", "12/10/2000")
        self.clinica.agregar_paciente(nuevo)
        pacientes = self.clinica.obtener_pacientes()
        self.assertIn(nuevo, pacientes)

    def test_agregar_medico(self):
        nuevo = Medico("Daniel Morales","0002",["Neurología"])
        self.clinica.agregar_medico(nuevo)
        self.assertIn(nuevo, self.clinica.obtener_medicos())

    def test_obtener_medico_por_matricula(self):
        medico = self.clinica.obtener_medico_por_matricula("0001")
        especialidad = medico.obtener_especialidad_para_dia("martes") 
        self.assertEqual(especialidad, "Pediatría")

    def test_validar_existencia_paciente_ok(self):
        self.clinica.validar_existencia_paciente("12345678")

    def test_validar_existencia_paciente_error(self):
        with self.assertRaises(PacienteError):
            self.clinica.validar_existencia_paciente("99999999")

    def test_validar_existencia_medico_ok(self):
        self.clinica.validar_existencia_medico("0001")

    def test_validar_existencia_medico_error(self):
        with self.assertRaises(MedicoError):
            self.clinica.validar_existencia_medico("11111111")

    def test_agendar_turno_ok(self):
        fecha = datetime(2025, 6, 10, 10, 0)
        self.clinica.agendar_turno("12345678", "0001", "Pediatría", fecha)
        turnos = self.clinica.obtener_turnos()
        self.assertEqual(len(turnos), 1)
        self.assertEqual(turnos[0].obtener_fecha_hora(), fecha)


    def test_agendar_turno_duplicado_error(self):
        fecha = datetime.strptime("2025-06-10 10:00", "%Y-%m-%d %H:%M")
        self.clinica.agendar_turno("12345678", "0001", "Pediatría", fecha)
        with self.assertRaises(TurnoDuplicadoError):
            self.clinica.agendar_turno("12345678", "0001", "Pediatría", fecha)



    def test_emitir_receta(self):
        fecha = datetime(2025, 6, 10, 10, 0)
        self.clinica.agendar_turno("12345678", "0001", "Pediatría", fecha)
        self.clinica.emitir_receta("12345678", "0001", ["Paracetamol", "Ibuprofeno"])
        recetas = self.clinica.obtener_historia_clinica_por_dni("12345678").obtener_recetas()
        self.assertEqual(len(recetas), 1)
        self.assertEqual(recetas[0].obtener_medicamentos(), ["Paracetamol", "Ibuprofeno"])


    def test_obtener_dia_semana(self):
        fecha = datetime.strptime("2025-06-06 14:30", "%Y-%m-%d %H:%M") 
        dia = self.clinica.obtener_dia_semana_en_espanol(fecha)
        self.assertEqual(dia, "viernes")

if __name__ == "__main__":
    unittest.main()
