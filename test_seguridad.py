"""Pruebas de seguridad (Fase 3 del Seminario). Ejecutar: python -m unittest test_seguridad -v"""
import os
import sqlite3
import tempfile
import unittest

import seguridad


class PruebasPassword(unittest.TestCase):
    def test_hash_no_es_texto_plano_y_tiene_formato(self):
        h = seguridad.hashear_password("ClaveSegura1")
        self.assertNotIn("ClaveSegura1", h)
        alg, iters, sal, dig = h.split("$")
        self.assertEqual(alg, "pbkdf2_sha256")
        self.assertGreaterEqual(int(iters), 200_000)
        self.assertEqual(len(bytes.fromhex(sal)), 16)

    def test_sal_unica_hashes_distintos_para_misma_clave(self):
        self.assertNotEqual(seguridad.hashear_password("igual1234"), seguridad.hashear_password("igual1234"))

    def test_verificacion_correcta_e_incorrecta(self):
        h = seguridad.hashear_password("ClaveSegura1")
        self.assertTrue(seguridad.verificar_password("ClaveSegura1", h))
        self.assertFalse(seguridad.verificar_password("clavesegura1", h))
        self.assertFalse(seguridad.verificar_password("admin123", h))

    def test_hash_corrupto_no_lanza_excepcion(self):
        self.assertFalse(seguridad.verificar_password("x", "basura"))
        self.assertFalse(seguridad.verificar_password("x", None))

    def test_politica_de_contrasena(self):
        self.assertFalse(seguridad.validar_password_nueva("corta")[0])
        self.assertFalse(seguridad.validar_password_nueva("12345678")[0])
        self.assertTrue(seguridad.validar_password_nueva("Docente2026")[0])


class PruebasAlmacenamiento(unittest.TestCase):
    def test_guardar_y_leer_hash(self):
        with tempfile.TemporaryDirectory() as d:
            db = os.path.join(d, "t.db")
            seguridad.inicializar_seguridad(db)
            self.assertIsNone(seguridad.obtener_hash_docente(db))
            seguridad.guardar_password_docente("Docente2026", db)
            h = seguridad.obtener_hash_docente(db)
            self.assertTrue(seguridad.verificar_password("Docente2026", h))
            con = sqlite3.connect(db)
            crudo = con.execute("SELECT valor FROM configuracion").fetchall()
            con.close()
            self.assertNotIn("Docente2026", str(crudo))


class PruebasBloqueo(unittest.TestCase):
    def test_bloquea_tras_tres_fallos_y_libera_con_el_tiempo(self):
        t = [0.0]
        lim = seguridad.LimiteIntentos(3, 30, reloj=lambda: t[0])
        self.assertFalse(lim.registrar_fallo())
        self.assertFalse(lim.registrar_fallo())
        self.assertFalse(lim.bloqueado())
        self.assertTrue(lim.registrar_fallo())
        self.assertTrue(lim.bloqueado())
        t[0] = 31.0
        self.assertFalse(lim.bloqueado())

    def test_exito_reinicia_contador(self):
        lim = seguridad.LimiteIntentos(3, 30)
        lim.registrar_fallo()
        lim.registrar_fallo()
        lim.registrar_exito()
        self.assertFalse(lim.registrar_fallo())


class PruebasNombre(unittest.TestCase):
    def test_validos(self):
        self.assertEqual(seguridad.validar_nombre("  María   José  Pérez ")[1], "María José Pérez")
        self.assertTrue(seguridad.validar_nombre("O'Connor-Díaz")[0])

    def test_invalidos(self):
        for malo in (None, "", "   ", "A", "x" * 61, "Juan123", "Robert'); DROP TABLE estudiantes;--", "<script>"):
            self.assertFalse(seguridad.validar_nombre(malo)[0], malo)


class PruebasSQL(unittest.TestCase):
    def test_consultas_de_app_estan_parametrizadas(self):
        """Ninguna llamada a execute() concatena/formatea datos en el SQL (salvo el ALTER de migración)."""
        import re
        ruta = os.path.join(os.path.dirname(__file__), "app.py")
        with open(ruta, encoding="utf-8") as f:
            codigo = f.read()
        sospechosas = re.findall(r'execute\(\s*(?:f["\']|["\'][^"\']*["\']\s*(?:%|\+))', codigo)
        self.assertEqual(sospechosas, [])

    def test_no_hay_contrasena_hardcodeada(self):
        ruta = os.path.join(os.path.dirname(__file__), "app.py")
        with open(ruta, encoding="utf-8") as f:
            self.assertNotIn("admin123", f.read())


class PruebasLog(unittest.TestCase):
    def test_sanea_saltos_de_linea(self):
        self.assertNotIn("\n", seguridad._limpiar("uno\nFALSO | evento\r\n"))


if __name__ == "__main__":
    unittest.main()
