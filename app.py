import sqlite3
import random
import time
import datetime
import tkinter as tk
import tkinter.font as tkfont
from tkinter import messagebox, simpledialog, ttk
from contenido_primero import MODULOS_PRIMERO
from contenido_segundo import MODULOS_SEGUNDO
from contenido_tercero import MODULOS_TERCERO
from contenido_mecanografia import FILAS_TECLADO, DEDO_COLOR, LECCIONES_MECANOGRAFIA
import logging
import traceback
import seguridad
import panel_docente
import inicio_animado
import os
import sys


def ruta_recurso(nombre):
    """Ruta de un archivo incluido con la app (funciona con python app.py y dentro del .exe)."""
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, nombre)

# Número de módulos de Primero Básico (se calcula solo a partir del contenido).
TOTAL_MODULOS_PRIMERO = len(MODULOS_PRIMERO)

# Grados que usan el sistema de módulos (Primero, Segundo y Tercero). El motor es el mismo para todos.
MODULOS_POR_GRADO = {1: MODULOS_PRIMERO, 2: MODULOS_SEGUNDO, 3: MODULOS_TERCERO}
PREFIJO_GRADO = {1: "", 2: "s2", 3: "s3"}   # prefijo de las claves de actividad/evaluación por grado
PUNTOS_EVAL_GRADO = {1: 15, 2: 20, 3: 25}   # puntos por aprobar la evaluación de un módulo


def datos_grado(grado):
    """Devuelve (modulos, prefijo, total_modulos) del grado dado (por defecto, Primero)."""
    modulos = MODULOS_POR_GRADO.get(grado, MODULOS_PRIMERO)
    return modulos, PREFIJO_GRADO.get(grado, ""), len(modulos)


def inicializar_bd():
    conexion = sqlite3.connect("encarta_educativa.db")
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estudiantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            grado INTEGER NOT NULL,
            puntos INTEGER DEFAULT 0,
            insignias TEXT DEFAULT ""
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS progreso (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            estudiante_id INTEGER,
            tema TEXT,
            completado INTEGER DEFAULT 0,
            calificacion INTEGER DEFAULT 0,
            FOREIGN KEY(estudiante_id) REFERENCES estudiantes(id)
        )
    """)
    # --- Nuevas tablas para el sistema de puntos, módulos y evaluaciones de Primero Básico ---
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS actividades_completadas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            estudiante_id INTEGER,
            actividad_key TEXT,
            puntos INTEGER DEFAULT 0,
            UNIQUE(estudiante_id, actividad_key)
        )
    """)
    # --- Reto diario: una fila por estudiante y día ---
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS retos_diarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            estudiante_id INTEGER,
            fecha TEXT,
            hecho INTEGER DEFAULT 0,
            UNIQUE(estudiante_id, fecha)
        )
    """)
    # --- Curso de mecanografía: progreso por practicante y lección ---
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mecanografia (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            perfil TEXT,
            leccion INTEGER,
            mejor_ppm INTEGER DEFAULT 0,
            mejor_precision INTEGER DEFAULT 0,
            completada INTEGER DEFAULT 0,
            UNIQUE(perfil, leccion)
        )
    """)
    # --- Migración compatible: agrega columnas nuevas a 'estudiantes' si aún no existen ---
    cursor.execute("PRAGMA table_info(estudiantes)")
    columnas_existentes = {fila[1] for fila in cursor.fetchall()}
    nuevas_columnas = {
        "xp": "INTEGER DEFAULT 0",
        "racha": "INTEGER DEFAULT 0",
        "mejor_racha": "INTEGER DEFAULT 0",
        "ultima_fecha": "TEXT DEFAULT ''",
    }
    for col, definicion in nuevas_columnas.items():
        if col not in columnas_existentes:
            cursor.execute("ALTER TABLE estudiantes ADD COLUMN {} {}".format(col, definicion))
    conexion.commit()
    conexion.close()
    seguridad.inicializar_seguridad()


# =====================================================================================
#  CONTENIDO EDUCATIVO - PRIMERO BÁSICO
#  El contenido de los 12 módulos vive en contenido_primero.py (MODULOS_PRIMERO).
#  Aquí solo quedan las insignias y el motor, que funciona con cualquier número de módulos.
# =====================================================================================

INSIGNIAS_INFO = {
    "primeros_pasos": {"nombre": "🏅 Primeros pasos", "desc": "Completar el primer módulo"},
    "explorador_digital": {"nombre": "💻 Explorador digital", "desc": "Completar los módulos 1 y 2"},
    "mente_logica": {"nombre": "🧠 Mente lógica", "desc": "Dominar el módulo de pensamiento lógico"},
    "resolutor": {"nombre": "🧩 Resolutor", "desc": "Dominar el módulo de resolución de problemas"},
    "navegante_seguro": {"nombre": "🛡️ Navegante seguro", "desc": "Completar Internet y Seguridad digital"},
    "programador_junior": {"nombre": "🧑‍💻 Programador junior", "desc": "Completar Pensamiento computacional y Programación"},
    "maestro_juegos": {"nombre": "🎮 Maestro de retos", "desc": "Superar los retos del módulo final"},
    "experto_primero": {"nombre": "🏆 Experto Digital – Primero Básico", "desc": "Completar los 12 módulos"},
    # --- Insignias de Segundo Básico ---
    "s2_tecnico": {"nombre": "💻 Técnico Junior", "desc": "Dominar Hardware y software avanzado"},
    "s2_redes": {"nombre": "🌐 Explorador de Redes", "desc": "Completar el módulo de Redes"},
    "s2_guardian": {"nombre": "🔐 Guardián Digital", "desc": "Completar Seguridad informática"},
    "s2_logica": {"nombre": "🧠 Maestro de la Lógica", "desc": "Dominar Pensamiento lógico"},
    "s2_resolutor": {"nombre": "🧩 Resolutor de Problemas", "desc": "Dominar Algoritmos y diagramas de flujo"},
    "s2_prog": {"nombre": "👨‍💻 Programador Junior", "desc": "Completar Introducción a la programación"},
    "s2_datos": {"nombre": "📊 Analista de Datos", "desc": "Completar Datos y bases de datos"},
    "s2_ia": {"nombre": "🤖 Explorador de IA", "desc": "Completar Inteligencia artificial"},
    "s2_maestro": {"nombre": "🏆 Maestro Digital de Segundo Básico", "desc": "Completar los 12 módulos de Segundo"},
    # --- Insignias de Tercero Básico ---
    "s3_tecnico": {"nombre": "💻 Técnico Junior", "desc": "Dominar Arquitectura de computadoras"},
    "s3_algoritmos": {"nombre": "🧠 Maestro de Algoritmos", "desc": "Completar Algoritmos avanzados"},
    "s3_prog": {"nombre": "👨‍💻 Programador Junior", "desc": "Completar el módulo de Programación"},
    "s3_web": {"nombre": "🌐 Desarrollador Web Junior", "desc": "Completar Desarrollo web"},
    "s3_datos": {"nombre": "🗄️ Analista de Datos Junior", "desc": "Dominar Bases de datos y SQL"},
    "s3_redes": {"nombre": "🌐 Ingeniero de Redes Junior", "desc": "Completar el módulo de Redes"},
    "s3_guardian": {"nombre": "🔐 Guardián de la Seguridad", "desc": "Completar Ciberseguridad"},
    "s3_ia": {"nombre": "🤖 Explorador de IA", "desc": "Completar IA y ciencia de datos"},
    "s3_ciudadano": {"nombre": "🌎 Ciudadano Digital", "desc": "Completar Ética y ciudadanía digital"},
    "s3_innovador": {"nombre": "🚀 Innovador Tecnológico", "desc": "Completar Nube y tecnologías modernas"},
    "s3_maestro": {"nombre": "🏆 Maestro Digital – Tercero Básico", "desc": "Completar el proyecto final"},
    "s3_explorador": {"nombre": "🚀 Joven Explorador de Tecnología", "desc": "Completar los 12 módulos de Tercero"},
}

# =====================================================================================
#  FUNCIONES AUXILIARES: PUNTOS, DESBLOQUEO, INSIGNIAS Y EVALUACIONES
# =====================================================================================

def actividad_ya_completada(estudiante_id, actividad_key):
    conexion = sqlite3.connect("encarta_educativa.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT id FROM actividades_completadas WHERE estudiante_id=? AND actividad_key=?",
                    (estudiante_id, actividad_key))
    existe = cursor.fetchone() is not None
    conexion.close()
    return existe


def registrar_actividad_y_sumar_puntos(estudiante_id, actividad_key, puntos):
    """Registra una actividad como completada (una sola vez) y suma los puntos al estudiante.
    Devuelve (puntos_totales_nuevos, se_otorgaron_puntos)."""
    if actividad_ya_completada(estudiante_id, actividad_key):
        conexion = sqlite3.connect("encarta_educativa.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT puntos FROM estudiantes WHERE id=?", (estudiante_id,))
        puntos_actuales = cursor.fetchone()[0]
        conexion.close()
        return puntos_actuales, False

    conexion = sqlite3.connect("encarta_educativa.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO actividades_completadas (estudiante_id, actividad_key, puntos) VALUES (?, ?, ?)",
                    (estudiante_id, actividad_key, puntos))
    cursor.execute("UPDATE estudiantes SET puntos = puntos + ?, xp = xp + ? WHERE id=?",
                    (puntos, puntos, estudiante_id))
    conexion.commit()
    cursor.execute("SELECT puntos FROM estudiantes WHERE id=?", (estudiante_id,))
    puntos_totales = cursor.fetchone()[0]
    conexion.close()
    return puntos_totales, True


# =====================================================================================
#  XP / NIVELES, RACHAS Y RETOS DIARIOS
# =====================================================================================

XP_POR_NIVEL = 100


def _hoy():
    return datetime.date.today().isoformat()


