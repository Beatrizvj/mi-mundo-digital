"""Pruebas del Panel del Docente (usan una base de datos temporal). Ejecutar: python -m unittest test_panel_docente -v"""
import os
import tempfile
import unittest


class PruebasPanel(unittest.TestCase):
    def setUp(self):
        self._cwd = os.getcwd()
        self._tmp = tempfile.TemporaryDirectory()
        os.chdir(self._tmp.name)
        import app
        import panel_docente
        self.app, self.panel = app, panel_docente
        app.inicializar_bd()

    def tearDown(self):
        os.chdir(self._cwd)
        self._tmp.cleanup()

    def test_reiniciar_deja_al_estudiante_como_nuevo(self):
        est = self.panel.agregar_estudiante("Ana López", 1)
        self.app.registrar_actividad_y_sumar_puntos(est, "m1_a1", 10)
        self.app.registrar_intento_evaluacion(est, 1, 90, True, self.app.MODULOS_PRIMERO)
        self.app.registrar_dia_actividad(est)
        self.panel.reiniciar_progreso(est)
        d = self.panel.progreso_detalle(est)
        self.assertEqual((d["puntos"], d["xp"], d["modulos_completados"], len(d["evaluaciones"]), len(d["insignias"])), (0, 0, 0, 0, 0))
        self.assertFalse(self.app.actividad_ya_completada(est, "m1_a1"))           # puede volver a ganar los puntos
        self.assertEqual(self.app.obtener_racha(est), (0, 0))
        self.assertEqual(d["nombre"], "Ana López")                                  # conserva nombre y grado
        self.assertEqual(d["grado"], 1)

    def test_eliminar_borra_tambien_sus_registros(self):
        est = self.panel.agregar_estudiante("Luis Pérez", 2)
        self.app.registrar_actividad_y_sumar_puntos(est, "s2m1_a1", 10)
        self.panel.eliminar_estudiante(est)
        self.assertEqual(self.panel.listar_estudiantes(), [])
        self.assertFalse(self.app.actividad_ya_completada(est, "s2m1_a1"))

    def test_busqueda_y_filtro(self):
        self.panel.agregar_estudiante("Ana López", 1)
        self.panel.agregar_estudiante("Carlos Pérez", 2)
        self.assertEqual([e[1] for e in self.panel.listar_estudiantes(busqueda="carl")], ["Carlos Pérez"])
        self.assertEqual([e[1] for e in self.panel.listar_estudiantes(grado=1)], ["Ana López"])


if __name__ == "__main__":
    unittest.main()
