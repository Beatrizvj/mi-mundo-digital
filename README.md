# MI MUNDO DIGITAL

Aplicación de escritorio **educativa e interactiva** desarrollada en Python (Tkinter + SQLite),
pensada como una mezcla de **enciclopedia educativa + videojuego de aprendizaje** para
estudiantes de educación básica. Funciona **100 % sin internet**, ideal para entornos
educativos rurales o con recursos tecnológicos limitados.

> Proyecto de Seminario. **Los 3 grados (Primero, Segundo y Tercero Básico)** están completos,
> con 12 módulos cada uno, **más un Curso de Mecanografía** (estilo MecaNet) para todos.

---

## ✨ Características (Primero Básico)

- **12 módulos** con contenido teórico y muchas actividades interactivas.
- **Tipos de actividad** (no solo leer y responder):
  - 🔎 Exploración interactiva (habitación / escritorio virtual)
  - 🖱️ Arrastrar y soltar
  - ⌨️ Juegos de teclado (carrera, encuentra la tecla, reto de velocidad — con medición de PPM y precisión)
  - 🤖 Programación por bloques (lleva el robot al tesoro)
  - 🎯 Atrapa el objeto (puntería con el mouse, con niveles fácil/medio/difícil)
  - 🧩 Clasificar, relacionar, ordenar, memorama, patrones, laberintos y problemas
- **Progreso y evaluaciones:** puntos, desbloqueo de módulos por umbrales, evaluación final por módulo (70 % para aprobar).
- **Gamificación:** ⭐ XP y niveles, 🔥 rachas diarias, 🎯 reto del día (XP de bono) e 🏅 insignias.
- **🏆 Gran Reto Final** que encadena un reto de cada tema, con pantalla de victoria animada.
- **👩‍🏫 Panel del Docente** para ver el avance de los estudiantes y reiniciar progreso.

## ⌨️ Curso de Mecanografía (estilo MecaNet)

Acceso aparte (fuera de los 3 grados), en la pantalla de inicio. **9 lecciones progresivas**
(fila guía → todas las filas → números → frases → texto final) con **teclado en pantalla que
resalta la siguiente tecla y colorea cada dedo**, medición en vivo de **PPM y precisión**,
desbloqueo por lección (≥70 % de precisión) y **guardado del mejor resultado** por practicante.

## 🧩 Módulos de Primero Básico

1. 🌐 Conociendo el mundo digital
2. 🖥️ Conociendo y utilizando la computadora
3. ⌨️ Teclado y habilidades digitales
4. 📁 Archivos, carpetas y organización digital
5. 🌍 Internet y mundo digital
6. 🛡️ Seguridad digital
7. 🧠 Pensamiento lógico
8. 🧩 Resolución de problemas
9. 🔢 Pensamiento computacional
10. 🧑‍💻 Introducción a la programación
11. 🤖 Inteligencia artificial y tecnologías actuales
12. 🏆 Gran reto final

## 🧩 Módulos de Segundo Básico

Mayor dificultad: el estudiante **comprende, analiza, aplica, resuelve y crea**. Incluye un
tipo de actividad nuevo — **Retos con niveles 🟢🟡🔴 y pistas** (no revela la respuesta) — y 9
insignias propias.

1. 🧠 Hardware y software avanzado
2. 🖥️ Sistemas operativos y administración
3. 📊 Productividad digital (texto, hojas de cálculo, presentaciones)
4. 🌐 Redes de computadoras
5. 🔗 Internet y comunicación digital
6. 🔐 Seguridad informática
7. 🧩 Pensamiento lógico y resolución de problemas
8. 🔀 Algoritmos y diagramas de flujo
9. 🧑‍💻 Introducción a la programación
10. 🗃️ Datos y bases de datos
11. 🤖 Inteligencia artificial y tecnologías emergentes
12. 🏆 Proyecto y Gran Reto de Segundo Básico

## 🧩 Módulos de Tercero Básico

El nivel más avanzado: **introducción práctica al mundo de la informática**. Incluye un motor
nuevo — **Laboratorio de código** (escribe/observa código, ▶️ ejecútalo y ve el resultado como
texto, **tabla SQL** o **vista previa web**) — niveles 🟢 Comprender / 🟡 Aplicar / 🔴 Crear, y 11
insignias propias.

1. 🖥️ Arquitectura y funcionamiento de computadoras
2. ⚙️ Sistemas operativos y administración
3. 🧠 Algoritmos y resolución avanzada de problemas
4. 👨‍💻 Programación (con laboratorio de código y cazador de errores)
5. 🌐 Desarrollo web (HTML/CSS/JS con vista previa)
6. 🗄️ Bases de datos y SQL (consultas sobre tablas simuladas)
7. 📡 Redes de computadoras (simulador de IP)
8. 🔐 Ciberseguridad (análisis de incidentes)
9. 🤖 Inteligencia artificial y ciencia de datos
10. ☁️ Internet, nube y tecnologías modernas
11. 🌎 Ética y ciudadanía digital
12. 🏆 Proyecto final: crea tu solución tecnológica