def calcular_nivel(xp):
    return (xp // XP_POR_NIVEL) + 1


def xp_en_nivel(xp):
    """Progreso de XP dentro del nivel actual (0 a XP_POR_NIVEL - 1)."""
    return xp % XP_POR_NIVEL


def obtener_xp_estudiante(estudiante_id):
    conexion = sqlite3.connect("encarta_educativa.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT xp FROM estudiantes WHERE id=?", (estudiante_id,))
    fila = cursor.fetchone()
    conexion.close()
    return (fila[0] if fila and fila[0] is not None else 0)


def sumar_xp(estudiante_id, cantidad):
    conexion = sqlite3.connect("encarta_educativa.db")
    cursor = conexion.cursor()
    cursor.execute("UPDATE estudiantes SET xp = xp + ? WHERE id=?", (cantidad, estudiante_id))
    conexion.commit()
    conexion.close()


def obtener_racha(estudiante_id):
    """Devuelve (racha_actual, mejor_racha)."""
    conexion = sqlite3.connect("encarta_educativa.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT racha, mejor_racha FROM estudiantes WHERE id=?", (estudiante_id,))
    fila = cursor.fetchone()
    conexion.close()
    if not fila:
        return 0, 0
    return (fila[0] or 0), (fila[1] or 0)


def registrar_dia_actividad(estudiante_id):
    """Actualiza la racha diaria según la fecha de hoy. Devuelve (racha_actual, cambio_hoy)."""
    conexion = sqlite3.connect("encarta_educativa.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT racha, mejor_racha, ultima_fecha FROM estudiantes WHERE id=?", (estudiante_id,))
    fila = cursor.fetchone()
    racha = (fila[0] or 0) if fila else 0
    mejor = (fila[1] or 0) if fila else 0
    ultima = (fila[2] or "") if fila else ""

    hoy = datetime.date.today()
    hoy_s = hoy.isoformat()
    cambio = False
    if ultima != hoy_s:
        ayer_s = (hoy - datetime.timedelta(days=1)).isoformat()
        racha = racha + 1 if ultima == ayer_s else 1
        mejor = max(mejor, racha)
        cursor.execute("UPDATE estudiantes SET racha=?, mejor_racha=?, ultima_fecha=? WHERE id=?",
                        (racha, mejor, hoy_s, estudiante_id))
        conexion.commit()
        cambio = True
    conexion.close()
    return racha, cambio


def reto_diario_hecho(estudiante_id, fecha=None):
    fecha = fecha or _hoy()
    conexion = sqlite3.connect("encarta_educativa.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT hecho FROM retos_diarios WHERE estudiante_id=? AND fecha=?", (estudiante_id, fecha))
    fila = cursor.fetchone()
    conexion.close()
    return bool(fila and fila[0])


def marcar_reto_diario(estudiante_id, fecha=None):
    fecha = fecha or _hoy()
    conexion = sqlite3.connect("encarta_educativa.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT OR REPLACE INTO retos_diarios (estudiante_id, fecha, hecho) VALUES (?, ?, 1)",
                    (estudiante_id, fecha))
    conexion.commit()
    conexion.close()


# =====================================================================================
#  PROGRESO DEL CURSO DE MECANOGRAFÍA (por practicante y lección)
# =====================================================================================

def obtener_progreso_meca(perfil):
    """Devuelve {indice_leccion: (mejor_ppm, mejor_precision, completada)}."""
    conexion = sqlite3.connect("encarta_educativa.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT leccion, mejor_ppm, mejor_precision, completada FROM mecanografia WHERE perfil=?", (perfil,))
    datos = {r[0]: (r[1], r[2], r[3]) for r in cursor.fetchall()}
    conexion.close()
    return datos


def guardar_progreso_meca(perfil, leccion, ppm, precision, completada):
    """Guarda el mejor resultado de una lección (solo mejora los récords)."""
    conexion = sqlite3.connect("encarta_educativa.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT mejor_ppm, mejor_precision, completada FROM mecanografia WHERE perfil=? AND leccion=?",
                    (perfil, leccion))
    fila = cursor.fetchone()
    if fila is None:
        cursor.execute("INSERT INTO mecanografia (perfil, leccion, mejor_ppm, mejor_precision, completada) VALUES (?,?,?,?,?)",
                        (perfil, leccion, ppm, precision, 1 if completada else 0))
    else:
        mejor_ppm = max(fila[0] or 0, ppm)
        mejor_prec = max(fila[1] or 0, precision)
        comp = 1 if (completada or fila[2]) else 0
        cursor.execute("UPDATE mecanografia SET mejor_ppm=?, mejor_precision=?, completada=? WHERE perfil=? AND leccion=?",
                        (mejor_ppm, mejor_prec, comp, perfil, leccion))
    conexion.commit()
    conexion.close()


def obtener_puntos_estudiante(estudiante_id):
    conexion = sqlite3.connect("encarta_educativa.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT puntos FROM estudiantes WHERE id=?", (estudiante_id,))
    puntos = cursor.fetchone()[0]
    conexion.close()
    return puntos


def obtener_insignias_estudiante(estudiante_id):
    conexion = sqlite3.connect("encarta_educativa.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT insignias FROM estudiantes WHERE id=?", (estudiante_id,))
    texto = cursor.fetchone()[0] or ""
    conexion.close()
    return [k for k in texto.split(",") if k]


def otorgar_insignia(estudiante_id, clave_insignia):
    actuales = obtener_insignias_estudiante(estudiante_id)
    if clave_insignia in actuales:
        return False
    actuales.append(clave_insignia)
    conexion = sqlite3.connect("encarta_educativa.db")
    cursor = conexion.cursor()
    cursor.execute("UPDATE estudiantes SET insignias=? WHERE id=?", (",".join(actuales), estudiante_id))
    conexion.commit()
    conexion.close()
    return True


def contar_actividades_completadas(estudiante_id, categoria=None, prefijo_modulo=None):
    conexion = sqlite3.connect("encarta_educativa.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT actividad_key FROM actividades_completadas WHERE estudiante_id=?", (estudiante_id,))
    claves = [r[0] for r in cursor.fetchall()]
    conexion.close()
    if prefijo_modulo:
        claves = [c for c in claves if c.startswith(prefijo_modulo)]
    return len(claves)


def modulo_esta_desbloqueado(modulo_id, puntos, modulos=None):
    if modulos is None:
        modulos = MODULOS_PRIMERO
    return puntos >= modulos[modulo_id]["umbral"]


def modulo_esta_completo(estudiante_id, modulo_id, modulos=None, prefijo=""):
    """Un módulo está completo si todas sus actividades y su evaluación fueron aprobadas."""
    if modulos is None:
        modulos = MODULOS_PRIMERO
    data = modulos[modulo_id]
    for act in data["actividades"]:
        if not actividad_ya_completada(estudiante_id, act["id"]):
            return False
    return evaluacion_aprobada(estudiante_id, modulo_id, prefijo)


def evaluacion_aprobada(estudiante_id, modulo_id, prefijo=""):
    return actividad_ya_completada(estudiante_id, "{}m{}_evaluacion".format(prefijo, modulo_id))


def registrar_intento_evaluacion(estudiante_id, modulo_id, calificacion_pct, aprobado, modulos=None):
    if modulos is None:
        modulos = MODULOS_PRIMERO
    conexion = sqlite3.connect("encarta_educativa.db")
    cursor = conexion.cursor()
    tema = "Evaluación Módulo {} - {}".format(modulo_id, modulos[modulo_id]["titulo"])
    cursor.execute("INSERT INTO progreso (estudiante_id, tema, completado, calificacion) VALUES (?, ?, ?, ?)",
                    (estudiante_id, tema, 1 if aprobado else 0, calificacion_pct))
    conexion.commit()
    conexion.close()


def verificar_y_otorgar_insignias(estudiante_id, grado=1):
    """Revisa las condiciones de cada insignia y las otorga si corresponde.
    Devuelve la lista de insignias NUEVAS otorgadas en esta verificación."""
    if grado == 2:
        return verificar_insignias_segundo(estudiante_id)
    if grado == 3:
        return verificar_insignias_tercero(estudiante_id)
    nuevas = []

    if modulo_esta_completo(estudiante_id, 1):
        if otorgar_insignia(estudiante_id, "primeros_pasos"):
            nuevas.append("primeros_pasos")

    if modulo_esta_completo(estudiante_id, 1) and modulo_esta_completo(estudiante_id, 2):
        if otorgar_insignia(estudiante_id, "explorador_digital"):
            nuevas.append("explorador_digital")

    # Pensamiento lógico = Módulo 7
    logica_completadas = contar_actividades_completadas(estudiante_id, prefijo_modulo="m7_")
    if logica_completadas >= 5 and evaluacion_aprobada(estudiante_id, 7):
        if otorgar_insignia(estudiante_id, "mente_logica"):
            nuevas.append("mente_logica")

    # Resolución de problemas = Módulo 8
    problemas_completados = contar_actividades_completadas(estudiante_id, prefijo_modulo="m8_")
    if problemas_completados >= 5 and evaluacion_aprobada(estudiante_id, 8):
        if otorgar_insignia(estudiante_id, "resolutor"):
            nuevas.append("resolutor")

    # Internet (5) + Seguridad digital (6)
    if modulo_esta_completo(estudiante_id, 5) and modulo_esta_completo(estudiante_id, 6):
        if otorgar_insignia(estudiante_id, "navegante_seguro"):
            nuevas.append("navegante_seguro")

    # Pensamiento computacional (9) + Programación (10)
    if modulo_esta_completo(estudiante_id, 9) and modulo_esta_completo(estudiante_id, 10):
        if otorgar_insignia(estudiante_id, "programador_junior"):
            nuevas.append("programador_junior")

    # Retos del módulo final = Módulo 12
    juegos_completados = contar_actividades_completadas(estudiante_id, prefijo_modulo="m12_")
    if juegos_completados >= 6:
        if otorgar_insignia(estudiante_id, "maestro_juegos"):
            nuevas.append("maestro_juegos")

    if all(modulo_esta_completo(estudiante_id, m) for m in range(1, TOTAL_MODULOS_PRIMERO + 1)):
        if otorgar_insignia(estudiante_id, "experto_primero"):
            nuevas.append("experto_primero")

    return nuevas


def verificar_insignias_segundo(estudiante_id):
    """Insignias de Segundo Básico (claves con prefijo s2_), otorgadas al completar módulos."""
    nuevas = []
    mods = MODULOS_SEGUNDO

    def _completo(mid):
        return modulo_esta_completo(estudiante_id, mid, mods, "s2")

    reglas = [
        ("s2_tecnico", 1),
        ("s2_redes", 4),
        ("s2_guardian", 6),
        ("s2_logica", 7),
        ("s2_resolutor", 8),
        ("s2_prog", 9),
        ("s2_datos", 10),
        ("s2_ia", 11),
    ]
    for clave, mid in reglas:
        if _completo(mid) and otorgar_insignia(estudiante_id, clave):
            nuevas.append(clave)

    if all(_completo(m) for m in range(1, len(mods) + 1)):
        if otorgar_insignia(estudiante_id, "s2_maestro"):
            nuevas.append("s2_maestro")
    return nuevas


def verificar_insignias_tercero(estudiante_id):
    """Insignias de Tercero Básico (claves con prefijo s3_), otorgadas al completar módulos."""
    nuevas = []
    mods = MODULOS_TERCERO

    def _completo(mid):
        return modulo_esta_completo(estudiante_id, mid, mods, "s3")

    reglas = [
        ("s3_tecnico", 1),
        ("s3_algoritmos", 3),
        ("s3_prog", 4),
        ("s3_web", 5),
        ("s3_datos", 6),
        ("s3_redes", 7),
        ("s3_guardian", 8),
        ("s3_ia", 9),
        ("s3_innovador", 10),
        ("s3_ciudadano", 11),
        ("s3_maestro", 12),
    ]
    for clave, mid in reglas:
        if _completo(mid) and otorgar_insignia(estudiante_id, clave):
            nuevas.append(clave)

    if all(_completo(m) for m in range(1, len(mods) + 1)):
        if otorgar_insignia(estudiante_id, "s3_explorador"):
            nuevas.append("s3_explorador")
    return nuevas


class EncartaEducativaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MI MUNDO DIGITAL")
        self.root.geometry("1040x720")
        self.root.minsize(880, 620)

        # ---------- Sistema de diseño ----------
        self.font_family = "Segoe UI"        # tipografía moderna (fallback del sistema)
        self.bg_color = "#EEF2F7"            # fondo claro
        self.primary_color = "#4F46E5"       # índigo vibrante
        self.primary_dark = "#3730A3"        # índigo oscuro (degradados)
        self.secondary_color = "#0D9488"     # verde azulado
        self.accent_color = "#F59E0B"        # ámbar
        self.text_dark = "#0F172A"
        self.text_muted = "#64748B"

        self.root.configure(bg=self.bg_color)

        self.grado_actual = None
        self.estudiante_actual = None
        self._meca_perfil = None   # nombre del practicante del curso de mecanografía
        try:
            self._logo_img = tk.PhotoImage(file=ruta_recurso("logo_ineb.png"))
        except tk.TclError:
            self._logo_img = None   # sin logo, la app funciona igual

        # Historial de navegación (botones ← →)
        self._historial = []
        self._pos = -1
        self._navegando = False

        inicializar_bd()
        self.limite_docente = seguridad.LimiteIntentos()
        self.crear_pantalla_bienvenida()

    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # ============ Utilidades de diseño (degradados y formas redondeadas) ============
    def _interp_color(self, c1, c2, t):
        """Interpola dos colores hex (#rrggbb) con t en [0,1]."""
        r1, g1, b1 = int(c1[1:3], 16), int(c1[3:5], 16), int(c1[5:7], 16)
        r2, g2, b2 = int(c2[1:3], 16), int(c2[3:5], 16), int(c2[5:7], 16)
        r = int(r1 + (r2 - r1) * t)
        g = int(g1 + (g2 - g1) * t)
        b = int(b1 + (b2 - b1) * t)
        return "#{:02x}{:02x}{:02x}".format(max(0, min(255, r)), max(0, min(255, g)), max(0, min(255, b)))

    def _gradiente_vertical(self, canvas, w, h, c_top, c_bot, pasos=64):
        """Dibuja un degradado vertical llenando el canvas."""
        for i in range(pasos):
            y0 = int(h * i / pasos)
            y1 = int(h * (i + 1) / pasos) + 1
            color = self._interp_color(c_top, c_bot, i / (pasos - 1))
            canvas.create_rectangle(0, y0, w, y1, fill=color, outline=color)

    def _rect_redondeado(self, canvas, x0, y0, x1, y1, r, **kw):
        """Dibuja un rectángulo con esquinas redondeadas (polígono suavizado)."""
        pts = [x0 + r, y0, x1 - r, y0, x1, y0, x1, y0 + r, x1, y1 - r, x1, y1,
               x1 - r, y1, x0 + r, y1, x0, y1, x0, y1 - r, x0, y0 + r, x0, y0]
        return canvas.create_polygon(pts, smooth=True, **kw)

    def _gradiente_horizontal(self, canvas, w, h, c_izq, c_der, pasos=90):
        """Dibuja un degradado horizontal llenando el canvas."""
        for i in range(pasos):
            x0 = int(w * i / pasos)
            x1 = int(w * (i + 1) / pasos) + 1
            color = self._interp_color(c_izq, c_der, i / (pasos - 1))
            canvas.create_rectangle(x0, 0, x1, h, fill=color, outline=color)

    def _pill(self, canvas, x_der, cy, texto, fill_color, comando, tag, text_color="white", pad=15, alto=34):
        """Dibuja una pastilla (botón redondeado) que TERMINA en x_der y está centrada en cy.
        Devuelve el borde izquierdo (para encadenar pastillas de derecha a izquierda)."""
        f = tkfont.Font(family=self.font_family, size=10, weight="bold")
        ancho = f.measure(texto) + pad * 2
        x0 = x_der - ancho
        y0, y1 = cy - alto // 2, cy + alto // 2
        self._rect_redondeado(canvas, x0, y0, x_der, y1, alto // 2, fill=fill_color, outline="", tags=(tag,))
        canvas.create_text((x0 + x_der) // 2, cy, text=texto, font=(self.font_family, 10, "bold"),
                           fill=text_color, tags=(tag,))
        if comando is not None:
            canvas.tag_bind(tag, "<Button-1>", lambda e: comando())
            canvas.tag_bind(tag, "<Enter>", lambda e: canvas.config(cursor="hand2"))
            canvas.tag_bind(tag, "<Leave>", lambda e: canvas.config(cursor=""))
        return x0

    # ============ Navegación con historial (botones ← →) ============
    def _clave_estado(self, estado):
        if estado[0] == "bienvenida":
            return ("bienvenida",)
        return ("menu", estado[1][0], estado[2][0])   # tipo, grado, id_estudiante

    def _registrar_historial(self, estado):
        """Agrega un estado al historial (evita duplicar el estado actual)."""
        if self._navegando:
            return
        if self._pos >= 0 and self._clave_estado(self._historial[self._pos]) == self._clave_estado(estado):
            self._historial[self._pos] = estado   # actualiza datos sin duplicar
            return
        self._historial = self._historial[:self._pos + 1]
        self._historial.append(estado)
        self._pos = len(self._historial) - 1

    def _ir_a_estado(self, estado):
        self._navegando = True
        try:
            if estado[0] == "bienvenida":
                self.grado_actual = None
                self.estudiante_actual = None
                self.crear_pantalla_bienvenida()
            else:
                self.grado_actual = estado[1]
                self.estudiante_actual = estado[2]
                self.mostrar_menu_primero_basico()
        finally:
            self._navegando = False

    def ir_atras(self):
        if self._pos > 0:
            self._pos -= 1
            self._ir_a_estado(self._historial[self._pos])

    def ir_adelante(self):
        if self._pos < len(self._historial) - 1:
            self._pos += 1
            self._ir_a_estado(self._historial[self._pos])

    def _flechas_nav(self, canvas, x0, cy):
        """Dibuja los botones ← y → de navegación. Devuelve el borde derecho."""
        atras_ok = self._pos > 0
        adel_ok = self._pos < len(self._historial) - 1
        d, sep = 34, 8
        for i, (glf, ok, cmd, tag) in enumerate([
                ("←", atras_ok, self.ir_atras, "nav_atras"),
                ("→", adel_ok, self.ir_adelante, "nav_adelante")]):
            x = x0 + i * (d + sep)
            y0, y1 = cy - d // 2, cy + d // 2
            bg = "#FFFFFF" if ok else "#6D5DD3"
            fg = "#4F46E5" if ok else "#B9AFE8"
            self._rect_redondeado(canvas, x, y0, x + d, y1, 11, fill=bg, outline="", tags=(tag,))
            canvas.create_text(x + d // 2, cy - 1, text=glf, font=(self.font_family, 16, "bold"), fill=fg, tags=(tag,))
            if ok:
                canvas.tag_bind(tag, "<Button-1>", lambda e, c=cmd: c())
                canvas.tag_bind(tag, "<Enter>", lambda e: canvas.config(cursor="hand2"))
                canvas.tag_bind(tag, "<Leave>", lambda e: canvas.config(cursor=""))
        return x0 + 2 * d + sep

    def _opciones_barajadas(self, opciones, correcta):
        """Devuelve (opciones_mezcladas, nuevo_indice_correcto) para que la respuesta
        correcta no siempre quede en la misma posición."""
        indices = list(range(len(opciones)))
        random.shuffle(indices)
        nuevas = [opciones[i] for i in indices]
        return nuevas, indices.index(correcta)

    def crear_pantalla_bienvenida(self):
        self.limpiar_ventana()
        self.grado_actual = None
        self.estudiante_actual = None
        self._registrar_historial(("bienvenida", None, None))

        canvas = tk.Canvas(self.root, bg=self.primary_dark, highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        encabezado = inicio_animado.EncabezadoInicio(self, canvas, "#4F46E5", "#7C3AED")
        self._encabezado_inicio = encabezado   # evita que se libere mientras la pantalla está activa

        cards = [
            ("PRIMERO", "🌐", "#3B82F6", 1, "Fundamentos digitales"),
            ("SEGUNDO", "🧩", "#10B981", 2, "Productividad y redes"),
            ("TERCERO", "🚀", "#8B5CF6", 3, "Programación y datos"),
        ]

        def tarjeta(x, y, w, h, nombre, icono, color, nivel, desc):
            tag = "g%d" % nivel
            # Sombra + tarjeta blanca redondeada
            self._rect_redondeado(canvas, x + 5, y + 8, x + w + 5, y + h + 8, 24,
                                   fill=self._interp_color(self.primary_dark, "#000000", 0.3), outline="")
            self._rect_redondeado(canvas, x, y, x + w, y + h, 24, fill="white", outline="", tags=(tag,))
            # Insignia circular con el icono
            r = 34; cxx = x + w // 2; cyy = y + 54
            canvas.create_oval(cxx - r, cyy - r, cxx + r, cyy + r, fill=color, outline="", tags=(tag,))
            canvas.create_text(cxx, cyy, text=icono, font=(self.font_family, 30), tags=(tag,))
            canvas.create_text(cxx, y + 110, text=nombre, font=(self.font_family, 19, "bold"), fill=self.text_dark, tags=(tag,))
            canvas.create_text(cxx, y + 132, text="BÁSICO", font=(self.font_family, 11), fill=self.text_muted, tags=(tag,))
            canvas.create_text(cxx, y + 168, text=desc, font=(self.font_family, 10), fill="#94A3B8",
                               width=w - 34, justify="center", tags=(tag,))
            # Pastilla "Comenzar"
            self._rect_redondeado(canvas, x + 34, y + h - 56, x + w - 34, y + h - 20, 18, fill=color, outline="", tags=(tag,))
            canvas.create_text(cxx, y + h - 38, text="Comenzar  →", font=(self.font_family, 11, "bold"), fill="white", tags=(tag,))
            canvas.tag_bind(tag, "<Button-1>", lambda e, n=nivel, nm=nombre: self.seleccionar_grado(n, nm + " BÁSICO"))
            canvas.tag_bind(tag, "<Enter>", lambda e: canvas.config(cursor="hand2"))
            canvas.tag_bind(tag, "<Leave>", lambda e: canvas.config(cursor=""))

        def dibujar(evento=None):
            w = canvas.winfo_width(); h = canvas.winfo_height()
            if w < 20 or h < 20:
                return
            canvas.delete("all")
            self._gradiente_vertical(canvas, w, h, "#4F46E5", "#7C3AED")
            self._flechas_nav(canvas, 24, 42)   # ← → navegación (arriba a la izquierda)
            # Logo institucional (arriba a la derecha, sin fondo: el PNG ya trae borde blanco y sombra suave)
            if self._logo_img is not None:
                canvas.create_image(w - 14, 8, image=self._logo_img, anchor="ne")
            cx = w // 2
            oy = max(0, (h - 660) // 2)   # centra verticalmente el bloque
            cw, ch, gap = 216, 252, 34
            total = len(cards) * cw + (len(cards) - 1) * gap
            # Título animado, subtítulo, astronauta y destellos (solo presentación: ver inicio_animado.py)
            encabezado.dibujar(w, h, oy, cx - total // 2)
            canvas.create_text(cx, 150 + oy, text="Elige tu grado para comenzar",
                               font=(self.font_family, 14, "bold"), fill="white")
            x = cx - total // 2; y = 186 + oy
            for (nombre, icono, color, nivel, desc) in cards:
                tarjeta(x, y, cw, ch, nombre, icono, color, nivel, desc)
                x += cw + gap

            # Curso de Mecanografía (fuera de los 3 grados)
            mw, mh = total, 72
            mx = cx - mw // 2; my = y + ch + 22
            self._rect_redondeado(canvas, mx + 4, my + 6, mx + mw + 4, my + mh + 6, 20,
                                   fill=self._interp_color(self.primary_dark, "#000000", 0.3), outline="")
            self._rect_redondeado(canvas, mx, my, mx + mw, my + mh, 20, fill="#F59E0B", outline="", tags=("meca",))
            canvas.create_text(mx + 34, my + mh // 2, text="⌨️", font=(self.font_family, 28), anchor="w", tags=("meca",))
            canvas.create_text(mx + 84, my + 26, text="Curso de Mecanografía", font=(self.font_family, 15, "bold"),
                               fill="white", anchor="w", tags=("meca",))
            canvas.create_text(mx + 84, my + 48, text="Aprende a escribir rápido y sin ver el teclado",
                               font=(self.font_family, 10), fill="#FEF3C7", anchor="w", tags=("meca",))
            canvas.create_text(mx + mw - 28, my + mh // 2, text="→", font=(self.font_family, 20, "bold"),
                               fill="white", tags=("meca",))
            canvas.tag_bind("meca", "<Button-1>", lambda e: self.abrir_mecanografia())
            canvas.tag_bind("meca", "<Enter>", lambda e: canvas.config(cursor="hand2"))
            canvas.tag_bind("meca", "<Leave>", lambda e: canvas.config(cursor=""))
            # Botón docente (pastilla)
            bw, bh = 190, 42; bx = w - bw - 32; by = h - bh - 26
            self._rect_redondeado(canvas, bx, by, bx + bw, by + bh, 21, fill="#312E81", outline="", tags=("doc",))
            canvas.create_text(bx + bw // 2, by + bh // 2, text="🔒  Panel del Docente",
                               font=(self.font_family, 10, "bold"), fill="white", tags=("doc",))
            canvas.tag_bind("doc", "<Button-1>", lambda e: self.abrir_panel_docente())
            canvas.tag_bind("doc", "<Enter>", lambda e: canvas.config(cursor="hand2"))
            canvas.tag_bind("doc", "<Leave>", lambda e: canvas.config(cursor=""))
            canvas.create_text(30, h - 22, text="Proyecto de Seminario · 100% sin internet",
                               font=(self.font_family, 9), fill="#C7D2FE", anchor="w")

        canvas.bind("<Configure>", dibujar)
        canvas.after(60, dibujar)
        canvas.after(80, encabezado.iniciar)

    # =================================================================================
    #  CURSO DE MECANOGRAFÍA (estilo MecaNet)
    # =================================================================================
    def abrir_mecanografia(self):
        self.limpiar_ventana()
        if not self._meca_perfil:
            nombre = simpledialog.askstring("Curso de Mecanografía",
                                            "¿Cuál es tu nombre? (para guardar tu progreso)", parent=self.root)
            self._meca_perfil = (nombre or "Invitado").strip() or "Invitado"
        perfil = self._meca_perfil
        progreso = obtener_progreso_meca(perfil)

        top = tk.Canvas(self.root, height=76, highlightthickness=0, bg="#F59E0B")
        top.pack(fill="x", side="top")

        def dib_top(e=None):
            w = top.winfo_width()
            if w < 20:
                return
            top.delete("all")
            self._gradiente_horizontal(top, w, 76, "#F59E0B", "#EA580C")
            top.create_text(24, 30, text="⌨️  Curso de Mecanografía", anchor="w",
                            font=(self.font_family, 15, "bold"), fill="white")
            top.create_text(26, 52, text="Practicante: {}".format(perfil), anchor="w",
                            font=(self.font_family, 10), fill="#FFEDD5")
            x = w - 20
            x = self._pill(top, x, 38, "🏠 Inicio", "#9A3412", self.crear_pantalla_bienvenida, "meca_inicio") - 10
            self._pill(top, x, 38, "✏️ Cambiar nombre", "#B45309", self._cambiar_perfil_meca, "meca_cambiar")
        top.bind("<Configure>", dib_top)
        top.after(30, dib_top)

        cont = tk.Frame(self.root, bg=self.bg_color)
        cont.pack(expand=True, fill="both", padx=25, pady=15)
        tk.Label(cont, text="🎓 Lecciones de mecanografía", font=(self.font_family, 16, "bold"),
                 bg=self.bg_color, fg="#B45309").pack(anchor="w")
        completadas = sum(1 for i in range(len(LECCIONES_MECANOGRAFIA)) if progreso.get(i, (0, 0, 0))[2])
        tk.Label(cont, text="Completadas: {} / {}   ·   Aprende a escribir sin ver el teclado".format(
                    completadas, len(LECCIONES_MECANOGRAFIA)),
                 font=(self.font_family, 10), bg=self.bg_color, fg="#6B7280").pack(anchor="w", pady=(2, 10))

        cg = tk.Frame(cont, bg=self.bg_color)
        cg.pack(fill="both", expand=True)
        cv = tk.Canvas(cg, bg=self.bg_color, highlightthickness=0)
        sb = ttk.Scrollbar(cg, orient="vertical", command=cv.yview)
        gf = tk.Frame(cv, bg=self.bg_color)
        gf.bind("<Configure>", lambda e: cv.configure(scrollregion=cv.bbox("all")))
        vid = cv.create_window((0, 0), window=gf, anchor="nw")
        cv.bind("<Configure>", lambda e: cv.itemconfigure(vid, width=e.width))
        cv.configure(yscrollcommand=sb.set)
        cv.pack(side="left", fill="both", expand=True)
        sb.pack(side="right", fill="y")

        def _rueda_meca(evento):
            try:
                if not cv.winfo_exists():
                    self.root.unbind_all("<MouseWheel>")
                    return
                cv.yview_scroll(int(-1 * (evento.delta / 120)), "units")
            except tk.TclError:
                pass
        self.root.bind_all("<MouseWheel>", _rueda_meca)

        columnas = 3
        # --- Antes de los ejercicios: posición correcta de los dedos ---
        guia = tk.Frame(gf, bg="white", bd=0, highlightthickness=2, highlightbackground="#F59E0B")
        guia.grid(row=0, column=0, columnspan=columnas, padx=10, pady=(4, 12), sticky="nsew")
        tk.Label(guia, text="👐 Antes de empezar: ¡así se colocan los dedos!", font=(self.font_family, 13, "bold"),
                 bg="white", fg="#B45309").pack(pady=(10, 0))
        cv_guia = tk.Canvas(guia, height=350, bg="white", highlightthickness=0)
        cv_guia.pack(fill="x", padx=10)
        cv_guia.bind("<Configure>", lambda e: self._dibujar_guia_manos(cv_guia))
        cv_guia.after(40, lambda: self._dibujar_guia_manos(cv_guia))
        tk.Label(guia, text=("•  Apoya tus dedos en la fila guía: mano izquierda  A S D F  ·  mano derecha  J K L Ñ.\n"
                             "•  Los índices descansan en F y J (tienen una rayita en relieve para encontrarlas sin mirar). "
                             "Los pulgares van sobre la barra espaciadora.\n"
                             "•  Cada dedo tiene su color y sus teclas (están escritas en la palma): escribe cada tecla con el dedo "
                             "que le corresponde y regresa siempre a la fila guía."),
                 font=(self.font_family, 10), bg="white", fg="#374151", justify="left", wraplength=860
                 ).pack(padx=16, pady=(4, 12), anchor="w")

        for i, lec in enumerate(LECCIONES_MECANOGRAFIA):
            ppm, prec, comp = progreso.get(i, (0, 0, 0))
            desbloq = (i == 0) or progreso.get(i - 1, (0, 0, 0))[2]
            fila, col = i // columnas + 1, i % columnas
            borde = "#10B981" if comp else ("#F59E0B" if desbloq else "#9CA3AF")
            card = tk.Frame(gf, bg="white", bd=0, highlightthickness=2, highlightbackground=borde, highlightcolor=borde)
            card.grid(row=fila, column=col, padx=10, pady=10, sticky="nsew")
            estado_ico = "✅" if comp else ("⌨️" if desbloq else "🔒")
            tk.Label(card, text="{}  Lección {}".format(estado_ico, i + 1), font=(self.font_family, 11, "bold"),
                     bg="white", fg="#B45309").pack(pady=(12, 2))
            tk.Label(card, text=lec["titulo"], font=(self.font_family, 10, "bold"), bg="white", fg="#1F2937",
                     wraplength=180, justify="center").pack(padx=8)
            if desbloq:
                tk.Label(card, text=("🏆 {} PPM · {}%".format(ppm, prec) if ppm else "Sin intentos aún"),
                         font=(self.font_family, 8), bg="white", fg="#059669" if comp else "#6B7280").pack(pady=(4, 4))
                tk.Button(card, text="Repasar" if comp else "Practicar", font=(self.font_family, 9, "bold"),
                          bg="#9CA3AF" if comp else "#F59E0B", fg="white", bd=0, padx=12, pady=5, cursor="hand2",
                          command=lambda idx=i: self.mecanografia_leccion(idx)).pack(pady=(0, 10))
            else:
                tk.Label(card, text="Completa la lección {}".format(i), font=(self.font_family, 8),
                         bg="white", fg="#9CA3AF").pack(pady=(4, 10))
        for c in range(columnas):
            gf.columnconfigure(c, weight=1)

    def _cambiar_perfil_meca(self):
        nombre = simpledialog.askstring("Cambiar nombre", "Escribe tu nombre:", parent=self.root)
        if nombre and nombre.strip():
            self._meca_perfil = nombre.strip()
            self.abrir_mecanografia()

    def mecanografia_leccion(self, idx):
        lec = LECCIONES_MECANOGRAFIA[idx]
        texto = lec["texto"]
        win = tk.Toplevel(self.root)
        win.title("Mecanografía · " + lec["titulo"])
        win.geometry("920x640")
        win.configure(bg=self.bg_color)
        win.grab_set()

        estado = {"pos": 0, "correctos": 0, "errores": 0, "inicio": None, "terminado": False}

        cab = tk.Canvas(win, height=64, highlightthickness=0, bg="#F59E0B")
        cab.pack(fill="x", side="top")

        def dib_cab(e=None):
            w = cab.winfo_width()
            if w < 20:
                return
            cab.delete("all")
            self._gradiente_horizontal(cab, w, 64, "#F59E0B", "#EA580C")
            cab.create_text(20, 32, text="⌨️  Lección {} · {}".format(idx + 1, lec["titulo"]),
                            anchor="w", font=(self.font_family, 13, "bold"), fill="white")
            self._pill(cab, w - 18, 32, "← Volver", "#9A3412", win.destroy, "lec_volver")
        cab.bind("<Configure>", dib_cab)
        cab.after(30, dib_cab)

        tk.Label(win, text=lec["desc"], font=(self.font_family, 10), bg=self.bg_color, fg="#6B7280").pack(pady=(8, 2))

        barra = tk.Frame(win, bg=self.bg_color)
        barra.pack(fill="x", padx=34)
        lbl_ppm = tk.Label(barra, text="⚡ 0 PPM", font=(self.font_family, 13, "bold"), bg=self.bg_color, fg="#4F46E5")
        lbl_ppm.pack(side="left")
        lbl_prec = tk.Label(barra, text="🎯 100%", font=(self.font_family, 13, "bold"), bg=self.bg_color, fg="#059669")
        lbl_prec.pack(side="right")

        txt = tk.Text(win, height=3, font=("Consolas", 17), wrap="word", bd=0, padx=16, pady=12,
                      bg="white", relief="flat", cursor="arrow")
        txt.pack(fill="x", padx=34, pady=10)
        txt.insert("1.0", texto)
        txt.tag_configure("ok", foreground="#059669")
        txt.tag_configure("mal", foreground="white", background="#EF4444")
        txt.tag_configure("actual", background="#FDE68A")
        txt.config(state="disabled")

        def pintar():
            txt.config(state="normal")
            for t in ("ok", "mal", "actual"):
                txt.tag_remove(t, "1.0", "end")
            if estado["pos"] > 0:
                txt.tag_add("ok", "1.0", "1.0+{}c".format(estado["pos"]))
            if estado["pos"] < len(texto):
                txt.tag_add("actual", "1.0+{}c".format(estado["pos"]), "1.0+{}c".format(estado["pos"] + 1))
            txt.config(state="disabled")

        kb = tk.Canvas(win, height=252, bg=self.bg_color, highlightthickness=0)
        kb.pack(fill="x", padx=20, pady=6)

        def dib_kb(e=None):
            self._dibujar_teclado(kb, texto[estado["pos"]] if estado["pos"] < len(texto) else "")
        kb.bind("<Configure>", dib_kb)
        kb.after(40, dib_kb)

        def actualizar_stats():
            tot = estado["correctos"] + estado["errores"]
            prec = round(estado["correctos"] / tot * 100) if tot else 100
            if estado["inicio"]:
                mins = max(0.001, (time.time() - estado["inicio"]) / 60.0)
                ppm = round((estado["correctos"] / 5) / mins)
            else:
                ppm = 0
            lbl_ppm.config(text="⚡ {} PPM".format(ppm))
            lbl_prec.config(text="🎯 {}%".format(prec))
            return ppm, prec

        modificadoras = ("Shift_L", "Shift_R", "Control_L", "Control_R", "Alt_L", "Alt_R",
                         "Caps_Lock", "Win_L", "Win_R", "Super_L", "Super_R")

        def terminar():
            estado["terminado"] = True
            ppm, prec = actualizar_stats()
            completada = prec >= 70
            guardar_progreso_meca(self._meca_perfil, idx, ppm, prec, completada)
            self._resultado_mecanografia(win, idx, ppm, prec, completada)

        def on_key(event):
            if estado["terminado"] or estado["pos"] >= len(texto):
                return
            if event.keysym in modificadoras:
                return
            ch = event.char
            if not ch:
                return
            esperado = texto[estado["pos"]]
            if estado["inicio"] is None:
                estado["inicio"] = time.time()
            if ch == esperado:
                estado["correctos"] += 1
                estado["pos"] += 1
                pintar()
                dib_kb()
                actualizar_stats()
                if estado["pos"] >= len(texto):
                    win.after(120, terminar)
            else:
                estado["errores"] += 1
                txt.config(state="normal")
                txt.tag_add("mal", "1.0+{}c".format(estado["pos"]), "1.0+{}c".format(estado["pos"] + 1))
                txt.config(state="disabled")
                win.after(160, pintar)
                actualizar_stats()

        win.bind("<Key>", on_key)
        win.focus_force()

        def tic():
            if estado["terminado"]:
                return
            if estado["inicio"]:
                actualizar_stats()
            try:
                win.after(500, tic)
            except tk.TclError:
                pass
        win.after(500, tic)
        pintar()

    def _resultado_mecanografia(self, win_leccion, idx, ppm, prec, completada):
        res = tk.Toplevel(win_leccion)
        res.title("Resultado")
        res.geometry("470x380")
        res.configure(bg=self.bg_color)
        res.grab_set()
        color = "#059669" if completada else "#B45309"
        tk.Label(res, text="🎉 ¡Lección completada!" if completada else "💪 ¡Sigue practicando!",
                 font=(self.font_family, 17, "bold"), bg=self.bg_color, fg=color).pack(pady=(24, 8))
        fila = tk.Frame(res, bg=self.bg_color)
        fila.pack(pady=8)
        for etiqueta, valor, col in [("Velocidad", "{} PPM".format(ppm), "#4F46E5"),
                                     ("Precisión", "{}%".format(prec), "#059669")]:
            caja = tk.Frame(fila, bg="white", highlightthickness=2, highlightbackground=col, highlightcolor=col)
            caja.pack(side="left", padx=10)
            tk.Label(caja, text=valor, font=(self.font_family, 22, "bold"), bg="white", fg=col).pack(padx=26, pady=(14, 0))
            tk.Label(caja, text=etiqueta, font=(self.font_family, 9), bg="white", fg="#6B7280").pack(padx=26, pady=(0, 14))
        if not completada:
            tk.Label(res, text="Necesitas 70% de precisión para desbloquear la siguiente lección.",
                     font=(self.font_family, 9), bg=self.bg_color, fg="#B45309", wraplength=400).pack(pady=6)
        botones = tk.Frame(res, bg=self.bg_color)
        botones.pack(pady=18)

        def repetir():
            res.destroy(); win_leccion.destroy(); self.mecanografia_leccion(idx)

        def siguiente():
            res.destroy(); win_leccion.destroy(); self.mecanografia_leccion(idx + 1)

        def volver():
            res.destroy(); win_leccion.destroy(); self.abrir_mecanografia()

        tk.Button(botones, text="🔁 Repetir", font=(self.font_family, 10, "bold"), bg="#6B7280", fg="white",
                  bd=0, padx=12, pady=8, cursor="hand2", command=repetir).pack(side="left", padx=5)
        if completada and idx + 1 < len(LECCIONES_MECANOGRAFIA):
            tk.Button(botones, text="➡️ Siguiente", font=(self.font_family, 10, "bold"), bg="#F59E0B", fg="white",
                      bd=0, padx=12, pady=8, cursor="hand2", command=siguiente).pack(side="left", padx=5)
        tk.Button(botones, text="📚 Volver al curso", font=(self.font_family, 10, "bold"), bg=self.primary_color,
                  fg="white", bd=0, padx=12, pady=8, cursor="hand2", command=volver).pack(side="left", padx=5)

    def _dibujar_teclado(self, canvas, char_esperado):
        try:
            canvas.delete("all")
        except tk.TclError:
            return
        w = canvas.winfo_width() or 860
        esperado = (char_esperado or "").upper()
        tw, th, gap = 54, 44, 6
        max_teclas = max(len(f) for f in FILAS_TECLADO)
        total_w = max_teclas * (tw + gap)
        x0 = max(10, (w - total_w) // 2)
        offsets = [0, 12, 22, 34]
        y = 8
        for r, fila in enumerate(FILAS_TECLADO):
            x = x0 + offsets[r]
            for tecla in fila:
                color = DEDO_COLOR.get(tecla, "#CBD5E1")
                if esperado == tecla:
                    self._rect_redondeado(canvas, x, y, x + tw, y + th, 8, fill=color, outline="#1F2937")
                    canvas.create_text(x + tw // 2, y + th // 2, text=tecla, font=(self.font_family, 13, "bold"), fill="white")
                else:
                    self._rect_redondeado(canvas, x, y, x + tw, y + th, 8, fill=self._interp_color(color, "#FFFFFF", 0.55), outline="")
                    canvas.create_text(x + tw // 2, y + th // 2, text=tecla, font=(self.font_family, 12, "bold"), fill="#374151")
                x += tw + gap
            y += th + gap
        bx0, bx1 = x0 + 70, x0 + total_w - 70
        if esperado == " ":
            self._rect_redondeado(canvas, bx0, y, bx1, y + th, 8, fill="#94A3B8", outline="#1F2937")
            canvas.create_text((bx0 + bx1) // 2, y + th // 2, text="Espacio", font=(self.font_family, 10, "bold"), fill="white")
        else:
            self._rect_redondeado(canvas, bx0, y, bx1, y + th, 8, fill="#E2E8F0", outline="")
            canvas.create_text((bx0 + bx1) // 2, y + th // 2, text="Espacio", font=(self.font_family, 10, "bold"), fill="#475569")

    def _dibujar_guia_manos(self, canvas):
        """Imagen de la posición correcta de las manos sobre el teclado (fila guía ASDF JKLÑ).
        Las manos entran desde ABAJO, con los dedos hacia arriba y las puntas sobre la fila guía."""
        import math
        try:
            canvas.delete("all")
        except tk.TclError:
            return
        w = canvas.winfo_width()
        if w < 300:
            return
        tw, th, gap = 46, 34, 5
        paso_x, paso_y = tw + gap, th + gap
        offsets = [0, 12, 22, 34]
        y_kb = 12
        x0 = max(10, (w - (10 * paso_x + offsets[3])) // 2)

        def centro(fila, col):
            return x0 + offsets[fila] + col * paso_x + tw // 2

        # --- Teclado: la fila guía resaltada, el resto en tono suave ---
        for r, fila in enumerate(FILAS_TECLADO):
            for c, tecla in enumerate(fila):
                kx = x0 + offsets[r] + c * paso_x
                ky = y_kb + r * paso_y
                color = DEDO_COLOR.get(tecla, "#CBD5E1")
                if r == 2 and tecla in "ASDFJKLÑ":
                    self._rect_redondeado(canvas, kx, ky, kx + tw, ky + th, 8, fill=color, outline="#1F2937", width=2)
                    canvas.create_text(kx + tw // 2, ky + th // 2 - 2, text=tecla,
                                       font=(self.font_family, 12, "bold"), fill="white")
                    if tecla in "FJ":   # rayita en relieve que guía a los índices sin mirar
                        canvas.create_line(kx + tw // 2 - 8, ky + th - 7, kx + tw // 2 + 8, ky + th - 7,
                                           width=2, fill="#1F2937")
                else:
                    self._rect_redondeado(canvas, kx, ky, kx + tw, ky + th, 8,
                                          fill=self._interp_color(color, "#FFFFFF", 0.62), outline="")
                    canvas.create_text(kx + tw // 2, ky + th // 2, text=tecla,
                                       font=(self.font_family, 10, "bold"), fill="#64748B")
        y_esp = y_kb + 4 * paso_y
        bx0, bx1 = x0 + 70, x0 + 10 * paso_x + offsets[3] - 70
        self._rect_redondeado(canvas, bx0, y_esp, bx1, y_esp + th, 8, fill="#CBD5E1", outline="#64748B", width=2)
        cx_teclado = (bx0 + bx1) // 2
        canvas.create_text(cx_teclado, y_esp + th // 2, text="Espacio",
                           font=(self.font_family, 8, "bold"), fill="#475569")
        y_guia = y_kb + 2 * paso_y
        canvas.create_text(x0 + offsets[2] + 10 * paso_x + 4, y_guia + th // 2, text="◀ Fila guía", anchor="w",
                           font=(self.font_family, 9, "bold"), fill="#B45309")

        # --- Manos: entran desde ABAJO, dedos hacia arriba y la punta (uña) sobre la fila guía ---
        piel, piel_borde, pliegue = "#F3C9A5", "#B9784A", "#DDA878"

        def miembro(p0, p1, w0, w1):
            """Dedo o pulgar: forma alargada que se afina hacia la punta, con extremos redondeados."""
            r0, r1 = w0 / 2.0, w1 / 2.0
            ang = math.atan2(p1[1] - p0[1], p1[0] - p0[0])
            pts = []
            for k in range(13):
                a = ang - math.pi / 2 + math.pi * k / 12.0
                pts += [p1[0] + r1 * math.cos(a), p1[1] + r1 * math.sin(a)]
            for k in range(13):
                a = ang + math.pi / 2 + math.pi * k / 12.0
                pts += [p0[0] + r0 * math.cos(a), p0[1] + r0 * math.sin(a)]
            canvas.create_polygon(*pts, fill=piel, outline=piel_borde, width=2)

        # teclas que le corresponden a cada dedo (se obtienen de los colores del teclado)
        def teclas_del_dedo(tecla_guia):
            color = DEDO_COLOR[tecla_guia]
            return [t for fila_t in FILAS_TECLADO for t in fila_t if DEDO_COLOR.get(t) == color]

        manos = [
            ("Mano izquierda", [("Meñique", "A"), ("Anular", "S"), ("Medio", "D"), ("Índice", "F")], 0),
            ("Mano derecha", [("Índice", "J"), ("Medio", "K"), ("Anular", "L"), ("Meñique", "Ñ")], 6),
        ]
        ancho_dedo = {"Meñique": 31, "Anular": 36, "Medio": 38, "Índice": 38}
        nudillo = {"Meñique": 200, "Anular": 214, "Medio": 222, "Índice": 212}   # el medio es el más largo
        y_punta = y_guia + 10                      # la punta de cada dedo cae sobre su tecla guía
        y_fondo = 345
        for titulo, dedos, col0 in manos:
            xs = [centro(2, col0 + i) for i in range(4)]
            yk = [nudillo[n] for (n, _t) in dedos]
            izquierda = (col0 == 0)
            lado = 1 if izquierda else -1          # hacia dónde apunta el pulgar (el centro del teclado)
            # Pulgar (primero, para que la palma tape su base)
            xb = (xs[3] + 4) if izquierda else (xs[0] - 4)
            b, j, pt = (xb, 262), (xb + lado * 36, 236), (cx_teclado - lado * 44, y_esp + th // 2 + 6)
            miembro(b, j, 40, 36)
            miembro(j, pt, 36, 31)
            # Dedos
            for (nombre, tecla), x, ykk in zip(dedos, xs, yk):
                wd = ancho_dedo[nombre]
                miembro((x, ykk + 16), (x, y_punta + (wd * 0.88) / 2.0), wd, wd * 0.88)
            # Palma + antebrazo (tapa la base de los dedos; sin borde arriba para que se fundan con los dedos)
            xl, xr = xs[0] - 24, xs[3] + 24
            bl = 36 if not izquierda else 26
            br = 36 if izquierda else 26
            palma = [xl, yk[0] + 8]
            for x, ykk in zip(xs, yk):
                palma += [x, ykk - 2]
            palma += [xr, yk[3] + 8, xr + (br - 24), 250, xr - 6, 290, xr - 12, y_fondo,
                      xl + 12, y_fondo, xl + 6, 290, xl - (bl - 24), 252]
            canvas.create_polygon(*palma, fill=piel, outline="", smooth=True)
            canvas.create_line(xr, yk[3] + 8, xr + (br - 24), 250, xr - 6, 290, xr - 12, y_fondo,
                               fill=piel_borde, width=2, smooth=True)
            canvas.create_line(xl, yk[0] + 8, xl - (bl - 24), 252, xl + 6, 290, xl + 12, y_fondo,
                               fill=piel_borde, width=2, smooth=True)
            # Pliegues de las articulaciones y uña con la letra guía
            for (nombre, tecla), x, ykk in zip(dedos, xs, yk):
                wd = ancho_dedo[nombre]
                largo = ykk - y_punta
                for fr in (0.38, 0.68):
                    yy = ykk - largo * fr
                    canvas.create_line(x - wd * 0.28, yy, x, yy + 2, x + wd * 0.28, yy, fill=pliegue, width=1, smooth=True)
                color = DEDO_COLOR[tecla]
                self._rect_redondeado(canvas, x - 11, y_punta + 5, x + 11, y_punta + 24, 7, fill=color,
                                      outline=self._interp_color(color, "#000000", 0.35), width=1)
                canvas.create_text(x, y_punta + 15, text=tecla, font=(self.font_family, 10, "bold"), fill="#111827")
            # Etiqueta sobre la palma: nombre del dedo y las teclas que le tocan
            for (nombre, tecla), x in zip(dedos, xs):
                color = DEDO_COLOR[tecla]
                teclas = teclas_del_dedo(tecla)
                lineas = [" ".join(teclas[:4])] + ([" ".join(teclas[4:])] if len(teclas) > 4 else [])
                y0c = 238
                alto = 24 + 13 * len(lineas)
                self._rect_redondeado(canvas, x - 24, y0c, x + 24, y0c + alto, 8,
                                      fill=self._interp_color(color, "#FFFFFF", 0.35),
                                      outline=self._interp_color(color, "#000000", 0.35), width=1)
                canvas.create_text(x, y0c + 10, text=nombre, font=(self.font_family, 8, "bold"), fill="#3B2412")
                for i, linea in enumerate(lineas):
                    canvas.create_text(x, y0c + 24 + i * 13, text=linea, font=(self.font_family, 8, "bold"), fill="#111827")
            canvas.create_text((xs[0] + xs[3]) // 2, y_fondo - 18, text=titulo,
                               font=(self.font_family, 10, "bold"), fill="#5B3A1E")
        for i, linea in enumerate(("Pulgares", "sobre la barra", "espaciadora")):
            canvas.create_text(cx_teclado, 232 + i * 13, text=linea, font=(self.font_family, 8, "bold"), fill="#64748B")

    def seleccionar_grado(self, nivel, nombre_grado):
        self.grado_actual = (nivel, nombre_grado)
        
        conexion = sqlite3.connect("encarta_educativa.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, puntos FROM estudiantes WHERE grado = ?", (nivel,))
        estudiantes = cursor.fetchall()
        conexion.close()
        
        if not estudiantes:
            msg = "No hay estudiantes registrados en " + nombre_grado + ". Ingresa tu Nombre y Apellido:"
            nombre = self._pedir_nombre_valido("Nuevo Estudiante", msg, self.root)
            if nombre:
                conexion = sqlite3.connect("encarta_educativa.db")
                cursor = conexion.cursor()
                cursor.execute("INSERT INTO estudiantes (nombre, grado, puntos) VALUES (?, ?, ?)", (nombre, nivel, 0))
                conexion.commit()
                estudiante_id = cursor.lastrowid
                conexion.close()
                seguridad.registrar_evento("ESTUDIANTE_REGISTRADO", "id={} grado={}".format(estudiante_id, nivel))
                self.estudiante_actual = (estudiante_id, nombre, nivel, 0)
                self.mostrar_menu_principal()
            else:
                return
        else:
            self.ventana_seleccion_estudiante(estudiantes, nivel, nombre_grado)

    def ventana_seleccion_estudiante(self, estudiantes, nivel, nombre_grado):
        top = tk.Toplevel(self.root)
        top.title("Modo Turnos - " + nombre_grado)
        top.geometry("400x450")
        top.configure(bg=self.bg_color)
        top.grab_set()
        
        tk.Label(top, text="Selecciona tu Perfil de Estudiante", font=("Segoe UI", 13, "bold"), bg=self.bg_color, fg=self.primary_color).pack(pady=15)
        
        frame_lista = tk.Frame(top, bg=self.bg_color)
        frame_lista.pack(fill="both", expand=True, padx=20, pady=10)
        
        for est in estudiantes:
            est_id, nombre, puntos = est
            texto_btn = "👤 " + nombre + "  (" + str(puntos) + " pts)"
            btn_est = tk.Button(
                frame_lista, text=texto_btn, font=("Segoe UI", 11),
                bg="white", fg="#1F2937", anchor="w", padx=15, pady=8, bd=1, relief="solid",
                command=lambda id_e=est_id, nom=nombre, p=puntos: [self.asignar_estudiante(id_e, nom, nivel, p), top.destroy()]
            )
            btn_est.pack(fill="x", pady=5)
            
        def nuevo_estudiante():
            nombre = self._pedir_nombre_valido("Nuevo Estudiante", "Ingresa tu Nombre y Apellido:", top)
            if nombre:
                conexion = sqlite3.connect("encarta_educativa.db")
                cursor = conexion.cursor()
                cursor.execute("INSERT INTO estudiantes (nombre, grado, puntos) VALUES (?, ?, ?)", (nombre, nivel, 0))
                conexion.commit()
                est_id = cursor.lastrowid
                conexion.close()
                seguridad.registrar_evento("ESTUDIANTE_REGISTRADO", "id={} grado={}".format(est_id, nivel))
                self.asignar_estudiante(est_id, nombre, nivel, 0)
                top.destroy()
                
        tk.Button(top, text="+ Registrar Nuevo Estudiante", font=("Segoe UI", 10, "bold"), bg=self.secondary_color, fg="white", bd=0, padx=10, pady=8, command=nuevo_estudiante).pack(pady=15)

    def _pedir_nombre_valido(self, titulo, mensaje, parent):
        """Pide el nombre hasta que sea válido; devuelve None si se cancela."""
        while True:
            crudo = simpledialog.askstring(titulo, mensaje, parent=parent)
            if crudo is None:
                return None
            ok, resultado = seguridad.validar_nombre(crudo)
            if ok:
                return resultado
            messagebox.showwarning("Nombre no válido", resultado, parent=parent)

    def asignar_estudiante(self, est_id, nombre, grado, puntos):
        self.estudiante_actual = (est_id, nombre, grado, puntos)
        self.mostrar_menu_principal()

    def mostrar_menu_principal(self):
        # Primero, Segundo y Tercero Básico usan el sistema de módulos con puntos y desbloqueo.
        if self.grado_actual[0] in (1, 2, 3):
            self.mostrar_menu_primero_basico()
            return
        self.limpiar_ventana()
        
        top_bar = tk.Frame(self.root, bg=self.primary_color, height=65)
        top_bar.pack(fill="x", side="top")
        
        info_texto = "Grado: " + self.grado_actual[1] + "  |  Estudiante: " + self.estudiante_actual[1] + "  ⭐ " + str(self.estudiante_actual[3]) + " pts"
        lbl_info = tk.Label(
            top_bar, text=info_texto, 
            font=("Segoe UI", 12, "bold"), bg=self.primary_color, fg="white"
        )
        lbl_info.pack(side="left", padx=20, pady=18)
        
        btn_cambiar = tk.Button(
            top_bar, text="Cambiar de Estudiante / Grado", font=("Segoe UI", 9, "bold"),
            bg="#EF4444", fg="white", bd=0, padx=10, pady=6,
            cursor="hand2", command=self.crear_pantalla_bienvenida
        )
        btn_cambiar.pack(side="right", padx=20, pady=15)
        
        content_frame = tk.Frame(self.root, bg=self.bg_color)
        content_frame.pack(expand=True, fill="both", padx=30, pady=25)
        
        opciones = [
            ("📚 Aprender", "Enciclopedia educativa interactiva"),
            ("🧠 Pensamiento lógico", "Secuencias, patrones y acertijos"),
            ("💻 Conociendo la PC", "Partes, teclado y sistema operativo"),
            ("🧩 Resolución de problemas", "Casos cotidianos y análisis"),
            ("🔢 Razon. Computacional", "Algoritmos, condiciones y bucles"),
            ("🎮 Juegos y retos", "Minijuegos interactivos y puntos"),
            ("📝 Evaluaciones", "Cuestionarios de comprensión"),
            ("🏆 Mi Progreso", "Insignias y estadísticas")
        ]
        
        for i, (titulo_op, desc) in enumerate(opciones):
            fila = i // 4
            col = i % 4
            
            card = tk.Frame(content_frame, bg="white", bd=1, relief="solid", highlightbackground="#D1D5DB")
            card.grid(row=fila, column=col, padx=12, pady=12, sticky="nsew")
            
            lbl_btn_titulo = tk.Label(card, text=titulo_op, font=("Segoe UI", 11, "bold"), bg="white", fg=self.primary_color)
            lbl_btn_titulo.pack(pady=(15, 5))
            
            lbl_btn_desc = tk.Label(card, text=desc, font=("Segoe UI", 9), bg="white", fg="#6B7280", wraplength=180)
            lbl_btn_desc.pack(pady=(0, 15), padx=10)
            
            card.bind("<Button-1>", lambda e, t=titulo_op: self.abrir_seccion(t))
            lbl_btn_titulo.bind("<Button-1>", lambda e, t=titulo_op: self.abrir_seccion(t))
            lbl_btn_desc.bind("<Button-1>", lambda e, t=titulo_op: self.abrir_seccion(t))
            
        for i in range(4):
            content_frame.columnconfigure(i, weight=1)
        for i in range(2):
            content_frame.rowconfigure(i, weight=1)

    # =================================================================================
    #  PRIMERO BÁSICO — Menú de módulos, progreso, perfil e insignias
    # =================================================================================

    def refrescar_estudiante_actual(self):
        est_id = self.estudiante_actual[0]
        puntos = obtener_puntos_estudiante(est_id)
        self.estudiante_actual = (est_id, self.estudiante_actual[1], self.estudiante_actual[2], puntos)

    def mostrar_menu_primero_basico(self):
        self.limpiar_ventana()
        self.refrescar_estudiante_actual()
        est_id, nombre, grado, puntos = self.estudiante_actual
        modulos, prefijo, total = datos_grado(grado)
        self._registrar_historial(("menu", self.grado_actual, self.estudiante_actual))

        xp = obtener_xp_estudiante(est_id)
        nivel = calcular_nivel(xp)
        racha, _mejor = obtener_racha(est_id)

        # Barra superior con degradado y botones tipo pastilla (incluye 🏠 Inicio para regresar)
        top = tk.Canvas(self.root, height=76, highlightthickness=0, bg=self.primary_color)
        top.pack(fill="x", side="top")
        dia_txt = "🔥 {} día".format(racha) + ("" if racha == 1 else "s")
        info2 = "Nivel {}   ·   ⭐ {} XP   ·   {}   ·   {} pts".format(nivel, xp, dia_txt, puntos)
        reto_pendiente = not reto_diario_hecho(est_id)

        def dibujar_top(e=None):
            w = top.winfo_width()
            if w < 20:
                return
            top.delete("all")
            self._gradiente_horizontal(top, w, 76, "#4F46E5", "#7C3AED")
            xr = self._flechas_nav(top, 20, 38)   # ← → navegación a la izquierda
            top.create_text(xr + 16, 28, text="👋 " + nombre, anchor="w", font=(self.font_family, 14, "bold"), fill="white")
            top.create_text(xr + 18, 51, text=info2, anchor="w", font=(self.font_family, 10), fill="#E0E7FF")
            x = w - 20
            x = self._pill(top, x, 38, "🚪 Salir", "#312E81", self.crear_pantalla_bienvenida, "p_home") - 10
            x = self._pill(top, x, 38, "👤 Mi Perfil", self.accent_color, self.ventana_perfil_primero, "p_perfil") - 10
            reto_txt = "🎯 Reto del día" + ("  ¡NUEVO!" if reto_pendiente else "  ✓")
            self._pill(top, x, 38, reto_txt, "#22C55E" if reto_pendiente else "#64748B", self.ventana_reto_diario, "p_reto")

        top.bind("<Configure>", dibujar_top)
        top.after(30, dibujar_top)

        content = tk.Frame(self.root, bg=self.bg_color)
        content.pack(expand=True, fill="both", padx=25, pady=15)

        tk.Label(content, text="📚 {} — Ruta de aprendizaje".format(self.grado_actual[1].title()),
                  font=("Segoe UI", 16, "bold"), bg=self.bg_color, fg=self.primary_color).pack(anchor="w")

        # Barra de progreso general hacia el próximo módulo
        siguiente = None
        for m_id in range(1, total + 1):
            if not modulo_esta_desbloqueado(m_id, puntos, modulos):
                siguiente = m_id
                break

        barra_frame = tk.Frame(content, bg="white", bd=1, relief="solid")
        barra_frame.pack(fill="x", pady=(10, 15))
        if siguiente:
            umbral = modulos[siguiente]["umbral"]
            umbral_anterior = modulos[siguiente - 1]["umbral"]
            rango = umbral - umbral_anterior
            avance = max(0, puntos - umbral_anterior)
            porcentaje = min(1.0, avance / rango) if rango else 1.0
            tk.Label(barra_frame, text="Puntos: {} / {}   (faltan {} para desbloquear el Módulo {})".format(
                        puntos, umbral, max(0, umbral - puntos), siguiente),
                      font=("Segoe UI", 10, "bold"), bg="white", fg="#1F2937").pack(anchor="w", padx=12, pady=(8, 2))
        else:
            porcentaje = 1.0
            tk.Label(barra_frame, text="🎉 ¡Has desbloqueado todos los módulos! Puntos: {}".format(puntos),
                      font=("Segoe UI", 10, "bold"), bg="white", fg="#1F2937").pack(anchor="w", padx=12, pady=(8, 2))

        canvas_barra = tk.Canvas(barra_frame, height=18, bg="white", highlightthickness=0)
        canvas_barra.pack(fill="x", padx=12, pady=(0, 10))
        canvas_barra.update_idletasks()
        canvas_barra.after(10, lambda: self._dibujar_barra(canvas_barra, porcentaje))

        # Cuadrícula de módulos (desplazable, para que quepan los 12)
        cont_grid = tk.Frame(content, bg=self.bg_color)
        cont_grid.pack(fill="both", expand=True)
        canvas_grid = tk.Canvas(cont_grid, bg=self.bg_color, highlightthickness=0)
        sb_grid = ttk.Scrollbar(cont_grid, orient="vertical", command=canvas_grid.yview)
        grid_frame = tk.Frame(canvas_grid, bg=self.bg_color)
        grid_frame.bind("<Configure>", lambda e: canvas_grid.configure(scrollregion=canvas_grid.bbox("all")))
        ventana_grid = canvas_grid.create_window((0, 0), window=grid_frame, anchor="nw")
        canvas_grid.bind("<Configure>", lambda e: canvas_grid.itemconfigure(ventana_grid, width=e.width))
        canvas_grid.configure(yscrollcommand=sb_grid.set)
        canvas_grid.pack(side="left", fill="both", expand=True)
        sb_grid.pack(side="right", fill="y")

        def _rueda_menu(evento):
            try:
                canvas_grid.yview_scroll(int(-1 * (evento.delta / 120)), "units")
            except tk.TclError:
                pass
        canvas_grid.bind("<Enter>", lambda e: canvas_grid.bind_all("<MouseWheel>", _rueda_menu))
        canvas_grid.bind("<Leave>", lambda e: canvas_grid.unbind_all("<MouseWheel>"))

        columnas = 4
        for i in range(1, total + 1):
            m = modulos[i]
            fila = (i - 1) // columnas
            col = (i - 1) % columnas
            desbloqueado = modulo_esta_desbloqueado(i, puntos, modulos)
            completo = desbloqueado and modulo_esta_completo(est_id, i, modulos, prefijo)

            if completo:
                borde = "#10B981"
            elif desbloqueado:
                borde = "#3B82F6"
            else:
                borde = "#9CA3AF"

            card = tk.Frame(grid_frame, bg="white", bd=0, relief="flat",
                            highlightthickness=2, highlightbackground=borde, highlightcolor=borde)
            card.grid(row=fila, column=col, padx=10, pady=10, sticky="nsew")

            estado_icono = "✅" if completo else ("🔓" if desbloqueado else "🔒")
            tk.Label(card, text="{} {}".format(estado_icono, m["icono"]), font=("Segoe UI", 20), bg="white").pack(pady=(12, 0))
            tk.Label(card, text="Módulo {}".format(i), font=("Segoe UI", 10, "bold"), bg="white", fg=self.primary_color).pack()
            tk.Label(card, text=m["titulo"], font=("Segoe UI", 9, "bold"), bg="white", fg="#1F2937",
                      wraplength=160, justify="center").pack(pady=(2, 6), padx=8)

            if desbloqueado:
                estado_txt = "¡Completado!" if completo else "Disponible"
                tk.Label(card, text=estado_txt, font=("Segoe UI", 8), bg="white", fg="#059669" if completo else "#2563EB").pack(pady=(0, 10))
                card.bind("<Button-1>", lambda e, mid=i: self.abrir_modulo_primero(mid))
                for w in card.winfo_children():
                    w.bind("<Button-1>", lambda e, mid=i: self.abrir_modulo_primero(mid))
            else:
                tk.Label(card, text="Necesitas {} pts".format(m["umbral"]), font=("Segoe UI", 8), bg="white", fg="#9CA3AF").pack(pady=(0, 10))

        for c in range(columnas):
            grid_frame.columnconfigure(c, weight=1)
        filas_totales = (total + columnas - 1) // columnas
        for r in range(filas_totales):
            grid_frame.rowconfigure(r, weight=1)

    def _dibujar_barra(self, canvas, porcentaje):
        try:
            canvas.delete("all")
            ancho = canvas.winfo_width() or 800
            alto = canvas.winfo_height() or 18
            r = max(2, alto // 2)
            self._rect_redondeado(canvas, 1, 1, ancho - 1, alto - 1, r, fill="#E2E8F0", outline="")
            if porcentaje and porcentaje > 0:
                fw = max(alto, (ancho - 2) * porcentaje)
                self._rect_redondeado(canvas, 1, 1, fw, alto - 1, r, fill="#10B981", outline="")
        except tk.TclError:
            pass

    def anunciar_desbloqueos(self, puntos_antes, puntos_despues, parent):
        modulos, _prefijo, total = datos_grado(self.grado_actual[0])
        for m_id in range(1, total + 1):
            umbral = modulos[m_id]["umbral"]
            if puntos_antes < umbral <= puntos_despues:
                messagebox.showinfo(
                    "🎉 ¡Felicidades!",
                    "Has conseguido {} puntos.\n¡El Módulo {} – {} está desbloqueado!".format(
                        umbral, m_id, modulos[m_id]["titulo"]),
                    parent=parent)

    def anunciar_insignias(self, nuevas_insignias, parent):
        for clave in nuevas_insignias:
            info = INSIGNIAS_INFO[clave]
            messagebox.showinfo("🏅 ¡Nueva insignia!",
                                  "¡Has obtenido la insignia {}!\n{}".format(info["nombre"], info["desc"]),
                                  parent=parent)

    def otorgar_puntos_actividad(self, actividad_key, puntos, parent):
        """Punto central para registrar el resultado de cualquier actividad, otorgar puntos
        una sola vez, avisar desbloqueos de módulo y revisar insignias nuevas."""
        est_id = self.estudiante_actual[0]
        puntos_antes = obtener_puntos_estudiante(est_id)
        puntos_despues, otorgado = registrar_actividad_y_sumar_puntos(est_id, actividad_key, puntos)
        self.refrescar_estudiante_actual()
        if otorgado:
            xp_despues = obtener_xp_estudiante(est_id)
            nivel_antes = calcular_nivel(max(0, xp_despues - puntos))
            nivel_despues = calcular_nivel(xp_despues)
            racha, cambio_racha = registrar_dia_actividad(est_id)

            mensaje = "✨ ¡Actividad completada!\n+{} puntos   ·   +{} XP ⭐".format(puntos, puntos)
            if cambio_racha and racha > 1:
                mensaje += "\n🔥 ¡Llevas una racha de {} días!".format(racha)
            messagebox.showinfo("¡Muy bien!", mensaje, parent=parent)
            if nivel_despues > nivel_antes:
                messagebox.showinfo("⭐ ¡Subiste de nivel!",
                                      "¡Alcanzaste el Nivel {}! Sigue aprendiendo.".format(nivel_despues), parent=parent)
            self.anunciar_desbloqueos(puntos_antes, puntos_despues, parent)
            nuevas = verificar_y_otorgar_insignias(est_id, self.grado_actual[0])
            self.anunciar_insignias(nuevas, parent)
        else:
            messagebox.showinfo("Ya completada", "Ya habías completado esta actividad antes, por eso no se repiten los puntos. "
                                                    "¡Pero puedes seguir practicando!", parent=parent)
        return otorgado

    def abrir_modulo_primero(self, modulo_id):
        grado = self.grado_actual[0]
        modulos, prefijo, _total = datos_grado(grado)
        puntos_eval = PUNTOS_EVAL_GRADO.get(grado, 15)
        m = modulos[modulo_id]
        est_id = self.estudiante_actual[0]

        top = tk.Toplevel(self.root)
        top.title("Módulo {} – {}".format(modulo_id, m["titulo"]))
        top.geometry("860x640")
        top.configure(bg=self.bg_color)
        top.grab_set()

        # Al cerrar el módulo (Volver o la X) se refresca el menú: así la barra de
        # progreso y el estado de los módulos se actualizan sin salir y volver a entrar.
        def cerrar_modulo():
            top.destroy()
            if self.grado_actual and self.grado_actual[0] in (1, 2, 3):
                self.mostrar_menu_primero_basico()
        top.protocol("WM_DELETE_WINDOW", cerrar_modulo)

        # Encabezado con degradado + botón "← Volver"
        cab = tk.Canvas(top, height=70, highlightthickness=0, bg=self.primary_color)
        cab.pack(fill="x", side="top")

        def dib_cab(e=None):
            w = cab.winfo_width()
            if w < 20:
                return
            cab.delete("all")
            self._gradiente_horizontal(cab, w, 70, "#4F46E5", "#7C3AED")
            cab.create_text(24, 35, text="{}  Módulo {} · {}".format(m["icono"], modulo_id, m["titulo"]),
                            anchor="w", font=(self.font_family, 14, "bold"), fill="white")
            self._pill(cab, w - 20, 35, "← Volver", "#312E81", cerrar_modulo, "cab_volver")
        cab.bind("<Configure>", dib_cab)
        cab.after(30, dib_cab)

        notebook = ttk.Notebook(top)
        notebook.pack(expand=True, fill="both", padx=15, pady=10)

        # --- Pestaña Contenido ---
        tab_contenido = tk.Frame(notebook, bg="white")
        notebook.add(tab_contenido, text="📖 Contenido")
        canvas = tk.Canvas(tab_contenido, bg="white", highlightthickness=0)
        scrollbar = ttk.Scrollbar(tab_contenido, orient="vertical", command=canvas.yview)
        frame_scroll = tk.Frame(canvas, bg="white")
        frame_scroll.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=frame_scroll, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        paleta = ["#4F46E5", "#0D9488", "#F59E0B", "#EC4899", "#3B82F6", "#8B5CF6", "#10B981", "#EF4444"]
        iconos = ["💡", "🔎", "📌", "🧠", "⭐", "🖥️", "📖", "🎯"]
        for i, (subtitulo, texto) in enumerate(m["contenido"]):
            color = paleta[i % len(paleta)]
            ico = iconos[i % len(iconos)]
            card = tk.Frame(frame_scroll, bg="white", highlightthickness=1, highlightbackground="#E5E7EB")
            card.pack(fill="x", padx=16, pady=8)
            tk.Frame(card, bg=color, width=6).pack(side="left", fill="y")   # franja de color
            cont = tk.Frame(card, bg="white")
            cont.pack(side="left", fill="both", expand=True, padx=12, pady=10)
            fila_tit = tk.Frame(cont, bg="white")
            fila_tit.pack(fill="x", anchor="w")
            badge = tk.Canvas(fila_tit, width=42, height=42, bg="white", highlightthickness=0)
            badge.pack(side="left")
            badge.create_oval(4, 4, 38, 38, fill=self._interp_color(color, "#FFFFFF", 0.78), outline="")
            badge.create_text(21, 21, text=ico, font=(self.font_family, 16))
            tk.Label(fila_tit, text=subtitulo, font=(self.font_family, 12, "bold"), bg="white", fg=color,
                     anchor="w", justify="left", wraplength=650).pack(side="left", padx=10, fill="x", expand=True)
            tk.Label(cont, text=texto, font=(self.font_family, 10), bg="white", fg="#374151",
                     anchor="w", justify="left", wraplength=700).pack(fill="x", pady=(6, 0))

        # --- Pestaña Actividades ---
        tab_act = tk.Frame(notebook, bg=self.bg_color)
        notebook.add(tab_act, text="🎯 Actividades")
        tk.Label(tab_act, text="Completa las actividades para ganar puntos:", font=("Segoe UI", 11, "bold"),
                  bg=self.bg_color, fg="#1F2937").pack(anchor="w", padx=15, pady=(15, 10))

        lista_act = tk.Frame(tab_act, bg=self.bg_color)
        lista_act.pack(fill="both", expand=True, padx=15)

        def refrescar_lista_actividades():
            for w in lista_act.winfo_children():
                w.destroy()
            for act in m["actividades"]:
                hecha = actividad_ya_completada(est_id, act["id"])
                fila = tk.Frame(lista_act, bg="white", bd=1, relief="solid")
                fila.pack(fill="x", pady=5)
                icono = "✅" if hecha else "▶️"
                tk.Label(fila, text="{} {}".format(icono, act["titulo"]), font=("Segoe UI", 10, "bold"),
                          bg="white", fg="#1F2937").pack(side="left", padx=12, pady=10)
                tk.Label(fila, text="+{} pts".format(act["puntos"]), font=("Segoe UI", 9), bg="white",
                          fg="#059669" if hecha else "#6B7280").pack(side="right", padx=12)
                tk.Button(fila, text="Repasar" if hecha else "Comenzar", font=("Segoe UI", 9, "bold"),
                          bg="#9CA3AF" if hecha else self.secondary_color, fg="white", bd=0, padx=10, pady=5,
                          cursor="hand2",
                          command=lambda a=act: self.lanzar_actividad(a, top, refrescar_lista_actividades)
                          ).pack(side="right", padx=8, pady=8)

        refrescar_lista_actividades()

        # --- Pestaña Evaluación ---
        tab_eval = tk.Frame(notebook, bg=self.bg_color)
        notebook.add(tab_eval, text="📝 Evaluación")
        tk.Label(tab_eval, text="Evaluación final del Módulo {}".format(modulo_id), font=("Segoe UI", 13, "bold"),
                  bg=self.bg_color, fg=self.primary_color).pack(pady=(20, 5))
        tk.Label(tab_eval, text="{} preguntas · necesitas 70% para aprobar · +{} puntos si apruebas".format(len(m["evaluacion"]), puntos_eval),
                  font=("Segoe UI", 10), bg=self.bg_color, fg="#4B5563").pack(pady=(0, 15))

        estado_eval = tk.Label(tab_eval,
                                 text="✅ Evaluación ya aprobada" if evaluacion_aprobada(est_id, modulo_id, prefijo) else "Aún no has aprobado esta evaluación.",
                                 font=("Segoe UI", 10, "bold"), bg=self.bg_color,
                                 fg="#059669" if evaluacion_aprobada(est_id, modulo_id, prefijo) else "#B45309")
        estado_eval.pack(pady=(0, 15))

        tk.Button(tab_eval, text="📝 Iniciar Evaluación", font=("Segoe UI", 11, "bold"), bg=self.primary_color,
                   fg="white", bd=0, padx=15, pady=10, cursor="hand2",
                   command=lambda: self.iniciar_evaluacion(modulo_id, top, refrescar_lista_actividades, estado_eval)
                   ).pack(pady=10)

    def lanzar_actividad(self, actividad, parent_win, on_close_callback):
        tipo = actividad["tipo"]
        if tipo == "seleccion":
            self.actividad_seleccion(actividad, parent_win, on_close_callback)
        elif tipo == "relacionar":
            self.actividad_relacionar(actividad, parent_win, on_close_callback)
        elif tipo == "ordenar":
            self.actividad_ordenar(actividad, parent_win, on_close_callback)
        elif tipo == "memoria":
            self.actividad_memoria(actividad, parent_win, on_close_callback)
        elif tipo == "clasificar":
            self.actividad_clasificar(actividad, parent_win, on_close_callback)
        elif tipo == "patron":
            self.actividad_patron(actividad, parent_win, on_close_callback)
        elif tipo == "problema":
            self.actividad_problema(actividad, parent_win, on_close_callback)
        elif tipo == "laberinto":
            self.actividad_laberinto(actividad, parent_win, on_close_callback)
        elif tipo == "explorar":
            self.actividad_explorar(actividad, parent_win, on_close_callback)
        elif tipo == "arrastrar":
            self.actividad_arrastrar(actividad, parent_win, on_close_callback)
        elif tipo == "teclado":
            self.actividad_teclado(actividad, parent_win, on_close_callback)
        elif tipo == "bloques":
            self.actividad_bloques(actividad, parent_win, on_close_callback)
        elif tipo == "atrapa":
            self.actividad_atrapa(actividad, parent_win, on_close_callback)
        elif tipo == "gran_reto":
            self.actividad_gran_reto(actividad, parent_win, on_close_callback)
        elif tipo == "reto":
            self.actividad_reto(actividad, parent_win, on_close_callback)
        elif tipo == "codigo":
            self.actividad_codigo(actividad, parent_win, on_close_callback)

    # --- Actividad: selección múltiple (una o varias preguntas encadenadas) ---
    def actividad_seleccion(self, actividad, parent_win, on_close_callback):
        win = tk.Toplevel(parent_win)
        win.title(actividad["titulo"])
        win.geometry("500x380")
        win.configure(bg=self.bg_color)
        win.grab_set()
        preguntas = actividad["preguntas"]
        estado = {"idx": 0, "aciertos": 0}

        tk.Label(win, text=actividad["titulo"], font=("Segoe UI", 13, "bold"), bg=self.bg_color, fg=self.primary_color).pack(pady=15)
        lbl_pregunta = tk.Label(win, text="", font=("Segoe UI", 12), bg=self.bg_color, fg="#1F2937", wraplength=440, justify="left")
        lbl_pregunta.pack(pady=10, padx=20)
        frame_opciones = tk.Frame(win, bg=self.bg_color)
        frame_opciones.pack(pady=10)

        def mostrar_pregunta():
            for w in frame_opciones.winfo_children():
                w.destroy()
            p = preguntas[estado["idx"]]
            lbl_pregunta.config(text="Pregunta {}/{}: {}".format(estado["idx"] + 1, len(preguntas), p["pregunta"]))
            ops, correcta = self._opciones_barajadas(p["opciones"], p["correcta"])
            estado["correcta_actual"] = correcta
            for i, opcion in enumerate(ops):
                tk.Button(frame_opciones, text=opcion, font=("Segoe UI", 10, "bold"), bg="white", fg="#1F2937",
                           bd=1, relief="solid", width=30, pady=8,
                           command=lambda idx=i: responder(idx)).pack(pady=5)

        def responder(idx):
            if idx == estado["correcta_actual"]:
                estado["aciertos"] += 1
            estado["idx"] += 1
            if estado["idx"] < len(preguntas):
                mostrar_pregunta()
            else:
                finalizar()

        def finalizar():
            win.destroy()
            self.otorgar_puntos_actividad(actividad["id"], actividad["puntos"], parent_win)
            on_close_callback()

        mostrar_pregunta()

    # --- Actividad: relacionar (clic izquierda -> clic derecha) ---
    def actividad_relacionar(self, actividad, parent_win, on_close_callback):
        win = tk.Toplevel(parent_win)
        win.title(actividad["titulo"])
        win.geometry("650x420")
        win.configure(bg=self.bg_color)
        win.grab_set()

        pares = actividad["pares"]
        izquierda = [p[0] for p in pares]
        derecha = [p[1] for p in pares]
        random.shuffle(derecha)

        tk.Label(win, text=actividad["titulo"] + "\nHaz clic en un elemento de la izquierda y luego su pareja a la derecha.",
                  font=("Segoe UI", 11, "bold"), bg=self.bg_color, fg=self.primary_color, justify="center").pack(pady=10)

        cuerpo = tk.Frame(win, bg=self.bg_color)
        cuerpo.pack(expand=True, fill="both", padx=20)
        col_izq = tk.Frame(cuerpo, bg=self.bg_color)
        col_izq.pack(side="left", expand=True, fill="both", padx=10)
        col_der = tk.Frame(cuerpo, bg=self.bg_color)
        col_der.pack(side="left", expand=True, fill="both", padx=10)

        seleccion = {"izq": None}
        emparejados = set()
        botones_izq = {}
        botones_der = {}

        def click_izq(texto, btn):
            if texto in emparejados:
                return
            seleccion["izq"] = texto
            for t, b in botones_izq.items():
                b.config(bg="#DBEAFE" if t == texto else "white")

        def click_der(texto, btn):
            if seleccion["izq"] is None or texto in emparejados:
                return
            correcto = dict(pares).get(seleccion["izq"]) == texto
            if correcto:
                emparejados.add(seleccion["izq"])
                emparejados.add(texto)
                botones_izq[seleccion["izq"]].config(bg="#BBF7D0", state="disabled")
                botones_der[texto].config(bg="#BBF7D0", state="disabled")
                seleccion["izq"] = None
                if len(emparejados) == len(izquierda) + len(derecha):
                    win.after(400, terminar)
            else:
                btn.config(bg="#FCA5A5")
                win.after(300, lambda: btn.config(bg="white"))

        for texto in izquierda:
            b = tk.Button(col_izq, text=texto, font=("Segoe UI", 9), bg="white", wraplength=180, justify="left",
                           anchor="w", padx=8, pady=8, bd=1, relief="solid")
            b.config(command=lambda t=texto, bb=b: click_izq(t, bb))
            b.pack(fill="x", pady=5)
            botones_izq[texto] = b

        for texto in derecha:
            b = tk.Button(col_der, text=texto, font=("Segoe UI", 9, "bold"), bg="white", padx=8, pady=8, bd=1, relief="solid")
            b.config(command=lambda t=texto, bb=b: click_der(t, bb))
            b.pack(fill="x", pady=5)
            botones_der[texto] = b

        def terminar():
            win.destroy()
            self.otorgar_puntos_actividad(actividad["id"], actividad["puntos"], parent_win)
            on_close_callback()

    # --- Actividad: ordenar pasos (clic en el orden correcto) ---
    def actividad_ordenar(self, actividad, parent_win, on_close_callback):
        win = tk.Toplevel(parent_win)
        win.title(actividad["titulo"])
        win.geometry("560x440")
        win.configure(bg=self.bg_color)
        win.grab_set()

        items_correctos = actividad["items"]
        items_mezclados = items_correctos[:]
        random.shuffle(items_mezclados)

        tk.Label(win, text=actividad["titulo"], font=("Segoe UI", 12, "bold"), bg=self.bg_color, fg=self.primary_color).pack(pady=10)
        tk.Label(win, text=actividad.get("instruccion", "Haz clic en cada paso en el orden correcto:"),
                  font=("Segoe UI", 10), bg=self.bg_color, fg="#4B5563", wraplength=480).pack(pady=(0, 10))

        seleccionados_lbl = tk.Label(win, text="Tu orden: (vacío)", font=("Segoe UI", 9, "italic"), bg=self.bg_color,
                                       fg="#374151", wraplength=480, justify="left")
        seleccionados_lbl.pack(pady=(0, 10))

        frame_botones = tk.Frame(win, bg=self.bg_color)
        frame_botones.pack(pady=5)

        estado = {"orden": []}
        botones = {}

        def click_item(texto, btn):
            if texto in estado["orden"]:
                return
            estado["orden"].append(texto)
            btn.config(state="disabled", bg="#DBEAFE")
            seleccionados_lbl.config(text="Tu orden: " + " → ".join(
                str(i + 1) + ") " + t for i, t in enumerate(estado["orden"])))
            if len(estado["orden"]) == len(items_correctos):
                win.after(300, evaluar)

        for texto in items_mezclados:
            b = tk.Button(frame_botones, text=texto, font=("Segoe UI", 9), bg="white", width=48, anchor="w",
                           padx=8, pady=8, bd=1, relief="solid")
            b.config(command=lambda t=texto, bb=b: click_item(t, bb))
            b.pack(pady=4)
            botones[texto] = b

        def evaluar():
            correcto = estado["orden"] == items_correctos
            if correcto:
                messagebox.showinfo("¡Correcto!", "🎉 ¡Ordenaste todos los pasos correctamente!", parent=win)
                win.destroy()
                self.otorgar_puntos_actividad(actividad["id"], actividad["puntos"], parent_win)
                on_close_callback()
            else:
                messagebox.showinfo("Casi...", "El orden no es correcto todavía. ¡Vuelve a intentarlo!", parent=win)
                estado["orden"] = []
                seleccionados_lbl.config(text="Tu orden: (vacío)")
                for b in botones.values():
                    b.config(state="normal", bg="white")

    # --- Actividad: memorama ---
    def actividad_memoria(self, actividad, parent_win, on_close_callback):
        win = tk.Toplevel(parent_win)
        win.title(actividad["titulo"])
        win.geometry("560x460")
        win.configure(bg=self.bg_color)
        win.grab_set()

        pares = actividad["pares"]
        cartas = []
        for a, b in pares:
            cartas.append(("icono", a, (a, b)))
            cartas.append(("texto", b, (a, b)))
        random.shuffle(cartas)

        tk.Label(win, text=actividad["titulo"] + "\nEncuentra todas las parejas.", font=("Segoe UI", 12, "bold"),
                  bg=self.bg_color, fg=self.primary_color, justify="center").pack(pady=10)

        grid = tk.Frame(win, bg=self.bg_color)
        grid.pack(pady=10)

        estado = {"volteadas": [], "encontradas": set(), "bloqueado": False}
        botones = []

        cols = 4
        for idx, (tipo, valor, par) in enumerate(cartas):
            fila, col = idx // cols, idx % cols
            btn = tk.Button(grid, text="❓", font=("Segoe UI", 14, "bold"), width=8, height=3, bg="#DBEAFE", bd=1, relief="solid")
            btn.grid(row=fila, column=col, padx=5, pady=5)
            botones.append({"btn": btn, "valor": valor, "par": par, "idx": idx})

        def voltear(carta):
            if estado["bloqueado"] or carta["idx"] in estado["encontradas"] or carta in estado["volteadas"]:
                return
            carta["btn"].config(text=carta["valor"], bg="white")
            estado["volteadas"].append(carta)
            if len(estado["volteadas"]) == 2:
                estado["bloqueado"] = True
                win.after(600, comprobar)

        def comprobar():
            c1, c2 = estado["volteadas"]
            if c1["par"] == c2["par"] and c1["idx"] != c2["idx"]:
                c1["btn"].config(bg="#BBF7D0", state="disabled")
                c2["btn"].config(bg="#BBF7D0", state="disabled")
                estado["encontradas"].add(c1["idx"])
                estado["encontradas"].add(c2["idx"])
            else:
                c1["btn"].config(text="❓", bg="#DBEAFE")
                c2["btn"].config(text="❓", bg="#DBEAFE")
            estado["volteadas"] = []
            estado["bloqueado"] = False
            if len(estado["encontradas"]) == len(cartas):
                win.after(300, terminar)

        for c in botones:
            c["btn"].config(command=lambda cc=c: voltear(cc))

        def terminar():
            messagebox.showinfo("¡Bien hecho!", "🎉 ¡Encontraste todas las parejas!", parent=win)
            win.destroy()
            self.otorgar_puntos_actividad(actividad["id"], actividad["puntos"], parent_win)
            on_close_callback()

    # --- Actividad: clasificar en categorías ---
    def actividad_clasificar(self, actividad, parent_win, on_close_callback):
        win = tk.Toplevel(parent_win)
        win.title(actividad["titulo"])
        win.geometry("560x420")
        win.configure(bg=self.bg_color)
        win.grab_set()

        items = actividad["items"][:]
        random.shuffle(items)
        categorias = actividad["categorias"]
        estado = {"idx": 0, "aciertos": 0}

        tk.Label(win, text=actividad["titulo"], font=("Segoe UI", 12, "bold"), bg=self.bg_color, fg=self.primary_color).pack(pady=15)
        lbl_item = tk.Label(win, text="", font=("Segoe UI", 16, "bold"), bg=self.bg_color, fg="#1F2937")
        lbl_item.pack(pady=15)
        lbl_progreso = tk.Label(win, text="", font=("Segoe UI", 9), bg=self.bg_color, fg="#6B7280")
        lbl_progreso.pack()

        frame_botones = tk.Frame(win, bg=self.bg_color)
        frame_botones.pack(pady=20)

        def mostrar_item():
            nombre, _cat = items[estado["idx"]]
            lbl_item.config(text=nombre)
            lbl_progreso.config(text="Elemento {}/{}".format(estado["idx"] + 1, len(items)))

        def elegir(categoria_elegida):
            nombre, cat_correcta = items[estado["idx"]]
            if categoria_elegida == cat_correcta:
                estado["aciertos"] += 1
            estado["idx"] += 1
            if estado["idx"] < len(items):
                mostrar_item()
            else:
                win.destroy()
                self.otorgar_puntos_actividad(actividad["id"], actividad["puntos"], parent_win)
                on_close_callback()

        for cat in categorias:
            tk.Button(frame_botones, text=cat, font=("Segoe UI", 11, "bold"), bg=self.secondary_color, fg="white",
                       bd=0, padx=20, pady=12, cursor="hand2", command=lambda c=cat: elegir(c)).pack(side="left", padx=10)

        mostrar_item()

    # --- Actividad: completar patrones/secuencias ---
    def actividad_patron(self, actividad, parent_win, on_close_callback):
        win = tk.Toplevel(parent_win)
        win.title(actividad["titulo"])
        win.geometry("500x350")
        win.configure(bg=self.bg_color)
        win.grab_set()

        patrones = actividad["patrones"]
        estado = {"idx": 0}

        tk.Label(win, text=actividad["titulo"], font=("Segoe UI", 13, "bold"), bg=self.bg_color, fg=self.primary_color).pack(pady=15)
        lbl_sec = tk.Label(win, text="", font=("Segoe UI", 20, "bold"), bg=self.bg_color, fg="#1F2937")
        lbl_sec.pack(pady=20)
        frame_op = tk.Frame(win, bg=self.bg_color)
        frame_op.pack()

        def mostrar():
            for w in frame_op.winfo_children():
                w.destroy()
            p = patrones[estado["idx"]]
            lbl_sec.config(text=p["secuencia"] + " ___")
            ops = p["opciones"][:]
            random.shuffle(ops)
            for i, op in enumerate(ops):
                tk.Button(frame_op, text=op, font=("Segoe UI", 14, "bold"), bg="white", bd=1, relief="solid",
                           width=6, height=2, command=lambda idx=i: responder(idx)).pack(side="left", padx=8)

        def responder(idx):
            estado["idx"] += 1
            if estado["idx"] < len(patrones):
                mostrar()
            else:
                win.destroy()
                self.otorgar_puntos_actividad(actividad["id"], actividad["puntos"], parent_win)
                on_close_callback()

        mostrar()

    # --- Actividad: situación problema con explicación ---
    def actividad_problema(self, actividad, parent_win, on_close_callback):
        win = tk.Toplevel(parent_win)
        win.title(actividad["titulo"])
        win.geometry("520x360")
        win.configure(bg=self.bg_color)
        win.grab_set()

        tk.Label(win, text="🧩 " + actividad["titulo"], font=("Segoe UI", 13, "bold"), bg=self.bg_color,
                  fg=self.primary_color, wraplength=460, justify="left").pack(pady=15)
        tk.Label(win, text=actividad["pregunta"], font=("Segoe UI", 11), bg=self.bg_color, fg="#1F2937",
                  wraplength=460, justify="left").pack(pady=10, padx=20)

        frame_op = tk.Frame(win, bg=self.bg_color)
        frame_op.pack(pady=10)

        ops, correcta_idx = self._opciones_barajadas(actividad["opciones"], actividad["correcta"])

        def responder(idx):
            for w in frame_op.winfo_children():
                w.config(state="disabled")
            if idx == correcta_idx:
                messagebox.showinfo("¡Correcto!", "🎉 ¡Muy bien! " + actividad.get("explicacion", ""), parent=win)
            else:
                messagebox.showinfo("Sigue intentando", actividad.get("explicacion", "Esa no era la mejor opción."), parent=win)
            win.destroy()
            self.otorgar_puntos_actividad(actividad["id"], actividad["puntos"], parent_win)
            on_close_callback()

        for i, op in enumerate(ops):
            tk.Button(frame_op, text=op, font=("Segoe UI", 10, "bold"), bg="white", bd=1, relief="solid",
                       width=38, pady=8, command=lambda idx=i: responder(idx)).pack(pady=5)

    # --- Actividad: laberinto simple con botones de dirección ---
    def actividad_laberinto(self, actividad, parent_win, on_close_callback):
        win = tk.Toplevel(parent_win)
        win.title(actividad["titulo"])
        win.geometry("420x480")
        win.configure(bg=self.bg_color)
        win.grab_set()

        # 0 = camino libre, 1 = pared
        mapa = [
            [0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 0],
        ]
        inicio = (0, 0)
        meta = (4, 4)
        pos = {"f": inicio[0], "c": inicio[1]}
        tam = 60

        tk.Label(win, text="🌀 " + actividad["titulo"] + "\nLlega desde 🙂 hasta 🏁", font=("Segoe UI", 12, "bold"),
                  bg=self.bg_color, fg=self.primary_color, justify="center").pack(pady=10)

        canvas = tk.Canvas(win, width=tam * 5, height=tam * 5, bg="white", highlightthickness=1, highlightbackground="#D1D5DB")
        canvas.pack(pady=10)

        def dibujar():
            canvas.delete("all")
            for f in range(5):
                for c in range(5):
                    x0, y0 = c * tam, f * tam
                    x1, y1 = x0 + tam, y0 + tam
                    color = "#374151" if mapa[f][c] == 1 else "#F0F4F8"
                    canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="#D1D5DB")
            fx, fy = meta[1] * tam + tam // 2, meta[0] * tam + tam // 2
            canvas.create_text(fx, fy, text="🏁", font=("Segoe UI", 20))
            px, py = pos["c"] * tam + tam // 2, pos["f"] * tam + tam // 2
            canvas.create_text(px, py, text="🙂", font=("Segoe UI", 20))

        def mover(df, dc):
            nf, nc = pos["f"] + df, pos["c"] + dc
            if 0 <= nf < 5 and 0 <= nc < 5 and mapa[nf][nc] == 0:
                pos["f"], pos["c"] = nf, nc
                dibujar()
                if (nf, nc) == meta:
                    win.after(200, ganar)

        def ganar():
            messagebox.showinfo("¡Meta alcanzada!", "🎉 ¡Llegaste a la meta del laberinto!", parent=win)
            win.destroy()
            self.otorgar_puntos_actividad(actividad["id"], actividad["puntos"], parent_win)
            on_close_callback()

        frame_ctrl = tk.Frame(win, bg=self.bg_color)
        frame_ctrl.pack(pady=10)
        tk.Button(frame_ctrl, text="⬆️", font=("Segoe UI", 12, "bold"), width=4, command=lambda: mover(-1, 0)).grid(row=0, column=1, pady=2)
        tk.Button(frame_ctrl, text="⬅️", font=("Segoe UI", 12, "bold"), width=4, command=lambda: mover(0, -1)).grid(row=1, column=0, padx=2)
        tk.Button(frame_ctrl, text="➡️", font=("Segoe UI", 12, "bold"), width=4, command=lambda: mover(0, 1)).grid(row=1, column=2, padx=2)
        tk.Button(frame_ctrl, text="⬇️", font=("Segoe UI", 12, "bold"), width=4, command=lambda: mover(1, 0)).grid(row=2, column=1, pady=2)

        dibujar()

    # --- Actividad: exploración interactiva (clic en objetos para descubrir información) ---
    def actividad_explorar(self, actividad, parent_win, on_close_callback):
        win = tk.Toplevel(parent_win)
        win.title(actividad["titulo"])
        win.geometry("660x580")
        win.configure(bg=self.bg_color)
        win.grab_set()

        objetos = actividad["objetos"]
        explorados = set()

        tk.Label(win, text=actividad["titulo"], font=("Segoe UI", 14, "bold"),
                 bg=self.bg_color, fg=self.primary_color).pack(pady=(15, 2))
        tk.Label(win, text=actividad.get("instruccion", "Haz clic en cada objeto para descubrir información."),
                 font=("Segoe UI", 10), bg=self.bg_color, fg="#4B5563", wraplength=580, justify="center").pack(pady=(0, 6))

        lbl_progreso = tk.Label(win, text="Explorados 0/{}".format(len(objetos)),
                                font=("Segoe UI", 10, "bold"), bg=self.bg_color, fg="#2563EB")
        lbl_progreso.pack()

        # Panel donde aparece la información del objeto seleccionado
        panel = tk.Frame(win, bg="white", bd=0, highlightthickness=2, highlightbackground="#93C5FD")
        panel.pack(fill="x", padx=20, pady=10)
        lbl_info_titulo = tk.Label(panel, text="👆 Toca un objeto para conocerlo", font=("Segoe UI", 11, "bold"),
                                   bg="white", fg=self.primary_color)
        lbl_info_titulo.pack(anchor="w", padx=12, pady=(10, 0))
        lbl_info_texto = tk.Label(panel, text="", font=("Segoe UI", 10), bg="white", fg="#374151",
                                  wraplength=600, justify="left")
        lbl_info_texto.pack(anchor="w", padx=12, pady=(2, 10))

        grid = tk.Frame(win, bg=self.bg_color)
        grid.pack(pady=10)
        botones = {}
        cols = 3

        def terminar():
            messagebox.showinfo("¡Exploración completa!", "🎉 ¡Descubriste todos los objetos!", parent=win)
            win.destroy()
            self.otorgar_puntos_actividad(actividad["id"], actividad["puntos"], parent_win)
            on_close_callback()

        def al_explorar(idx):
            obj = objetos[idx]
            lbl_info_titulo.config(text="{} {}".format(obj["icono"], obj["nombre"]))
            lbl_info_texto.config(text=obj["info"])
            if idx not in explorados:
                explorados.add(idx)
                botones[idx].config(bg="#BBF7D0")
                self._animar_pulso(botones[idx], "#BBF7D0")
                lbl_progreso.config(text="Explorados {}/{}".format(len(explorados), len(objetos)))
                if len(explorados) == len(objetos):
                    win.after(500, terminar)

        for idx, obj in enumerate(objetos):
            fila, col = idx // cols, idx % cols
            b = tk.Button(grid, text="{}\n{}".format(obj["icono"], obj["nombre"]),
                          font=("Segoe UI", 12, "bold"), bg="white", fg="#1F2937",
                          width=14, height=3, bd=0, relief="flat",
                          highlightthickness=1, highlightbackground="#D1D5DB", cursor="hand2",
                          command=lambda i=idx: al_explorar(i))
            b.grid(row=fila, column=col, padx=8, pady=8)
            botones[idx] = b

    def _animar_pulso(self, widget, color_final="#BBF7D0"):
        """Pequeña animación de feedback: destello y regreso al color final."""
        try:
            widget.config(bg="#FDE68A")
            widget.after(140, lambda: widget.config(bg=color_final))
        except tk.TclError:
            pass

    # --- Actividad: arrastrar y soltar (arrastra cada tarjeta a su categoría) ---
    def actividad_arrastrar(self, actividad, parent_win, on_close_callback):
        win = tk.Toplevel(parent_win)
        win.title(actividad["titulo"])
        win.geometry("680x560")
        win.configure(bg=self.bg_color)
        win.grab_set()

        tk.Label(win, text=actividad["titulo"], font=("Segoe UI", 14, "bold"),
                 bg=self.bg_color, fg=self.primary_color).pack(pady=(15, 2))
        tk.Label(win, text=actividad.get("instruccion", "Arrastra cada tarjeta a su lugar correcto."),
                 font=("Segoe UI", 10), bg=self.bg_color, fg="#4B5563", wraplength=600, justify="center").pack(pady=(0, 4))
        lbl_prog = tk.Label(win, text="", font=("Segoe UI", 10, "bold"), bg=self.bg_color, fg="#2563EB")
        lbl_prog.pack()

        W, H = 640, 440
        canvas = tk.Canvas(win, width=W, height=H, bg="white", highlightthickness=1, highlightbackground="#D1D5DB")
        canvas.pack(pady=10)

        categorias = actividad["categorias"]
        items = actividad["items"]
        n = len(categorias)
        bin_top = H - 130
        bins = []
        contador_bin = {}
        ancho_bin = W // n
        for i, cat in enumerate(categorias):
            x0 = i * ancho_bin + 8
            x1 = (i + 1) * ancho_bin - 8
            y0, y1 = bin_top, H - 10
            canvas.create_rectangle(x0, y0, x1, y1, fill="#EFF6FF", outline="#93C5FD", width=2)
            canvas.create_text((x0 + x1) // 2, y0 + 15, text="📂 " + cat, font=("Segoe UI", 10, "bold"), fill="#1E3A8A")
            bins.append((x0, y0, x1, y1, cat))
            contador_bin[i] = 0

        tw, th = 190, 34
        tokens = {}
        for idx, it in enumerate(items):
            x = 15 + (idx % 3) * 205
            y = 15 + (idx // 3) * 44
            rect = canvas.create_rectangle(x, y, x + tw, y + th, fill="#FDE68A", outline="#D97706", width=2, tags=("tok%d" % idx,))
            canvas.create_text(x + tw // 2, y + th // 2, text=it["texto"], font=("Segoe UI", 10, "bold"), tags=("tok%d" % idx,))
            tokens[idx] = {"rect": rect, "origin": (x, y), "pos": (x, y), "cat": it["cat"], "placed": False}

        drag = {"idx": None, "lx": 0, "ly": 0}
        colocados = {"n": 0}

        def actualizar_prog():
            lbl_prog.config(text="Colocadas {}/{}".format(colocados["n"], len(items)))
        actualizar_prog()

        def mover_a(idx, nx, ny):
            px, py = tokens[idx]["pos"]
            canvas.move("tok%d" % idx, nx - px, ny - py)
            tokens[idx]["pos"] = (nx, ny)

        def on_press(event, idx):
            if tokens[idx]["placed"]:
                return
            drag["idx"] = idx
            drag["lx"], drag["ly"] = event.x, event.y
            canvas.tag_raise("tok%d" % idx)

        def on_move(event):
            idx = drag["idx"]
            if idx is None:
                return
            dx, dy = event.x - drag["lx"], event.y - drag["ly"]
            canvas.move("tok%d" % idx, dx, dy)
            px, py = tokens[idx]["pos"]
            tokens[idx]["pos"] = (px + dx, py + dy)
            drag["lx"], drag["ly"] = event.x, event.y

        def terminar():
            messagebox.showinfo("¡Muy bien!", "🎉 ¡Colocaste todo en su lugar!", parent=win)
            win.destroy()
            self.otorgar_puntos_actividad(actividad["id"], actividad["puntos"], parent_win)
            on_close_callback()

        def on_release(event):
            idx = drag["idx"]
            drag["idx"] = None
            if idx is None:
                return
            px, py = tokens[idx]["pos"]
            cx, cy = px + tw / 2, py + th / 2
            destino = None
            for bi, (x0, y0, x1, y1, cat) in enumerate(bins):
                if x0 <= cx <= x1 and y0 <= cy <= y1:
                    destino = (bi, cat)
                    break
            if destino and destino[1] == tokens[idx]["cat"]:
                bi = destino[0]
                x0, y0, x1, y1, cat = bins[bi]
                slot = contador_bin[bi]
                contador_bin[bi] += 1
                mover_a(idx, x0 + 6, y0 + 32 + slot * 20)
                tokens[idx]["placed"] = True
                canvas.itemconfig(tokens[idx]["rect"], fill="#BBF7D0", outline="#059669")
                colocados["n"] += 1
                actualizar_prog()
                if colocados["n"] == len(items):
                    win.after(400, terminar)
            else:
                ox, oy = tokens[idx]["origin"]
                canvas.itemconfig(tokens[idx]["rect"], fill="#FCA5A5")
                mover_a(idx, ox, oy)
                canvas.after(250, lambda i=idx: canvas.itemconfig(tokens[i]["rect"], fill="#FDE68A"))

        for idx in tokens:
            canvas.tag_bind("tok%d" % idx, "<ButtonPress-1>", lambda e, i=idx: on_press(e, i))
        canvas.bind("<B1-Motion>", on_move)
        canvas.bind("<ButtonRelease-1>", on_release)

    # --- Actividad: juegos de teclado (escribir palabras o encontrar teclas, con medición) ---
    def actividad_teclado(self, actividad, parent_win, on_close_callback):
        modo = actividad.get("modo", "escribir")
        win = tk.Toplevel(parent_win)
        win.title(actividad["titulo"])
        win.geometry("560x430")
        win.configure(bg=self.bg_color)
        win.grab_set()

        reactivos = actividad["reactivos"]
        estado = {"idx": 0, "correctos": 0, "intentos": 0, "inicio": None, "chars": 0}

        tk.Label(win, text=actividad["titulo"], font=("Segoe UI", 14, "bold"),
                 bg=self.bg_color, fg=self.primary_color).pack(pady=(15, 2))
        tk.Label(win, text=actividad.get("instruccion", ""), font=("Segoe UI", 10),
                 bg=self.bg_color, fg="#4B5563", wraplength=480, justify="center").pack(pady=(0, 6))
        lbl_prog = tk.Label(win, text="", font=("Segoe UI", 9, "bold"), bg=self.bg_color, fg="#2563EB")
        lbl_prog.pack()
        lbl_objetivo = tk.Label(win, text="", font=("Segoe UI", 26, "bold"), bg=self.bg_color, fg="#1F2937")
        lbl_objetivo.pack(pady=16)
        lbl_feedback = tk.Label(win, text="", font=("Segoe UI", 11, "bold"), bg=self.bg_color, fg="#059669")
        lbl_feedback.pack()

        def actualizar_prog():
            lbl_prog.config(text="Reactivo {}/{}".format(estado["idx"] + 1, len(reactivos)))

        def finalizar():
            tiempo = max(0.5, time.time() - estado["inicio"]) if estado["inicio"] else 1.0
            precision = round(estado["correctos"] / estado["intentos"] * 100) if estado["intentos"] else 100
            if modo == "escribir":
                ppm = round((estado["chars"] / 5) / (tiempo / 60))
                msg = "🎉 ¡Completado!\n\nVelocidad: {} PPM\nPrecisión: {}%".format(ppm, precision)
            else:
                msg = "🎉 ¡Completado!\n\nPrecisión: {}%\nTiempo: {} segundos".format(precision, round(tiempo))
            messagebox.showinfo("Resultado", msg, parent=win)
            win.destroy()
            self.otorgar_puntos_actividad(actividad["id"], actividad["puntos"], parent_win)
            on_close_callback()

        if modo == "escribir":
            entry = tk.Entry(win, font=("Segoe UI", 16), justify="center", width=26)
            entry.pack(pady=8)

            def mostrar():
                actualizar_prog()
                lbl_objetivo.config(text=reactivos[estado["idx"]])
                lbl_feedback.config(text="")
                entry.delete(0, "end")
                entry.focus_set()

            def revisar(event=None):
                if estado["inicio"] is None:
                    estado["inicio"] = time.time()
                escrito = entry.get().strip()
                objetivo = reactivos[estado["idx"]]
                estado["intentos"] += 1
                if escrito == objetivo:
                    estado["correctos"] += 1
                    estado["chars"] += len(objetivo)
                    estado["idx"] += 1
                    if estado["idx"] < len(reactivos):
                        mostrar()
                    else:
                        finalizar()
                else:
                    lbl_feedback.config(text="❌ Casi... revísalo e inténtalo de nuevo", fg="#DC2626")
                    entry.select_range(0, "end")

            entry.bind("<Return>", revisar)
            tk.Button(win, text="Comprobar ✓", font=("Segoe UI", 10, "bold"), bg=self.secondary_color,
                      fg="white", bd=0, padx=12, pady=6, cursor="hand2", command=revisar).pack(pady=4)
            mostrar()
        else:
            tk.Label(win, text="Presiona la tecla en tu teclado", font=("Segoe UI", 10, "italic"),
                     bg=self.bg_color, fg="#6B7280").pack()
            modificadoras = ("Shift_L", "Shift_R", "Control_L", "Control_R", "Alt_L", "Alt_R",
                             "Caps_Lock", "Win_L", "Win_R", "Super_L", "Super_R")

            def coincide(objetivo, event):
                o = objetivo.strip()
                ks, ch = event.keysym, event.char
                if o == "Espacio":
                    return ks == "space"
                if o == "Enter":
                    return ks == "Return"
                if o == "Shift":
                    return ks in ("Shift_L", "Shift_R")
                if o == "Backspace":
                    return ks == "BackSpace"
                if len(o) == 1:
                    return (ch and ch.upper() == o.upper()) or ks.upper() == o.upper()
                return False

            def mostrar():
                actualizar_prog()
                lbl_objetivo.config(text=reactivos[estado["idx"]])
                lbl_feedback.config(text="")

            def on_key(event):
                objetivo = reactivos[estado["idx"]]
                if event.keysym in modificadoras and objetivo != "Shift":
                    return
                if estado["inicio"] is None:
                    estado["inicio"] = time.time()
                estado["intentos"] += 1
                if coincide(objetivo, event):
                    estado["correctos"] += 1
                    estado["idx"] += 1
                    if estado["idx"] < len(reactivos):
                        mostrar()
                    else:
                        win.after(150, finalizar)
                else:
                    lbl_feedback.config(text="❌ Esa no era, intenta de nuevo", fg="#DC2626")

            win.bind("<Key>", on_key)
            win.focus_set()
            mostrar()

    # --- Actividad: programación por bloques (lleva al robot hasta el tesoro) ---
    def actividad_bloques(self, actividad, parent_win, on_close_callback):
        win = tk.Toplevel(parent_win)
        win.title(actividad["titulo"])
        win.geometry("720x600")
        win.configure(bg=self.bg_color)
        win.grab_set()

        mapa = actividad["mapa"]
        filas, cols = len(mapa), len(mapa[0])
        inicio = tuple(actividad.get("inicio", [0, 0]))
        meta = tuple(actividad.get("meta", [filas - 1, cols - 1]))
        dir_inicial = {"arriba": 0, "derecha": 1, "abajo": 2, "izquierda": 3}.get(actividad.get("mirando", "derecha"), 1)
        bloques_disp = actividad.get("bloques", ["AVANZAR", "GIRAR IZQUIERDA", "GIRAR DERECHA"])

        tk.Label(win, text=actividad["titulo"], font=("Segoe UI", 14, "bold"),
                 bg=self.bg_color, fg=self.primary_color).pack(pady=(12, 2))
        tk.Label(win, text=actividad.get("instruccion", "Arma el programa para llevar el robot hasta el tesoro."),
                 font=("Segoe UI", 10), bg=self.bg_color, fg="#4B5563", wraplength=640, justify="center").pack(pady=(0, 6))

        cuerpo = tk.Frame(win, bg=self.bg_color)
        cuerpo.pack(fill="both", expand=True, padx=12, pady=6)

        izq = tk.Frame(cuerpo, bg=self.bg_color)
        izq.pack(side="left", padx=8)
        tam = 62
        canvas = tk.Canvas(izq, width=tam * cols, height=tam * filas, bg="white",
                           highlightthickness=1, highlightbackground="#D1D5DB")
        canvas.pack()
        lbl_mirando = tk.Label(izq, text="", font=("Segoe UI", 11, "bold"), bg=self.bg_color, fg="#1F2937")
        lbl_mirando.pack(pady=6)

        der = tk.Frame(cuerpo, bg=self.bg_color)
        der.pack(side="left", fill="both", expand=True, padx=8)
        tk.Label(der, text="Tu programa:", font=("Segoe UI", 11, "bold"), bg=self.bg_color, fg=self.primary_color).pack(anchor="w")
        lista = tk.Listbox(der, font=("Consolas", 11), height=8, activestyle="none")
        lista.pack(fill="both", expand=True, pady=4)

        programa = []
        flechas = {0: "⬆️", 1: "➡️", 2: "⬇️", 3: "⬅️"}
        deltas = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
        estado = {"f": inicio[0], "c": inicio[1], "d": dir_inicial, "corriendo": False}

        def dibujar():
            canvas.delete("all")
            for f in range(filas):
                for c in range(cols):
                    x0, y0 = c * tam, f * tam
                    color = "#374151" if mapa[f][c] == 1 else "#F0F4F8"
                    canvas.create_rectangle(x0, y0, x0 + tam, y0 + tam, fill=color, outline="#D1D5DB")
            mx, my = meta[1] * tam + tam // 2, meta[0] * tam + tam // 2
            canvas.create_text(mx, my, text="🎯", font=("Segoe UI", 26))
            rx, ry = estado["c"] * tam + tam // 2, estado["f"] * tam + tam // 2
            canvas.create_text(rx, ry, text="🤖", font=("Segoe UI", 24))
            lbl_mirando.config(text="El robot mira: " + flechas[estado["d"]])

        def refrescar_lista():
            lista.delete(0, "end")
            for i, b in enumerate(programa):
                lista.insert("end", " {}. {}".format(i + 1, b))

        def agregar(bloque):
            if estado["corriendo"]:
                return
            programa.append(bloque)
            refrescar_lista()

        def limpiar():
            if estado["corriendo"]:
                return
            programa.clear()
            refrescar_lista()
            estado["f"], estado["c"], estado["d"] = inicio[0], inicio[1], dir_inicial
            dibujar()

        def exito():
            messagebox.showinfo("¡Lo lograste!", "🎉 ¡El robot llegó al tesoro! ¡Gran trabajo!", parent=win)
            win.destroy()
            self.otorgar_puntos_actividad(actividad["id"], actividad["puntos"], parent_win)
            on_close_callback()

        def ejecutar():
            if estado["corriendo"] or not programa:
                return
            estado["f"], estado["c"], estado["d"] = inicio[0], inicio[1], dir_inicial
            dibujar()
            estado["corriendo"] = True
            pasos = list(programa)

            def paso(i):
                if not estado["corriendo"]:
                    return
                if i >= len(pasos):
                    estado["corriendo"] = False
                    if (estado["f"], estado["c"]) == meta:
                        exito()
                    else:
                        messagebox.showinfo("Casi...", "El robot no llegó al tesoro. ¡Ajusta tu programa e inténtalo otra vez!", parent=win)
                    return
                b = pasos[i]
                if b == "AVANZAR":
                    df, dc = deltas[estado["d"]]
                    nf, nc = estado["f"] + df, estado["c"] + dc
                    if 0 <= nf < filas and 0 <= nc < cols and mapa[nf][nc] == 0:
                        estado["f"], estado["c"] = nf, nc
                elif b == "GIRAR DERECHA":
                    estado["d"] = (estado["d"] + 1) % 4
                elif b == "GIRAR IZQUIERDA":
                    estado["d"] = (estado["d"] - 1) % 4
                dibujar()
                if (estado["f"], estado["c"]) == meta:
                    estado["corriendo"] = False
                    win.after(250, exito)
                    return
                win.after(450, lambda: paso(i + 1))

            paso(0)

        panel_bloques = tk.Frame(der, bg=self.bg_color)
        panel_bloques.pack(fill="x", pady=6)
        etiquetas = {"AVANZAR": "⬆️ AVANZAR", "GIRAR IZQUIERDA": "↩️ GIRAR IZQUIERDA", "GIRAR DERECHA": "↪️ GIRAR DERECHA"}
        for b in bloques_disp:
            tk.Button(panel_bloques, text=etiquetas.get(b, b), font=("Segoe UI", 10, "bold"),
                      bg="#3B82F6", fg="white", bd=0, padx=8, pady=6, cursor="hand2",
                      command=lambda bb=b: agregar(bb)).pack(fill="x", pady=3)

        acciones = tk.Frame(der, bg=self.bg_color)
        acciones.pack(fill="x", pady=6)
        tk.Button(acciones, text="▶️ Ejecutar", font=("Segoe UI", 10, "bold"), bg=self.secondary_color,
                  fg="white", bd=0, padx=10, pady=6, cursor="hand2", command=ejecutar).pack(side="left", padx=4)
        tk.Button(acciones, text="🗑️ Borrar", font=("Segoe UI", 10, "bold"), bg="#9CA3AF",
                  fg="white", bd=0, padx=10, pady=6, cursor="hand2", command=limpiar).pack(side="left", padx=4)

        dibujar()
        refrescar_lista()

    # --- Actividad: atrapa el objeto (juego de puntería con el mouse, con niveles) ---
    def actividad_atrapa(self, actividad, parent_win, on_close_callback):
        win = tk.Toplevel(parent_win)
        win.title(actividad["titulo"])
        win.geometry("560x560")
        win.configure(bg=self.bg_color)
        win.grab_set()

        emoji = actividad.get("emoji", "🎯")
        tk.Label(win, text=actividad["titulo"], font=("Segoe UI", 14, "bold"),
                 bg=self.bg_color, fg=self.primary_color).pack(pady=(15, 2))
        tk.Label(win, text=actividad.get("instruccion", "Haz clic en los objetos antes de que se acabe el tiempo."),
                 font=("Segoe UI", 10), bg=self.bg_color, fg="#4B5563", wraplength=480, justify="center").pack(pady=(0, 6))

        cont = tk.Frame(win, bg=self.bg_color)
        cont.pack(fill="both", expand=True)

        niveles = {
            "Fácil":   {"objetivo": 8,  "tiempo": 25, "intervalo": 1100, "color": "#10B981"},
            "Medio":   {"objetivo": 12, "tiempo": 22, "intervalo": 850,  "color": "#F59E0B"},
            "Difícil": {"objetivo": 16, "tiempo": 20, "intervalo": 600,  "color": "#EF4444"},
        }

        def elegir_nivel():
            for w in cont.winfo_children():
                w.destroy()
            tk.Label(cont, text="Elige el nivel de dificultad:", font=("Segoe UI", 12, "bold"),
                     bg=self.bg_color, fg="#1F2937").pack(pady=20)
            for nombre, cfg in niveles.items():
                tk.Button(cont, text="{}   ({} objetos · {} s)".format(nombre, cfg["objetivo"], cfg["tiempo"]),
                          font=("Segoe UI", 11, "bold"), bg=cfg["color"], fg="white", bd=0, padx=16, pady=12,
                          width=26, cursor="hand2", command=lambda n=nombre: iniciar(n)).pack(pady=8)

        def iniciar(nivel_nombre):
            for w in cont.winfo_children():
                w.destroy()
            cfg = niveles[nivel_nombre]
            objetivo = cfg["objetivo"]
            estado = {"puntos": 0, "tiempo": cfg["tiempo"], "jugando": True}

            barra = tk.Frame(cont, bg=self.bg_color)
            barra.pack(fill="x", padx=25)
            lbl_score = tk.Label(barra, text="", font=("Segoe UI", 12, "bold"), bg=self.bg_color, fg=self.primary_color)
            lbl_score.pack(side="left")
            lbl_time = tk.Label(barra, text="", font=("Segoe UI", 12, "bold"), bg=self.bg_color, fg="#DC2626")
            lbl_time.pack(side="right")

            W, H = 500, 380
            canvas = tk.Canvas(cont, width=W, height=H, bg="white", highlightthickness=1, highlightbackground="#D1D5DB")
            canvas.pack(pady=10)
            R = 34

            def actualizar_barra():
                lbl_score.config(text="Atrapados: {}/{}".format(estado["puntos"], objetivo))
                lbl_time.config(text="⏱️ {} s".format(estado["tiempo"]))

            def nuevo_objeto():
                if not estado["jugando"]:
                    return
                canvas.delete("obj")
                x = random.randint(R, W - R)
                y = random.randint(R, H - R)
                canvas.create_oval(x - R, y - R, x + R, y + R, fill="#DBEAFE", outline="#3B82F6", width=2, tags=("obj",))
                canvas.create_text(x, y, text=emoji, font=("Segoe UI", 26), tags=("obj",))

            def terminar(gano):
                if not estado["jugando"]:
                    return
                estado["jugando"] = False
                try:
                    canvas.delete("all")
                except tk.TclError:
                    return
                if gano:
                    messagebox.showinfo("¡Ganaste!", "🎉 ¡Atrapaste {} objetos! ¡Excelente puntería!".format(estado["puntos"]), parent=win)
                    win.destroy()
                    self.otorgar_puntos_actividad(actividad["id"], actividad["puntos"], parent_win)
                    on_close_callback()
                else:
                    if messagebox.askyesno("¡Casi!", "Atrapaste {}/{}. ¿Quieres intentarlo de nuevo?".format(estado["puntos"], objetivo), parent=win):
                        elegir_nivel()
                    else:
                        win.destroy()

            def click(event):
                if not estado["jugando"]:
                    return
                tocados = canvas.find_overlapping(event.x - 2, event.y - 2, event.x + 2, event.y + 2)
                if any("obj" in canvas.gettags(t) for t in tocados):
                    estado["puntos"] += 1
                    actualizar_barra()
                    if estado["puntos"] >= objetivo:
                        terminar(True)
                    else:
                        nuevo_objeto()

            canvas.bind("<Button-1>", click)

            def mover_periodico():
                if not estado["jugando"]:
                    return
                nuevo_objeto()
                win.after(cfg["intervalo"], mover_periodico)

            def contar_tiempo():
                if not estado["jugando"]:
                    return
                estado["tiempo"] -= 1
                actualizar_barra()
                if estado["tiempo"] <= 0:
                    terminar(estado["puntos"] >= objetivo)
                else:
                    win.after(1000, contar_tiempo)

            actualizar_barra()
            nuevo_objeto()
            win.after(cfg["intervalo"], mover_periodico)
            win.after(1000, contar_tiempo)

        elegir_nivel()

    # --- Actividad: Gran Reto Final (encadena un reto de cada tema con pantalla de victoria) ---
    def actividad_gran_reto(self, actividad, parent_win, on_close_callback):
        win = tk.Toplevel(parent_win)
        win.title(actividad["titulo"])
        win.geometry("620x520")
        win.configure(bg=self.bg_color)
        win.grab_set()

        pasos = actividad["pasos"]
        estado = {"idx": 0}

        tk.Label(win, text=actividad["titulo"], font=("Segoe UI", 16, "bold"),
                 bg=self.bg_color, fg=self.primary_color).pack(pady=(15, 4))
        lbl_prog = tk.Label(win, text="", font=("Segoe UI", 10, "bold"), bg=self.bg_color, fg="#8B5CF6")
        lbl_prog.pack()
        canvas_prog = tk.Canvas(win, height=14, bg="#E5E7EB", highlightthickness=0)
        canvas_prog.pack(fill="x", padx=30, pady=(4, 10))
        lbl_tema = tk.Label(win, text="", font=("Segoe UI", 12, "bold"), bg=self.bg_color, fg=self.secondary_color)
        lbl_tema.pack(pady=(4, 2))
        lbl_pregunta = tk.Label(win, text="", font=("Segoe UI", 12), bg=self.bg_color, fg="#1F2937",
                                wraplength=520, justify="center")
        lbl_pregunta.pack(pady=8, padx=20)
        frame_op = tk.Frame(win, bg=self.bg_color)
        frame_op.pack(pady=10)
        lbl_feedback = tk.Label(win, text="", font=("Segoe UI", 11, "bold"), bg=self.bg_color, fg="#DC2626")
        lbl_feedback.pack()

        def dibujar_prog():
            try:
                canvas_prog.delete("all")
                ancho = canvas_prog.winfo_width() or 540
                frac = estado["idx"] / len(pasos)
                canvas_prog.create_rectangle(0, 0, ancho, 14, fill="#E5E7EB", width=0)
                canvas_prog.create_rectangle(0, 0, ancho * frac, 14, fill="#8B5CF6", width=0)
            except tk.TclError:
                pass

        def mostrar():
            p = pasos[estado["idx"]]
            lbl_prog.config(text="Reto {} de {}".format(estado["idx"] + 1, len(pasos)))
            lbl_tema.config(text="🎯 " + p.get("tema", ""))
            lbl_pregunta.config(text=p["pregunta"])
            lbl_feedback.config(text="")
            for w in frame_op.winfo_children():
                w.destroy()
            ops, correcta = self._opciones_barajadas(p["opciones"], p["correcta"])
            estado["correcta_actual"] = correcta
            for i, op in enumerate(ops):
                tk.Button(frame_op, text=op, font=("Segoe UI", 10, "bold"), bg="white", fg="#1F2937",
                          bd=1, relief="solid", width=36, pady=8, cursor="hand2",
                          command=lambda idx=i: responder(idx)).pack(pady=4)
            win.after(30, dibujar_prog)

        def responder(idx):
            if idx == estado["correcta_actual"]:
                estado["idx"] += 1
                if estado["idx"] < len(pasos):
                    mostrar()
                else:
                    victoria()
            else:
                lbl_feedback.config(text="❌ Inténtalo otra vez, ¡tú puedes!")

        def cerrar():
            win.destroy()
            self.otorgar_puntos_actividad(actividad["id"], actividad["puntos"], parent_win)
            on_close_callback()

        def victoria():
            for w in win.winfo_children():
                w.destroy()
            win.configure(bg=self.primary_color)
            canvas_v = tk.Canvas(win, bg=self.primary_color, highlightthickness=0)
            canvas_v.pack(fill="both", expand=True)
            canvas_v.create_text(310, 130, text="🎉", font=("Segoe UI", 60))
            canvas_v.create_text(310, 210, text="¡GRAN RETO COMPLETADO!", font=("Segoe UI", 18, "bold"), fill="white")
            canvas_v.create_text(310, 250, text="Demostraste todo lo aprendido en {}.".format(self.grado_actual[1].title()),
                                 font=("Segoe UI", 11), fill="#DBEAFE")
            self._confeti(canvas_v, 620, 520)
            tk.Button(win, text="🏆 Reclamar mi recompensa", font=("Segoe UI", 12, "bold"),
                      bg=self.accent_color, fg="white", bd=0, padx=16, pady=10, cursor="hand2",
                      command=cerrar).pack(pady=18)

        mostrar()

    def _confeti(self, canvas, ancho, alto, n=40):
        """Animación ligera de confeti cayendo sobre un canvas."""
        colores = ["#EF4444", "#F59E0B", "#10B981", "#3B82F6", "#8B5CF6", "#EC4899"]
        piezas = []
        for _ in range(n):
            x = random.randint(0, ancho)
            y = random.randint(-alto, 0)
            pid = canvas.create_oval(x, y, x + 8, y + 8, fill=random.choice(colores), outline="")
            piezas.append([pid, random.randint(3, 9)])

        def caer(paso=0):
            try:
                if paso > 60:
                    return
                for pieza in piezas:
                    canvas.move(pieza[0], 0, pieza[1])
                canvas.after(60, lambda: caer(paso + 1))
            except tk.TclError:
                return
        caer()

    # --- Reto del día: mini-cuestionario con XP de bono y racha ---
    def ventana_reto_diario(self):
        est_id = self.estudiante_actual[0]
        if reto_diario_hecho(est_id):
            racha, mejor = obtener_racha(est_id)
            messagebox.showinfo("🎯 Reto del día",
                                  "¡Ya completaste el reto de hoy! 🎉\n\n🔥 Racha actual: {} días\n🏆 Mejor racha: {} días\n\n"
                                  "Vuelve mañana por un reto nuevo.".format(racha, mejor), parent=self.root)
            return

        modulos, _prefijo, _total = datos_grado(self.grado_actual[0])
        banco = [q for m in modulos.values() for q in m.get("evaluacion", [])]
        if not banco:
            return
        n = min(5, len(banco))
        preguntas = random.sample(banco, n)

        win = tk.Toplevel(self.root)
        win.title("🎯 Reto del día")
        win.geometry("560x430")
        win.configure(bg=self.bg_color)
        win.grab_set()

        tk.Label(win, text="🎯 Reto del día", font=("Segoe UI", 15, "bold"), bg=self.bg_color, fg="#8B5CF6").pack(pady=(15, 2))
        tk.Label(win, text="Responde {} preguntas y gana XP extra. ¡Mantén tu racha!".format(n),
                 font=("Segoe UI", 10), bg=self.bg_color, fg="#4B5563").pack(pady=(0, 6))
        lbl_prog = tk.Label(win, text="", font=("Segoe UI", 9, "bold"), bg=self.bg_color, fg="#2563EB")
        lbl_prog.pack()
        lbl_preg = tk.Label(win, text="", font=("Segoe UI", 12), bg=self.bg_color, fg="#1F2937", wraplength=480, justify="center")
        lbl_preg.pack(pady=10, padx=20)
        frame_op = tk.Frame(win, bg=self.bg_color)
        frame_op.pack(pady=8)

        estado = {"idx": 0, "aciertos": 0}

        def mostrar():
            p = preguntas[estado["idx"]]
            lbl_prog.config(text="Pregunta {}/{}".format(estado["idx"] + 1, n))
            lbl_preg.config(text=p["pregunta"])
            for w in frame_op.winfo_children():
                w.destroy()
            ops, correcta = self._opciones_barajadas(p["opciones"], p["correcta"])
            estado["correcta_actual"] = correcta
            for i, op in enumerate(ops):
                tk.Button(frame_op, text=op, font=("Segoe UI", 10, "bold"), bg="white", fg="#1F2937",
                          bd=1, relief="solid", width=32, pady=7, cursor="hand2",
                          command=lambda idx=i: responder(idx)).pack(pady=4)

        def responder(idx):
            if idx == estado["correcta_actual"]:
                estado["aciertos"] += 1
            estado["idx"] += 1
            if estado["idx"] < n:
                mostrar()
            else:
                finalizar()

        def finalizar():
            bono = 25 + estado["aciertos"] * 5
            sumar_xp(est_id, bono)
            marcar_reto_diario(est_id)
            racha, _cambio = registrar_dia_actividad(est_id)
            win.destroy()
            messagebox.showinfo("🎯 ¡Reto del día completado!",
                                  "Acertaste {}/{}.\n\n⭐ Ganaste {} XP de bono.\n🔥 Racha: {} días.\n\n"
                                  "¡Vuelve mañana por otro reto!".format(estado["aciertos"], n, bono, racha), parent=self.root)
            if self.grado_actual and self.grado_actual[0] in (1, 2, 3):
                self.mostrar_menu_primero_basico()

        mostrar()

    # --- Actividad: reto con niveles (no revela la respuesta; da una PISTA al fallar) ---
    def actividad_reto(self, actividad, parent_win, on_close_callback):
        win = tk.Toplevel(parent_win)
        win.title(actividad["titulo"])
        win.geometry("560x460")
        win.configure(bg=self.bg_color)
        win.grab_set()

        nivel = actividad.get("nivel", "🎯 Reto")
        opciones, correcta = self._opciones_barajadas(actividad["opciones"], actividad["correcta"])
        pista = actividad.get("pista", "Vuelve a leer con atención.")
        intentos = {"n": 0}

        tk.Label(win, text=nivel, font=("Segoe UI", 11, "bold"), bg=self.bg_color, fg="#8B5CF6").pack(pady=(14, 0))
        tk.Label(win, text=actividad["titulo"], font=("Segoe UI", 14, "bold"),
                 bg=self.bg_color, fg=self.primary_color).pack(pady=(0, 6))
        tk.Label(win, text=actividad["pregunta"], font=("Segoe UI", 12), bg=self.bg_color, fg="#1F2937",
                 wraplength=500, justify="center").pack(pady=10, padx=20)

        frame_op = tk.Frame(win, bg=self.bg_color)
        frame_op.pack(pady=10)
        lbl_pista = tk.Label(win, text="", font=("Segoe UI", 10, "italic"), bg=self.bg_color, fg="#B45309",
                             wraplength=500, justify="center")
        lbl_pista.pack(pady=6)

        def responder(idx):
            if idx == correcta:
                win.destroy()
                self.otorgar_puntos_actividad(actividad["id"], actividad["puntos"], parent_win)
                on_close_callback()
            else:
                intentos["n"] += 1
                lbl_pista.config(text="❌ Aún no. 💡 Pista: " + pista)

        for i, op in enumerate(opciones):
            tk.Button(frame_op, text=op, font=("Segoe UI", 10, "bold"), bg="white", fg="#1F2937",
                      bd=1, relief="solid", width=36, pady=8, cursor="hand2",
                      command=lambda idx=i: responder(idx)).pack(pady=4)

    # --- Actividad: laboratorio de código (escribe/observa código, ▶️ ejecuta y ve el resultado) ---
    def actividad_codigo(self, actividad, parent_win, on_close_callback):
        win = tk.Toplevel(parent_win)
        win.title(actividad["titulo"])
        win.geometry("700x680")
        win.configure(bg=self.bg_color)
        win.grab_set()

        # Cuerpo desplazable (por si el código + resultado + opciones son largos)
        cont = tk.Canvas(win, bg=self.bg_color, highlightthickness=0)
        sb = ttk.Scrollbar(win, orient="vertical", command=cont.yview)
        cuerpo = tk.Frame(cont, bg=self.bg_color)
        cuerpo.bind("<Configure>", lambda e: cont.configure(scrollregion=cont.bbox("all")))
        vent = cont.create_window((0, 0), window=cuerpo, anchor="nw")
        cont.bind("<Configure>", lambda e: cont.itemconfigure(vent, width=e.width))
        cont.configure(yscrollcommand=sb.set)
        cont.pack(side="left", fill="both", expand=True)
        sb.pack(side="right", fill="y")

        def _rueda(evento):
            try:
                cont.yview_scroll(int(-1 * (evento.delta / 120)), "units")
            except tk.TclError:
                pass
        cont.bind("<Enter>", lambda e: cont.bind_all("<MouseWheel>", _rueda))
        cont.bind("<Leave>", lambda e: cont.unbind_all("<MouseWheel>"))

        tk.Label(cuerpo, text=actividad.get("nivel", "💻 Laboratorio"), font=("Segoe UI", 11, "bold"),
                 bg=self.bg_color, fg="#8B5CF6").pack(pady=(12, 0))
        tk.Label(cuerpo, text=actividad["titulo"], font=("Segoe UI", 14, "bold"),
                 bg=self.bg_color, fg=self.primary_color).pack(pady=(0, 6))
        if actividad.get("instruccion"):
            tk.Label(cuerpo, text=actividad["instruccion"], font=("Segoe UI", 10), bg=self.bg_color,
                     fg="#4B5563", wraplength=600, justify="center").pack(pady=(0, 4))

        # Panel de código (estilo editor oscuro)
        marco_codigo = tk.Frame(cuerpo, bg="#1E293B")
        marco_codigo.pack(fill="x", padx=20, pady=6)
        tk.Label(marco_codigo, text=actividad.get("codigo", ""), font=("Consolas", 11), bg="#1E293B",
                 fg="#E2E8F0", justify="left", anchor="w").pack(fill="x", padx=12, pady=10)

        salida_frame = tk.Frame(cuerpo, bg=self.bg_color)
        salida_frame.pack(fill="x", padx=20, pady=2)

        def render_salida():
            for w in salida_frame.winfo_children():
                w.destroy()
            tipo = actividad.get("salida_tipo", "texto")
            salida = actividad.get("salida", "")
            tk.Label(salida_frame, text="▼ Resultado:", font=("Segoe UI", 9, "bold"),
                     bg=self.bg_color, fg="#059669").pack(anchor="w")
            if tipo == "tabla":
                cols = salida["columnas"]
                tabla = ttk.Treeview(salida_frame, columns=cols, show="headings", height=min(6, len(salida["filas"]) + 1))
                for c in cols:
                    tabla.heading(c, text=c)
                    tabla.column(c, width=110, anchor="center")
                for f in salida["filas"]:
                    tabla.insert("", "end", values=f)
                tabla.pack(fill="x", pady=4)
            elif tipo == "web":
                prev = tk.Frame(salida_frame, bg="white", bd=1, relief="solid")
                prev.pack(fill="x", pady=4)
                for etiqueta, texto in salida:
                    if etiqueta == "h1":
                        tk.Label(prev, text=texto, font=("Segoe UI", 18, "bold"), bg="white", fg="#111827").pack(anchor="w", padx=10, pady=(8, 2))
                    elif etiqueta == "h2":
                        tk.Label(prev, text=texto, font=("Segoe UI", 14, "bold"), bg="white", fg="#111827").pack(anchor="w", padx=10, pady=(6, 2))
                    elif etiqueta == "button":
                        tk.Button(prev, text=texto, font=("Segoe UI", 10, "bold"), bg="#3B82F6", fg="white", bd=0, padx=10, pady=4).pack(anchor="w", padx=10, pady=4)
                    elif etiqueta == "a":
                        tk.Label(prev, text=texto, font=("Segoe UI", 11, "underline"), bg="white", fg="#2563EB").pack(anchor="w", padx=10, pady=2)
                    else:  # p y demás
                        tk.Label(prev, text=texto, font=("Segoe UI", 11), bg="white", fg="#374151", wraplength=560, justify="left").pack(anchor="w", padx=10, pady=2)
                tk.Label(prev, text="", bg="white").pack(pady=1)
            else:
                tk.Label(salida_frame, text=str(salida), font=("Consolas", 12, "bold"),
                         bg=self.bg_color, fg="#059669", justify="left").pack(anchor="w", pady=4)

        tk.Button(cuerpo, text="▶️ Ejecutar", font=("Segoe UI", 10, "bold"), bg=self.secondary_color, fg="white",
                  bd=0, padx=14, pady=6, cursor="hand2", command=render_salida).pack(pady=4)

        tk.Label(cuerpo, text=actividad["pregunta"], font=("Segoe UI", 11, "bold"), bg=self.bg_color,
                 fg="#1F2937", wraplength=600, justify="center").pack(pady=(10, 4), padx=20)
        frame_op = tk.Frame(cuerpo, bg=self.bg_color)
        frame_op.pack(pady=4)
        lbl_pista = tk.Label(cuerpo, text="", font=("Segoe UI", 10, "italic"), bg=self.bg_color,
                             fg="#B45309", wraplength=600, justify="center")
        lbl_pista.pack(pady=4)

        opciones_baraj, correcta = self._opciones_barajadas(actividad["opciones"], actividad["correcta"])
        pista = actividad.get("pista", "Ejecuta el código y observa el resultado.")

        def responder(idx):
            if idx == correcta:
                win.destroy()
                self.otorgar_puntos_actividad(actividad["id"], actividad["puntos"], parent_win)
                on_close_callback()
            else:
                lbl_pista.config(text="❌ Aún no. 💡 Pista: " + pista)

        for i, op in enumerate(opciones_baraj):
            tk.Button(frame_op, text=op, font=("Segoe UI", 10, "bold"), bg="white", fg="#1F2937", bd=1, relief="solid",
                      width=42, pady=6, cursor="hand2", command=lambda idx=i: responder(idx)).pack(pady=3)

    # --- Evaluación final de módulo (~10 preguntas, 70% para aprobar, +15/+20/+25 pts) ---
    def iniciar_evaluacion(self, modulo_id, parent_win, on_close_callback, estado_eval_lbl):
        grado = self.grado_actual[0]
        modulos, prefijo, _total = datos_grado(grado)
        puntos_eval = PUNTOS_EVAL_GRADO.get(grado, 15)
        m = modulos[modulo_id]
        preguntas = m["evaluacion"][:]

        win = tk.Toplevel(parent_win)
        win.title("Evaluación – Módulo {}".format(modulo_id))
        win.geometry("560x400")
        win.configure(bg=self.bg_color)
        win.grab_set()

        estado = {"idx": 0, "aciertos": 0, "respuestas": []}

        tk.Label(win, text="📝 Evaluación – {}".format(m["titulo"]), font=("Segoe UI", 13, "bold"),
                  bg=self.bg_color, fg=self.primary_color).pack(pady=15)
        lbl_pregunta = tk.Label(win, text="", font=("Segoe UI", 11), bg=self.bg_color, fg="#1F2937",
                                  wraplength=480, justify="left")
        lbl_pregunta.pack(pady=10, padx=20)
        frame_op = tk.Frame(win, bg=self.bg_color)
        frame_op.pack(pady=10)

        def mostrar():
            for w in frame_op.winfo_children():
                w.destroy()
            p = preguntas[estado["idx"]]
            lbl_pregunta.config(text="Pregunta {}/{}: {}".format(estado["idx"] + 1, len(preguntas), p["pregunta"]))
            ops, correcta = self._opciones_barajadas(p["opciones"], p["correcta"])
            estado["ops_actual"] = ops
            estado["correcta_actual"] = correcta
            for i, op in enumerate(ops):
                tk.Button(frame_op, text=op, font=("Segoe UI", 10, "bold"), bg="white", bd=1, relief="solid",
                           width=34, pady=8, command=lambda idx=i: responder(idx)).pack(pady=4)

        def responder(idx):
            p = preguntas[estado["idx"]]
            estado["respuestas"].append({"pregunta": p["pregunta"], "opciones": estado["ops_actual"],
                                          "elegida": idx, "correcta": estado["correcta_actual"]})
            if idx == estado["correcta_actual"]:
                estado["aciertos"] += 1
            estado["idx"] += 1
            if estado["idx"] < len(preguntas):
                mostrar()
            else:
                terminar()

        def terminar():
            win.destroy()
            porcentaje = round((estado["aciertos"] / len(preguntas)) * 100)
            aprobado = porcentaje >= 70
            est_id = self.estudiante_actual[0]
            registrar_intento_evaluacion(est_id, modulo_id, porcentaje, aprobado, modulos)
            if aprobado:
                self.otorgar_puntos_actividad("{}m{}_evaluacion".format(prefijo, modulo_id), puntos_eval, parent_win)
                estado_eval_lbl.config(text="✅ Evaluación ya aprobada", fg="#059669")
            on_close_callback()
            self._resultado_evaluacion(parent_win, porcentaje, aprobado, puntos_eval, estado["respuestas"])

        mostrar()

    def _resultado_evaluacion(self, parent_win, porcentaje, aprobado, puntos_eval, respuestas):
        """Pantalla de resultado con el porcentaje y opción de ver las respuestas correctas."""
        win = tk.Toplevel(parent_win)
        win.title("Resultado de la evaluación")
        win.geometry("520x440")
        win.configure(bg=self.bg_color)
        win.grab_set()
        color = "#059669" if aprobado else "#B45309"
        tk.Label(win, text="🎉 ¡Evaluación aprobada!" if aprobado else "📚 Sigue practicando",
                 font=(self.font_family, 18, "bold"), bg=self.bg_color, fg=color).pack(pady=(24, 4))

        c = tk.Canvas(win, width=150, height=150, bg=self.bg_color, highlightthickness=0)
        c.pack(pady=6)
        c.create_oval(15, 15, 135, 135, outline="#E5E7EB", width=12)
        if porcentaje > 0:
            c.create_arc(15, 15, 135, 135, start=90, extent=-round(360 * porcentaje / 100.0),
                         style="arc", outline=color, width=12)
        c.create_text(75, 68, text="{}%".format(porcentaje), font=(self.font_family, 26, "bold"), fill=color)
        c.create_text(75, 96, text="de aciertos", font=(self.font_family, 9), fill="#6B7280")

        aciertos = sum(1 for r in respuestas if r["elegida"] == r["correcta"])
        tk.Label(win, text="Acertaste {} de {} preguntas".format(aciertos, len(respuestas)),
                 font=(self.font_family, 11), bg=self.bg_color, fg="#374151").pack(pady=(4, 0))
        if aprobado:
            tk.Label(win, text="¡Recibes +{} puntos! 🎁".format(puntos_eval), font=(self.font_family, 10, "bold"),
                     bg=self.bg_color, fg="#059669").pack(pady=2)
        else:
            tk.Label(win, text="Necesitas al menos 70% para aprobar. ¡Puedes reintentar!",
                     font=(self.font_family, 9), bg=self.bg_color, fg="#B45309").pack(pady=2)

        botones = tk.Frame(win, bg=self.bg_color)
        botones.pack(pady=18)
        tk.Button(botones, text="📋 Ver respuestas correctas", font=(self.font_family, 10, "bold"),
                  bg=self.primary_color, fg="white", bd=0, padx=14, pady=8, cursor="hand2",
                  command=lambda: self._revisar_respuestas(win, respuestas)).pack(side="left", padx=6)
        tk.Button(botones, text="Cerrar", font=(self.font_family, 10, "bold"), bg="#9CA3AF", fg="white",
                  bd=0, padx=16, pady=8, cursor="hand2", command=win.destroy).pack(side="left", padx=6)

    def _revisar_respuestas(self, parent, respuestas):
        """Lista cada pregunta con la respuesta del estudiante y la respuesta correcta."""
        win = tk.Toplevel(parent)
        win.title("Respuestas correctas")
        win.geometry("660x600")
        win.configure(bg=self.bg_color)
        win.grab_set()
        tk.Label(win, text="📋 Revisión de respuestas", font=(self.font_family, 14, "bold"),
                 bg=self.bg_color, fg=self.primary_color).pack(pady=(14, 8))

        cv = tk.Canvas(win, bg=self.bg_color, highlightthickness=0)
        sb = ttk.Scrollbar(win, orient="vertical", command=cv.yview)
        fr = tk.Frame(cv, bg=self.bg_color)
        fr.bind("<Configure>", lambda e: cv.configure(scrollregion=cv.bbox("all")))
        vid = cv.create_window((0, 0), window=fr, anchor="nw")
        cv.bind("<Configure>", lambda e: cv.itemconfigure(vid, width=e.width))
        cv.configure(yscrollcommand=sb.set)
        cv.pack(side="left", fill="both", expand=True, padx=(12, 0))
        sb.pack(side="right", fill="y")

        for i, r in enumerate(respuestas):
            ok = r["elegida"] == r["correcta"]
            card = tk.Frame(fr, bg="white", highlightthickness=1, highlightbackground="#E5E7EB")
            card.pack(fill="x", padx=12, pady=6)
            tk.Frame(card, bg="#10B981" if ok else "#EF4444", width=6).pack(side="left", fill="y")
            cont = tk.Frame(card, bg="white")
            cont.pack(side="left", fill="both", expand=True, padx=10, pady=8)
            tk.Label(cont, text="{} {}. {}".format("✅" if ok else "❌", i + 1, r["pregunta"]),
                     font=(self.font_family, 10, "bold"), bg="white", fg="#1F2937",
                     anchor="w", justify="left", wraplength=540).pack(fill="x")
            if not ok:
                elegida = r["opciones"][r["elegida"]] if 0 <= r["elegida"] < len(r["opciones"]) else "—"
                tk.Label(cont, text="Tu respuesta: " + elegida, font=(self.font_family, 9),
                         bg="white", fg="#DC2626", anchor="w", justify="left", wraplength=540).pack(fill="x", pady=(3, 0))
            tk.Label(cont, text="✔ Correcta: " + r["opciones"][r["correcta"]], font=(self.font_family, 9, "bold"),
                     bg="white", fg="#059669", anchor="w", justify="left", wraplength=540).pack(fill="x", pady=(2, 0))

        tk.Button(win, text="Cerrar", font=(self.font_family, 10, "bold"), bg="#9CA3AF", fg="white",
                  bd=0, padx=16, pady=8, cursor="hand2", command=win.destroy).pack(pady=10)

    def ventana_perfil_primero(self):
        est_id, nombre, grado, puntos = self.estudiante_actual
        self.refrescar_estudiante_actual()
        est_id, nombre, grado, puntos = self.estudiante_actual

        win = tk.Toplevel(self.root)
        win.title("Perfil del Estudiante")
        win.geometry("500x680")
        win.configure(bg=self.bg_color)
        win.grab_set()

        tk.Label(win, text="👤 " + nombre, font=("Segoe UI", 16, "bold"), bg=self.bg_color, fg=self.primary_color).pack(pady=(20, 2))
        tk.Label(win, text=self.grado_actual[1], font=("Segoe UI", 11), bg=self.bg_color, fg="#4B5563").pack()

        modulos, prefijo, total = datos_grado(grado)
        modulos_desbloqueados = sum(1 for m_id in range(1, total + 1) if modulo_esta_desbloqueado(m_id, puntos, modulos))
        modulos_completos = sum(1 for m_id in range(1, total + 1) if modulo_esta_desbloqueado(m_id, puntos, modulos) and modulo_esta_completo(est_id, m_id, modulos, prefijo))
        total_actividades = contar_actividades_completadas(est_id)
        juegos_completados = contar_actividades_completadas(est_id, prefijo_modulo="{}m12_".format(prefijo))

        conexion = sqlite3.connect("encarta_educativa.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM progreso WHERE estudiante_id=? AND tema LIKE 'Evaluación%'", (est_id,))
        evaluaciones_realizadas = cursor.fetchone()[0]
        conexion.close()

        xp = obtener_xp_estudiante(est_id)
        nivel = calcular_nivel(xp)
        prog_nivel = xp_en_nivel(xp)
        racha, mejor_racha = obtener_racha(est_id)

        # Tarjeta de Nivel con barra de progreso de XP
        nivel_frame = tk.Frame(win, bg=self.primary_color)
        nivel_frame.pack(fill="x", padx=25, pady=(12, 4))
        tk.Label(nivel_frame, text="⭐ Nivel {}".format(nivel), font=("Segoe UI", 14, "bold"),
                  bg=self.primary_color, fg="white").pack(side="left", padx=12, pady=8)
        tk.Label(nivel_frame, text="{} / {} XP".format(prog_nivel, XP_POR_NIVEL), font=("Segoe UI", 10, "bold"),
                  bg=self.primary_color, fg="#DBEAFE").pack(side="right", padx=12)
        canvas_xp = tk.Canvas(win, height=14, bg=self.bg_color, highlightthickness=0)
        canvas_xp.pack(fill="x", padx=25)
        canvas_xp.after(20, lambda: self._dibujar_barra(canvas_xp, prog_nivel / XP_POR_NIVEL))

        stats_frame = tk.Frame(win, bg="white", bd=1, relief="solid")
        stats_frame.pack(fill="x", padx=25, pady=15)
        stats = [
            ("✨ XP total", str(xp)),
            ("🔥 Racha actual", "{} días".format(racha)),
            ("🏅 Mejor racha", "{} días".format(mejor_racha)),
            ("🏆 Puntos acumulados", str(puntos)),
            ("📚 Módulos desbloqueados", "{} / {}".format(modulos_desbloqueados, total)),
            ("🎯 Módulos completados", "{} / {}".format(modulos_completos, total)),
            ("🧩 Actividades completadas", str(total_actividades)),
            ("🎮 Retos finales completados", str(juegos_completados)),
            ("📝 Evaluaciones realizadas", str(evaluaciones_realizadas)),
        ]
        for etiqueta, valor in stats:
            fila = tk.Frame(stats_frame, bg="white")
            fila.pack(fill="x", padx=15, pady=6)
            tk.Label(fila, text=etiqueta, font=("Segoe UI", 10), bg="white", fg="#374151").pack(side="left")
            tk.Label(fila, text=valor, font=("Segoe UI", 10, "bold"), bg="white", fg=self.primary_color).pack(side="right")

        tk.Label(win, text="🏅 Insignias obtenidas", font=("Segoe UI", 12, "bold"), bg=self.bg_color,
                  fg=self.primary_color).pack(pady=(15, 5))
        insignias = obtener_insignias_estudiante(est_id)
        insignias_frame = tk.Frame(win, bg=self.bg_color)
        insignias_frame.pack(fill="x", padx=25)
        if insignias:
            for clave in insignias:
                info = INSIGNIAS_INFO.get(clave)
                if info:
                    tk.Label(insignias_frame, text="{} — {}".format(info["nombre"], info["desc"]),
                              font=("Segoe UI", 9), bg=self.bg_color, fg="#1F2937", anchor="w").pack(fill="x", pady=2)
        else:
            tk.Label(insignias_frame, text="Aún no tienes insignias. ¡Sigue aprendiendo!", font=("Segoe UI", 9, "italic"),
                      bg=self.bg_color, fg="#6B7280").pack(pady=5)

        tk.Button(win, text="Cerrar", font=("Segoe UI", 10, "bold"), bg="#4B5563", fg="white", bd=0,
                   padx=15, pady=8, command=win.destroy).pack(pady=20)

    def abrir_seccion(self, seccion):
        top = tk.Toplevel(self.root)
        top.title(seccion + " - " + self.grado_actual[1])
        top.geometry("700x500")
        top.configure(bg=self.bg_color)
        
        tk.Label(top, text="Sección: " + seccion, font=("Segoe UI", 16, "bold"), bg=self.bg_color, fg=self.primary_color).pack(pady=20)
        
        grado_num = self.grado_actual[0]
        texto_contenido = "Contenido educativo interactivo correspondiente a " + self.grado_actual[1] + " para la sección de " + seccion + ".\n\n"
        
        if grado_num == 1:
            texto_contenido += "• Nivel 1: Conceptos básicos de hardware, uso del mouse y teclado."
        elif grado_num == 2:
            texto_contenido += "• Nivel 2: Sistemas operativos, organización de carpetas y procesadores de texto."
        else:
            texto_contenido += "• Nivel 3: Algoritmos, diagramas de flujo y bases de la programación."
            
        lbl_cont = tk.Label(top, text=texto_contenido, font=("Segoe UI", 11), bg="white", fg="#374151", justify="left", bd=1, relief="solid", padx=20, pady=20)
        lbl_cont.pack(fill="both", expand=True, padx=30, pady=10)
        
        def completar_actividad():
            est_id = self.estudiante_actual[0]
            nuevos_puntos = self.estudiante_actual[3] + 10
            
            conexion = sqlite3.connect("encarta_educativa.db")
            cursor = conexion.cursor()
            cursor.execute("UPDATE estudiantes SET puntos = ? WHERE id = ?", (nuevos_puntos, est_id))
            conexion.commit()
            conexion.close()
            
            self.estudiante_actual = (est_id, self.estudiante_actual[1], self.estudiante_actual[2], nuevos_puntos)
            messagebox.showinfo("¡Excelente!", "¡Actividad completada con éxito! Has ganado 10 puntos 🌟", parent=top)
            top.destroy()
            self.mostrar_menu_principal()

        tk.Button(top, text="✨ Completar Actividad y Ganar Puntos", font=("Segoe UI", 11, "bold"), bg=self.secondary_color, fg="white", bd=0, padx=15, pady=10, command=completar_actividad).pack(pady=20)

    def _crear_password_docente(self):
        """Primer uso: el docente define su contraseña (se guarda solo como hash con sal)."""
        messagebox.showinfo("Primer acceso docente",
                            "Aún no hay contraseña de docente. Crea una ahora "
                            "(mínimo {} caracteres).".format(seguridad.MIN_LARGO_PASSWORD))
        while True:
            nueva = simpledialog.askstring("Crear contraseña", "Nueva contraseña del docente:", show="*")
            if nueva is None:
                return False
            ok, msg = seguridad.validar_password_nueva(nueva)
            if not ok:
                messagebox.showwarning("Contraseña débil", msg)
                continue
            confirmar = simpledialog.askstring("Crear contraseña", "Repite la contraseña:", show="*")
            if confirmar is None:
                return False
            if confirmar != nueva:
                messagebox.showwarning("No coinciden", "Las contraseñas no coinciden. Intenta de nuevo.")
                continue
            seguridad.guardar_password_docente(nueva)
            seguridad.registrar_evento("DOCENTE_PASSWORD_CREADA")
            return True

    def abrir_panel_docente(self):
        almacenado = seguridad.obtener_hash_docente()
        if almacenado is None:
            if self._crear_password_docente():
                self.limite_docente.registrar_exito()
                seguridad.registrar_evento("DOCENTE_LOGIN_OK", "tras crear contraseña")
                self.mostrar_ventana_docente()
            return
        if self.limite_docente.bloqueado():
            messagebox.showwarning("Acceso bloqueado", "Demasiados intentos. Espera {} segundos.".format(
                self.limite_docente.segundos_restantes()))
            seguridad.registrar_evento("DOCENTE_LOGIN_BLOQUEADO", "intento durante bloqueo", logging.WARNING)
            return
        password = simpledialog.askstring("Acceso Docente", "Ingrese la contraseña del docente:", show="*")
        if password is None:
            return
        if seguridad.verificar_password(password, almacenado):
            self.limite_docente.registrar_exito()
            seguridad.registrar_evento("DOCENTE_LOGIN_OK")
            self.mostrar_ventana_docente()
        else:
            bloqueo = self.limite_docente.registrar_fallo()
            seguridad.registrar_evento("DOCENTE_LOGIN_FALLIDO", "contraseña incorrecta", logging.WARNING)
            if bloqueo:
                seguridad.registrar_evento("DOCENTE_LOGIN_BLOQUEO_ACTIVADO",
                                           "{} intentos fallidos; {} s".format(seguridad.MAX_INTENTOS,
                                                                              seguridad.SEGUNDOS_BLOQUEO),
                                           logging.ERROR)
                messagebox.showerror("Acceso bloqueado", "Demasiados intentos. Espera {} segundos.".format(
                    seguridad.SEGUNDOS_BLOQUEO))
            else:
                messagebox.showerror("Error", "Contraseña incorrecta.")

    def mostrar_ventana_docente(self):
        """Toda la implementación del Panel del Docente vive en panel_docente.py
        (gestión de estudiantes, progreso, reportes PDF y cambio de contraseña),
        para no mezclar esa funcionalidad con las pantallas del estudiante."""
        panel_docente.abrir(self)

def _manejar_error_inesperado(tipo, valor, tb):
    """Detalle técnico solo al log; al usuario, un mensaje genérico (sin trazas ni SQL)."""
    detalle = "".join(traceback.format_exception(tipo, valor, tb))
    seguridad._obtener_logger().error("ERROR_INESPERADO | %s", detalle.replace("\n", " | "))
    try:
        messagebox.showerror("Ocurrió un problema",
                             "Algo salió mal. Tu progreso guardado está a salvo.\n"
                             "Si el problema continúa, avisa a tu docente.\n\n"
                             "Código: {}".format(tipo.__name__))
    except tk.TclError:
        pass


if __name__ == "__main__":
    root = tk.Tk()
    root.report_callback_exception = _manejar_error_inesperado
    app = EncartaEducativaApp(root)
    root.mainloop()