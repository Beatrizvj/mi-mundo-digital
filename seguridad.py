"""Controles de seguridad de Mi Mundo Digital (solo biblioteca estándar).

- Contraseña del docente con PBKDF2-HMAC-SHA256 + sal aleatoria (nunca en texto plano).
- Bloqueo temporal tras varios intentos fallidos.
- Bitácora de eventos de seguridad en archivo (seguridad.log) con rotación.
- Validación de nombres de estudiante.
"""
import hashlib
import hmac
import logging
import os
import re
import secrets
import sqlite3
import time
from logging.handlers import RotatingFileHandler

DB_PATH = "encarta_educativa.db"
LOG_PATH = "seguridad.log"

ITERACIONES = 310_000          # recomendación OWASP para PBKDF2-HMAC-SHA256
ALGORITMO = "pbkdf2_sha256"
MIN_LARGO_PASSWORD = 8
MAX_INTENTOS = 3
SEGUNDOS_BLOQUEO = 30

_NOMBRE_RE = re.compile(r"^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ][A-Za-zÁÉÍÓÚÜÑáéíóúüñ '.\-]*$")

_logger = None


def _obtener_logger():
    global _logger
    if _logger is None:
        _logger = logging.getLogger("encarta.seguridad")
        _logger.setLevel(logging.INFO)
        if not _logger.handlers:
            try:
                h = RotatingFileHandler(LOG_PATH, maxBytes=512_000, backupCount=3, encoding="utf-8")
                h.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s",
                                                 "%Y-%m-%dT%H:%M:%S"))
                _logger.addHandler(h)
            except OSError:
                _logger.addHandler(logging.NullHandler())
    return _logger


def _limpiar(texto):
    """Evita inyección de líneas en el log: quita saltos de línea/control y recorta."""
    return re.sub(r"[\x00-\x1f\x7f]", " ", str(texto))[:200]


def registrar_evento(evento, detalle="", nivel=logging.INFO):
    """Escribe una línea en la bitácora. Nunca pasar contraseñas como detalle."""
    _obtener_logger().log(nivel, "%s | %s | usuario=%s", _limpiar(evento), _limpiar(detalle),
                          _limpiar(os.environ.get("USERNAME", "desconocido")))


# ---------------------------------------------------------------- contraseñas ----

def hashear_password(password, sal=None, iteraciones=ITERACIONES):
    """Devuelve 'pbkdf2_sha256$iteraciones$sal_hex$hash_hex'."""
    sal = sal if sal is not None else secrets.token_bytes(16)
    derivada = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), sal, iteraciones)
    return "{}${}${}${}".format(ALGORITMO, iteraciones, sal.hex(), derivada.hex())


def verificar_password(password, almacenado):
    try:
        algoritmo, iters, sal_hex, hash_hex = almacenado.split("$")
        if algoritmo != ALGORITMO:
            return False
        derivada = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"),
                                       bytes.fromhex(sal_hex), int(iters))
        return hmac.compare_digest(derivada.hex(), hash_hex)
    except (ValueError, AttributeError):
        return False


def validar_password_nueva(password):
    """Devuelve (ok, mensaje)."""
    if password is None or len(password) < MIN_LARGO_PASSWORD:
        return False, "La contraseña debe tener al menos {} caracteres.".format(MIN_LARGO_PASSWORD)
    if password.strip() != password or password.isdigit():
        return False, "No uses espacios al inicio/fin ni solo números."
    return True, ""


# ------------------------------------------------------------ almacenamiento ----

def inicializar_seguridad(db=None):
    conexion = sqlite3.connect(db or DB_PATH)
    try:
        conexion.execute("CREATE TABLE IF NOT EXISTS configuracion (clave TEXT PRIMARY KEY, valor TEXT NOT NULL)")
        conexion.commit()
    finally:
        conexion.close()


def obtener_hash_docente(db=None):
    conexion = sqlite3.connect(db or DB_PATH)
    try:
        fila = conexion.execute("SELECT valor FROM configuracion WHERE clave='docente_hash'").fetchone()
        return fila[0] if fila else None
    finally:
        conexion.close()


def guardar_password_docente(password, db=None):
    conexion = sqlite3.connect(db or DB_PATH)
    try:
        conexion.execute("INSERT OR REPLACE INTO configuracion (clave, valor) VALUES ('docente_hash', ?)",
                         (hashear_password(password),))
        conexion.commit()
    finally:
        conexion.close()


# ------------------------------------------------------------------- bloqueo ----

class LimiteIntentos:
    """Bloquea temporalmente tras MAX_INTENTOS fallos seguidos (en memoria)."""

    def __init__(self, max_intentos=MAX_INTENTOS, segundos=SEGUNDOS_BLOQUEO, reloj=time.monotonic):
        self.max_intentos = max_intentos
        self.segundos = segundos
        self._reloj = reloj
        self.fallos = 0
        self._bloqueado_hasta = 0.0

    def segundos_restantes(self):
        return max(0, int(self._bloqueado_hasta - self._reloj() + 0.999))

    def bloqueado(self):
        return self.segundos_restantes() > 0

    def registrar_fallo(self):
        """Devuelve True si este fallo dispara el bloqueo."""
        self.fallos += 1
        if self.fallos >= self.max_intentos:
            self._bloqueado_hasta = self._reloj() + self.segundos
            self.fallos = 0
            return True
        return False

    def registrar_exito(self):
        self.fallos = 0
        self._bloqueado_hasta = 0.0


# ---------------------------------------------------------------- validación ----

def validar_nombre(nombre):
    """Devuelve (ok, valor_limpio_o_mensaje)."""
    if nombre is None:
        return False, "Escribe tu nombre."
    limpio = " ".join(nombre.split())
    if len(limpio) < 2:
        return False, "El nombre es demasiado corto."
    if len(limpio) > 60:
        return False, "El nombre es demasiado largo (máximo 60 caracteres)."
    if not _NOMBRE_RE.match(limpio):
        return False, "Usa solo letras, espacios, punto, apóstrofe o guion."
    return True, limpio