---

## 🖥️ Requisitos

- **Con el ejecutable (`.exe`):** no requiere instalar nada. Solo Windows.
- **Con Python:** Python 3.8 o superior (Tkinter y SQLite ya vienen incluidos en la instalación estándar de Python).

## ▶️ Cómo ejecutar

### Opción A — Con el ejecutable (recomendado para demostrar)
1. Entra a la carpeta `dist/`.
2. Doble clic en **`EncartaEducativa.exe`**.
3. La base de datos se crea sola la primera vez, junto al ejecutable.

### Opción B — Con Python
> Importante: `app.py` y los archivos `contenido_*.py` (primero, segundo, tercero y mecanografía) deben estar **en la misma carpeta**.

```bash
python app.py
```

## 📁 Archivos del proyecto

| Archivo | Descripción |
|---|---|
| `app.py` | Motor de la aplicación: pantallas, puntos, niveles, evaluaciones, juegos y panel docente. |
| `contenido_primero.py` | Contenido de los 12 módulos de Primero. **Necesario junto a `app.py`.** |
| `contenido_segundo.py` | Contenido de los 12 módulos de Segundo. **Necesario junto a `app.py`.** |
| `contenido_tercero.py` | Contenido de los 12 módulos de Tercero. **Necesario junto a `app.py`.** |
| `contenido_mecanografia.py` | Lecciones y teclado del Curso de Mecanografía. **Necesario junto a `app.py`.** |
| `inicio_animado.py` | Presentación de la pantalla de inicio: título animado, subtítulo, astronauta y destellos (solo diseño). **Necesario junto a `app.py`.** |
| `astronauta_*.png`, `logo_ineb.png` | Imágenes de la pantalla de inicio (astronauta en 4 tamaños y logo del INEB). **Necesarias junto a `app.py`.** |
| `seguridad.py` | Controles de seguridad: hash de contraseña, bloqueo, bitácora y validación. **Necesario junto a `app.py`.** |
| `test_seguridad.py` | Pruebas automáticas de seguridad. |
| `encarta_educativa.db` | Base de datos SQLite (estudiantes, progreso, XP, rachas, mecanografía). **Se crea sola** si no existe. |
| `TEMARIO.md` | Temario completo de los 3 grados. |
| `dist/EncartaEducativa.exe` | Ejecutable para Windows (se genera al empaquetar). |

## 🔒 Seguridad

- **Contraseña del Panel del Docente:** ya no existe una contraseña por defecto. En el **primer acceso** al panel
  la app pide crear una (mínimo 8 caracteres). Se guarda solo como hash **PBKDF2-HMAC-SHA256 con sal aleatoria**
  (310 000 iteraciones) en la tabla `configuracion`; nunca en texto plano.
- **Bloqueo por intentos:** 3 contraseñas incorrectas seguidas bloquean el acceso 30 segundos.
- **Bitácora:** `seguridad.log` (junto a la base de datos, con rotación) registra acceso docente exitoso/fallido,
  bloqueos, creación de contraseña, reinicios de progreso, registro de estudiantes y errores inesperados.
  Nunca se escriben contraseñas.
- **Errores:** ante un fallo inesperado el usuario ve un mensaje genérico; el detalle técnico va solo al log.
- **Entrada validada:** los nombres de estudiante se limpian y validan (2–60 caracteres, solo letras y signos básicos).
- **SQL:** todas las consultas están parametrizadas.
- **Pruebas:** `python -m unittest test_seguridad -v`
- **¿Olvidaste la contraseña?** Cierra la app y ejecuta en la carpeta del proyecto:
  `python -c "import sqlite3;c=sqlite3.connect('encarta_educativa.db');c.execute(\"DELETE FROM configuracion WHERE clave='docente_hash'\");c.commit()"`
  y al abrir el panel se pedirá crear una nueva.

## 🔁 Reconstruir el ejecutable (opcional)

Si cambias el código y quieres regenerar el `.exe`:

```bash
pyinstaller --onefile --windowed --name "EncartaEducativa" app.py
```

El ejecutable queda en la carpeta `dist/`. Las carpetas `build/` y el archivo
`EncartaEducativa.spec` son temporales de PyInstaller y se pueden borrar.

---

## 📌 Estado del proyecto

- ✅ **Primero Básico:** completo (12 módulos, juegos, gamificación).
- ✅ **Segundo Básico:** completo (12 módulos, mayor dificultad, retos con pistas, 9 insignias).
- ✅ **Tercero Básico:** completo (12 módulos avanzados, laboratorios de código/SQL/web, 11 insignias).

**Los 3 grados de básico están terminados.** 🎉
