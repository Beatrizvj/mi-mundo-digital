"""Generador mínimo de PDF, sin dependencias externas (solo biblioteca estándar).

Pensado para los reportes del Panel del Docente de Mi Mundo Digital: texto con
Helvetica/Helvetica-Bold (codificación WinAnsi, cubre tildes y eñes), tablas
simples por columnas y salto de página automático.

No pretende ser un generador de PDF de propósito general: alcanza para reportes
de una sola fuente con texto y tablas, que es lo que necesita este proyecto.
"""
import datetime
import textwrap

ANCHO, ALTO = 612, 792      # tamaño carta (Letter) en puntos
MARGEN = 50
LINEA = 16                  # alto de línea por defecto


def _escapar(texto):
    """Escapa paréntesis y barras invertidas, que son especiales dentro de un PDF."""
    return str(texto).replace("\\", r"\\").replace("(", r"\(").replace(")", r"\)")


def _codificar(texto):
    """WinAnsiEncoding ~ cp1252: cubre á é í ó ú ñ Á É Í Ó Ú Ñ ¿ ¡ en una sola fuente."""
    return str(texto).encode("cp1252", errors="replace")


class PDFReporte:
    """Reporte PDF de una sola fuente, con texto y tablas simples."""

    def __init__(self):
        self._paginas = []
        self._ops = []
        self._y = ALTO - MARGEN

    # ------------------------------------------------------------- bajo nivel
    def _nueva_pagina(self):
        self._paginas.append(self._ops)
        self._ops = []
        self._y = ALTO - MARGEN

    def _asegurar_espacio(self, alto_necesario=LINEA):
        if self._y - alto_necesario < MARGEN:
            self._nueva_pagina()

    def _texto(self, x, texto, fuente="F1", tam=11):
        pre = "BT /{} {} Tf {:.2f} {:.2f} Td (".format(fuente, tam, x, self._y).encode("ascii")
        cuerpo = _codificar(_escapar(texto))
        post = b") Tj ET"
        self._ops.append(pre + cuerpo + post)

    def _linea_horizontal(self, x0, x1):
        self._ops.append("{:.2f} {:.2f} m {:.2f} {:.2f} l S".format(x0, self._y, x1, self._y).encode("ascii"))

    # ------------------------------------------------------------- alto nivel
    def titulo(self, texto):
        self._asegurar_espacio(28)
        self._texto(MARGEN, texto, "F2", 16)
        self._y -= 24

    def subtitulo(self, texto):
        self._asegurar_espacio(20)
        self._texto(MARGEN, texto, "F2", 12)
        self._y -= 18

    def parrafo(self, texto, tam=10.5):
        ancho_disponible = ANCHO - 2 * MARGEN
        caracteres_por_linea = max(20, int(ancho_disponible / (tam * 0.52)))
        for linea in textwrap.wrap(str(texto), caracteres_por_linea) or [""]:
            self._asegurar_espacio(LINEA)
            self._texto(MARGEN, linea, "F1", tam)
            self._y -= LINEA

    def espacio(self, alto=8):
        self._y -= alto

    def separador(self):
        self._asegurar_espacio(10)
        self._linea_horizontal(MARGEN, ANCHO - MARGEN)
        self._y -= 10

    def tabla(self, encabezados, filas, anchos=None):
        """Tabla simple: cada celda se trunca para no invadir la columna siguiente."""
        n = len(encabezados)
        if anchos is None:
            disponible = ANCHO - 2 * MARGEN
            anchos = [disponible / n] * n
        xs = [MARGEN]
        for w in anchos[:-1]:
            xs.append(xs[-1] + w)

        def _ajustar(celda, ancho_col, tam=9.5):
            maximo = max(3, int(ancho_col / (tam * 0.52)))
            texto = "" if celda is None else str(celda)
            return texto if len(texto) <= maximo else texto[: maximo - 1] + "…"

        self._asegurar_espacio(LINEA)
        for x, h, w in zip(xs, encabezados, anchos):
            self._texto(x, _ajustar(h, w), "F2", 9.5)
        self._y -= 4
        self.separador()

        for fila in filas:
            self._asegurar_espacio(LINEA)
            for x, celda, w in zip(xs, fila, anchos):
                self._texto(x, _ajustar(celda, w), "F1", 9.5)
            self._y -= LINEA

    def pie_fecha(self):
        self.separador()
        self.parrafo("Generado: {}".format(datetime.datetime.now().strftime("%d/%m/%Y %H:%M")))

    # --------------------------------------------------------------------- IO
    def guardar(self, ruta):
        self._paginas.append(self._ops)
        self._ops = []
        _escribir_pdf(self._paginas, ruta)


def _escribir_pdf(paginas, ruta):
    if not paginas:
        paginas = [[]]
    n = len(paginas)

    id_catalogo, id_pages, id_f1, id_f2 = 1, 2, 3, 4
    primer_pagina = 5
    primer_contenido = primer_pagina + n
    total_objetos = primer_contenido + n - 1

    cuerpos = {}
    cuerpos[id_catalogo] = "<< /Type /Catalog /Pages {} 0 R >>".format(id_pages).encode("ascii")

    hijos = " ".join("{} 0 R".format(primer_pagina + i) for i in range(n))
    cuerpos[id_pages] = "<< /Type /Pages /Kids [{}] /Count {} >>".format(hijos, n).encode("ascii")

    cuerpos[id_f1] = b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>"
    cuerpos[id_f2] = b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>"

    for i in range(n):
        id_pag = primer_pagina + i
        id_cont = primer_contenido + i
        cuerpos[id_pag] = (
            "<< /Type /Page /Parent {pages} 0 R /MediaBox [0 0 {w} {h}] "
            "/Resources << /Font << /F1 {f1} 0 R /F2 {f2} 0 R >> >> /Contents {c} 0 R >>"
        ).format(pages=id_pages, w=ANCHO, h=ALTO, f1=id_f1, f2=id_f2, c=id_cont).encode("ascii")

        datos = b"\n".join(paginas[i]) + (b"\n" if paginas[i] else b"")
        cuerpos[id_cont] = "<< /Length {} >>\nstream\n".format(len(datos)).encode("ascii") + datos + b"endstream"

    partes = [b"%PDF-1.4\n"]
    offsets = {}
    cursor = len(partes[0])
    for oid in range(1, total_objetos + 1):
        pieza = "{} 0 obj\n".format(oid).encode("ascii") + cuerpos[oid] + b"\nendobj\n"
        offsets[oid] = cursor
        partes.append(pieza)
        cursor += len(pieza)

    inicio_xref = cursor
    xref = ["xref", "0 {}".format(total_objetos + 1), "0000000000 65535 f "]
    for oid in range(1, total_objetos + 1):
        xref.append("{:010d} 00000 n ".format(offsets[oid]))
    xref_bytes = ("\n".join(xref) + "\n").encode("ascii")

    trailer = (
        "trailer\n<< /Size {} /Root {} 0 R >>\nstartxref\n{}\n%%EOF".format(
            total_objetos + 1, id_catalogo, inicio_xref
        )
    ).encode("ascii")

    with open(ruta, "wb") as f:
        f.write(b"".join(partes))
        f.write(xref_bytes)
        f.write(trailer)
