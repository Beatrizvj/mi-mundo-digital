# -*- coding: utf-8 -*-
"""
Contenido educativo de TERCERO BÁSICO — Mi Primera Encarta Educativa.

Solo datos. El motor (puntos, niveles, desbloqueos, evaluaciones, insignias) vive en app.py
y funciona con cualquier grado. Tercero es el nivel más avanzado: programación, algoritmos,
bases de datos (SQL), redes, ciberseguridad, desarrollo web, IA y proyectos.

Ids con prefijo "s3m..." para no chocar con Primero/Segundo. Umbrales: 0,50,100,...,500,600.

Tipo de actividad nuevo:
  "codigo" -> laboratorio: muestra código, "▶️ Ejecutar" revela el resultado (texto, tabla SQL
              o vista previa web) y hace una pregunta con pista.
También usa: seleccion, relacionar, ordenar, clasificar, problema, patron, reto, bloques,
arrastrar, gran_reto.

Niveles de dificultad: 🟢 Comprender · 🟡 Aplicar · 🔴 Crear.
"""

MODULOS_TERCERO = {
    # =================================================================================
    1: {
        "titulo": "Arquitectura y funcionamiento de computadoras",
        "icono": "🖥️",
        "umbral": 0,
        "contenido": [
            ("Arquitectura básica",
             "Una computadora recibe datos (entrada), los procesa y entrega resultados (salida). La CPU dirige "
             "todo; la memoria y el almacenamiento guardan la información; los buses conectan las partes."),
            ("El procesador y sus núcleos",
             "La CPU ejecuta las instrucciones. Sus NÚCLEOS permiten hacer varias tareas a la vez (más núcleos = "
             "más trabajo en paralelo). La memoria CACHÉ es una memoria muy rápida y pequeña dentro/junto a la CPU "
             "que guarda lo que se usa más seguido."),
            ("Memorias: RAM, ROM y almacenamiento",
             "• RAM: memoria de trabajo, rápida y volátil (se borra al apagar).\n"
             "• ROM: memoria solo de lectura, guarda instrucciones básicas.\n"
             "• HDD vs SSD: ambos guardan datos de forma permanente; el SSD es más rápido y sin partes móviles."),
            ("Otras piezas y el arranque",
             "• GPU: procesa gráficos y video.\n• Tarjeta madre: conecta todo.\n• Fuente: entrega energía.\n"
             "• BIOS/UEFI: programa que arranca la computadora y prepara el hardware antes del sistema operativo."),
            ("El software del sistema",
             "El sistema operativo administra los recursos; los drivers permiten usar cada pieza; los procesos son "
             "los programas en ejecución que consumen memoria y CPU."),
        ],
        "actividades": [
            {"id": "s3m1_a1", "tipo": "relacionar", "titulo": "Componente y su función", "puntos": 10, "categoria": "hardware",
             "pares": [("Ejecuta las instrucciones", "CPU"), ("Permiten tareas en paralelo", "Núcleos"),
                       ("Memoria muy rápida junto a la CPU", "Caché"), ("Procesa gráficos y video", "GPU"),
                       ("Arranca el hardware antes del SO", "BIOS/UEFI")]},
            {"id": "s3m1_a2", "tipo": "clasificar", "titulo": "¿Memoria volátil o permanente?", "puntos": 10, "categoria": "hardware",
             "categorias": ["Volátil (se borra al apagar)", "Permanente"],
             "items": [("RAM", "Volátil (se borra al apagar)"), ("SSD", "Permanente"), ("Caché", "Volátil (se borra al apagar)"),
                       ("HDD", "Permanente"), ("Memoria USB", "Permanente")]},
            {"id": "s3m1_a3", "tipo": "clasificar", "titulo": "🔬 Laboratorio: arma la PC para edición de video", "puntos": 15, "categoria": "hardware",
             "instruccion": "Clasifica qué componentes conviene priorizar para una PC de edición de video.",
             "categorias": ["Prioridad ALTA", "No es prioridad"],
             "items": [("GPU potente", "Prioridad ALTA"), ("Mucha RAM", "Prioridad ALTA"), ("SSD rápido", "Prioridad ALTA"),
                       ("Bocinas de lujo", "No es prioridad"), ("Teclado con luces", "No es prioridad")]},
            {"id": "s3m1_r1", "tipo": "reto", "nivel": "🟢 Comprender", "titulo": "Reto: ¿qué es la caché?", "puntos": 5, "categoria": "hardware",
             "pregunta": "¿Para qué sirve la memoria caché del procesador?",
             "opciones": ["Guardar lo que se usa más seguido para ir más rápido", "Guardar todo para siempre", "Dar energía"], "correcta": 0,
             "pista": "Es pequeña y muy rápida, y está muy cerca de la CPU."},
            {"id": "s3m1_r2", "tipo": "reto", "nivel": "🔴 Crear", "titulo": "Reto: analiza el rendimiento", "puntos": 15, "categoria": "hardware",
             "pregunta": "Una PC para juegos va lenta al mostrar gráficos, aunque tiene buen CPU y RAM. ¿Qué componente conviene mejorar?",
             "opciones": ["La GPU (tarjeta gráfica)", "La fuente de poder", "El teclado"], "correcta": 0,
             "pista": "El problema son los gráficos, no el cálculo general ni la energía."},
        ],
        "evaluacion": [
            {"pregunta": "La CPU se encarga de...", "opciones": ["Ejecutar las instrucciones", "Dar energía", "Mostrar video"], "correcta": 0},
            {"pregunta": "Los núcleos del procesador permiten...", "opciones": ["Hacer tareas en paralelo", "Guardar fotos", "Imprimir"], "correcta": 0},
            {"pregunta": "La caché es una memoria...", "opciones": ["Muy rápida y cercana a la CPU", "Lenta y grande", "De papel"], "correcta": 0},
            {"pregunta": "La RAM es memoria...", "opciones": ["Volátil (se borra al apagar)", "Permanente", "De solo lectura"], "correcta": 0},
            {"pregunta": "La ROM es memoria...", "opciones": ["De solo lectura", "De trabajo temporal", "Gráfica"], "correcta": 0},
            {"pregunta": "Comparado con un HDD, el SSD es...", "opciones": ["Más rápido y sin partes móviles", "Más lento", "Igual"], "correcta": 0},
            {"pregunta": "La GPU procesa...", "opciones": ["Gráficos y video", "El sonido", "La energía"], "correcta": 0},
            {"pregunta": "BIOS/UEFI sirve para...", "opciones": ["Arrancar el hardware antes del SO", "Navegar", "Escribir"], "correcta": 0},
            {"pregunta": "Un 'proceso' es...", "opciones": ["Un programa en ejecución", "Un cable", "Una carpeta"], "correcta": 0},
            {"pregunta": "Los drivers permiten...", "opciones": ["Que el sistema use cada pieza", "Dar energía", "Imprimir en papel"], "correcta": 0},
        ],
    },
    # =================================================================================
    2: {
        "titulo": "Sistemas operativos y administración",
        "icono": "⚙️",
        "umbral": 50,
        "contenido": [
            ("Funciones de un sistema operativo",
             "El SO administra: los procesos (programas en ejecución), la memoria, el sistema de archivos, los "
             "usuarios y sus permisos, y los servicios que corren en segundo plano."),
            ("Usuarios y permisos",
             "Cada usuario tiene sus datos y sus permisos. Los permisos deciden quién puede leer, escribir o "
             "ejecutar un archivo o carpeta. Si un usuario 'no tiene permiso', no puede abrirla."),
            ("Mantener el sistema sano",
             "• Actualizaciones: corrigen fallos y cierran huecos de seguridad.\n"
             "• Controladores: mantienen el hardware funcionando.\n"
             "• Copias de seguridad y recuperación: permiten volver atrás si algo falla."),
            ("Diferentes sistemas operativos",
             "Windows (PC, fácil y común), Linux (libre y muy usado en servidores), Android e iOS (celulares). "
             "Cada uno administra los mismos recursos a su manera."),
        ],
        "actividades": [
            {"id": "s3m2_a1", "tipo": "relacionar", "titulo": "¿Qué administra el SO?", "puntos": 10, "categoria": "so",
             "pares": [("Programas en ejecución", "Procesos"), ("Espacio de trabajo temporal", "Memoria"),
                       ("Archivos y carpetas", "Sistema de archivos"), ("Quién puede hacer qué", "Permisos")]},
            {"id": "s3m2_a2", "tipo": "problema", "titulo": "🔬 Incidente: app consume demasiada memoria", "puntos": 15, "categoria": "so",
             "pregunta": "El SO reporta que una aplicación usa el 95% de la memoria y todo va lento. ¿Qué acción es la correcta?",
             "opciones": ["Abrir el Administrador de tareas y cerrar esa aplicación", "Quitar la RAM", "Apagar la pantalla"],
             "correcta": 0, "explicacion": "El Administrador de tareas permite ver el consumo y cerrar el proceso problemático para liberar memoria."},
            {"id": "s3m2_a3", "tipo": "problema", "titulo": "🔬 Incidente: no puedo abrir una carpeta", "puntos": 15, "categoria": "so",
             "pregunta": "Un usuario no puede abrir una carpeta y aparece 'Acceso denegado'. ¿Cuál es la causa más probable?",
             "opciones": ["No tiene los permisos necesarios", "La pantalla está sucia", "El mouse no sirve"],
             "correcta": 0, "explicacion": "El mensaje 'Acceso denegado' casi siempre indica un problema de permisos del usuario."},
            {"id": "s3m2_a4", "tipo": "ordenar", "titulo": "Hacer una copia de seguridad", "puntos": 10, "categoria": "so",
             "instruccion": "Ordena los pasos:",
             "items": ["Elegir los archivos importantes", "Conectar un disco externo o abrir la nube",
                       "Copiar los archivos al respaldo", "Verificar que la copia esté completa"]},
            {"id": "s3m2_a5", "tipo": "clasificar", "titulo": "¿PC o celular?", "puntos": 10, "categoria": "so",
             "categorias": ["Sistema de PC/servidor", "Sistema de celular"],
             "items": [("Windows", "Sistema de PC/servidor"), ("Linux", "Sistema de PC/servidor"),
                       ("Android", "Sistema de celular"), ("iOS", "Sistema de celular")]},
        ],
        "evaluacion": [
            {"pregunta": "El SO administra los procesos, que son...", "opciones": ["Programas en ejecución", "Cables", "Colores"], "correcta": 0},
            {"pregunta": "Los permisos deciden...", "opciones": ["Quién puede leer/escribir/ejecutar algo", "El volumen", "La hora"], "correcta": 0},
            {"pregunta": "'Acceso denegado' a una carpeta suele ser problema de...", "opciones": ["Permisos", "Batería", "Pantalla"], "correcta": 0},
            {"pregunta": "Si una app consume el 95% de memoria conviene...", "opciones": ["Cerrarla desde el Administrador de tareas", "Quitar la RAM", "Nada"], "correcta": 0},
            {"pregunta": "Las actualizaciones sirven para...", "opciones": ["Corregir fallos y mejorar la seguridad", "Gastar datos", "Nada"], "correcta": 0},
            {"pregunta": "Una copia de seguridad permite...", "opciones": ["Recuperar la información si algo falla", "Ir más rápido", "Imprimir"], "correcta": 0},
            {"pregunta": "Linux se usa mucho en...", "opciones": ["Servidores", "Ningún lugar", "Solo relojes"], "correcta": 0},
            {"pregunta": "Android es un sistema de...", "opciones": ["Celulares", "Impresoras", "Routers"], "correcta": 0},
            {"pregunta": "Los servicios del SO corren...", "opciones": ["En segundo plano", "En papel", "En la nube solamente"], "correcta": 0},
            {"pregunta": "El sistema de archivos organiza...", "opciones": ["Archivos y carpetas", "La energía", "El sonido"], "correcta": 0},
        ],
    },
    # =================================================================================
    3: {
        "titulo": "Algoritmos y resolución avanzada de problemas",
        "icono": "🧠",
        "umbral": 100,
        "contenido": [
            ("Algoritmos y pseudocódigo",
             "Un algoritmo son pasos ordenados para resolver un problema. El pseudocódigo lo escribe en palabras "
             "parecidas a un programa, sin un lenguaje real. Estructura: ENTRADA → PROCESO → SALIDA."),
            ("Herramientas del pensamiento",
             "• Variables: guardan datos.\n• Condicionales (SI/SINO): deciden.\n• Ciclos: repiten.\n"
             "• Funciones: agrupan pasos reutilizables."),
            ("Las 4 técnicas clave",
             "• Descomposición: dividir el problema en partes.\n• Patrones: detectar lo que se repite.\n"
             "• Abstracción: quedarse con lo importante.\n• Algoritmos eficientes: lograr el resultado con menos pasos."),
        ],
        "actividades": [
            {"id": "s3m3_a1", "tipo": "ordenar", "titulo": "Pseudocódigo: ¿aprobado o reprobado?", "puntos": 15, "categoria": "algoritmos",
             "instruccion": "Ordena el pseudocódigo:",
             "items": ["INICIO", "Leer la nota", "SI nota >= 60 → Mostrar 'Aprobado'", "SINO → Mostrar 'Reprobado'", "FIN"]},
            {"id": "s3m3_a2", "tipo": "codigo", "nivel": "🟡 Aplicar", "titulo": "🔬 Lab: ¿qué muestra el algoritmo?", "puntos": 15, "categoria": "algoritmos",
             "codigo": "nota = 45\nSI nota >= 60\n    mostrar(\"Aprobado\")\nSINO\n    mostrar(\"Reprobado\")",
             "salida_tipo": "texto", "salida": "Reprobado",
             "pregunta": "Ejecuta el algoritmo. ¿Qué muestra en pantalla?",
             "opciones": ["Reprobado", "Aprobado", "Un error"], "correcta": 0,
             "pista": "¿45 es mayor o igual a 60? Si la condición es falsa, corre el SINO."},
            {"id": "s3m3_a3", "tipo": "relacionar", "titulo": "Técnica del pensamiento computacional", "puntos": 10, "categoria": "algoritmos",
             "pares": [("Dividir el problema en partes", "Descomposición"), ("Detectar lo que se repite", "Patrones"),
                       ("Quedarse con lo importante", "Abstracción"), ("Lograr el resultado con menos pasos", "Algoritmo eficiente")]},
            {"id": "s3m3_r1", "tipo": "reto", "nivel": "🔴 Crear", "titulo": "Reto de lógica de varios pasos", "puntos": 15, "categoria": "logica",
             "pregunta": "Un algoritmo suma los números del 1 al 5 (1+2+3+4+5). ¿Cuál es la SALIDA?",
             "opciones": ["15", "10", "25"], "correcta": 0,
             "pista": "Suma paso a paso: 1+2=3, +3=6, +4=10, +5=15."},
            {"id": "s3m3_a4", "tipo": "bloques", "titulo": "🤖 Programa al robot (algoritmo)", "puntos": 15, "categoria": "algoritmos",
             "instruccion": "Diseña el algoritmo con bloques para llevar el robot 🤖 al tesoro 🎯.",
             "mapa": [[0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0]],
             "inicio": [0, 0], "meta": [4, 0], "mirando": "derecha"},
        ],
        "evaluacion": [
            {"pregunta": "Un algoritmo es...", "opciones": ["Pasos ordenados para resolver un problema", "Un color", "Un cable"], "correcta": 0},
            {"pregunta": "El pseudocódigo se escribe...", "opciones": ["En palabras parecidas a un programa", "En un idioma secreto", "Con dibujos únicamente"], "correcta": 0},
            {"pregunta": "La estructura básica es...", "opciones": ["Entrada, proceso y salida", "Solo salida", "Nada"], "correcta": 0},
            {"pregunta": "Si nota = 45 y se pide nota >= 60, muestra...", "opciones": ["Reprobado", "Aprobado", "Error"], "correcta": 0},
            {"pregunta": "Descomponer es...", "opciones": ["Dividir el problema en partes", "Hacerlo más grande", "Ignorarlo"], "correcta": 0},
            {"pregunta": "Reconocer patrones es...", "opciones": ["Detectar lo que se repite", "Borrar datos", "Apagar"], "correcta": 0},
            {"pregunta": "Abstraer es...", "opciones": ["Quedarse con lo importante", "Complicar todo", "Nada"], "correcta": 0},
            {"pregunta": "Un ciclo sirve para...", "opciones": ["Repetir instrucciones", "Borrar", "Apagar"], "correcta": 0},
            {"pregunta": "Una función agrupa...", "opciones": ["Pasos reutilizables", "Cables", "Colores"], "correcta": 0},
            {"pregunta": "La suma de 1 a 5 da...", "opciones": ["15", "10", "20"], "correcta": 0},
        ],
    },
    # =================================================================================
    4: {
        "titulo": "Programación",
        "icono": "👨‍💻",
        "umbral": 150,
        "contenido": [
            ("¿Qué es programar?",
             "Programar es escribir instrucciones en un lenguaje que la computadora entiende. Debe ser claro y "
             "ordenado. Los comentarios explican el código a las personas."),
            ("Variables y tipos de datos",
             "Una variable guarda un valor. Tipos comunes:\n• String (texto): \"Hola\".\n• Integer (número entero): 15.\n"
             "• Boolean (verdadero/falso): True / False.\nUna constante es un valor que no cambia."),
            ("Operadores y decisiones",
             "• Matemáticos: + - * /.\n• Comparación: >, <, ==, !=.\n"
             "• Condicional IF/ELSE: hace algo según una condición."),
            ("Repetir y organizar",
             "• Ciclo FOR: repite un número conocido de veces.\n• Ciclo WHILE: repite mientras se cumpla una condición.\n"
             "• Funciones y parámetros: bloques reutilizables que reciben datos.\n• Arreglos: listas de valores."),
            ("Los errores son parte del proceso",
             "Un error (bug) impide que el programa funcione bien. Depurar es buscarlo y corregirlo. ¡Paciencia y "
             "lectura con calma!"),
        ],
        "actividades": [
            {"id": "s3m4_a1", "tipo": "codigo", "nivel": "🟡 Aplicar", "titulo": "🔬 Lab de código: ¿qué imprime?", "puntos": 20, "categoria": "programacion",
             "codigo": "edad = 15\nif edad >= 13:\n    print(\"Puedes continuar\")\nelse:\n    print(\"No puedes continuar\")",
             "salida_tipo": "texto", "salida": "Puedes continuar",
             "pregunta": "Ejecuta el programa. ¿Qué imprime?",
             "opciones": ["Puedes continuar", "No puedes continuar", "Un error"], "correcta": 0,
             "pista": "¿15 es mayor o igual a 13? Si es verdadero, corre el bloque del if."},
            {"id": "s3m4_a2", "tipo": "codigo", "nivel": "🔴 Crear", "titulo": "🐞 Cazador de errores", "puntos": 20, "categoria": "programacion",
             "codigo": "contador = 0\nwhile contador < 3\n    print(contador)\n    contador = contador + 1",
             "salida_tipo": "texto", "salida": "❌ Error: falta ':' al final de la línea del while",
             "pregunta": "El programa tiene un error. ¿Cuál es?",
             "opciones": ["Falta el ':' al final de la línea 'while contador < 3'", "El nombre 'contador' está mal", "Falta apagar la PC"], "correcta": 0,
             "pista": "En Python, las líneas 'if', 'while' y 'for' terminan con dos puntos ':'."},
            {"id": "s3m4_a3", "tipo": "relacionar", "titulo": "Tipo de dato del valor", "puntos": 10, "categoria": "programacion",
             "pares": [("\"Hola\"", "String (texto)"), ("15", "Integer (entero)"),
                       ("True", "Boolean (verdadero/falso)"), ("[1, 2, 3]", "Arreglo (lista)")]},
            {"id": "s3m4_a4", "tipo": "ordenar", "titulo": "Ordena el programa (pedir y saludar)", "puntos": 10, "categoria": "programacion",
             "instruccion": "Ordena las líneas del programa:",
             "items": ["nombre = pedir_dato()", "if nombre != \"\":", "    print(\"Hola \" + nombre)", "else:", "    print(\"No escribiste tu nombre\")"]},
            {"id": "s3m4_a5", "tipo": "seleccion", "titulo": "Ciclos y operadores", "puntos": 10, "categoria": "programacion",
             "preguntas": [
                {"pregunta": "Para repetir un número conocido de veces uso...", "opciones": ["Ciclo FOR", "Ciclo WHILE infinito", "Nada"], "correcta": 0},
                {"pregunta": "El operador '!=' significa...", "opciones": ["Distinto de", "Igual a", "Mayor que"], "correcta": 0},
                {"pregunta": "Los comentarios en el código sirven para...", "opciones": ["Explicar el código a las personas", "Ejecutarse más rápido", "Borrar"], "correcta": 0},
             ]},
        ],
        "evaluacion": [
            {"pregunta": "Programar es...", "opciones": ["Escribir instrucciones para la computadora", "Dormir", "Dibujar"], "correcta": 0},
            {"pregunta": "\"Hola\" es un dato de tipo...", "opciones": ["String (texto)", "Integer", "Boolean"], "correcta": 0},
            {"pregunta": "15 es un dato de tipo...", "opciones": ["Integer (entero)", "String", "Boolean"], "correcta": 0},
            {"pregunta": "True o False es un dato de tipo...", "opciones": ["Boolean", "String", "Integer"], "correcta": 0},
            {"pregunta": "Si edad = 15 y se pide edad >= 13, imprime...", "opciones": ["Puedes continuar", "No puedes continuar", "Error"], "correcta": 0},
            {"pregunta": "En Python, un 'while' o 'if' termina la línea con...", "opciones": ["Dos puntos ':'", "Un punto", "Nada"], "correcta": 0},
            {"pregunta": "El ciclo FOR se usa para...", "opciones": ["Repetir un número conocido de veces", "Apagar", "Guardar fotos"], "correcta": 0},
            {"pregunta": "El operador '!=' significa...", "opciones": ["Distinto de", "Igual", "Menor"], "correcta": 0},
            {"pregunta": "Un arreglo (lista) guarda...", "opciones": ["Varios valores juntos", "Un solo cable", "Nada"], "correcta": 0},
            {"pregunta": "Depurar es...", "opciones": ["Buscar y corregir errores", "Apagar", "Copiar"], "correcta": 0},
        ],
    },
    # =================================================================================
    5: {
        "titulo": "Desarrollo web",
        "icono": "🌐",
        "umbral": 200,
        "contenido": [
            ("Cliente, servidor y las 3 tecnologías",
             "Al abrir una página, tu navegador (cliente) pide los archivos a un servidor. La web se construye con "
             "tres tecnologías:\n• HTML: la estructura y el contenido.\n• CSS: los estilos (colores, tamaños).\n"
             "• JavaScript: la interactividad."),
            ("Etiquetas HTML",
             "El HTML usa 'etiquetas':\n• <h1> título grande.\n• <p> párrafo.\n• <a> enlace.\n• <img> imagen.\n"
             "• <button> botón.\nLas etiquetas casi siempre abren y cierran: <p>texto</p>."),
            ("Estructura de una página",
             "Una página tiene <html>, dentro <head> (información) y <body> (lo que se ve). El contenido va en el body."),
            ("CSS y JavaScript (idea básica)",
             "Con CSS cambiamos la apariencia (por ejemplo, el tamaño del título). Con JavaScript agregamos acciones "
             "(por ejemplo, que un botón muestre un mensaje). Aquí es solo una introducción práctica."),
        ],
        "actividades": [
            {"id": "s3m5_a1", "tipo": "relacionar", "titulo": "¿Para qué sirve cada tecnología?", "puntos": 10, "categoria": "web",
             "pares": [("Estructura y contenido", "HTML"), ("Estilos (colores, tamaños)", "CSS"),
                       ("Interactividad", "JavaScript"), ("Pide la página al servidor", "Navegador (cliente)")]},
            {"id": "s3m5_a2", "tipo": "relacionar", "titulo": "Etiqueta HTML y su función", "puntos": 10, "categoria": "web",
             "pares": [("<h1>", "Título grande"), ("<p>", "Párrafo"), ("<a>", "Enlace"), ("<button>", "Botón")]},
            {"id": "s3m5_a3", "tipo": "codigo", "nivel": "🟡 Aplicar", "titulo": "🔬 Lab web: ejecuta este HTML", "puntos": 15, "categoria": "web",
             "codigo": "<h1>Mi página web</h1>\n<p>Hola mundo</p>\n<button>Aceptar</button>",
             "salida_tipo": "web", "salida": [["h1", "Mi página web"], ["p", "Hola mundo"], ["button", "Aceptar"]],
             "pregunta": "Ejecuta el HTML y observa la vista previa. ¿Qué etiqueta creó el título grande 'Mi página web'?",
             "opciones": ["<h1>", "<p>", "<button>"], "correcta": 0,
             "pista": "El título grande lo crea la etiqueta de encabezado principal."},
            {"id": "s3m5_a4", "tipo": "codigo", "nivel": "🟡 Aplicar", "titulo": "🔬 Lab web: agrega un enlace", "puntos": 15, "categoria": "web",
             "codigo": "<h2>Mi blog</h2>\n<p>Bienvenido a mi sitio.</p>\n<a>Ir a la página de inicio</a>",
             "salida_tipo": "web", "salida": [["h2", "Mi blog"], ["p", "Bienvenido a mi sitio."], ["a", "Ir a la página de inicio"]],
             "pregunta": "En la vista previa, ¿qué etiqueta crea el enlace subrayado?",
             "opciones": ["<a>", "<h2>", "<p>"], "correcta": 0,
             "pista": "La etiqueta de enlace (anchor) empieza con la letra 'a'."},
            {"id": "s3m5_a5", "tipo": "ordenar", "titulo": "Estructura de una página HTML", "puntos": 10, "categoria": "web",
             "instruccion": "Ordena las partes de una página:",
             "items": ["<html>", "<head> (información)", "<body> (lo que se ve)", "Contenido: <h1>, <p>, imágenes"]},
        ],
        "evaluacion": [
            {"pregunta": "El HTML define...", "opciones": ["La estructura y el contenido", "Los colores", "La interactividad"], "correcta": 0},
            {"pregunta": "El CSS define...", "opciones": ["Los estilos (colores, tamaños)", "La estructura", "La red"], "correcta": 0},
            {"pregunta": "JavaScript agrega...", "opciones": ["Interactividad", "Solo texto", "Energía"], "correcta": 0},
            {"pregunta": "La etiqueta <h1> crea...", "opciones": ["Un título grande", "Un párrafo", "Una imagen"], "correcta": 0},
            {"pregunta": "La etiqueta <p> crea...", "opciones": ["Un párrafo", "Un botón", "Un enlace"], "correcta": 0},
            {"pregunta": "La etiqueta <a> crea...", "opciones": ["Un enlace", "Un título", "Una tabla"], "correcta": 0},
            {"pregunta": "El navegador es el...", "opciones": ["Cliente que pide la página", "Servidor", "Cable"], "correcta": 0},
            {"pregunta": "El contenido visible va dentro de...", "opciones": ["<body>", "<head>", "<title>"], "correcta": 0},
            {"pregunta": "Las etiquetas normalmente...", "opciones": ["Abren y cierran", "No existen", "Son imágenes"], "correcta": 0},
            {"pregunta": "El servidor...", "opciones": ["Envía la página al navegador", "Enfría la CPU", "Imprime"], "correcta": 0},
        ],
    },
    # =================================================================================
    6: {
        "titulo": "Bases de datos y SQL",
        "icono": "🗄️",
        "umbral": 250,
        "contenido": [
            ("Bases de datos relacionales",
             "Una base de datos guarda información organizada en TABLAS (filas = registros, columnas = campos). "
             "La CLAVE PRIMARIA es un campo único que identifica cada registro (por ejemplo, el ID). Las tablas "
             "pueden RELACIONARSE entre sí."),
            ("¿Qué es SQL?",
             "SQL es el lenguaje para 'hablar' con la base de datos y hacer consultas."),
            ("Comandos básicos de SQL",
             "• SELECT ... FROM ...: elige qué columnas mostrar y de qué tabla.\n"
             "• WHERE: filtra por una condición.\n• ORDER BY: ordena los resultados.\n"
             "• INSERT: agrega un registro.\n• UPDATE: modifica.\n• DELETE: elimina."),
            ("Ejemplo",
             "SELECT * FROM estudiantes WHERE grado = '3o'\nMuestra TODOS los datos de los estudiantes cuyo grado "
             "es 3o. El '*' significa 'todas las columnas'."),
        ],
        "actividades": [
            {"id": "s3m6_a1", "tipo": "relacionar", "titulo": "Comando SQL y su función", "puntos": 10, "categoria": "datos",
             "pares": [("Elegir y mostrar datos", "SELECT"), ("Filtrar por una condición", "WHERE"),
                       ("Ordenar los resultados", "ORDER BY"), ("Agregar un registro", "INSERT")]},
            {"id": "s3m6_a2", "tipo": "codigo", "nivel": "🟡 Aplicar", "titulo": "🔬 Lab SQL: filtra estudiantes de 3o", "puntos": 20, "categoria": "datos",
             "codigo": "SELECT * FROM estudiantes\nWHERE grado = '3o';",
             "salida_tipo": "tabla",
             "salida": {"columnas": ["ID", "Nombre", "Grado", "Edad"],
                         "filas": [["001", "Ana", "3o", "15"], ["003", "Luis", "3o", "16"]]},
             "pregunta": "Ejecuta la consulta. En la tabla original hay estudiantes de 2o y 3o. ¿Qué hace WHERE grado = '3o'?",
             "opciones": ["Muestra solo los estudiantes de 3o", "Muestra a todos", "Borra los de 3o"], "correcta": 0,
             "pista": "WHERE aplica un filtro: solo pasan los registros que cumplen la condición."},
            {"id": "s3m6_a3", "tipo": "codigo", "nivel": "🟡 Aplicar", "titulo": "🔬 Lab SQL: ordena por nombre", "puntos": 20, "categoria": "datos",
             "codigo": "SELECT Nombre, Edad FROM estudiantes\nORDER BY Nombre;",
             "salida_tipo": "tabla",
             "salida": {"columnas": ["Nombre", "Edad"],
                         "filas": [["Ana", "15"], ["Carlos", "14"], ["Luis", "16"], ["Sofía", "15"]]},
             "pregunta": "Ejecuta la consulta. ¿Qué hace ORDER BY Nombre?",
             "opciones": ["Ordena los resultados por nombre (A→Z)", "Los muestra al azar", "Los borra"], "correcta": 0,
             "pista": "ORDER BY acomoda los resultados según la columna indicada."},
            {"id": "s3m6_a4", "tipo": "seleccion", "titulo": "¿Qué consulta uso?", "puntos": 10, "categoria": "datos",
             "preguntas": [
                {"pregunta": "Para AGREGAR un nuevo estudiante uso...", "opciones": ["INSERT", "DELETE", "SELECT"], "correcta": 0},
                {"pregunta": "Para MOSTRAR estudiantes mayores de 15 uso...", "opciones": ["SELECT ... WHERE edad > 15", "DELETE", "ORDER BY"], "correcta": 0},
                {"pregunta": "Para ELIMINAR un registro uso...", "opciones": ["DELETE", "SELECT", "INSERT"], "correcta": 0},
             ]},
            {"id": "s3m6_r1", "tipo": "reto", "nivel": "🔴 Crear", "titulo": "Reto de datos: la clave primaria", "puntos": 15, "categoria": "datos",
             "pregunta": "En una tabla de estudiantes, ¿qué campo conviene usar como CLAVE PRIMARIA?",
             "opciones": ["El ID (único para cada estudiante)", "La edad (se repite)", "El grado (todos igual)"], "correcta": 0,
             "pista": "La clave primaria debe ser ÚNICA: no puede repetirse en dos registros."},
        ],
        "evaluacion": [
            {"pregunta": "Una tabla organiza los datos en...", "opciones": ["Filas y columnas", "Cables", "Colores"], "correcta": 0},
            {"pregunta": "La clave primaria...", "opciones": ["Identifica de forma única cada registro", "Se repite", "Da energía"], "correcta": 0},
            {"pregunta": "SQL sirve para...", "opciones": ["Hacer consultas a la base de datos", "Navegar", "Imprimir"], "correcta": 0},
            {"pregunta": "SELECT sirve para...", "opciones": ["Elegir y mostrar datos", "Borrar", "Apagar"], "correcta": 0},
            {"pregunta": "WHERE sirve para...", "opciones": ["Filtrar por una condición", "Ordenar", "Sumar"], "correcta": 0},
            {"pregunta": "ORDER BY sirve para...", "opciones": ["Ordenar los resultados", "Filtrar", "Eliminar"], "correcta": 0},
            {"pregunta": "INSERT sirve para...", "opciones": ["Agregar un registro", "Borrar todo", "Ordenar"], "correcta": 0},
            {"pregunta": "DELETE sirve para...", "opciones": ["Eliminar un registro", "Agregar", "Mostrar"], "correcta": 0},
            {"pregunta": "El '*' en SELECT * significa...", "opciones": ["Todas las columnas", "Ninguna", "Solo el ID"], "correcta": 0},
            {"pregunta": "Para mostrar mayores de 15 uso...", "opciones": ["WHERE edad > 15", "ORDER BY", "DELETE"], "correcta": 0},
        ],
    },
    # =================================================================================
    7: {
        "titulo": "Redes de computadoras",
        "icono": "📡",
        "umbral": 300,
        "contenido": [
            ("Repaso y direccionamiento",
             "Una red conecta dispositivos. La dirección IP identifica a cada uno (IPv4, ej. 192.168.1.10). La "
             "MÁSCARA de red (ej. 255.255.255.0) define qué parte es la red y qué parte el dispositivo. El GATEWAY "
             "(router) es la salida hacia otras redes."),
            ("Misma red = mismos primeros números",
             "Con máscara 255.255.255.0, dos dispositivos están en la MISMA red si comparten los tres primeros "
             "grupos (ej. 192.168.1.x). Así pueden comunicarse directamente."),
            ("Servicios y protocolos",
             "• DNS: traduce nombres (web.com) a IP.\n• DHCP: entrega IP automáticamente.\n"
             "• TCP/IP: el conjunto de reglas para comunicarse en Internet.\n• Los PUERTOS identifican servicios "
             "(por ejemplo, la web suele usar el puerto 80/443)."),
        ],
        "actividades": [
            {"id": "s3m7_a1", "tipo": "relacionar", "titulo": "Concepto de red", "puntos": 10, "categoria": "redes",
             "pares": [("Identifica un dispositivo", "Dirección IP"), ("Salida hacia otras redes", "Gateway (router)"),
                       ("Traduce nombres a IP", "DNS"), ("Entrega IP automáticamente", "DHCP")]},
            {"id": "s3m7_a2", "tipo": "ordenar", "titulo": "Camino de la conexión", "puntos": 10, "categoria": "redes",
             "instruccion": "Ordena el camino de los datos hacia Internet:",
             "items": ["PC", "Switch", "Router", "Internet"]},
            {"id": "s3m7_a3", "tipo": "codigo", "nivel": "🟡 Aplicar", "titulo": "🔬 Simulador de red: ¿se comunican?", "puntos": 20, "categoria": "redes",
             "codigo": "Máscara: 255.255.255.0\nPC1  -> 192.168.1.10\nPC2  -> 192.168.1.11\nRouter -> 192.168.1.1",
             "salida_tipo": "tabla",
             "salida": {"columnas": ["Dispositivo", "IP", "¿Misma red?"],
                         "filas": [["PC1", "192.168.1.10", "Sí"], ["PC2", "192.168.1.11", "Sí"], ["Router", "192.168.1.1", "Sí"]]},
             "pregunta": "Ejecuta el simulador. ¿PC1 y PC2 pueden comunicarse?",
             "opciones": ["Sí, están en la misma red (192.168.1.x)", "No, están en redes distintas", "No tienen IP"], "correcta": 0,
             "pista": "Con máscara 255.255.255.0 comparten los tres primeros grupos (192.168.1), así que son la misma red."},
            {"id": "s3m7_r1", "tipo": "reto", "nivel": "🔴 Crear", "titulo": "Reto de redes: encuentra la IP mal configurada", "puntos": 20, "categoria": "redes",
             "pregunta": "La red usa 192.168.1.x (máscara 255.255.255.0). ¿Cuál dispositivo NO podrá comunicarse con los demás?",
             "opciones": ["PC3 con IP 192.168.2.50", "PC1 con IP 192.168.1.10", "PC2 con IP 192.168.1.20"], "correcta": 0,
             "pista": "Busca la IP que NO empieza con 192.168.1 — está en otra red."},
            {"id": "s3m7_a4", "tipo": "seleccion", "titulo": "Conceptos de red", "puntos": 10, "categoria": "redes",
             "preguntas": [
                {"pregunta": "La máscara 255.255.255.0 sirve para...", "opciones": ["Definir qué parte es la red", "Dar energía", "Imprimir"], "correcta": 0},
                {"pregunta": "El DNS traduce...", "opciones": ["Nombres de páginas a IP", "IP a energía", "Nada"], "correcta": 0},
                {"pregunta": "Los puertos identifican...", "opciones": ["Servicios (como la web)", "El color", "La marca"], "correcta": 0},
             ]},
        ],
        "evaluacion": [
            {"pregunta": "La dirección IP sirve para...", "opciones": ["Identificar un dispositivo en la red", "Dar sonido", "Imprimir"], "correcta": 0},
            {"pregunta": "La máscara de red define...", "opciones": ["Qué parte es la red y qué parte el dispositivo", "El color", "La marca"], "correcta": 0},
            {"pregunta": "El gateway (router) es...", "opciones": ["La salida hacia otras redes", "Una impresora", "Un cable de video"], "correcta": 0},
            {"pregunta": "Con máscara 255.255.255.0, 192.168.1.10 y 192.168.1.11 están...", "opciones": ["En la misma red", "En redes distintas", "Sin red"], "correcta": 0},
            {"pregunta": "192.168.2.50 respecto a la red 192.168.1.x está...", "opciones": ["En otra red", "En la misma red", "Sin definir"], "correcta": 0},
            {"pregunta": "El DNS traduce...", "opciones": ["Nombres a IP", "IP a energía", "Nada"], "correcta": 0},
            {"pregunta": "El DHCP...", "opciones": ["Entrega IP automáticamente", "Enfría la CPU", "Imprime"], "correcta": 0},
            {"pregunta": "TCP/IP es...", "opciones": ["El conjunto de reglas para comunicarse en Internet", "Un cable", "Un color"], "correcta": 0},
            {"pregunta": "Los puertos identifican...", "opciones": ["Servicios", "Colores", "Marcas"], "correcta": 0},
            {"pregunta": "El camino típico es...", "opciones": ["PC → Switch → Router → Internet", "Internet → PC directo sin nada", "Nada"], "correcta": 0},
        ],
    },
    # =================================================================================
    8: {
        "titulo": "Ciberseguridad",
        "icono": "🔐",
        "umbral": 350,
        "contenido": [
            ("Los 3 pilares (CIA)",
             "La seguridad busca proteger 3 cosas:\n• Confidencialidad: que solo vean la información quienes deben.\n"
             "• Integridad: que la información no se altere.\n• Disponibilidad: que esté disponible cuando se necesita."),
            ("Identidad y contraseñas",
             "Autenticación es demostrar quién eres. Una contraseña fuerte + la verificación en dos pasos (MFA) "
             "protegen mucho mejor tu cuenta."),
            ("Amenazas frecuentes",
             "• Phishing e ingeniería social: te engañan para robar datos.\n"
             "• Malware: virus, ransomware (secuestra archivos), spyware (espía).\n"
             "Señales de alerta: urgencia, remitente raro, enlaces y archivos desconocidos, pedir contraseñas."),
            ("Defensa (enfoque educativo)",
             "Actualizar, usar antivirus, hacer copias de seguridad, cuidar el Wi-Fi y la privacidad, y pensar antes "
             "de hacer clic. La mejor defensa es analizar con calma."),
        ],
        "actividades": [
            {"id": "s3m8_a1", "tipo": "clasificar", "titulo": "Los 3 pilares (CIA)", "puntos": 10, "categoria": "seguridad",
             "instruccion": "Clasifica qué pilar de seguridad protege cada acción.",
             "categorias": ["Confidencialidad", "Integridad", "Disponibilidad"],
             "items": [("Cifrar un mensaje para que solo lo vea el destinatario", "Confidencialidad"),
                       ("Evitar que alteren un documento", "Integridad"),
                       ("Tener copias para que el servicio no se caiga", "Disponibilidad"),
                       ("Una contraseña que oculta tus datos", "Confidencialidad"),
                       ("Verificar que un archivo no fue modificado", "Integridad")]},
            {"id": "s3m8_a2", "tipo": "reto", "nivel": "🔴 Crear", "titulo": "🕵️ SOC: analiza el incidente", "puntos": 15, "categoria": "seguridad",
             "pregunta": "Un correo del 'banco' dice: 'Cambia tu contraseña YA por este enlace o perderás tu cuenta hoy'. ¿Cuál es el nivel de riesgo y por qué?",
             "opciones": ["Riesgo ALTO: usa urgencia y pide datos por un enlace (phishing)", "Riesgo nulo: los bancos hacen eso", "No se puede saber"], "correcta": 0,
             "pista": "Urgencia + enlace + pedir credenciales = señales clásicas de phishing."},
            {"id": "s3m8_a3", "tipo": "problema", "titulo": "🕵️ SOC: elige la respuesta segura", "puntos": 15, "categoria": "seguridad",
             "pregunta": "Ante ese correo de phishing, ¿cuál es la respuesta correcta del equipo de seguridad?",
             "opciones": ["No hacer clic, reportarlo y entrar al banco por el sitio oficial", "Hacer clic y escribir la contraseña", "Reenviarlo a todos"],
             "correcta": 0, "explicacion": "Nunca se ingresan credenciales desde un enlace de correo. Se reporta y se accede solo por el sitio oficial."},
            {"id": "s3m8_a4", "tipo": "relacionar", "titulo": "Tipo de amenaza", "puntos": 10, "categoria": "seguridad",
             "pares": [("Secuestra tus archivos y pide dinero", "Ransomware"), ("Te espía", "Spyware"),
                       ("Correo falso para robar datos", "Phishing"), ("Te convencen de dar acceso", "Ingeniería social")]},
            {"id": "s3m8_a5", "tipo": "seleccion", "titulo": "Buenas prácticas", "puntos": 10, "categoria": "seguridad",
             "preguntas": [
                {"pregunta": "La verificación en dos pasos (MFA)...", "opciones": ["Añade seguridad extra", "Borra archivos", "Da Internet"], "correcta": 0},
                {"pregunta": "Ante un archivo desconocido de un extraño debo...", "opciones": ["No abrirlo", "Abrirlo rápido", "Compartirlo"], "correcta": 0},
                {"pregunta": "La 'disponibilidad' se protege con...", "opciones": ["Copias de seguridad", "Contraseñas débiles", "Nada"], "correcta": 0},
             ]},
        ],
        "evaluacion": [
            {"pregunta": "La confidencialidad busca que...", "opciones": ["Solo vean la información quienes deben", "Todos la vean", "Se borre"], "correcta": 0},
            {"pregunta": "La integridad busca que la información...", "opciones": ["No se altere", "Se pierda", "Se copie sola"], "correcta": 0},
            {"pregunta": "La disponibilidad busca que la información...", "opciones": ["Esté disponible cuando se necesita", "Desaparezca", "Se oculte siempre"], "correcta": 0},
            {"pregunta": "El MFA...", "opciones": ["Agrega seguridad extra al iniciar sesión", "Borra datos", "Da Internet"], "correcta": 0},
            {"pregunta": "El phishing usa...", "opciones": ["Engaño y urgencia para robar datos", "Cables", "Colores"], "correcta": 0},
            {"pregunta": "El ransomware...", "opciones": ["Secuestra archivos y pide dinero", "Enfría la PC", "Imprime"], "correcta": 0},
            {"pregunta": "La ingeniería social ataca...", "opciones": ["A la persona (la engaña)", "Solo cables", "La impresora"], "correcta": 0},
            {"pregunta": "Ante un correo que pide tu contraseña por enlace debo...", "opciones": ["No hacer clic y reportarlo", "Escribir la contraseña", "Reenviarlo"], "correcta": 0},
            {"pregunta": "Una señal de alerta es...", "opciones": ["Urgencia exagerada", "Un saludo normal", "Nada"], "correcta": 0},
            {"pregunta": "La mejor defensa es...", "opciones": ["Analizar con calma antes de hacer clic", "Hacer clic rápido", "Ignorar todo"], "correcta": 0},
        ],
    },
    # =================================================================================
    9: {
        "titulo": "Inteligencia artificial y ciencia de datos",
        "icono": "🤖",
        "umbral": 400,
        "contenido": [
            ("¿Cómo aprende una IA? (Machine Learning)",
             "El aprendizaje automático (Machine Learning) entrena un MODELO con muchos DATOS y ejemplos. El modelo "
             "encuentra PATRONES y luego los usa para clasificar o predecir cosas nuevas."),
            ("Qué puede hacer",
             "Clasificar imágenes, reconocer voz, traducir, recomendar y generar textos o imágenes (IA generativa). "
             "Los chatbots conversan usando estos modelos."),
            ("Límites importantes",
             "• La IA puede equivocarse y 'inventar' datos.\n• Puede tener SESGOS si sus datos estaban desbalanceados.\n"
             "• Los DEEPFAKES son imágenes/videos falsos creados con IA.\nPor eso: verifica siempre la información."),
            ("Uso responsable",
             "Usa la IA como ayuda para estudiar, cuida tu privacidad (no le des datos personales) y verifica lo que "
             "genera con fuentes confiables."),
        ],
        "actividades": [
            {"id": "s3m9_a1", "tipo": "clasificar", "titulo": "🤖 Entrena el clasificador", "puntos": 10, "categoria": "ia",
             "instruccion": "Como un modelo de IA, agrupa cada objeto según su patrón.",
             "categorias": ["Frutas", "No es fruta"],
             "items": [("Manzana", "Frutas"), ("Banano", "Frutas"), ("Martillo", "No es fruta"),
                       ("Uva", "Frutas"), ("Silla", "No es fruta")]},
            {"id": "s3m9_a2", "tipo": "relacionar", "titulo": "Concepto de Machine Learning", "puntos": 10, "categoria": "ia",
             "pares": [("Los ejemplos que se usan", "Datos"), ("Lo que se repite en los datos", "Patrones"),
                       ("Enseñar al modelo con ejemplos", "Entrenamiento"), ("Lo que aprende y usa la IA", "Modelo")]},
            {"id": "s3m9_r1", "tipo": "reto", "nivel": "🔴 Crear", "titulo": "Reto de IA: verifica la información", "puntos": 15, "categoria": "ia",
             "pregunta": "Una IA afirma: 'El agua hierve a 50°C y Guatemala tiene 5 océanos'. ¿Qué debes hacer?",
             "opciones": ["Verificar: ambos datos son falsos (el agua hierve a 100°C; Guatemala no tiene 5 océanos)", "Creerlo tal cual", "Compartirlo sin revisar"], "correcta": 0,
             "pista": "La IA puede sonar segura y equivocarse. Contrasta cada dato con una fuente confiable."},
            {"id": "s3m9_a3", "tipo": "seleccion", "titulo": "Límites de la IA", "puntos": 10, "categoria": "ia",
             "preguntas": [
                {"pregunta": "¿La IA puede tener sesgos?", "opciones": ["Sí, si sus datos estaban desbalanceados", "No, nunca"], "correcta": 0},
                {"pregunta": "Un deepfake es...", "opciones": ["Un video/imagen falso creado con IA", "Un antivirus", "Un cable"], "correcta": 0},
                {"pregunta": "Antes de usar un dato de una IA debo...", "opciones": ["Verificarlo", "Creerlo siempre", "Ignorarlo"], "correcta": 0},
             ]},
            {"id": "s3m9_a4", "tipo": "problema", "titulo": "¿Qué dato verificar?", "puntos": 10, "categoria": "ia",
             "pregunta": "Una IA te da una fecha histórica y una cifra para tu tarea. ¿Qué conviene hacer antes de entregarla?",
             "opciones": ["Verificar la fecha y la cifra en una fuente confiable", "Entregar sin revisar", "Cambiar el tema"],
             "correcta": 0, "explicacion": "Los datos concretos (fechas, cifras, nombres) son los que más conviene verificar, porque la IA puede equivocarse."},
        ],
        "evaluacion": [
            {"pregunta": "El Machine Learning entrena un modelo con...", "opciones": ["Muchos datos y ejemplos", "La suerte", "Nada"], "correcta": 0},
            {"pregunta": "El modelo encuentra...", "opciones": ["Patrones en los datos", "Cables", "Colores"], "correcta": 0},
            {"pregunta": "La IA generativa...", "opciones": ["Crea textos o imágenes", "Enfría la PC", "Imprime"], "correcta": 0},
            {"pregunta": "¿La IA puede equivocarse?", "opciones": ["Sí", "No, nunca", "Solo los lunes"], "correcta": 0},
            {"pregunta": "Un sesgo ocurre cuando...", "opciones": ["Los datos estaban desbalanceados", "Hay mucha luz", "Nunca"], "correcta": 0},
            {"pregunta": "Un deepfake es...", "opciones": ["Un video/imagen falso hecho con IA", "Un cable", "Un antivirus"], "correcta": 0},
            {"pregunta": "Antes de usar información de una IA debo...", "opciones": ["Verificarla", "Creerla siempre", "Borrarla"], "correcta": 0},
            {"pregunta": "¿Debo dar datos personales a una IA?", "opciones": ["No", "Sí, todos", "Solo mi dirección"], "correcta": 0},
            {"pregunta": "Un chatbot...", "opciones": ["Conversa usando modelos de IA", "Es una impresora", "Es un cable"], "correcta": 0},
            {"pregunta": "La base de la IA son...", "opciones": ["Los datos y los patrones", "Las bocinas", "Los cables"], "correcta": 0},
        ],
    },
    # =================================================================================
    10: {
        "titulo": "Internet, nube y tecnologías modernas",
        "icono": "☁️",
        "umbral": 450,
        "contenido": [
            ("La nube",
             "La computación en la nube significa usar servidores de Internet (en grandes centros de datos) para "
             "guardar archivos, correr aplicaciones web o hacer streaming, sin depender solo de tu equipo."),
            ("Tecnologías conectadas",
             "• Internet de las cosas (IoT): objetos cotidianos conectados (focos, sensores, relojes).\n"
             "• Dispositivos inteligentes y automatización.\n• Robótica: máquinas que actúan en el mundo real."),
            ("Nuevas experiencias",
             "• Realidad virtual (VR): un mundo digital que te 'rodea'.\n"
             "• Realidad aumentada (AR): agrega elementos digitales sobre el mundo real.\n"
             "• Tecnología móvil: llevar todo esto en el bolsillo."),
        ],
        "actividades": [
            {"id": "s3m10_a1", "tipo": "relacionar", "titulo": "Tecnología y su idea", "puntos": 10, "categoria": "moderna",
             "pares": [("Guardar y usar recursos por Internet", "Nube"), ("Objetos cotidianos conectados", "IoT"),
                       ("Un mundo digital que te rodea", "Realidad virtual"), ("Elementos digitales sobre el mundo real", "Realidad aumentada")]},
            {"id": "s3m10_a2", "tipo": "clasificar", "titulo": "🏙️ Ciudad inteligente: ¿qué tecnología?", "puntos": 10, "categoria": "moderna",
             "instruccion": "Relaciona cada lugar con la tecnología que más usaría.",
             "categorias": ["Sensores / IoT", "Datos / apps"],
             "items": [("🚦 Semáforos que miden el tráfico", "Sensores / IoT"), ("🏥 Hospital con expedientes digitales", "Datos / apps"),
                       ("🏠 Casa con luces automáticas", "Sensores / IoT"), ("🏫 Escuela con plataforma de tareas", "Datos / apps"),
                       ("📡 Sensores de calidad del aire", "Sensores / IoT")]},
            {"id": "s3m10_a3", "tipo": "seleccion", "titulo": "Nube y tecnologías", "puntos": 10, "categoria": "moderna",
             "preguntas": [
                {"pregunta": "Los centros de datos guardan...", "opciones": ["Los servidores de la nube", "Comida", "Ropa"], "correcta": 0},
                {"pregunta": "El streaming permite...", "opciones": ["Ver/escuchar contenido sin descargarlo todo", "Imprimir", "Apagar"], "correcta": 0},
                {"pregunta": "La realidad aumentada (AR)...", "opciones": ["Agrega elementos digitales al mundo real", "Borra todo", "Es un cable"], "correcta": 0},
             ]},
            {"id": "s3m10_r1", "tipo": "reto", "nivel": "🚀 Crear", "titulo": "Reto innovador: elige la tecnología", "puntos": 15, "categoria": "moderna",
             "pregunta": "Tu escuela quiere apagar automáticamente las luces cuando no hay nadie en el aula. ¿Qué tecnología encaja mejor?",
             "opciones": ["Sensores IoT (detectan presencia y automatizan)", "Realidad virtual", "Un procesador de texto"], "correcta": 0,
             "pista": "Necesitas 'detectar' algo del mundo real y que actúe solo: eso es IoT + automatización."},
        ],
        "evaluacion": [
            {"pregunta": "La computación en la nube usa...", "opciones": ["Servidores de Internet", "Solo tu equipo", "Papel"], "correcta": 0},
            {"pregunta": "Los servidores de la nube están en...", "opciones": ["Centros de datos", "El techo", "Un cuaderno"], "correcta": 0},
            {"pregunta": "El IoT conecta...", "opciones": ["Objetos cotidianos a Internet", "Solo PCs grandes", "Nada"], "correcta": 0},
            {"pregunta": "El streaming permite...", "opciones": ["Ver/escuchar sin descargar todo", "Imprimir", "Apagar"], "correcta": 0},
            {"pregunta": "La realidad virtual (VR)...", "opciones": ["Crea un mundo digital que te rodea", "Es un cable", "Imprime"], "correcta": 0},
            {"pregunta": "La realidad aumentada (AR)...", "opciones": ["Agrega elementos digitales al mundo real", "Borra el mundo", "Nada"], "correcta": 0},
            {"pregunta": "La robótica crea máquinas que...", "opciones": ["Actúan en el mundo real", "Solo hablan", "No sirven"], "correcta": 0},
            {"pregunta": "La automatización sirve para...", "opciones": ["Que tareas se hagan solas", "Gastar energía", "Nada"], "correcta": 0},
            {"pregunta": "Para apagar luces solo cuando no hay nadie conviene...", "opciones": ["Sensores IoT", "VR", "Un lápiz"], "correcta": 0},
            {"pregunta": "Una aplicación web corre...", "opciones": ["En el navegador usando servidores", "En papel", "Sin Internet nunca"], "correcta": 0},
        ],
    },
    # =================================================================================
    11: {
        "titulo": "Ética, ciudadanía digital y tecnología",
        "icono": "🌎",
        "umbral": 500,
        "contenido": [
            ("Ciudadanía digital",
             "Ser buen ciudadano digital es usar la tecnología con respeto y responsabilidad: cuidar tu privacidad y "
             "la de los demás, y pensar antes de publicar (tu huella digital queda)."),
            ("Derechos de autor y licencias",
             "No todo lo que hay en Internet se puede usar libremente. Muchas imágenes y textos tienen DERECHOS DE "
             "AUTOR. Hay que buscar contenido con LICENCIA de uso (o de dominio público) y dar crédito. El SOFTWARE "
             "LIBRE se puede usar y compartir con ciertas reglas."),
            ("Convivencia y verificación",
             "• Respeto: nada de ciberacoso; si lo ves, apoya y avisa a un adulto.\n"
             "• No compartas información privada de otras personas.\n"
             "• Verifica las fuentes antes de compartir información."),
            ("Bienestar digital",
             "Cuida tu identidad digital y equilibra el tiempo frente a pantallas con otras actividades."),
        ],
        "actividades": [
            {"id": "s3m11_a1", "tipo": "problema", "titulo": "Usar una imagen de Internet", "puntos": 15, "categoria": "etica",
             "pregunta": "Quieres usar una imagen de Internet en una presentación escolar. ¿Qué debes verificar primero?",
             "opciones": ["Que tenga licencia de uso o sea libre, y dar crédito al autor", "Nada, todo es gratis", "Solo que sea bonita"],
             "correcta": 0, "explicacion": "Muchas imágenes tienen derechos de autor. Hay que usar contenido con licencia libre y citar la fuente."},
            {"id": "s3m11_a2", "tipo": "problema", "titulo": "Información privada de otra persona", "puntos": 15, "categoria": "etica",
             "pregunta": "Un compañero comparte en un grupo la dirección y el teléfono de otro estudiante sin permiso. ¿Qué haces?",
             "opciones": ["No difundirlo, pedir que lo borren y avisar a un adulto", "Reenviarlo a más personas", "Guardarlo para usarlo"],
             "correcta": 0, "explicacion": "Compartir datos privados de otros sin permiso viola su privacidad. Lo correcto es no difundirlo y avisar."},
            {"id": "s3m11_a3", "tipo": "relacionar", "titulo": "Concepto de ciudadanía digital", "puntos": 10, "categoria": "etica",
             "pares": [("Lo que dejamos publicado y queda", "Huella digital"), ("Protección de contenido de un autor", "Derechos de autor"),
                       ("Software que se puede usar y compartir", "Software libre"), ("Permiso para usar un contenido", "Licencia")]},
            {"id": "s3m11_a4", "tipo": "clasificar", "titulo": "¿Acción responsable o no?", "puntos": 10, "categoria": "etica",
             "categorias": ["Responsable", "No responsable"],
             "items": [("Citar la fuente de una imagen", "Responsable"), ("Copiar un texto y decir que es tuyo", "No responsable"),
                       ("Verificar una noticia antes de compartirla", "Responsable"), ("Publicar datos privados de un amigo", "No responsable"),
                       ("Equilibrar el tiempo de pantalla", "Responsable")]},
            {"id": "s3m11_a5", "tipo": "seleccion", "titulo": "Convivencia digital", "puntos": 10, "categoria": "etica",
             "preguntas": [
                {"pregunta": "Ante el ciberacoso debo...", "opciones": ["Apoyar a la víctima y avisar a un adulto", "Reírme", "Participar"], "correcta": 0},
                {"pregunta": "Antes de compartir una noticia debo...", "opciones": ["Verificar la fuente", "Compartir de inmediato", "Ignorar"], "correcta": 0},
                {"pregunta": "El software libre...", "opciones": ["Se puede usar y compartir con ciertas reglas", "Es ilegal siempre", "No existe"], "correcta": 0},
             ]},
        ],
        "evaluacion": [
            {"pregunta": "Ser buen ciudadano digital es...", "opciones": ["Usar la tecnología con respeto y responsabilidad", "Molestar", "Copiar todo"], "correcta": 0},
            {"pregunta": "La huella digital es...", "opciones": ["Lo que dejamos publicado y queda", "Una marca del dedo", "Un virus"], "correcta": 0},
            {"pregunta": "Antes de usar una imagen de Internet debo...", "opciones": ["Verificar su licencia y dar crédito", "Nada", "Solo copiarla"], "correcta": 0},
            {"pregunta": "Los derechos de autor protegen...", "opciones": ["El contenido de un autor", "La energía", "El cable"], "correcta": 0},
            {"pregunta": "Una licencia es...", "opciones": ["Un permiso para usar un contenido", "Un virus", "Un color"], "correcta": 0},
            {"pregunta": "Compartir datos privados de otro sin permiso es...", "opciones": ["Incorrecto (viola su privacidad)", "Correcto", "Obligatorio"], "correcta": 0},
            {"pregunta": "Ante el ciberacoso debo...", "opciones": ["Apoyar y avisar a un adulto", "Participar", "Callar siempre"], "correcta": 0},
            {"pregunta": "Antes de compartir información debo...", "opciones": ["Verificar la fuente", "Creerla siempre", "Ignorar"], "correcta": 0},
            {"pregunta": "El software libre se puede...", "opciones": ["Usar y compartir con ciertas reglas", "Nunca usar", "Solo mirar"], "correcta": 0},
            {"pregunta": "El bienestar digital incluye...", "opciones": ["Equilibrar el tiempo de pantalla", "Nunca descansar", "Nada"], "correcta": 0},
        ],
    },
    # =================================================================================
    12: {
        "titulo": "Proyecto final: crea tu solución tecnológica",
        "icono": "🏆",
        "umbral": 600,
        "contenido": [
            ("Tu gran proyecto",
             "Diseña una SOLUCIÓN TECNOLÓGICA para tu escuela. Elige un problema (préstamo de libros, registro de "
             "estudiantes, organizar computadoras, inventario o una página informativa) y aplica TODO lo aprendido."),
            ("Las 7 etapas",
             "1. Analizar (problema, usuarios, necesidades, información).\n2. Diseñar (objetivo, solución, algoritmo, "
             "diagrama).\n3. Datos (una pequeña base de datos).\n4. Programación (un algoritmo o programa).\n"
             "5. Interfaz (una pantalla sencilla).\n6. Seguridad (cómo proteger la información).\n7. Presentación.\n\n"
             "Al terminar desbloqueas la insignia final 🚀 'Joven Explorador de Tecnología'."),
        ],
        "actividades": [
            {"id": "s3m12_a1", "tipo": "reto", "nivel": "🟢 Comprender", "titulo": "Etapa 1: analiza el problema", "puntos": 10, "categoria": "proyecto",
             "pregunta": "Eliges 'controlar el préstamo de libros'. ¿Quiénes son los USUARIOS principales?",
             "opciones": ["Los estudiantes y el/la bibliotecario(a)", "Los vecinos de la escuela", "Nadie"], "correcta": 0,
             "pista": "Piensa en quién presta y quién recibe los libros."},
            {"id": "s3m12_a2", "tipo": "clasificar", "titulo": "Etapa 1: ¿qué datos necesito?", "puntos": 10, "categoria": "proyecto",
             "instruccion": "Para el préstamo de libros, ¿qué datos sirven?",
             "categorias": ["Dato útil", "Dato innecesario"],
             "items": [("Título del libro", "Dato útil"), ("Nombre del estudiante", "Dato útil"), ("Fecha de préstamo", "Dato útil"),
                       ("Color favorito del director", "Dato innecesario"), ("Marca del carro del vecino", "Dato innecesario")]},
            {"id": "s3m12_a3", "tipo": "ordenar", "titulo": "Etapa 2: diseña el algoritmo", "puntos": 15, "categoria": "proyecto",
             "instruccion": "Ordena el algoritmo para registrar un préstamo:",
             "items": ["INICIO", "Buscar el libro y al estudiante", "SI el libro está disponible → registrar préstamo y fecha",
                       "SINO → avisar 'no disponible'", "FIN"]},
            {"id": "s3m12_a4", "tipo": "codigo", "nivel": "🟡 Aplicar", "titulo": "🔬 Etapa 3: diseña la base de datos", "puntos": 15, "categoria": "proyecto",
             "codigo": "Tabla: Prestamos\n----------------\nID  | Libro | Estudiante | Fecha",
             "salida_tipo": "tabla",
             "salida": {"columnas": ["ID", "Libro", "Estudiante", "Fecha"],
                         "filas": [["001", "Matemática 3", "Ana", "10/03"], ["002", "Historia", "Luis", "11/03"]]},
             "pregunta": "Ejecuta y observa la tabla. ¿Cuál campo conviene como CLAVE PRIMARIA?",
             "opciones": ["ID (único por préstamo)", "Fecha (se puede repetir)", "Libro (se repite)"], "correcta": 0,
             "pista": "La clave primaria debe ser única para cada registro."},
            {"id": "s3m12_r1", "tipo": "reto", "nivel": "🔴 Crear", "titulo": "Etapa 6: seguridad", "puntos": 15, "categoria": "proyecto",
             "pregunta": "¿Cómo proteges la información del sistema de préstamos?",
             "opciones": ["Contraseñas, permisos y copias de seguridad", "Publicándola en redes", "Sin proteger nada"], "correcta": 0,
             "pista": "Recuerda los pilares: confidencialidad (permisos/contraseñas) y disponibilidad (respaldos)."},
            {"id": "s3m12_final", "tipo": "gran_reto", "titulo": "🏆 PROYECTO FINAL DE TERCERO", "puntos": 50, "categoria": "proyecto",
             "instruccion": "Recorre las 7 etapas del proyecto. ¡Responde bien para completar tu solución tecnológica!",
             "pasos": [
                {"tema": "Etapa 1 · Analizar", "pregunta": "Lo primero al resolver un problema es...", "opciones": ["Analizar el problema y sus usuarios", "Comprar cosas", "Adivinar"], "correcta": 0},
                {"tema": "Etapa 2 · Diseñar", "pregunta": "Para planear la lógica antes de programar uso un...", "opciones": ["Diagrama de flujo / algoritmo", "Grito", "Dibujo libre"], "correcta": 0},
                {"tema": "Etapa 3 · Datos", "pregunta": "La información organizada se guarda en...", "opciones": ["Una base de datos (tabla)", "Una servilleta", "El aire"], "correcta": 0},
                {"tema": "Etapa 4 · Programación", "pregunta": "Para decidir 'si el libro está disponible' uso un...", "opciones": ["Condicional IF/ELSE", "Color", "Cable"], "correcta": 0},
                {"tema": "Etapa 5 · Interfaz", "pregunta": "La pantalla para el usuario se construye con...", "opciones": ["HTML (y estilos)", "Un martillo", "Nada"], "correcta": 0},
                {"tema": "Etapa 6 · Seguridad", "pregunta": "Para proteger los datos uso...", "opciones": ["Contraseñas, permisos y respaldos", "Wi-Fi abierto", "Publicarlos"], "correcta": 0},
                {"tema": "Etapa 7 · Presentar", "pregunta": "Al presentar debo explicar...", "opciones": ["Qué resolví, cómo funciona y cómo protejo los datos", "Nada", "Solo el color"], "correcta": 0},
             ]},
        ],
        "evaluacion": [
            {"pregunta": "Lo primero en un proyecto es...", "opciones": ["Analizar el problema", "Comprar cosas", "Adivinar"], "correcta": 0},
            {"pregunta": "Los usuarios son...", "opciones": ["Las personas que usarán la solución", "Los cables", "Los colores"], "correcta": 0},
            {"pregunta": "Para planear la lógica uso un...", "opciones": ["Algoritmo / diagrama de flujo", "Grito", "Nada"], "correcta": 0},
            {"pregunta": "La información se guarda en...", "opciones": ["Una base de datos", "Una servilleta", "El aire"], "correcta": 0},
            {"pregunta": "La clave primaria debe ser...", "opciones": ["Única", "Repetida", "Vacía"], "correcta": 0},
            {"pregunta": "Para decidir entre dos caminos uso...", "opciones": ["Un condicional IF/ELSE", "Un color", "Un cable"], "correcta": 0},
            {"pregunta": "La pantalla del usuario se hace con...", "opciones": ["HTML y estilos", "Un martillo", "Nada"], "correcta": 0},
            {"pregunta": "Para proteger los datos uso...", "opciones": ["Contraseñas, permisos y respaldos", "Wi-Fi abierto", "Publicarlos"], "correcta": 0},
            {"pregunta": "Al presentar explico...", "opciones": ["Qué resolví, cómo funciona y cómo protejo los datos", "Solo mi nombre", "Nada"], "correcta": 0},
            {"pregunta": "El proyecto demuestra que sé...", "opciones": ["Analizar, diseñar, programar, usar datos y proteger", "Solo memorizar", "Nada"], "correcta": 0},
        ],
    },
}
