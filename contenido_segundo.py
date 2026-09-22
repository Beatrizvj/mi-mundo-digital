# -*- coding: utf-8 -*-
"""
Contenido educativo de SEGUNDO BÁSICO — Mi Primera Encarta Educativa.

Solo datos. El motor (puntos, niveles, desbloqueos, evaluaciones, insignias) vive en app.py
y funciona con cualquier grado. Segundo Básico es más difícil que Primero: el estudiante
ya conoce lo básico y ahora ANALIZA, APLICA, RESUELVE y CREA.

Ids con prefijo "s2m..." para no chocar con Primero. Umbrales: 0,40,80,...,450.

Tipos de actividad soportados por el motor:
  seleccion, relacionar, ordenar, memoria, clasificar, patron, problema, laberinto,
  explorar, arrastrar, teclado, bloques, atrapa, gran_reto, reto
El tipo "reto" muestra niveles 🟢🟡🔴, no revela la respuesta y da una PISTA al fallar.
"""

MODULOS_SEGUNDO = {
    # =================================================================================
    1: {
        "titulo": "Hardware y software avanzado",
        "icono": "🧠",
        "umbral": 0,
        "contenido": [
            ("El cerebro y la memoria",
             "• CPU (procesador): ejecuta las instrucciones; es el 'cerebro'. Su velocidad se mide en GHz.\n"
             "• RAM (memoria): guarda temporalmente lo que se está usando. Es rápida pero se borra al apagar.\n"
             "• Diferencia clave: la RAM es memoria de trabajo (temporal); el almacenamiento guarda a largo plazo."),
            ("Dónde se guarda todo",
             "• HDD (disco duro): más barato y lento, usa partes mecánicas.\n"
             "• SSD (estado sólido): más rápido y resistente, sin partes móviles.\n"
             "Ambos conservan la información aunque apagues la computadora."),
            ("Las piezas internas",
             "• Tarjeta madre: conecta todos los componentes.\n"
             "• Tarjeta gráfica (GPU): procesa imágenes y video; clave para juegos y edición.\n"
             "• Fuente de alimentación: entrega energía a las piezas."),
            ("Puertos y conexiones",
             "• USB: conectar periféricos y memorias.\n• HDMI: enviar video y audio a una pantalla.\n"
             "• Ethernet: conexión de red por cable.\n• Bluetooth y Wi-Fi: conexiones inalámbricas."),
            ("El software que da vida al hardware",
             "• Sistema operativo: administra todo (Windows, Linux, Android).\n"
             "• Drivers (controladores): permiten que el sistema use cada pieza.\n"
             "• Firmware: programa base grabado dentro de un dispositivo.\n"
             "• Aplicaciones: los programas que usamos."),
        ],
        "actividades": [
            {"id": "s2m1_a1", "tipo": "relacionar", "titulo": "Componente y su función", "puntos": 10, "categoria": "hardware",
             "pares": [("Ejecuta las instrucciones", "CPU"), ("Memoria de trabajo temporal", "RAM"),
                       ("Guarda datos a largo plazo", "SSD"), ("Procesa las imágenes", "Tarjeta gráfica")]},
            {"id": "s2m1_a2", "tipo": "clasificar", "titulo": "¿Hardware o software?", "puntos": 10, "categoria": "hardware",
             "categorias": ["Hardware", "Software"],
             "items": [("Tarjeta madre", "Hardware"), ("Driver de impresora", "Software"), ("Fuente de poder", "Hardware"),
                       ("Sistema operativo", "Software"), ("Memoria RAM", "Hardware"), ("Firmware", "Software")]},
            {"id": "s2m1_a3", "tipo": "clasificar", "titulo": "Arma la computadora correcta", "puntos": 15, "categoria": "hardware",
             "instruccion": "Clasifica cada componente según para qué computadora es más importante.",
             "categorias": ["PC para videojuegos", "PC de oficina"],
             "items": [("Tarjeta gráfica potente", "PC para videojuegos"), ("Procesador básico y bajo consumo", "PC de oficina"),
                       ("Mucha RAM y GPU", "PC para videojuegos"), ("Programas de texto y hoja de cálculo", "PC de oficina"),
                       ("Refrigeración avanzada", "PC para videojuegos"), ("SSD pequeño y económico", "PC de oficina")]},
            {"id": "s2m1_a4", "tipo": "seleccion", "titulo": "Analiza las necesidades", "puntos": 10, "categoria": "hardware",
             "preguntas": [
                {"pregunta": "Necesitas editar video. ¿Qué componente es MÁS importante reforzar?", "opciones": ["Tarjeta gráfica y RAM", "Bocinas", "Cámara web"], "correcta": 0},
                {"pregunta": "Quieres que los programas abran más rápido. ¿Qué conviene?", "opciones": ["Un SSD", "Un HDD más grande", "Más puertos USB"], "correcta": 0},
                {"pregunta": "¿Qué mide la velocidad del procesador?", "opciones": ["GHz", "Megapíxeles", "Decibeles"], "correcta": 0},
             ]},
            {"id": "s2m1_r1", "tipo": "reto", "nivel": "🟢 Fácil", "titulo": "Reto: la memoria de trabajo", "puntos": 5, "categoria": "hardware",
             "pregunta": "¿Qué componente guarda temporalmente lo que la computadora está usando en este momento?",
             "opciones": ["La RAM", "El disco duro", "La fuente de poder"], "correcta": 0,
             "pista": "Piensa en la memoria rápida que se borra al apagar el equipo."},
            {"id": "s2m1_r2", "tipo": "reto", "nivel": "🔴 Avanzado", "titulo": "Reto: análisis de rendimiento", "puntos": 15, "categoria": "hardware",
             "pregunta": "Una computadora abre programas muy lento y solo tiene 4 GB de RAM con un HDD. ¿Qué DOS cambios mejorarían más el rendimiento?",
             "opciones": ["Cambiar a SSD y aumentar la RAM", "Cambiar el mouse y el teclado", "Poner más bocinas y una cámara"], "correcta": 0,
             "pista": "El problema es la memoria de trabajo y la velocidad del almacenamiento, no los periféricos."},
        ],
        "evaluacion": [
            {"pregunta": "El 'cerebro' que ejecuta las instrucciones es...", "opciones": ["La CPU", "La fuente", "El monitor"], "correcta": 0},
            {"pregunta": "La RAM se caracteriza por...", "opciones": ["Ser memoria temporal y rápida", "Guardar todo para siempre", "Mostrar imágenes"], "correcta": 0},
            {"pregunta": "Comparado con un HDD, un SSD es...", "opciones": ["Más rápido y sin partes móviles", "Más lento", "Igual"], "correcta": 0},
            {"pregunta": "La tarjeta madre sirve para...", "opciones": ["Conectar todos los componentes", "Dar sonido", "Imprimir"], "correcta": 0},
            {"pregunta": "La GPU (tarjeta gráfica) es clave para...", "opciones": ["Juegos y edición de video", "Escribir texto", "Apagar la PC"], "correcta": 0},
            {"pregunta": "El puerto HDMI se usa para...", "opciones": ["Enviar video y audio a una pantalla", "Cargar el mouse", "Conectar a Internet por cable"], "correcta": 0},
            {"pregunta": "Un 'driver' o controlador...", "opciones": ["Permite que el sistema use una pieza", "Es un cable", "Es una silla"], "correcta": 0},
            {"pregunta": "El firmware es...", "opciones": ["Programa base dentro de un dispositivo", "Un tipo de mouse", "Una red"], "correcta": 0},
            {"pregunta": "Para conexión de red POR CABLE usamos...", "opciones": ["Ethernet", "Bluetooth", "HDMI"], "correcta": 0},
            {"pregunta": "La diferencia entre RAM y almacenamiento es que la RAM...", "opciones": ["Es temporal; el almacenamiento es permanente", "Es permanente", "No existe"], "correcta": 0},
        ],
    },
    # =================================================================================
    2: {
        "titulo": "Sistemas operativos y administración",
        "icono": "🖥️",
        "umbral": 40,
        "contenido": [
            ("El administrador de la computadora",
             "El sistema operativo (SO) controla el hardware, los programas y los archivos. Ejemplos: "
             "Windows y Linux (computadoras), Android e iOS (celulares)."),
            ("Usuarios y permisos",
             "Cada persona puede tener su usuario con su configuración. Los permisos deciden quién puede "
             "instalar programas o cambiar ajustes importantes (por eso a veces pide 'administrador')."),
            ("Instalar y desinstalar",
             "Instalar agrega un programa al sistema; desinstalar lo quita correctamente (mejor que solo "
             "borrar su carpeta). Las actualizaciones corrigen errores y mejoran la seguridad."),
            ("Procesos y administrador de tareas",
             "Cada programa abierto es un 'proceso' que usa memoria y procesador. El Administrador de tareas "
             "muestra qué está corriendo y permite cerrar un programa que no responde o que consume demasiado."),
        ],
        "actividades": [
            {"id": "s2m2_a1", "tipo": "clasificar", "titulo": "¿Qué SO es?", "puntos": 10, "categoria": "so",
             "categorias": ["Computadora", "Teléfono"],
             "items": [("Windows", "Computadora"), ("Android", "Teléfono"), ("Linux", "Computadora"),
                       ("iOS", "Teléfono")]},
            {"id": "s2m2_a2", "tipo": "ordenar", "titulo": "Instalar un programa correctamente", "puntos": 10, "categoria": "so",
             "instruccion": "Ordena los pasos:",
             "items": ["Descargar el instalador de un sitio oficial", "Ejecutar el instalador",
                       "Aceptar las opciones y esperar", "Abrir el programa ya instalado"]},
            {"id": "s2m2_a3", "tipo": "ordenar", "titulo": "Desinstalar correctamente", "puntos": 10, "categoria": "so",
             "instruccion": "Ordena los pasos:",
             "items": ["Abrir Configuración o Panel de control", "Ir a 'Aplicaciones'",
                       "Seleccionar el programa", "Elegir 'Desinstalar'"]},
            {"id": "s2m2_a4", "tipo": "problema", "titulo": "Un programa consume demasiados recursos", "puntos": 15, "categoria": "so",
             "pregunta": "La computadora va muy lenta y un programa aparece usando 90% del procesador. ¿Qué es lo más adecuado?",
             "opciones": ["Abrir el Administrador de tareas y cerrar ese programa", "Desconectar el monitor", "Quitar el teclado"],
             "correcta": 0,
             "explicacion": "El Administrador de tareas permite ver y cerrar el proceso que consume demasiados recursos."},
            {"id": "s2m2_r1", "tipo": "reto", "nivel": "🟡 Intermedio", "titulo": "Reto: permisos", "puntos": 10, "categoria": "so",
             "pregunta": "Al instalar un programa, el sistema pide permiso de 'administrador'. ¿Por qué?",
             "opciones": ["Porque instalar cambia el sistema y requiere autorización", "Porque el programa es un juego", "Porque no hay Internet"], "correcta": 0,
             "pista": "Piensa en quién debe autorizar cambios importantes en la computadora."},
        ],
        "evaluacion": [
            {"pregunta": "El sistema operativo sirve para...", "opciones": ["Administrar hardware, programas y archivos", "Solo jugar", "Nada"], "correcta": 0},
            {"pregunta": "¿Cuál es un SO de computadora?", "opciones": ["Linux", "Android", "iOS"], "correcta": 0},
            {"pregunta": "¿Cuál es un SO de teléfono?", "opciones": ["Android", "Windows", "Linux"], "correcta": 0},
            {"pregunta": "Los 'permisos' sirven para...", "opciones": ["Controlar quién hace cambios importantes", "Subir el volumen", "Imprimir"], "correcta": 0},
            {"pregunta": "Desinstalar un programa es mejor que...", "opciones": ["Solo borrar su carpeta", "Actualizarlo", "Usarlo"], "correcta": 0},
            {"pregunta": "Las actualizaciones sirven para...", "opciones": ["Corregir errores y mejorar seguridad", "Gastar batería", "Nada"], "correcta": 0},
            {"pregunta": "Un 'proceso' es...", "opciones": ["Un programa en ejecución", "Un cable", "Una carpeta"], "correcta": 0},
            {"pregunta": "El Administrador de tareas permite...", "opciones": ["Ver y cerrar procesos", "Cargar el mouse", "Navegar"], "correcta": 0},
            {"pregunta": "Si un programa 'no responde', puedo...", "opciones": ["Cerrarlo desde el Administrador de tareas", "Jalar el cable", "Golpear la PC"], "correcta": 0},
            {"pregunta": "Descargar programas conviene hacerlo desde...", "opciones": ["Sitios oficiales", "Enlaces desconocidos", "Cualquier lado"], "correcta": 0},
        ],
    },
    # =================================================================================
    3: {
        "titulo": "Productividad digital",
        "icono": "📊",
        "umbral": 80,
        "contenido": [
            ("Procesador de texto (nivel intermedio)",
             "Además de escribir, podemos aplicar estilos de título, párrafos, listas, insertar imágenes y "
             "tablas, poner encabezado y pie de página, y exportar el documento a PDF para compartirlo."),
            ("Presentaciones efectivas",
             "Una buena presentación usa poco texto, imágenes claras, un diseño ordenado y transiciones sin "
             "exagerar. Las diapositivas apoyan lo que dices, no lo reemplazan."),
            ("Hojas de cálculo",
             "Se organizan en filas, columnas y celdas. Con fórmulas hacemos cálculos automáticos:\n"
             "• SUMA: suma un rango.\n• PROMEDIO: saca el promedio.\n• MAX y MIN: mayor y menor valor.\n"
             "También podemos calcular porcentajes y crear gráficos."),
            ("Ejemplo de hoja de cálculo",
             "Notas: 80, 90, 70, 100.\n• SUMA = 340\n• PROMEDIO = 85\n• MAX = 100\n• MIN = 70\n"
             "Las fórmulas se actualizan solas si cambian los datos."),
        ],
        "actividades": [
            {"id": "s2m3_a1", "tipo": "relacionar", "titulo": "¿Qué función uso?", "puntos": 10, "categoria": "ofimatica",
             "pares": [("Sumar un rango de celdas", "SUMA"), ("Sacar el promedio", "PROMEDIO"),
                       ("Encontrar el valor más alto", "MAX"), ("Encontrar el valor más bajo", "MIN")]},
            {"id": "s2m3_a2", "tipo": "seleccion", "titulo": "Hoja de cálculo virtual (notas: 80, 90, 70, 100)", "puntos": 10, "categoria": "ofimatica",
             "preguntas": [
                {"pregunta": "¿Cuál es el PROMEDIO de 80, 90, 70 y 100?", "opciones": ["85", "80", "90"], "correcta": 0},
                {"pregunta": "¿Cuál es la nota MÁS ALTA (MAX)?", "opciones": ["100", "90", "80"], "correcta": 0},
                {"pregunta": "¿Cuál es la nota MÁS BAJA (MIN)?", "opciones": ["70", "80", "100"], "correcta": 0},
             ]},
            {"id": "s2m3_a3", "tipo": "clasificar", "titulo": "¿Qué herramienta uso?", "puntos": 10, "categoria": "ofimatica",
             "categorias": ["Procesador de texto", "Hoja de cálculo", "Presentaciones"],
             "items": [("Escribir un informe con portada", "Procesador de texto"), ("Calcular promedios de notas", "Hoja de cálculo"),
                       ("Exponer un tema con diapositivas", "Presentaciones"), ("Insertar encabezado y pie de página", "Procesador de texto"),
                       ("Hacer un gráfico de barras de datos", "Hoja de cálculo"), ("Agregar transiciones", "Presentaciones")]},
            {"id": "s2m3_a4", "tipo": "ordenar", "titulo": "Exportar un documento a PDF", "puntos": 10, "categoria": "ofimatica",
             "instruccion": "Ordena los pasos:",
             "items": ["Abrir el menú Archivo", "Elegir 'Exportar' o 'Guardar como'",
                       "Seleccionar el formato PDF", "Guardar el archivo"]},
            {"id": "s2m3_r1", "tipo": "reto", "nivel": "🔴 Avanzado", "titulo": "Reto: calcula el porcentaje", "puntos": 15, "categoria": "ofimatica",
             "pregunta": "En un examen de 25 preguntas un estudiante acertó 20. ¿Qué porcentaje obtuvo?",
             "opciones": ["80%", "75%", "20%"], "correcta": 0,
             "pista": "Porcentaje = (aciertos ÷ total) × 100. Aquí: 20 ÷ 25 × 100."},
        ],
        "evaluacion": [
            {"pregunta": "En una hoja de cálculo, el cruce de una fila y una columna es...", "opciones": ["Una celda", "Un párrafo", "Una diapositiva"], "correcta": 0},
            {"pregunta": "La función para sumar un rango es...", "opciones": ["SUMA", "MAX", "PROMEDIO"], "correcta": 0},
            {"pregunta": "PROMEDIO de 80, 90, 70, 100 =", "opciones": ["85", "90", "80"], "correcta": 0},
            {"pregunta": "MAX encuentra...", "opciones": ["El valor más alto", "El más bajo", "El promedio"], "correcta": 0},
            {"pregunta": "MIN encuentra...", "opciones": ["El valor más bajo", "El más alto", "La suma"], "correcta": 0},
            {"pregunta": "Para compartir un documento sin que se descuadre conviene exportarlo a...", "opciones": ["PDF", "MP3", "JPG"], "correcta": 0},
            {"pregunta": "Una buena presentación usa...", "opciones": ["Poco texto e imágenes claras", "Mucho texto en cada diapositiva", "Solo colores"], "correcta": 0},
            {"pregunta": "El encabezado y pie de página se usan en...", "opciones": ["El procesador de texto", "La calculadora", "El navegador"], "correcta": 0},
            {"pregunta": "Un gráfico de barras se crea a partir de...", "opciones": ["Datos de una hoja de cálculo", "Una foto", "Una canción"], "correcta": 0},
            {"pregunta": "Si acierto 20 de 25, obtengo...", "opciones": ["80%", "50%", "20%"], "correcta": 0},
        ],
    },
    # =================================================================================
    4: {
        "titulo": "Redes de computadoras",
        "icono": "🌐",
        "umbral": 120,
        "contenido": [
            ("¿Qué es una red?",
             "Una red es un grupo de dispositivos conectados que comparten información. Una LAN es una red "
             "local (una casa o escuela); una WAN cubre grandes distancias; Internet es la red más grande."),
            ("Los aparatos que arman la red",
             "• Router: conecta la red local con Internet y reparte la conexión.\n"
             "• Switch: une varios dispositivos dentro de la red local.\n"
             "• Módem: comunica con el proveedor de Internet.\n"
             "• Punto de acceso: da conexión Wi-Fi."),
            ("Cómo se identifican los dispositivos",
             "• Dirección IP: identifica a cada dispositivo dentro de la red (como una dirección de casa).\n"
             "• Dirección MAC: identificador único de cada tarjeta de red.\n"
             "• Cliente y servidor: el cliente pide, el servidor entrega la información."),
            ("Dos ayudantes de la red (idea general)",
             "• DNS: traduce el nombre de una página (google.com) a su dirección IP.\n"
             "• DHCP: entrega automáticamente una IP a cada dispositivo que se conecta."),
        ],
        "actividades": [
            {"id": "s2m4_a1", "tipo": "relacionar", "titulo": "Aparato de red y su función", "puntos": 10, "categoria": "redes",
             "pares": [("Reparte Internet a la red", "Router"), ("Une dispositivos en la red local", "Switch"),
                       ("Da conexión Wi-Fi", "Punto de acceso"), ("Se comunica con el proveedor", "Módem")]},
            {"id": "s2m4_a2", "tipo": "clasificar", "titulo": "¿LAN o WAN?", "puntos": 10, "categoria": "redes",
             "categorias": ["LAN (local)", "WAN (amplia)"],
             "items": [("La red de tu salón de clases", "LAN (local)"), ("Internet", "WAN (amplia)"),
                       ("La red de tu casa", "LAN (local)"), ("La red que une ciudades", "WAN (amplia)")]},
            {"id": "s2m4_a3", "tipo": "arrastrar", "titulo": "🖱️ Arma la red virtual", "puntos": 15, "categoria": "redes",
             "instruccion": "Arrastra cada elemento a su rol en la red para que todos se comuniquen.",
             "categorias": ["Conecta a Internet", "Dispositivos de la red"],
             "items": [{"texto": "📡 Router", "cat": "Conecta a Internet"}, {"texto": "💻 Computadora", "cat": "Dispositivos de la red"},
                       {"texto": "📱 Teléfono", "cat": "Dispositivos de la red"}, {"texto": "🖨️ Impresora", "cat": "Dispositivos de la red"},
                       {"texto": "🔀 Switch", "cat": "Conecta a Internet"}, {"texto": "💻 Laptop", "cat": "Dispositivos de la red"}]},
            {"id": "s2m4_a4", "tipo": "ordenar", "titulo": "Diagnóstico: 'No hay Internet'", "puntos": 15, "categoria": "redes",
             "instruccion": "Ordena los pasos para investigar el problema, del más simple al más complejo:",
             "items": ["Revisar si el cable/Wi-Fi está conectado", "Ver si el router tiene luces encendidas",
                       "Reiniciar el router", "Avisar al proveedor de Internet"]},
            {"id": "s2m4_r1", "tipo": "reto", "nivel": "🟡 Intermedio", "titulo": "Reto: ¿quién traduce el nombre?", "puntos": 10, "categoria": "redes",
             "pregunta": "Escribes 'escuela.com' y la computadora encuentra su dirección IP. ¿Qué servicio hizo la traducción?",
             "opciones": ["El DNS", "El cable HDMI", "La impresora"], "correcta": 0,
             "pista": "Traduce nombres de páginas a direcciones IP."},
        ],
        "evaluacion": [
            {"pregunta": "Una red sirve para...", "opciones": ["Conectar dispositivos y compartir información", "Imprimir solamente", "Nada"], "correcta": 0},
            {"pregunta": "La red de tu escuela es una...", "opciones": ["LAN", "WAN", "Impresora"], "correcta": 0},
            {"pregunta": "Internet es un ejemplo de...", "opciones": ["WAN (red amplia)", "LAN pequeña", "Un cable"], "correcta": 0},
            {"pregunta": "El router sirve para...", "opciones": ["Repartir Internet a la red", "Escribir texto", "Guardar fotos"], "correcta": 0},
            {"pregunta": "El switch sirve para...", "opciones": ["Unir dispositivos en la red local", "Dar sonido", "Imprimir"], "correcta": 0},
            {"pregunta": "La dirección IP...", "opciones": ["Identifica a un dispositivo en la red", "Es una canción", "Es un color"], "correcta": 0},
            {"pregunta": "La dirección MAC es...", "opciones": ["Un identificador único de la tarjeta de red", "Una fruta", "Un cable"], "correcta": 0},
            {"pregunta": "El DNS...", "opciones": ["Traduce nombres de páginas a IP", "Da energía", "Imprime"], "correcta": 0},
            {"pregunta": "El DHCP...", "opciones": ["Entrega automáticamente una IP", "Enfría la CPU", "Reproduce música"], "correcta": 0},
            {"pregunta": "Si no hay Internet, primero conviene revisar...", "opciones": ["El cable o el Wi-Fi", "El volumen", "El color del mouse"], "correcta": 0},
        ],
    },
    # =================================================================================
    5: {
        "titulo": "Internet y comunicación digital",
        "icono": "🔗",
        "umbral": 160,
        "contenido": [
            ("Cómo llega una página web",
             "Al escribir una URL, tu navegador pide la página a un servidor y este la envía. La URL tiene "
             "partes: protocolo (https), dominio (escuela.edu.gt) y a veces una ruta."),
            ("HTTP y HTTPS",
             "HTTP transporta la página; HTTPS es la versión segura (cifrada), se muestra con un candado 🔒. "
             "Para escribir datos personales, siempre debe ser HTTPS."),
            ("Servicios para comunicarnos y guardar",
             "• Correo electrónico y videollamadas para comunicarnos.\n"
             "• Almacenamiento en la nube para guardar archivos y abrirlos desde cualquier dispositivo.\n"
             "• Redes sociales: útiles, pero con comunicación responsable."),
            ("Información confiable",
             "Para una tarea, prefiere sitios oficiales o educativos (.edu, .gob), con autor y fecha, y "
             "contrasta con otra fuente. Desconfía de páginas llenas de anuncios o sin autor."),
        ],
        "actividades": [
            {"id": "s2m5_a1", "tipo": "clasificar", "titulo": "Partes de una URL", "puntos": 10, "categoria": "internet",
             "categorias": ["Protocolo", "Dominio"],
             "items": [("https", "Protocolo"), ("escuela.edu.gt", "Dominio"), ("http", "Protocolo"), ("wikipedia.org", "Dominio")]},
            {"id": "s2m5_a2", "tipo": "clasificar", "titulo": "🔒 ¿Página segura?", "puntos": 10, "categoria": "internet",
             "categorias": ["Segura (HTTPS)", "No segura (HTTP)"],
             "items": [("https://banco.com con candado", "Segura (HTTPS)"), ("http://sitio-raro.net sin candado", "No segura (HTTP)"),
                       ("https://escuela.edu.gt", "Segura (HTTPS)"), ("http://ofertas-gratis.xyz", "No segura (HTTP)")]},
            {"id": "s2m5_a3", "tipo": "seleccion", "titulo": "Navegador simulado: identifica", "puntos": 10, "categoria": "internet",
             "preguntas": [
                {"pregunta": "En https://biblioteca.edu.gt/tarea el DOMINIO es...", "opciones": ["biblioteca.edu.gt", "https", "/tarea"], "correcta": 0},
                {"pregunta": "El candado 🔒 en el navegador indica...", "opciones": ["Conexión segura (HTTPS)", "Que la página es lenta", "Que hay virus"], "correcta": 0},
                {"pregunta": "Para escribir tu contraseña, la página debe ser...", "opciones": ["HTTPS", "HTTP", "Cualquiera"], "correcta": 0},
             ]},
            {"id": "s2m5_r1", "tipo": "reto", "nivel": "🔴 Avanzado", "titulo": "Reto: ¿cuál usarías para la tarea?", "puntos": 15, "categoria": "internet",
             "pregunta": "Para investigar una tarea, ¿cuál página es MÁS confiable?",
             "opciones": ["Un sitio .edu con autor, fecha y fuentes", "Un blog anónimo lleno de anuncios", "Una publicación sin autor que promete premios"], "correcta": 0,
             "pista": "Busca autor, fecha, tipo de dominio (.edu/.gob) y pocas señales de publicidad engañosa."},
            {"id": "s2m5_a4", "tipo": "relacionar", "titulo": "Servicio digital y su uso", "puntos": 10, "categoria": "internet",
             "pares": [("Guardar archivos y abrirlos desde cualquier lugar", "Nube"), ("Enviar mensajes con archivos", "Correo"),
                       ("Hablar viéndonos", "Videollamada"), ("Versión segura de la web", "HTTPS")]},
        ],
        "evaluacion": [
            {"pregunta": "En una URL, 'https' es el...", "opciones": ["Protocolo", "Dominio", "Color"], "correcta": 0},
            {"pregunta": "El dominio en https://escuela.edu.gt es...", "opciones": ["escuela.edu.gt", "https", "gt solamente"], "correcta": 0},
            {"pregunta": "HTTPS se diferencia de HTTP porque...", "opciones": ["Es seguro (cifrado)", "Es más lento", "No sirve"], "correcta": 0},
            {"pregunta": "El candado 🔒 significa...", "opciones": ["Conexión segura", "Página divertida", "Virus"], "correcta": 0},
            {"pregunta": "La nube sirve para...", "opciones": ["Guardar y acceder a archivos desde cualquier lugar", "Enfriar la PC", "Imprimir"], "correcta": 0},
            {"pregunta": "Una fuente confiable suele tener...", "opciones": ["Autor y fecha", "Muchos anuncios engañosos", "Nada"], "correcta": 0},
            {"pregunta": "Antes de escribir datos personales, la página debe ser...", "opciones": ["HTTPS", "HTTP", "Cualquiera"], "correcta": 0},
            {"pregunta": "El navegador pide la página a un...", "opciones": ["Servidor", "Teclado", "Mouse"], "correcta": 0},
            {"pregunta": "Comunicación responsable en redes significa...", "opciones": ["Respetar y cuidar lo que compartimos", "Insultar", "Dar datos a extraños"], "correcta": 0},
            {"pregunta": "Un dominio .edu suele indicar un sitio...", "opciones": ["Educativo", "De juegos", "Peligroso"], "correcta": 0},
        ],
    },
    # =================================================================================
    6: {
        "titulo": "Seguridad informática",
        "icono": "🔐",
        "umbral": 200,
        "contenido": [
            ("Proteger la información",
             "La seguridad informática cuida nuestros datos y equipos. Bases: contraseñas fuertes, no "
             "compartirlas y activar la verificación en dos pasos (2FA), un código extra al iniciar sesión."),
            ("Programas dañinos (malware)",
             "• Virus: se copia y daña archivos.\n• Troyano: se disfraza de algo útil.\n"
             "• Spyware: espía lo que haces.\n• Ransomware: 'secuestra' tus archivos y pide dinero.\n"
             "Nos protegemos con antivirus, actualizaciones y descargas de sitios oficiales."),
            ("Engaños humanos",
             "• Phishing: mensajes falsos que imitan a bancos o servicios para robar datos.\n"
             "• Ingeniería social: engañar a la persona para que entregue información o haga clic.\n"
             "Señales: remitente extraño, urgencia, enlaces raros, pedir contraseñas."),
            ("Buenas prácticas",
             "Haz copias de seguridad, mantén todo actualizado, cuida tu huella digital y usa el Wi-Fi público "
             "con cuidado (evita escribir contraseñas importantes en redes abiertas)."),
        ],
        "actividades": [
            {"id": "s2m6_a1", "tipo": "relacionar", "titulo": "Tipo de malware", "puntos": 10, "categoria": "seguridad",
             "pares": [("Se disfraza de algo útil", "Troyano"), ("Secuestra tus archivos y pide dinero", "Ransomware"),
                       ("Espía lo que haces", "Spyware"), ("Se copia y daña archivos", "Virus")]},
            {"id": "s2m6_a2", "tipo": "clasificar", "titulo": "🕵️ Detective de seguridad: ¿seguro o sospechoso?", "puntos": 15, "categoria": "seguridad",
             "instruccion": "Clasifica cada mensaje o situación.",
             "categorias": ["Seguro", "Sospechoso"],
             "items": [("Correo de un banco que pide tu contraseña 'urgente' por un enlace", "Sospechoso"),
                       ("Tu profesor comparte una tarea en la plataforma oficial", "Seguro"),
                       ("Mensaje: '¡Ganaste! Da tus datos ya'", "Sospechoso"),
                       ("Activar verificación en dos pasos", "Seguro"),
                       ("Archivo .exe de un desconocido", "Sospechoso"),
                       ("Actualizar el antivirus", "Seguro")]},
            {"id": "s2m6_a3", "tipo": "seleccion", "titulo": "Señales de phishing", "puntos": 10, "categoria": "seguridad",
             "preguntas": [
                {"pregunta": "¿Cuál NO es una señal típica de phishing?", "opciones": ["Un saludo normal de un amigo conocido", "Urgencia exagerada", "Pedir tu contraseña por enlace"], "correcta": 0},
                {"pregunta": "La verificación en dos pasos (2FA) sirve para...", "opciones": ["Añadir seguridad extra al iniciar sesión", "Ir más rápido", "Borrar archivos"], "correcta": 0},
                {"pregunta": "El ransomware...", "opciones": ["Secuestra archivos y pide dinero", "Es un antivirus", "Es un cable"], "correcta": 0},
             ]},
            {"id": "s2m6_a4", "tipo": "problema", "titulo": "Un correo sospechoso", "puntos": 15, "categoria": "seguridad",
             "pregunta": "Recibes un correo del 'banco' con un enlace que pide tu usuario y contraseña 'o se cerrará tu cuenta hoy'. ¿Qué haces?",
             "opciones": ["No hago clic, no doy datos y verifico por el sitio oficial", "Hago clic y escribo mis datos rápido", "Reenvío el correo a mis amigos"],
             "correcta": 0,
             "explicacion": "Es phishing: usa urgencia y pide datos por un enlace. Nunca ingreses datos así; entra al sitio oficial directamente."},
            {"id": "s2m6_r1", "tipo": "reto", "nivel": "🔴 Avanzado", "titulo": "Reto: analiza el caso", "puntos": 15, "categoria": "seguridad",
             "pregunta": "Un mensaje dice: 'Soporte técnico: instala este programa para arreglar tu PC y danos acceso remoto'. ¿Qué tipo de ataque es?",
             "opciones": ["Ingeniería social (te engañan para dar acceso)", "Una actualización normal", "Un antivirus"], "correcta": 0,
             "pista": "No es un virus por sí solo: buscan CONVENCERTE a ti de darles el control."},
        ],
        "evaluacion": [
            {"pregunta": "La seguridad informática protege...", "opciones": ["Nuestros datos y equipos", "El volumen", "La pantalla"], "correcta": 0},
            {"pregunta": "La verificación en dos pasos (2FA)...", "opciones": ["Agrega un código extra de seguridad", "Borra archivos", "Da Internet"], "correcta": 0},
            {"pregunta": "El phishing es...", "opciones": ["Un engaño para robar datos", "Un antivirus", "Un juego"], "correcta": 0},
            {"pregunta": "Un troyano...", "opciones": ["Se disfraza de algo útil", "Enfría la PC", "Es un cable"], "correcta": 0},
            {"pregunta": "El ransomware...", "opciones": ["Secuestra archivos y pide dinero", "Da energía", "Imprime"], "correcta": 0},
            {"pregunta": "La ingeniería social ataca...", "opciones": ["A la persona (la engaña)", "Solo al cable", "A la impresora"], "correcta": 0},
            {"pregunta": "Una señal de mensaje sospechoso es...", "opciones": ["Urgencia y pedir contraseñas", "Un saludo normal", "Nada"], "correcta": 0},
            {"pregunta": "Las copias de seguridad sirven para...", "opciones": ["No perder la información", "Gastar batería", "Nada"], "correcta": 0},
            {"pregunta": "En Wi-Fi público conviene...", "opciones": ["Evitar escribir contraseñas importantes", "Compartir todo", "Apagar el antivirus"], "correcta": 0},
            {"pregunta": "Ante un correo que pide datos por enlace debo...", "opciones": ["No hacer clic y verificar por el sitio oficial", "Dar mis datos", "Reenviarlo"], "correcta": 0},
        ],
    },
    # =================================================================================
    7: {
        "titulo": "Pensamiento lógico y resolución de problemas",
        "icono": "🧩",
        "umbral": 240,
        "contenido": [
            ("Patrones más complejos",
             "Algunos patrones se multiplican o combinan operaciones.\nEjemplo: 2 → 4 → 8 → 16 → ? "
             "(cada número se multiplica por 2, así que sigue 32)."),
            ("Lógica: verdadero y falso",
             "Una tabla de verdad muestra el resultado de combinar condiciones.\n"
             "• Y (AND): verdadero solo si AMBAS son verdaderas.\n"
             "• O (OR): verdadero si AL MENOS UNA es verdadera."),
            ("Problemas de varios pasos",
             "Para resolverlos: 1) entiende qué se pide, 2) separa en pasos, 3) resuelve por partes, "
             "4) revisa el resultado. La estrategia importa tanto como la respuesta."),
        ],
        "actividades": [
            {"id": "s2m7_a1", "tipo": "patron", "titulo": "🟢 Secuencias (fácil)", "puntos": 10, "categoria": "logica",
             "patrones": [
                {"secuencia": "2 - 4 - 8 - 16 -", "opciones": ["24", "32", "18"], "correcta": 1},
                {"secuencia": "1 - 3 - 9 - 27 -", "opciones": ["54", "81", "36"], "correcta": 1},
             ]},
            {"id": "s2m7_a2", "tipo": "patron", "titulo": "🟡 Secuencias (intermedio)", "puntos": 10, "categoria": "logica",
             "patrones": [
                {"secuencia": "1 - 1 - 2 - 3 - 5 - 8 -", "opciones": ["11", "13", "10"], "correcta": 1},
                {"secuencia": "100 - 90 - 81 - 73 -", "opciones": ["66", "64", "70"], "correcta": 0},
             ]},
            {"id": "s2m7_a3", "tipo": "seleccion", "titulo": "🔴 Tablas de verdad (avanzado)", "puntos": 15, "categoria": "logica",
             "preguntas": [
                {"pregunta": "Verdadero Y (AND) Falso = ?", "opciones": ["Falso", "Verdadero"], "correcta": 0},
                {"pregunta": "Verdadero O (OR) Falso = ?", "opciones": ["Verdadero", "Falso"], "correcta": 0},
                {"pregunta": "Falso Y (AND) Falso = ?", "opciones": ["Falso", "Verdadero"], "correcta": 0},
             ]},
            {"id": "s2m7_a4", "tipo": "problema", "titulo": "Problema de varios pasos", "puntos": 15, "categoria": "logica",
             "pregunta": "Un salón tiene 30 estudiantes. La mitad son niñas y de los niños, 6 usan lentes. ¿Cuántos niños NO usan lentes?",
             "opciones": ["9", "15", "6"], "correcta": 0,
             "explicacion": "Mitad de 30 = 15 niñas, entonces 15 niños. 15 - 6 = 9 niños sin lentes."},
            {"id": "s2m7_r1", "tipo": "reto", "nivel": "🔴 Avanzado", "titulo": "Reto: optimización", "puntos": 15, "categoria": "logica",
             "pregunta": "Debes copiar 3 archivos grandes. Copiar uno por uno toma 9 minutos en total. Si los copias a la vez y el tiempo total es el del archivo más lento (4 min), ¿qué estrategia es mejor?",
             "opciones": ["Copiarlos a la vez (4 min)", "Uno por uno (9 min)", "No copiarlos"], "correcta": 0,
             "pista": "Compara el tiempo total de cada estrategia: 4 minutos contra 9 minutos."},
        ],
        "evaluacion": [
            {"pregunta": "2 - 4 - 8 - 16 - __", "opciones": ["32", "24", "20"], "correcta": 0},
            {"pregunta": "1 - 3 - 9 - 27 - __", "opciones": ["81", "54", "36"], "correcta": 0},
            {"pregunta": "En la serie de Fibonacci 1,1,2,3,5,8 sigue...", "opciones": ["13", "11", "16"], "correcta": 0},
            {"pregunta": "Verdadero Y (AND) Falso =", "opciones": ["Falso", "Verdadero"], "correcta": 0},
            {"pregunta": "Verdadero O (OR) Falso =", "opciones": ["Verdadero", "Falso"], "correcta": 0},
            {"pregunta": "Para un problema de varios pasos conviene...", "opciones": ["Separarlo en partes", "Adivinar", "Ignorarlo"], "correcta": 0},
            {"pregunta": "De 15 niños, 6 usan lentes; sin lentes hay...", "opciones": ["9", "6", "15"], "correcta": 0},
            {"pregunta": "Optimizar significa...", "opciones": ["Lograr el mejor resultado con menos esfuerzo/tiempo", "Complicar", "Rendirse"], "correcta": 0},
            {"pregunta": "AND (Y) es verdadero cuando...", "opciones": ["Ambas condiciones son verdaderas", "Solo una", "Ninguna"], "correcta": 0},
            {"pregunta": "OR (O) es verdadero cuando...", "opciones": ["Al menos una es verdadera", "Ambas son falsas", "Nunca"], "correcta": 0},
        ],
    },
    # =================================================================================
    8: {
        "titulo": "Algoritmos y diagramas de flujo",
        "icono": "🔀",
        "umbral": 280,
        "contenido": [
            ("Algoritmo: entrada, proceso y salida",
             "Un algoritmo es una serie de pasos ordenados. Casi siempre tiene: ENTRADA (datos que recibe), "
             "PROCESO (lo que hace) y SALIDA (el resultado)."),
            ("Los símbolos del diagrama de flujo",
             "• Óvalo: Inicio / Fin.\n• Rectángulo: Proceso (una acción).\n"
             "• Rombo: Decisión (una pregunta con SÍ/NO).\n• Flechas: indican el orden."),
            ("Ejemplo: ¿aprobó o reprobó?",
             "Inicio → Ingresar la nota → ¿nota ≥ 60? → (SÍ) 'Aprobado' / (NO) 'Reprobado' → Fin.\n"
             "El rombo de decisión separa los dos caminos posibles."),
        ],
        "actividades": [
            {"id": "s2m8_a1", "tipo": "relacionar", "titulo": "Símbolo del diagrama de flujo", "puntos": 10, "categoria": "algoritmos",
             "pares": [("Inicio / Fin", "Óvalo"), ("Un proceso o acción", "Rectángulo"),
                       ("Una decisión (SÍ/NO)", "Rombo"), ("Indican el orden", "Flechas")]},
            {"id": "s2m8_a2", "tipo": "clasificar", "titulo": "Entrada, proceso o salida", "puntos": 10, "categoria": "algoritmos",
             "categorias": ["Entrada", "Proceso", "Salida"],
             "items": [("Ingresar la nota", "Entrada"), ("Comparar la nota con 60", "Proceso"), ("Mostrar 'Aprobado'", "Salida"),
                       ("Pedir la edad", "Entrada"), ("Calcular el promedio", "Proceso"), ("Imprimir el resultado", "Salida")]},
            {"id": "s2m8_a3", "tipo": "ordenar", "titulo": "Arma el diagrama: ¿aprobó?", "puntos": 15, "categoria": "algoritmos",
             "instruccion": "Ordena los bloques del diagrama de flujo:",
             "items": ["Inicio", "Ingresar la nota", "¿La nota es mayor o igual a 60?",
                       "Mostrar 'Aprobado' o 'Reprobado'", "Fin"]},
            {"id": "s2m8_a4", "tipo": "ordenar", "titulo": "Algoritmo: promedio de 3 notas", "puntos": 15, "categoria": "algoritmos",
             "instruccion": "Ordena los pasos del algoritmo:",
             "items": ["Inicio", "Ingresar las 3 notas", "Sumar las 3 notas", "Dividir la suma entre 3", "Mostrar el promedio", "Fin"]},
            {"id": "s2m8_r1", "tipo": "reto", "nivel": "🟡 Intermedio", "titulo": "Reto: la decisión", "puntos": 10, "categoria": "algoritmos",
             "pregunta": "En el diagrama '¿aprobó?', ¿qué símbolo representa la pregunta '¿nota ≥ 60?'?",
             "opciones": ["El rombo (decisión)", "El óvalo (inicio/fin)", "El rectángulo (proceso)"], "correcta": 0,
             "pista": "Es el símbolo que separa dos caminos: SÍ y NO."},
        ],
        "evaluacion": [
            {"pregunta": "Un algoritmo casi siempre tiene...", "opciones": ["Entrada, proceso y salida", "Solo colores", "Nada"], "correcta": 0},
            {"pregunta": "El óvalo en un diagrama de flujo indica...", "opciones": ["Inicio o Fin", "Una decisión", "Una flecha"], "correcta": 0},
            {"pregunta": "El rectángulo indica...", "opciones": ["Un proceso o acción", "Inicio", "Una pregunta"], "correcta": 0},
            {"pregunta": "El rombo indica...", "opciones": ["Una decisión (SÍ/NO)", "El fin", "Una acción"], "correcta": 0},
            {"pregunta": "Las flechas sirven para...", "opciones": ["Indicar el orden", "Dar color", "Nada"], "correcta": 0},
            {"pregunta": "'Ingresar la nota' es un paso de...", "opciones": ["Entrada", "Salida", "Fin"], "correcta": 0},
            {"pregunta": "'Mostrar Aprobado' es un paso de...", "opciones": ["Salida", "Entrada", "Decisión"], "correcta": 0},
            {"pregunta": "En '¿nota ≥ 60?' si es SÍ...", "opciones": ["Aprobado", "Reprobado", "Fin sin más"], "correcta": 0},
            {"pregunta": "Para el promedio de 3 notas, después de sumarlas hay que...", "opciones": ["Dividir entre 3", "Multiplicar por 3", "Restar 3"], "correcta": 0},
            {"pregunta": "El diagrama de flujo sirve para...", "opciones": ["Planear un algoritmo antes de programar", "Escuchar música", "Imprimir"], "correcta": 0},
        ],
    },
    # =================================================================================
    9: {
        "titulo": "Introducción a la programación",
        "icono": "🧑‍💻",
        "umbral": 320,
        "contenido": [
            ("Variables, constantes y datos",
             "• Variable: una 'caja' con nombre que guarda un valor que puede cambiar (edad = 13).\n"
             "• Constante: un valor que NO cambia (PI = 3.14).\n"
             "• Tipos de datos: números y texto (cadenas)."),
            ("Operadores",
             "• Matemáticos: + - × ÷.\n• Comparación: > (mayor), < (menor), == (igual).\n"
             "El resultado de una comparación es verdadero o falso."),
            ("Condicionales (SI / SINO)",
             "Permiten decidir:\nSI edad ≥ 13 → MOSTRAR 'Puedes continuar'\nSINO → MOSTRAR 'Debes consultar'."),
            ("Ciclos, funciones y errores",
             "• Ciclo (bucle): repite instrucciones (por ejemplo, 5 veces).\n"
             "• Función: un bloque con nombre que hace una tarea y se puede reutilizar.\n"
             "• Error (bug): fallo en el programa; corregirlo se llama depurar."),
        ],
        "actividades": [
            {"id": "s2m9_a1", "tipo": "relacionar", "titulo": "Concepto de programación", "puntos": 10, "categoria": "programacion",
             "pares": [("Caja con nombre que guarda un valor", "Variable"), ("Valor que no cambia", "Constante"),
                       ("Repite instrucciones", "Ciclo"), ("Corregir errores", "Depurar")]},
            {"id": "s2m9_a2", "tipo": "seleccion", "titulo": "Operadores y comparaciones", "puntos": 10, "categoria": "programacion",
             "preguntas": [
                {"pregunta": "¿El resultado de 7 > 3 es...?", "opciones": ["Verdadero", "Falso"], "correcta": 0},
                {"pregunta": "¿El resultado de 5 == 8 es...?", "opciones": ["Falso", "Verdadero"], "correcta": 0},
                {"pregunta": "El operador '==' compara si dos valores...", "opciones": ["Son iguales", "Se suman", "Se restan"], "correcta": 0},
             ]},
            {"id": "s2m9_a3", "tipo": "ordenar", "titulo": "Ordena el programa (SI/SINO)", "puntos": 15, "categoria": "programacion",
             "instruccion": "Ordena los bloques del programa:",
             "items": ["Pedir la edad", "SI edad >= 13", "MOSTRAR 'Puedes continuar'", "SINO", "MOSTRAR 'Debes consultar'"]},
            {"id": "s2m9_a4", "tipo": "bloques", "titulo": "🤖 Programa al robot con ciclos", "puntos": 15, "categoria": "programacion",
             "instruccion": "Usa AVANZAR y los giros para llevar el robot 🤖 al tesoro 🎯. ¡Planea la ruta!",
             "mapa": [[0, 0, 0, 0, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]],
             "inicio": [0, 0], "meta": [4, 4], "mirando": "derecha"},
            {"id": "s2m9_r1", "tipo": "reto", "nivel": "🔴 Avanzado", "titulo": "Reto: ¿qué muestra el programa?", "puntos": 15, "categoria": "programacion",
             "pregunta": "Si edad = 12 y el programa dice: SI edad >= 13 MOSTRAR 'Puedes continuar' SINO MOSTRAR 'Debes consultar'. ¿Qué muestra?",
             "opciones": ["Debes consultar", "Puedes continuar", "Un error"], "correcta": 0,
             "pista": "¿12 es mayor o igual a 13? Si la condición es falsa, se ejecuta el SINO."},
        ],
        "evaluacion": [
            {"pregunta": "Una variable es...", "opciones": ["Una caja con nombre que guarda un valor", "Un cable", "Una silla"], "correcta": 0},
            {"pregunta": "Una constante...", "opciones": ["No cambia de valor", "Cambia siempre", "Es un error"], "correcta": 0},
            {"pregunta": "El resultado de 7 > 3 es...", "opciones": ["Verdadero", "Falso"], "correcta": 0},
            {"pregunta": "El operador '==' compara si...", "opciones": ["Dos valores son iguales", "Uno es mayor", "Se suman"], "correcta": 0},
            {"pregunta": "Un condicional (SI/SINO) sirve para...", "opciones": ["Decidir según una condición", "Repetir siempre", "Nada"], "correcta": 0},
            {"pregunta": "Si edad = 12 y se pide edad >= 13, se ejecuta...", "opciones": ["El SINO", "El SI", "Un error"], "correcta": 0},
            {"pregunta": "Un ciclo (bucle) sirve para...", "opciones": ["Repetir instrucciones", "Borrar", "Apagar"], "correcta": 0},
            {"pregunta": "Una función es...", "opciones": ["Un bloque con nombre que se reutiliza", "Un virus", "Un cable"], "correcta": 0},
            {"pregunta": "Un 'bug' es...", "opciones": ["Un error en el programa", "Un premio", "Una red"], "correcta": 0},
            {"pregunta": "Depurar significa...", "opciones": ["Buscar y corregir errores", "Apagar", "Copiar"], "correcta": 0},
        ],
    },
    # =================================================================================
    10: {
        "titulo": "Datos y bases de datos",
        "icono": "🗃️",
        "umbral": 360,
        "contenido": [
            ("De datos a información",
             "Un dato es un valor suelto (14). La información es un dato con significado (Ana tiene 14 años). "
             "Organizar los datos nos permite entenderlos y usarlos."),
            ("Cómo se organizan los datos",
             "• Tabla: organiza datos en filas y columnas.\n• Fila (registro): todos los datos de un elemento (un estudiante).\n"
             "• Columna (campo): un tipo de dato (la edad de todos).\n"
             "• Llave o identificador (ID): valor único que distingue cada registro."),
            ("Qué podemos hacer con una base de datos",
             "• Buscar un registro (por su ID o nombre).\n• Filtrar (mostrar solo los que cumplen algo, "
             "por ejemplo edad = 14).\n• Ordenar (por nombre, por edad...)."),
            ("Ejemplo de tabla de estudiantes",
             "ID  | Nombre | Grado | Edad\n001 | Ana    | 2.º   | 14\n002 | Carlos | 2.º   | 15\n"
             "003 | Luis   | 2.º   | 14\n\nAquí 'ID' es la llave, cada fila es un registro y 'Edad' es un campo."),
        ],
        "actividades": [
            {"id": "s2m10_a1", "tipo": "relacionar", "titulo": "Vocabulario de bases de datos", "puntos": 10, "categoria": "datos",
             "pares": [("Todos los datos de un estudiante", "Registro (fila)"), ("Un tipo de dato (la edad)", "Campo (columna)"),
                       ("Valor único que identifica", "Llave (ID)"), ("Organiza datos en filas y columnas", "Tabla")]},
            {"id": "s2m10_a2", "tipo": "seleccion", "titulo": "Consulta la base de datos", "puntos": 15, "categoria": "datos",
             "preguntas": [
                {"pregunta": "En la tabla (Ana 14, Carlos 15, Luis 14), si FILTRAS por edad = 14, ¿quiénes aparecen?", "opciones": ["Ana y Luis", "Solo Carlos", "Todos"], "correcta": 0},
                {"pregunta": "¿Cuál es la llave (identificador único)?", "opciones": ["El ID", "El grado", "La edad"], "correcta": 0},
                {"pregunta": "Si ORDENAS los nombres alfabéticamente, ¿quién va primero?", "opciones": ["Ana", "Carlos", "Luis"], "correcta": 0},
             ]},
            {"id": "s2m10_a3", "tipo": "ordenar", "titulo": "Ordena los nombres (A→Z)", "puntos": 10, "categoria": "datos",
             "instruccion": "Ordena alfabéticamente de la A a la Z:",
             "items": ["Ana", "Carlos", "Luis", "Sofía"]},
            {"id": "s2m10_a4", "tipo": "clasificar", "titulo": "¿Dato o información?", "puntos": 10, "categoria": "datos",
             "categorias": ["Dato suelto", "Información"],
             "items": [("14", "Dato suelto"), ("Ana tiene 14 años", "Información"), ("2.º", "Dato suelto"),
                       ("Carlos está en 2.º básico", "Información")]},
            {"id": "s2m10_r1", "tipo": "reto", "nivel": "🟡 Intermedio", "titulo": "Reto: encuentra el registro", "puntos": 10, "categoria": "datos",
             "pregunta": "Quieres los datos del estudiante con ID 002 (Carlos, 15). Para encontrar UN registro exacto, ¿por qué campo conviene buscar?",
             "opciones": ["Por el ID (es único)", "Por la edad (se repite)", "Por el grado (todos igual)"], "correcta": 0,
             "pista": "Busca por el campo que NO se repite en ningún otro registro."},
        ],
        "evaluacion": [
            {"pregunta": "Un dato es...", "opciones": ["Un valor suelto", "Una red", "Un cable"], "correcta": 0},
            {"pregunta": "La información es...", "opciones": ["Un dato con significado", "Un error", "Un virus"], "correcta": 0},
            {"pregunta": "Una fila en una tabla es un...", "opciones": ["Registro", "Campo", "Gráfico"], "correcta": 0},
            {"pregunta": "Una columna es un...", "opciones": ["Campo", "Registro", "Botón"], "correcta": 0},
            {"pregunta": "La llave (ID) sirve para...", "opciones": ["Identificar de forma única un registro", "Sumar", "Apagar"], "correcta": 0},
            {"pregunta": "Filtrar significa...", "opciones": ["Mostrar solo los que cumplen algo", "Borrar todo", "Ordenar"], "correcta": 0},
            {"pregunta": "Ordenar significa...", "opciones": ["Acomodar según un criterio", "Eliminar", "Copiar"], "correcta": 0},
            {"pregunta": "Filtrando edad = 14 (Ana 14, Carlos 15, Luis 14) aparecen...", "opciones": ["Ana y Luis", "Solo Carlos", "Nadie"], "correcta": 0},
            {"pregunta": "Para encontrar un registro exacto conviene buscar por...", "opciones": ["Un campo único (ID)", "Un campo repetido", "El color"], "correcta": 0},
            {"pregunta": "Una tabla organiza datos en...", "opciones": ["Filas y columnas", "Cables", "Ventanas"], "correcta": 0},
        ],
    },
    # =================================================================================
    11: {
        "titulo": "Inteligencia artificial y tecnologías emergentes",
        "icono": "🤖",
        "umbral": 400,
        "contenido": [
            ("¿Cómo 'aprende' una IA?",
             "La IA analiza MUCHOS datos y ejemplos para encontrar patrones. Con esos patrones puede reconocer "
             "imágenes o voz, traducir, recomendar contenido o generar texto. No 'piensa' como una persona: "
             "calcula probabilidades a partir de lo que aprendió."),
            ("IA en el día a día",
             "Reconocimiento de imágenes y de voz, recomendaciones, traducción automática, chatbots y la IA "
             "generativa (crea textos e imágenes). Todo se basa en datos y patrones."),
            ("Ventajas, límites y errores",
             "Ventajas: rapidez y ayuda en tareas repetitivas. Límites: puede equivocarse o 'inventar' datos "
             "(información falsa). Por eso SIEMPRE hay que verificar lo que genera una IA."),
            ("Tecnologías emergentes",
             "• Automatización: máquinas que hacen tareas repetitivas.\n• Robótica: robots que actúan en el mundo real.\n"
             "• Internet de las cosas (IoT): objetos cotidianos conectados a Internet (focos, relojes, sensores)."),
        ],
        "actividades": [
            {"id": "s2m11_a1", "tipo": "clasificar", "titulo": "🤖 Entrena al clasificador (patrones)", "puntos": 15, "categoria": "ia",
             "instruccion": "Como una IA, agrupa cada elemento según su patrón/categoría.",
             "categorias": ["Frutas", "Animales", "Vehículos"],
             "items": [("Manzana", "Frutas"), ("Perro", "Animales"), ("Carro", "Vehículos"),
                       ("Banano", "Frutas"), ("Gato", "Animales"), ("Avión", "Vehículos")]},
            {"id": "s2m11_a2", "tipo": "relacionar", "titulo": "Ejemplo de IA y su tarea", "puntos": 10, "categoria": "ia",
             "pares": [("Identifica objetos en una foto", "Reconocimiento de imágenes"), ("Convierte tu voz en texto", "Reconocimiento de voz"),
                       ("Cambia un texto a otro idioma", "Traducción automática"), ("Crea textos o imágenes nuevas", "IA generativa")]},
            {"id": "s2m11_a3", "tipo": "seleccion", "titulo": "Ventajas y límites de la IA", "puntos": 10, "categoria": "ia",
             "preguntas": [
                {"pregunta": "¿La IA puede equivocarse o inventar datos?", "opciones": ["Sí, por eso hay que verificar", "No, nunca"], "correcta": 0},
                {"pregunta": "La IA aprende principalmente de...", "opciones": ["Muchos datos y ejemplos", "La suerte", "Nada"], "correcta": 0},
                {"pregunta": "El Internet de las cosas (IoT) conecta...", "opciones": ["Objetos cotidianos a Internet", "Solo computadoras grandes", "Nada"], "correcta": 0},
             ]},
            {"id": "s2m11_r1", "tipo": "reto", "nivel": "🔴 Avanzado", "titulo": "Reto: verifica a la IA", "puntos": 15, "categoria": "ia",
             "pregunta": "Una IA responde: 'La capital de Guatemala es Quetzaltenango y tiene 3 soles'. ¿Qué debes hacer?",
             "opciones": ["Verificar: contiene errores (la capital es Ciudad de Guatemala y hay un solo Sol)", "Creerlo tal cual", "Compartirlo sin revisar"], "correcta": 0,
             "pista": "La IA puede sonar segura y aun así equivocarse. Contrasta cada dato con una fuente confiable."},
        ],
        "evaluacion": [
            {"pregunta": "La IA aprende de...", "opciones": ["Muchos datos y ejemplos", "La magia", "Nada"], "correcta": 0},
            {"pregunta": "¿La IA siempre acierta?", "opciones": ["No, puede equivocarse", "Sí, siempre", "Nunca funciona"], "correcta": 0},
            {"pregunta": "Reconocer una cara en una foto es...", "opciones": ["Reconocimiento de imágenes", "Traducción", "Un cable"], "correcta": 0},
            {"pregunta": "La IA generativa...", "opciones": ["Crea textos o imágenes", "Enfría la PC", "Imprime"], "correcta": 0},
            {"pregunta": "Ante una respuesta de IA importante debo...", "opciones": ["Verificarla con una fuente confiable", "Creerla siempre", "Ignorar todo"], "correcta": 0},
            {"pregunta": "La automatización se refiere a...", "opciones": ["Máquinas que hacen tareas repetitivas", "Un juego", "Un color"], "correcta": 0},
            {"pregunta": "El IoT (Internet de las cosas) conecta...", "opciones": ["Objetos cotidianos a Internet", "Solo teléfonos", "Nada"], "correcta": 0},
            {"pregunta": "Un chatbot es...", "opciones": ["Un programa que conversa usando IA", "Una impresora", "Un cable"], "correcta": 0},
            {"pregunta": "La IA para estudiar debe usarse...", "opciones": ["De forma responsable y verificando", "Para copiar sin pensar", "Nunca"], "correcta": 0},
            {"pregunta": "La base del funcionamiento de la IA son...", "opciones": ["Los datos y los patrones", "Las bocinas", "Los cables"], "correcta": 0},
        ],
    },
    # =================================================================================
    12: {
        "titulo": "Proyecto y Gran Reto de Segundo Básico",
        "icono": "🏆",
        "umbral": 450,
        "contenido": [
            ("Proyecto: 'Diseña una solución tecnológica'",
             "Reto: la escuela quiere organizar mejor la información de sus estudiantes y mejorar el acceso a "
             "los recursos tecnológicos. Vas a combinar TODO lo aprendido para diseñar la solución."),
            ("Las 7 etapas del proyecto",
             "1. Analizar el problema.\n2. Identificar los datos necesarios.\n3. Diseñar la solución.\n"
             "4. Crear un pequeño algoritmo.\n5. Diseñar una red sencilla.\n6. Aplicar medidas de seguridad.\n"
             "7. Presentar la solución.\n\nCada etapa suma puntos: ¡demuestra que sabes comprender, analizar, "
             "aplicar, resolver y crear!"),
        ],
        "actividades": [
            {"id": "s2m12_a1", "tipo": "reto", "nivel": "🟢 Fácil", "titulo": "Etapa 1: analiza el problema", "puntos": 10, "categoria": "proyecto",
             "pregunta": "¿Cuál es el verdadero problema que hay que resolver?",
             "opciones": ["Organizar la información de estudiantes y mejorar el acceso a recursos", "Comprar más sillas", "Pintar la escuela"], "correcta": 0,
             "pista": "Relee el reto: habla de INFORMACIÓN de estudiantes y ACCESO a recursos tecnológicos."},
            {"id": "s2m12_a2", "tipo": "clasificar", "titulo": "Etapa 2: identifica los datos necesarios", "puntos": 10, "categoria": "proyecto",
             "instruccion": "¿Qué datos SÍ sirven para el registro de estudiantes?",
             "categorias": ["Dato útil", "Dato innecesario"],
             "items": [("Nombre del estudiante", "Dato útil"), ("Grado", "Dato útil"), ("Color favorito del director", "Dato innecesario"),
                       ("Edad", "Dato útil"), ("Marca del carro del vecino", "Dato innecesario")]},
            {"id": "s2m12_a3", "tipo": "ordenar", "titulo": "Etapa 4: crea el algoritmo", "puntos": 15, "categoria": "proyecto",
             "instruccion": "Ordena el algoritmo para registrar un estudiante nuevo:",
             "items": ["Inicio", "Pedir nombre, grado y edad", "Asignar un ID único", "Guardar el registro en la tabla", "Fin"]},
            {"id": "s2m12_a4", "tipo": "arrastrar", "titulo": "Etapa 5: diseña la red", "puntos": 15, "categoria": "proyecto",
             "instruccion": "Arrastra cada elemento a su rol para conectar la sala de cómputo.",
             "categorias": ["Reparte la conexión", "Equipos conectados"],
             "items": [{"texto": "📡 Router", "cat": "Reparte la conexión"}, {"texto": "🔀 Switch", "cat": "Reparte la conexión"},
                       {"texto": "💻 PC 1", "cat": "Equipos conectados"}, {"texto": "💻 PC 2", "cat": "Equipos conectados"},
                       {"texto": "🖨️ Impresora", "cat": "Equipos conectados"}]},
            {"id": "s2m12_final", "tipo": "gran_reto", "titulo": "🏆 GRAN RETO FINAL DE SEGUNDO", "puntos": 30, "categoria": "proyecto",
             "instruccion": "Recorre las 7 etapas del proyecto. ¡Responde bien para llegar a la victoria!",
             "pasos": [
                {"tema": "Análisis del problema", "pregunta": "El objetivo del proyecto es...", "opciones": ["Organizar información y mejorar el acceso a recursos", "Vender comida", "Pintar paredes"], "correcta": 0},
                {"tema": "Datos necesarios", "pregunta": "¿Qué dato SÍ es necesario para el registro?", "opciones": ["El grado del estudiante", "El color favorito del vecino", "La marca de un carro"], "correcta": 0},
                {"tema": "Diseño de la solución", "pregunta": "¿Dónde conviene guardar los datos de forma organizada?", "opciones": ["En una base de datos (tabla)", "En una servilleta", "En ningún lugar"], "correcta": 0},
                {"tema": "Algoritmo", "pregunta": "Para registrar un estudiante, primero hay que...", "opciones": ["Pedir sus datos", "Apagar la PC", "Imprimir"], "correcta": 0},
                {"tema": "Red", "pregunta": "El aparato que reparte Internet a la sala es el...", "opciones": ["Router", "Monitor", "Teclado"], "correcta": 0},
                {"tema": "Seguridad", "pregunta": "Para proteger los datos conviene...", "opciones": ["Contraseñas fuertes y copias de seguridad", "Compartir todo", "Apagar el antivirus"], "correcta": 0},
                {"tema": "Presentación", "pregunta": "Para presentar la solución, la mejor herramienta es...", "opciones": ["Una presentación clara con diapositivas", "Un grito", "Nada"], "correcta": 0},
             ]},
        ],
        "evaluacion": [
            {"pregunta": "El proyecto busca...", "opciones": ["Organizar información y mejorar el acceso a recursos", "Comprar sillas", "Pintar"], "correcta": 0},
            {"pregunta": "Un dato necesario para el registro es...", "opciones": ["El grado", "El color favorito del vecino", "La marca de un carro"], "correcta": 0},
            {"pregunta": "Los datos organizados se guardan mejor en...", "opciones": ["Una base de datos", "Una servilleta", "El aire"], "correcta": 0},
            {"pregunta": "Un algoritmo para registrar empieza por...", "opciones": ["Pedir los datos", "Imprimir", "Apagar"], "correcta": 0},
            {"pregunta": "El aparato que reparte Internet es el...", "opciones": ["Router", "Monitor", "Mouse"], "correcta": 0},
            {"pregunta": "Para proteger la información usamos...", "opciones": ["Contraseñas fuertes y respaldos", "Nada", "Wi-Fi abierto"], "correcta": 0},
            {"pregunta": "Para presentar la solución conviene usar...", "opciones": ["Una presentación clara", "Un grito", "Nada"], "correcta": 0},
            {"pregunta": "El ID en la base de datos sirve para...", "opciones": ["Identificar de forma única", "Sumar", "Apagar"], "correcta": 0},
            {"pregunta": "Un buen proyecto combina...", "opciones": ["Datos, algoritmo, red y seguridad", "Solo dibujos", "Nada"], "correcta": 0},
            {"pregunta": "El proyecto demuestra que sabes...", "opciones": ["Comprender, analizar, aplicar, resolver y crear", "Solo memorizar", "Nada"], "correcta": 0},
        ],
    },
}
