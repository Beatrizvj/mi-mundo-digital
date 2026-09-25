# -*- coding: utf-8 -*-
"""
Curso de Mecanografía (estilo MecaNet) para MI MUNDO DIGITAL.
Solo datos: distribución del teclado, colores por dedo y lecciones progresivas.
El motor (teclado en pantalla, PPM, precisión, guardado) vive en app.py.
"""

# Distribución del teclado en pantalla (mayúsculas para comparar sin importar el caso)
FILAS_TECLADO = [
    list("1234567890"),
    list("QWERTYUIOP"),
    list("ASDFGHJKLÑ"),
    list("ZXCVBNM"),
]


def _map_dedos():
    m = {}
    grupos = [
        ("1QAZ", "#F87171"),      # meñique izquierdo
        ("2WSX", "#FB923C"),      # anular izquierdo
        ("3EDC", "#FBBF24"),      # medio izquierdo
        ("45RTFGVB", "#34D399"),  # índice izquierdo
        ("67YUHJNM", "#22D3EE"),  # índice derecho
        ("8IK", "#60A5FA"),       # medio derecho
        ("9OL", "#A78BFA"),       # anular derecho
        ("0PÑ", "#F472B6"),       # meñique derecho
    ]
    for teclas, color in grupos:
        for t in teclas:
            m[t] = color
    return m


DEDO_COLOR = _map_dedos()

# Lecciones progresivas: de la fila guía a textos completos.
LECCIONES_MECANOGRAFIA = [
    {"titulo": "Fila guía · ASDF JKLÑ", "desc": "Aquí descansan tus dedos. No mires el teclado.",
     "texto": "asdf jklñ asdf jklñ fdsa ñlkj asdf jklñ ffjj ddkk"},
    {"titulo": "Fila guía + G H", "desc": "Estira los dedos índices hacia G y H.",
     "texto": "asdfg hjklñ gfds jhkl asdfg hjklñ ghgh fghj"},
    {"titulo": "Fila superior · QWERTY", "desc": "Sube desde la fila guía a la fila de arriba.",
     "texto": "qwert yuiop qwer tyui rueda pieza quito poeta"},
    {"titulo": "Fila inferior · ZXCVBNM", "desc": "Baja desde la fila guía a la fila de abajo.",
     "texto": "zxcvb nm zxcv bnm nave cebo mono vaca canbio"},
    {"titulo": "Palabras sencillas", "desc": "Ahora junta todas las letras en palabras.",
     "texto": "casa sol mesa gato luna pato dedo rana vela foca nube"},
    {"titulo": "Mayúsculas y punto", "desc": "Usa Shift para la mayúscula y el punto final.",
     "texto": "El gato duerme. La casa es azul. Ana lee un libro."},
    {"titulo": "Números", "desc": "Practica la fila de números de arriba.",
     "texto": "1 2 3 4 5 6 7 8 9 0 10 25 100 2024 55 80"},
    {"titulo": "Frases", "desc": "Escribe frases completas sin ver el teclado.",
     "texto": "me gusta aprender a escribir rapido y sin ver el teclado"},
    {"titulo": "Texto final", "desc": "¡El gran reto de mecanografía!",
     "texto": "la mecanografia me ayuda a usar la computadora de forma rapida y correcta"},
]
