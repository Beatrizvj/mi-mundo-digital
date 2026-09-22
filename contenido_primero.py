# -*- coding: utf-8 -*-
"""
Contenido educativo de PRIMERO BÁSICO — Mi Primera Encarta Educativa.

Este archivo SOLO contiene datos (texto, actividades y evaluaciones).
El "motor" (puntos, desbloqueos, evaluaciones, perfiles, progreso) vive en app.py
y funciona con cualquier número de módulos que se definan aquí.

Tipos de actividad soportados por el motor:
  seleccion, relacionar, ordenar, memoria, clasificar, patron, problema, laberinto,
  explorar   (exploración interactiva: clic en objetos para descubrir información)

Umbral = puntos acumulados necesarios para desbloquear el módulo.
"""

MODULOS_PRIMERO = {
    # =================================================================================
    1: {
        "titulo": "Conociendo el mundo digital",
        "icono": "🌐",
        "umbral": 0,
        "contenido": [
            ("¿Qué es una computadora?",
             "Una computadora es una máquina electrónica que recibe información (datos), la procesa "
             "siguiendo instrucciones y nos entrega un resultado. Con ella podemos escribir, dibujar, "
             "investigar, comunicarnos y aprender."),
            ("¿Cómo ha cambiado con el tiempo?",
             "Las primeras computadoras eran enormes y ocupaban cuartos completos. Hoy una computadora "
             "cabe en una mochila (laptop) o hasta en tu bolsillo (teléfono). Cada vez son más pequeñas, "
             "rápidas y fáciles de usar."),
            ("Muchos tipos de dispositivos",
             "• 🖥️ De escritorio: potente y se queda fija en un lugar.\n"
             "• 💻 Laptop: portátil, tiene batería y la puedes llevar contigo.\n"
             "• 📱 Tablet y teléfono inteligente: pantalla táctil, para uso rápido y comunicación.\n"
             "• ⌚ Reloj inteligente (smartwatch): muestra mensajes y mide tu actividad.\n"
             "• 📺 Smart TV: un televisor conectado a Internet.\n"
             "• 🎮 Consola de videojuegos: para jugar y conectarse en línea."),
            ("¿Qué es la tecnología?",
             "La tecnología son todas las herramientas e inventos que las personas creamos para resolver "
             "problemas y vivir mejor. La usamos a diario: al ver la hora, calentar comida o enviar un mensaje."),
            ("Dispositivo y computadora, ¿es lo mismo?",
             "Un 'dispositivo' es cualquier aparato tecnológico (audífonos, control remoto, teléfono). "
             "La computadora es un dispositivo especial porque puede procesar información y ejecutar "
             "muchos programas diferentes."),
            ("Hardware y software",
             "• Hardware: las partes que puedes tocar (pantalla, teclado, mouse).\n"
             "• Software: los programas que no puedes tocar, pero sí usar (juegos, navegador, procesador de texto)."),
            ("Entrada, salida y almacenamiento",
             "• Entrada: envían información a la computadora (teclado, mouse, micrófono, cámara).\n"
             "• Salida: nos muestran resultados (monitor, bocinas, impresora).\n"
             "• Almacenamiento: guardan la información (disco duro, memoria USB, tarjeta de memoria)."),
        ],
        "actividades": [
            {"id": "m1_a1", "tipo": "explorar", "titulo": "Explora la habitación digital",
             "puntos": 10, "categoria": "computacion",
             "instruccion": "Haz clic en cada aparato para descubrir cómo usa la tecnología. ¡Explóralos todos!",
             "objetos": [
                {"icono": "💻", "nombre": "Laptop", "info": "Computadora portátil con batería. Sirve para estudiar, trabajar y navegar en Internet en cualquier lugar."},
                {"icono": "📱", "nombre": "Teléfono inteligente", "info": "Tiene pantalla táctil. Sirve para llamar, enviar mensajes, tomar fotos y usar aplicaciones."},
                {"icono": "📺", "nombre": "Smart TV", "info": "Televisor conectado a Internet. Permite ver videos y series desde aplicaciones."},
                {"icono": "⌚", "nombre": "Reloj inteligente", "info": "Muestra la hora, tus mensajes y mide cuántos pasos caminas."},
                {"icono": "🎮", "nombre": "Consola de videojuegos", "info": "Sirve para jugar videojuegos y también para conectarse con otras personas en línea."},
                {"icono": "🔊", "nombre": "Bocina inteligente", "info": "Responde con la voz. Puede reproducir música o contestar preguntas usando Internet."},
             ]},
            {"id": "m1_a2", "tipo": "clasificar", "titulo": "¿Usa tecnología o no?",
             "puntos": 10, "categoria": "computacion",
             "categorias": ["Sí usa tecnología", "No usa tecnología"],
             "items": [("Smart TV", "Sí usa tecnología"), ("Silla de madera", "No usa tecnología"),
                       ("Teléfono", "Sí usa tecnología"), ("Cuaderno de papel", "No usa tecnología"),
                       ("Consola de juegos", "Sí usa tecnología"), ("Pelota", "No usa tecnología")]},
            {"id": "m1_a3", "tipo": "seleccion", "titulo": "Partes de la computadora",
             "puntos": 5, "categoria": "computacion",
             "preguntas": [
                {"pregunta": "¿Con qué parte escribimos letras y números?", "opciones": ["Mouse", "Teclado", "Bocinas"], "correcta": 1},
                {"pregunta": "¿Qué parte usamos para ver imágenes?", "opciones": ["Monitor", "Impresora", "CPU"], "correcta": 0},
                {"pregunta": "¿Qué parte es el 'cerebro' de la computadora?", "opciones": ["CPU", "Teclado", "Bocinas"], "correcta": 0},
             ]},
            {"id": "m1_a4", "tipo": "memoria", "titulo": "Memorama de dispositivos",
             "puntos": 10, "categoria": "computacion",
             "pares": [("💻", "Laptop"), ("📱", "Teléfono"), ("📺", "Smart TV"), ("⌚", "Reloj inteligente")]},
            {"id": "m1_a5", "tipo": "clasificar", "titulo": "Entrada o salida",
             "puntos": 10, "categoria": "computacion",
             "categorias": ["Entrada", "Salida"],
             "items": [("Teclado", "Entrada"), ("Monitor", "Salida"), ("Mouse", "Entrada"),
                       ("Bocinas", "Salida"), ("Cámara web", "Entrada"), ("Impresora", "Salida")]},
            {"id": "m1_a6", "tipo": "seleccion", "titulo": "Hardware o software",
             "puntos": 5, "categoria": "computacion",
             "preguntas": [
                {"pregunta": "El teclado, ¿es hardware o software?", "opciones": ["Hardware", "Software"], "correcta": 0},
                {"pregunta": "Un juego educativo, ¿es hardware o software?", "opciones": ["Hardware", "Software"], "correcta": 1},
             ]},
        ],
        "evaluacion": [
            {"pregunta": "¿Qué es una computadora?", "opciones": ["Un animal", "Una máquina que procesa información", "Una fruta"], "correcta": 1},
            {"pregunta": "¿Cuál de estos es una computadora portátil?", "opciones": ["Laptop", "Monitor de escritorio", "Impresora"], "correcta": 0},
            {"pregunta": "Un reloj inteligente sirve para...", "opciones": ["Solo dar la hora", "Ver mensajes y medir pasos", "Cocinar"], "correcta": 1},
            {"pregunta": "La tecnología sirve para...", "opciones": ["Resolver problemas y vivir mejor", "Nada", "Solo jugar"], "correcta": 0},
            {"pregunta": "¿Cuál de estas es hardware?", "opciones": ["Un juego", "El mouse", "Una canción"], "correcta": 1},
            {"pregunta": "¿Cuál de estas es software?", "opciones": ["El teclado", "El monitor", "Un programa educativo"], "correcta": 2},
            {"pregunta": "El teclado es un dispositivo de...", "opciones": ["Entrada", "Salida", "Almacenamiento"], "correcta": 0},
            {"pregunta": "El monitor es un dispositivo de...", "opciones": ["Entrada", "Salida", "Almacenamiento"], "correcta": 1},
            {"pregunta": "Una memoria USB sirve para...", "opciones": ["Guardar información", "Escuchar música", "Ver la hora"], "correcta": 0},
            {"pregunta": "Una Smart TV es un televisor...", "opciones": ["Conectado a Internet", "Sin pantalla", "Que no sirve"], "correcta": 0},
        ],
    },
    # =================================================================================
    2: {
        "titulo": "Conociendo y utilizando la computadora",
        "icono": "🖥️",
        "umbral": 30,
        "contenido": [
            ("Encender y apagar correctamente",
             "Para encender presionamos el botón de encendido y esperamos a que cargue el sistema.\n"
             "Para apagar correctamente: guardamos el trabajo, cerramos los programas y elegimos la opción "
             "'Apagar'. Nunca debemos jalar el cable ni apagar de golpe."),
            ("El escritorio y sus partes",
             "El escritorio es la primera pantalla que vemos.\n"
             "• Iconos: dibujos pequeños que abren programas o archivos.\n"
             "• Barra de tareas: la barra de abajo con los programas abiertos.\n"
             "• Menú de inicio: el botón para buscar y abrir programas."),
            ("Las ventanas",
             "Cada programa se abre en una ventana. Podemos: minimizarla (esconderla), maximizarla "
             "(hacerla grande), moverla o cerrarla con la X."),
            ("Formas de dar órdenes a la computadora",
             "• 🖱️ Mouse: mover el puntero, seleccionar y abrir con clic.\n"
             "• ⌨️ Teclado: escribir letras, números y usar teclas especiales.\n"
             "• 👆 Pantalla táctil: tocar directamente la pantalla (en tablets y teléfonos)."),
            ("Cámara, micrófono y bocinas",
             "• Cámara: toma fotos y sirve para videollamadas.\n"
             "• Micrófono: capta nuestra voz.\n"
             "• Bocinas: nos dejan escuchar sonidos y música."),
            ("Conectar dispositivos USB",
             "Una memoria USB o un mouse se conectan en el puerto USB. Se coloca con cuidado y, al terminar, "
             "conviene 'expulsar' la memoria antes de retirarla para no dañar la información."),
            ("Cuidados y qué hacer si falla",
             "• Cuida el equipo: manos limpias, sin comida ni líquidos cerca.\n"
             "• Ergonomía: siéntate derecho y coloca la pantalla frente a tus ojos.\n"
             "• Si la computadora se congela o un programa 'no responde', espera unos segundos; si sigue igual, "
             "pide ayuda a un adulto.\n"
             "• Guarda tu trabajo seguido para no perderlo."),
        ],
        "actividades": [
            {"id": "m2_a1", "tipo": "explorar", "titulo": "Explora el escritorio de Windows",
             "puntos": 10, "categoria": "computacion",
             "instruccion": "Haz clic en cada parte del escritorio para descubrir para qué sirve.",
             "objetos": [
                {"icono": "🗂️", "nombre": "Iconos", "info": "Dibujos pequeños que abren un programa o un archivo cuando haces doble clic."},
                {"icono": "📊", "nombre": "Barra de tareas", "info": "La barra de abajo. Muestra los programas abiertos y te deja cambiar entre ellos."},
                {"icono": "🔵", "nombre": "Menú de inicio", "info": "El botón para buscar y abrir todos los programas de la computadora."},
                {"icono": "🪟", "nombre": "Ventana", "info": "Cada programa se abre en una ventana. Puedes minimizar, maximizar, mover o cerrar."},
                {"icono": "🕐", "nombre": "Reloj y notificaciones", "info": "Muestra la hora, la fecha y avisos importantes del sistema."},
             ]},
            {"id": "m2_a2", "tipo": "ordenar", "titulo": "Pasos para encender la computadora",
             "puntos": 10, "categoria": "computacion", "instruccion": "Ordena los pasos correctamente:",
             "items": ["Conectar la computadora", "Presionar el botón de encendido",
                       "Esperar a que cargue el sistema", "Ingresar usuario si se pide"]},
            {"id": "m2_a3", "tipo": "ordenar", "titulo": "Pasos para apagar la computadora",
             "puntos": 10, "categoria": "computacion", "instruccion": "Ordena los pasos correctamente:",
             "items": ["Guardar el trabajo", "Cerrar los programas abiertos",
                       "Elegir la opción Apagar", "Esperar a que se apague por completo"]},
            {"id": "m2_a4", "tipo": "relacionar", "titulo": "Relaciona la acción del mouse",
             "puntos": 10, "categoria": "computacion",
             "pares": [("Seleccionar un objeto", "Clic izquierdo"),
                       ("Abrir un menú de opciones", "Clic derecho"),
                       ("Abrir un programa", "Doble clic"),
                       ("Mover un objeto de lugar", "Arrastrar y soltar")]},
            {"id": "m2_a5", "tipo": "problema", "titulo": "¡Un programa no responde!",
             "puntos": 10, "categoria": "problema",
             "pregunta": "Estás usando un programa y de repente se queda 'congelado'. ¿Qué es lo mejor que puedes hacer?",
             "opciones": ["Esperar unos segundos y, si sigue igual, pedir ayuda a un adulto", "Apagar de golpe con el cable", "Golpear la computadora"],
             "correcta": 0,
             "explicacion": "Lo correcto es tener paciencia unos segundos y, si no reacciona, pedir ayuda. Nunca apagues jalando el cable."},
            {"id": "m2_j1", "tipo": "atrapa", "titulo": "🖱️ Atrapa el objeto (puntería con el mouse)",
             "puntos": 10, "categoria": "computacion", "emoji": "🖱️",
             "instruccion": "Practica tu puntería: haz clic en cada objeto que aparezca antes de que se acabe el tiempo. Elige tu nivel."},
        ],
        "evaluacion": [
            {"pregunta": "¿Qué botón usamos primero para empezar a trabajar?", "opciones": ["El de apagado", "El de encendido", "Ninguno"], "correcta": 1},
            {"pregunta": "Antes de apagar la computadora debemos...", "opciones": ["Cerrar los programas y guardar", "Jalar el cable", "Nada"], "correcta": 0},
            {"pregunta": "Los iconos del escritorio sirven para...", "opciones": ["Abrir programas o archivos", "Escribir", "Apagar"], "correcta": 0},
            {"pregunta": "La barra de tareas muestra...", "opciones": ["Los programas abiertos", "La comida", "El clima"], "correcta": 0},
            {"pregunta": "Para hacer una ventana más grande la...", "opciones": ["Maximizamos", "Borramos", "Apagamos"], "correcta": 0},
            {"pregunta": "La pantalla táctil se usa...", "opciones": ["Tocándola con el dedo", "Con el cable", "Con la impresora"], "correcta": 0},
            {"pregunta": "El micrófono sirve para...", "opciones": ["Captar nuestra voz", "Ver imágenes", "Imprimir"], "correcta": 0},
            {"pregunta": "Antes de retirar una memoria USB conviene...", "opciones": ["Expulsarla", "Mojarla", "Nada"], "correcta": 0},
            {"pregunta": "Si un programa 'no responde' debemos...", "opciones": ["Esperar y pedir ayuda", "Jalar el cable", "Golpear la PC"], "correcta": 0},
            {"pregunta": "Para no perder nuestro trabajo debemos...", "opciones": ["Guardarlo seguido", "Apagar rápido", "Nada"], "correcta": 0},
        ],
    },
    # =================================================================================
    3: {
        "titulo": "Teclado y habilidades digitales",
        "icono": "⌨️",
        "umbral": 60,
        "contenido": [
            ("Las partes del teclado",
             "El teclado tiene: letras, números, teclas especiales y teclas de dirección (flechas). "
             "Aprender dónde está cada tecla nos ayuda a escribir más rápido."),
            ("Teclas especiales importantes",
             "• Enter: confirma o cambia de línea.\n"
             "• Shift: escribe mayúsculas y símbolos.\n"
             "• Backspace: borra hacia atrás.\n"
             "• Espacio: separa las palabras.\n"
             "• Esc: cancela una acción.\n"
             "• Ctrl y Alt: se usan junto a otras teclas para hacer atajos.\n"
             "• Flechas: mueven el cursor arriba, abajo, izquierda y derecha."),
            ("Mayúsculas y minúsculas",
             "Con la tecla Shift escribimos una letra mayúscula. Usamos mayúscula al inicio de cada oración "
             "y en los nombres propios."),
            ("Atajos de teclado básicos",
             "Los atajos son combinaciones que ahorran tiempo:\n"
             "• Ctrl + C: copiar.\n• Ctrl + V: pegar.\n• Ctrl + Z: deshacer.\n• Ctrl + S: guardar."),
            ("Escribir correctamente y con buena velocidad",
             "Al principio escribimos despacio, revisando que las letras sean correctas. Con la práctica "
             "aumentamos la velocidad sin dejar de ser precisos. ¡La constancia es la clave!"),
            ("Uso correcto del mouse",
             "Sostén el mouse con suavidad, mueve el puntero sin levantarlo demasiado y usa clic izquierdo "
             "para seleccionar y doble clic para abrir."),
        ],
        "actividades": [
            {"id": "m3_a1", "tipo": "seleccion", "titulo": "Identificando teclas",
             "puntos": 5, "categoria": "computacion",
             "preguntas": [
                {"pregunta": "¿Qué tecla usamos para borrar una letra?", "opciones": ["Enter", "Backspace", "Shift"], "correcta": 1},
                {"pregunta": "¿Qué tecla usamos para escribir en mayúscula?", "opciones": ["Shift", "Espacio", "Esc"], "correcta": 0},
                {"pregunta": "¿Qué tecla cancela una acción?", "opciones": ["Ctrl", "Esc", "Enter"], "correcta": 1},
                {"pregunta": "¿Qué tecla separa las palabras?", "opciones": ["Espacio", "Alt", "Enter"], "correcta": 0},
             ]},
            {"id": "m3_a2", "tipo": "relacionar", "titulo": "Relaciona el atajo con su función",
             "puntos": 10, "categoria": "computacion",
             "pares": [("Ctrl + C", "Copiar"), ("Ctrl + V", "Pegar"),
                       ("Ctrl + Z", "Deshacer"), ("Ctrl + S", "Guardar")]},
            {"id": "m3_a3", "tipo": "relacionar", "titulo": "Relaciona la tecla con lo que hace",
             "puntos": 10, "categoria": "computacion",
             "pares": [("Enter", "Confirmar o cambiar de línea"), ("Shift", "Escribir mayúscula"),
                       ("Backspace", "Borrar hacia atrás"), ("Espacio", "Separar palabras")]},
            {"id": "m3_a4", "tipo": "clasificar", "titulo": "¿Letra, número o tecla especial?",
             "puntos": 10, "categoria": "computacion",
             "categorias": ["Letra", "Número", "Tecla especial"],
             "items": [("A", "Letra"), ("7", "Número"), ("Enter", "Tecla especial"),
                       ("M", "Letra"), ("3", "Número"), ("Shift", "Tecla especial")]},
            {"id": "m3_a5", "tipo": "ordenar", "titulo": "Pasos para escribir tu nombre con mayúscula",
             "puntos": 10, "categoria": "computacion", "instruccion": "Ordena los pasos:",
             "items": ["Mantener presionada la tecla Shift", "Presionar la primera letra (mayúscula)",
                       "Soltar Shift", "Escribir el resto de las letras"]},
            {"id": "m3_t1", "tipo": "teclado", "modo": "escribir", "titulo": "🏁 Carrera de teclado",
             "puntos": 15, "categoria": "computacion",
             "instruccion": "Escribe cada palabra tal como aparece y presiona Enter. ¡Mide tu velocidad!",
             "reactivos": ["sol", "casa", "mesa", "libro", "escuela", "computadora"]},
            {"id": "m3_t2", "tipo": "teclado", "modo": "tecla", "titulo": "🎯 Encuentra la tecla",
             "puntos": 10, "categoria": "computacion",
             "instruccion": "Presiona en tu teclado la tecla que aparece en pantalla.",
             "reactivos": ["A", "S", "D", "F", "J", "K", "Espacio", "Enter"]},
            {"id": "m3_t3", "tipo": "teclado", "modo": "escribir", "titulo": "⚡ Reto de velocidad",
             "puntos": 15, "categoria": "computacion",
             "instruccion": "Escribe la frase completa y presiona Enter. ¡Hazlo rápido y con precisión!",
             "reactivos": ["el gato duerme", "me gusta aprender", "la computadora es util"]},
        ],
        "evaluacion": [
            {"pregunta": "¿Qué tecla usamos para borrar?", "opciones": ["Backspace", "Enter", "Ctrl"], "correcta": 0},
            {"pregunta": "¿Qué tecla usamos para mayúsculas?", "opciones": ["Shift", "Esc", "Espacio"], "correcta": 0},
            {"pregunta": "¿Qué tecla separa palabras?", "opciones": ["Espacio", "Enter", "Ctrl"], "correcta": 0},
            {"pregunta": "¿Qué tecla confirma o cambia de línea?", "opciones": ["Enter", "Shift", "Alt"], "correcta": 0},
            {"pregunta": "El atajo Ctrl + C sirve para...", "opciones": ["Copiar", "Borrar", "Apagar"], "correcta": 0},
            {"pregunta": "El atajo Ctrl + V sirve para...", "opciones": ["Pegar", "Guardar", "Cerrar"], "correcta": 0},
            {"pregunta": "El atajo Ctrl + Z sirve para...", "opciones": ["Deshacer", "Copiar", "Imprimir"], "correcta": 0},
            {"pregunta": "El atajo Ctrl + S sirve para...", "opciones": ["Guardar", "Pegar", "Salir"], "correcta": 0},
            {"pregunta": "Las flechas del teclado sirven para...", "opciones": ["Mover el cursor", "Borrar todo", "Apagar"], "correcta": 0},
            {"pregunta": "Para escribir bien debemos...", "opciones": ["Practicar con constancia", "Ir muy rápido sin fijarnos", "No practicar"], "correcta": 0},
        ],
    },
    # =================================================================================
    4: {
        "titulo": "Archivos, carpetas y organización digital",
        "icono": "📁",
        "umbral": 90,
        "contenido": [
            ("¿Qué es un archivo?",
             "Un archivo es información guardada en la computadora: un documento, una foto, una canción o un video. "
             "Cada archivo tiene un nombre y un tipo."),
            ("¿Qué es una carpeta?",
             "Una carpeta es como una caja donde guardamos varios archivos para tenerlos ordenados. "
             "Dentro de una carpeta puede haber más carpetas."),
            ("Acciones con archivos y carpetas",
             "• Crear y nombrar una carpeta.\n• Guardar un archivo dentro de ella.\n"
             "• Abrir con doble clic.\n• Copiar: hacer un duplicado.\n• Mover: cambiarlo de lugar.\n"
             "• Renombrar: cambiar su nombre.\n• Eliminar: enviarlo a la papelera (y se puede recuperar)."),
            ("Tipos de archivo",
             "• 📄 Documento (.docx): textos y tareas.\n• 🖼️ Imagen (.jpg): fotos y dibujos.\n"
             "• 🎵 Audio (.mp3): música y sonidos.\n• 🎬 Video (.mp4): películas y grabaciones.\n"
             "• 📕 PDF (.pdf): documentos para leer e imprimir."),
            ("Organización y copias de seguridad",
             "Ordenar los archivos en carpetas nos ayuda a encontrarlos rápido. Además conviene hacer "
             "'copias de seguridad' (respaldos) en una memoria USB o en la nube, por si algo se borra."),
        ],
        "actividades": [
            {"id": "m4_a1", "tipo": "clasificar", "titulo": "Organizador digital",
             "puntos": 10, "categoria": "computacion",
             "categorias": ["Documentos", "Imágenes", "Música", "Videos", "PDF"],
             "items": [("Tarea.docx", "Documentos"), ("Foto.jpg", "Imágenes"), ("Cancion.mp3", "Música"),
                       ("Pelicula.mp4", "Videos"), ("Libro.pdf", "PDF"), ("Carta.docx", "Documentos")]},
            {"id": "m4_a2", "tipo": "ordenar", "titulo": "Pasos para crear una carpeta",
             "puntos": 10, "categoria": "computacion", "instruccion": "Ordena los pasos:",
             "items": ["Hacer clic derecho en un espacio vacío", "Elegir la opción 'Nueva carpeta'",
                       "Escribir el nombre de la carpeta", "Presionar Enter para confirmar"]},
            {"id": "m4_a3", "tipo": "relacionar", "titulo": "Relaciona la acción con su nombre",
             "puntos": 10, "categoria": "computacion",
             "pares": [("Hacer un duplicado del archivo", "Copiar"),
                       ("Cambiarlo de lugar", "Mover"),
                       ("Cambiar su nombre", "Renombrar"),
                       ("Enviarlo a la papelera", "Eliminar")]},
            {"id": "m4_a4", "tipo": "memoria", "titulo": "Memorama de tipos de archivo",
             "puntos": 10, "categoria": "computacion",
             "pares": [("📄", "Documento"), ("🖼️", "Imagen"), ("🎵", "Audio"), ("🎬", "Video"), ("📕", "PDF")]},
            {"id": "m4_a5", "tipo": "seleccion", "titulo": "Archivos y carpetas",
             "puntos": 5, "categoria": "computacion",
             "preguntas": [
                {"pregunta": "¿Qué es un archivo?", "opciones": ["Información guardada", "Un ratón", "Un botón"], "correcta": 0},
                {"pregunta": "Para abrir un archivo hacemos...", "opciones": ["Doble clic", "Clic derecho solamente", "Nada"], "correcta": 0},
                {"pregunta": "Una copia de seguridad sirve para...", "opciones": ["No perder la información", "Borrar todo", "Apagar la PC"], "correcta": 0},
             ]},
            {"id": "m4_a6", "tipo": "arrastrar", "titulo": "🖱️ Arrastra cada archivo a su carpeta",
             "puntos": 15, "categoria": "computacion",
             "instruccion": "Arrastra cada archivo hasta la carpeta correcta.",
             "categorias": ["Documentos", "Imágenes", "Videos"],
             "items": [{"texto": "Tarea.docx", "cat": "Documentos"}, {"texto": "Foto.jpg", "cat": "Imágenes"},
                       {"texto": "Clip.mp4", "cat": "Videos"}, {"texto": "Carta.docx", "cat": "Documentos"},
                       {"texto": "Paisaje.jpg", "cat": "Imágenes"}, {"texto": "Baile.mp4", "cat": "Videos"}]},
        ],
        "evaluacion": [
            {"pregunta": "Un archivo es...", "opciones": ["Información guardada", "Un cable", "Un botón"], "correcta": 0},
            {"pregunta": "Una carpeta sirve para...", "opciones": ["Guardar y organizar archivos", "Escribir", "Escuchar música"], "correcta": 0},
            {"pregunta": "Para abrir un archivo hacemos...", "opciones": ["Doble clic", "Nada", "Apagar la PC"], "correcta": 0},
            {"pregunta": "Copiar un archivo significa...", "opciones": ["Hacer un duplicado", "Borrarlo", "Apagarlo"], "correcta": 0},
            {"pregunta": "Una foto se guarda como archivo de tipo...", "opciones": ["Imagen (.jpg)", "Audio (.mp3)", "Video (.mp4)"], "correcta": 0},
            {"pregunta": "Una canción se guarda como archivo de tipo...", "opciones": ["Audio (.mp3)", "Imagen (.jpg)", "PDF"], "correcta": 0},
            {"pregunta": "Una tarea escrita se guarda mejor como...", "opciones": ["Documento (.docx)", "Video", "Audio"], "correcta": 0},
            {"pregunta": "Si borramos un archivo por error, primero va a la...", "opciones": ["Papelera de reciclaje", "Impresora", "Cámara"], "correcta": 0},
            {"pregunta": "Organizar archivos en carpetas ayuda a...", "opciones": ["Encontrarlos más rápido", "Perderlos", "Borrarlos"], "correcta": 0},
            {"pregunta": "Una copia de seguridad (respaldo) sirve para...", "opciones": ["No perder la información", "Gastar batería", "Nada"], "correcta": 0},
        ],
    },
    # =================================================================================
    5: {
        "titulo": "Internet y mundo digital",
        "icono": "🌍",
        "umbral": 120,
        "contenido": [
            ("¿Qué es Internet?",
             "Internet es una red gigante que conecta millones de computadoras y dispositivos de todo el mundo. "
             "Gracias a ella podemos buscar información, comunicarnos y compartir contenido."),
            ("¿Cómo funciona (de forma sencilla)?",
             "Tu dispositivo se conecta a Internet por wifi o cable. Cuando pides una página, tu dispositivo "
             "envía un mensaje a otra computadora (un servidor) que te devuelve la información."),
            ("Navegadores, buscadores y páginas",
             "• Navegador: el programa para entrar a Internet (Chrome, Edge, Firefox).\n"
             "• Buscador: sirve para encontrar cosas escribiendo palabras clave (Google).\n"
             "• Página web: un sitio con información.\n• Enlace: un texto o imagen en el que haces clic para ir a otro lugar."),
            ("Comunicarnos por Internet",
             "• Correo electrónico: enviar mensajes y archivos.\n• Videollamadas: hablar viéndonos por cámara.\n"
             "• Mensajería: chats rápidos.\n• Redes sociales: compartir con otras personas (siempre con permiso de un adulto)."),
            ("Información confiable y falsa",
             "No todo lo que aparece en Internet es verdad. Para saber si algo es confiable: revisa quién lo publica, "
             "compáralo con otras fuentes y desconfía de titulares exagerados."),
            ("Huella digital y privacidad",
             "Todo lo que publicamos deja una 'huella digital' que puede quedar para siempre. Protege tus datos "
             "personales (nombre completo, dirección, teléfono) y no los compartas con desconocidos."),
        ],
        "actividades": [
            {"id": "m5_a1", "tipo": "clasificar", "titulo": "Detective de Internet: ¿confiable?",
             "puntos": 10, "categoria": "internet",
             "categorias": ["Confiable", "Poco confiable"],
             "items": [("Página de un museo con autor y fecha", "Confiable"),
                       ("Titular que dice '¡Gana un carro solo por dar clic!'", "Poco confiable"),
                       ("Noticia repetida por varios medios serios", "Confiable"),
                       ("Mensaje de un desconocido con muchos errores", "Poco confiable"),
                       ("Sitio oficial del Ministerio de Educación", "Confiable"),
                       ("Foto sin fuente que promete premios", "Poco confiable")]},
            {"id": "m5_a2", "tipo": "relacionar", "titulo": "Relaciona el término con su uso",
             "puntos": 10, "categoria": "internet",
             "pares": [("Programa para entrar a Internet", "Navegador"),
                       ("Buscar cosas con palabras clave", "Buscador"),
                       ("Enviar mensajes y archivos", "Correo electrónico"),
                       ("Hablar viéndonos por cámara", "Videollamada")]},
            {"id": "m5_a3", "tipo": "seleccion", "titulo": "Uso responsable de Internet",
             "puntos": 5, "categoria": "internet",
             "preguntas": [
                {"pregunta": "¿Debo compartir mi dirección con un desconocido en línea?", "opciones": ["Sí, siempre", "No, nunca"], "correcta": 1},
                {"pregunta": "Si veo una noticia increíble, primero debo...", "opciones": ["Compartirla de inmediato", "Verificar si es confiable"], "correcta": 1},
                {"pregunta": "La 'huella digital' es...", "opciones": ["Todo lo que dejamos publicado en Internet", "Una marca en el dedo"], "correcta": 0},
             ]},
            {"id": "m5_a4", "tipo": "clasificar", "titulo": "¿Dato personal o dato público?",
             "puntos": 10, "categoria": "internet",
             "categorias": ["Dato personal (protegerlo)", "Se puede compartir"],
             "items": [("Mi contraseña", "Dato personal (protegerlo)"),
                       ("Mi color favorito", "Se puede compartir"),
                       ("Mi dirección de casa", "Dato personal (protegerlo)"),
                       ("Mi caricatura favorita", "Se puede compartir"),
                       ("Mi número de teléfono", "Dato personal (protegerlo)")]},
        ],
        "evaluacion": [
            {"pregunta": "Internet es...", "opciones": ["Una red que conecta dispositivos del mundo", "Un juego", "Una fruta"], "correcta": 0},
            {"pregunta": "El programa para entrar a Internet se llama...", "opciones": ["Navegador", "Impresora", "Teclado"], "correcta": 0},
            {"pregunta": "Un buscador sirve para...", "opciones": ["Encontrar información con palabras clave", "Apagar la PC", "Guardar fotos"], "correcta": 0},
            {"pregunta": "Un enlace es...", "opciones": ["Algo en lo que haces clic para ir a otro lugar", "Una tecla", "Un cable"], "correcta": 0},
            {"pregunta": "El correo electrónico sirve para...", "opciones": ["Enviar mensajes y archivos", "Cocinar", "Ver la hora"], "correcta": 0},
            {"pregunta": "¿Todo lo que está en Internet es verdad?", "opciones": ["No, hay que verificar", "Sí, siempre", "Solo los videos"], "correcta": 0},
            {"pregunta": "La huella digital es...", "opciones": ["Todo lo que publicamos y queda", "Una marca del dedo", "Un virus"], "correcta": 0},
            {"pregunta": "¿Debo dar mis datos personales a un desconocido?", "opciones": ["No, nunca", "Sí, siempre", "Solo el teléfono"], "correcta": 0},
            {"pregunta": "Una videollamada nos permite...", "opciones": ["Hablar viéndonos por cámara", "Imprimir", "Apagar la PC"], "correcta": 0},
            {"pregunta": "Para saber si una página es confiable...", "opciones": ["Revisamos quién la publica", "La creemos sin pensar", "La compartimos de una"], "correcta": 0},
        ],
    },
    # =================================================================================
    6: {
        "titulo": "Seguridad digital",
        "icono": "🛡️",
        "umbral": 150,
        "contenido": [
            ("¿Qué es la seguridad digital?",
             "Es cuidar nuestra información y protegernos de peligros cuando usamos dispositivos e Internet. "
             "Igual que cerramos la puerta de casa, cuidamos nuestras cuentas."),
            ("Contraseñas seguras",
             "Una buena contraseña es larga, mezcla letras, números y símbolos, y no es fácil de adivinar. "
             "Nunca compartas tu contraseña, ni siquiera con amigos."),
            ("Datos personales y privacidad",
             "Tu nombre completo, dirección, teléfono y fotos son datos privados. No los publiques ni los "
             "envíes a desconocidos."),
            ("Engaños en Internet",
             "• Phishing: mensajes falsos que fingen ser de alguien conocido para robar tus datos.\n"
             "• Enlaces desconocidos: no hagas clic si no sabes de dónde vienen.\n"
             "• Descargas seguras: descarga solo de sitios oficiales."),
            ("Malware, antivirus y actualizaciones",
             "El 'malware' son programas dañinos (como los virus). Para protegernos usamos un antivirus y "
             "mantenemos el sistema actualizado."),
            ("Ciberacoso: pedir ayuda",
             "El ciberacoso es molestar o lastimar a alguien por medios digitales. Si te pasa a ti o a un "
             "compañero, no respondas con enojo, guarda las pruebas y habla con un adulto de confianza."),
        ],
        "actividades": [
            {"id": "m6_a1", "tipo": "clasificar", "titulo": "¿Seguro o peligroso?",
             "puntos": 15, "categoria": "seguridad",
             "categorias": ["Seguro", "Peligroso"],
             "items": [("Un desconocido te pide tu contraseña", "Peligroso"),
                       ("Tu profesor te da un enlace para una actividad", "Seguro"),
                       ("Un mensaje dice que ganaste un premio y pide tus datos", "Peligroso"),
                       ("Usar una contraseña larga y secreta", "Seguro"),
                       ("Descargar un juego de un sitio oficial", "Seguro"),
                       ("Hacer clic en un enlace raro de un desconocido", "Peligroso")]},
            {"id": "m6_a2", "tipo": "seleccion", "titulo": "Contraseñas seguras",
             "puntos": 5, "categoria": "seguridad",
             "preguntas": [
                {"pregunta": "¿Cuál es una contraseña más segura?", "opciones": ["1234", "Sol#Azul72", "hola"], "correcta": 1},
                {"pregunta": "¿Debo compartir mi contraseña con un amigo?", "opciones": ["No", "Sí"], "correcta": 0},
                {"pregunta": "¿Qué es el phishing?", "opciones": ["Un mensaje falso que quiere robar datos", "Un tipo de pez", "Un juego"], "correcta": 0},
             ]},
            {"id": "m6_a3", "tipo": "problema", "titulo": "Mensaje de un desconocido",
             "puntos": 10, "categoria": "seguridad",
             "pregunta": "Recibes un mensaje de alguien que no conoces y te pide una foto y tu dirección. ¿Qué debes hacer?",
             "opciones": ["No responder y avisar a un adulto de confianza", "Enviar la foto de inmediato", "Darle tu dirección"],
             "correcta": 0,
             "explicacion": "Nunca compartas datos personales con desconocidos. Lo correcto es no responder y avisar a un adulto."},
            {"id": "m6_a4", "tipo": "problema", "titulo": "Un enlace sospechoso",
             "puntos": 10, "categoria": "seguridad",
             "pregunta": "Te llega un enlace que dice '¡Haz clic y gana un teléfono gratis!'. ¿Qué haces?",
             "opciones": ["No hago clic; puede ser un engaño", "Hago clic rápido para ganar", "Lo comparto con todos"],
             "correcta": 0,
             "explicacion": "Los premios 'gratis' suelen ser trampas (phishing). Lo mejor es no hacer clic."},
            {"id": "m6_a5", "tipo": "relacionar", "titulo": "Relaciona el término de seguridad",
             "puntos": 10, "categoria": "seguridad",
             "pares": [("Programa dañino como un virus", "Malware"),
                       ("Programa que nos protege", "Antivirus"),
                       ("Mensaje falso para robar datos", "Phishing"),
                       ("Molestar a alguien por medios digitales", "Ciberacoso")]},
        ],
        "evaluacion": [
            {"pregunta": "La seguridad digital sirve para...", "opciones": ["Proteger nuestra información", "Gastar batería", "Nada"], "correcta": 0},
            {"pregunta": "Una contraseña segura es...", "opciones": ["Larga y difícil de adivinar", "1234", "Tu nombre"], "correcta": 0},
            {"pregunta": "¿Debo compartir mi contraseña?", "opciones": ["No, con nadie", "Sí, con amigos", "Sí, en redes"], "correcta": 0},
            {"pregunta": "El phishing es...", "opciones": ["Un mensaje falso para robar datos", "Un juego", "Un antivirus"], "correcta": 0},
            {"pregunta": "Si un desconocido pide tus datos debes...", "opciones": ["No dárselos y avisar a un adulto", "Dárselos", "Publicarlos"], "correcta": 0},
            {"pregunta": "El malware es...", "opciones": ["Un programa dañino", "Un programa bueno", "Una carpeta"], "correcta": 0},
            {"pregunta": "El antivirus sirve para...", "opciones": ["Protegernos de programas dañinos", "Escribir", "Imprimir"], "correcta": 0},
            {"pregunta": "Ante un enlace raro de un desconocido debemos...", "opciones": ["No hacer clic", "Hacer clic rápido", "Compartirlo"], "correcta": 0},
            {"pregunta": "El ciberacoso es...", "opciones": ["Molestar a alguien por medios digitales", "Un antivirus", "Un juego seguro"], "correcta": 0},
            {"pregunta": "Si sufro ciberacoso debo...", "opciones": ["Guardar pruebas y hablar con un adulto", "Responder con enojo", "Callar siempre"], "correcta": 0},
        ],
    },
    # =================================================================================
    7: {
        "titulo": "Pensamiento lógico",
        "icono": "🧠",
        "umbral": 180,
        "contenido": [
            ("Secuencias y patrones",
             "Un patrón es algo que se repite siguiendo un orden. Si observamos con atención podemos descubrir "
             "qué sigue.\n\nEjemplo:  🔵 🔴 🔵 🔴 🔵 __\n¡El patrón se repite cada dos!"),
            ("Comparar y clasificar",
             "Comparar es observar semejanzas y diferencias. Clasificar es agrupar según una característica, "
             "como el color, la forma o el tamaño."),
            ("Encontrar el error o la diferencia",
             "Observar con cuidado nos ayuda a detectar el elemento distinto o el error dentro de un grupo."),
            ("Resolver acertijos y laberintos",
             "Para resolver un reto: lee con calma, observa las pistas, piensa antes de actuar y prueba tu solución."),
        ],
        "actividades": [
            {"id": "m7_a1", "tipo": "patron", "titulo": "🟢 Fácil: completa la secuencia",
             "puntos": 10, "categoria": "logica",
             "patrones": [
                {"secuencia": "🔵 🔴 🔵 🔴 🔵", "opciones": ["🔵", "🔴", "🟢"], "correcta": 1},
                {"secuencia": "🟩 🟦 🟩 🟦 🟩", "opciones": ["🟩", "🟦", "🟥"], "correcta": 1},
                {"secuencia": "1 - 2 - 3 - 4 -", "opciones": ["5", "6", "9"], "correcta": 0},
             ]},
            {"id": "m7_a2", "tipo": "patron", "titulo": "🟡 Medio: secuencias numéricas",
             "puntos": 10, "categoria": "logica",
             "patrones": [
                {"secuencia": "2 - 4 - 6 - 8 -", "opciones": ["9", "10", "12"], "correcta": 1},
                {"secuencia": "5 - 10 - 15 -", "opciones": ["18", "20", "25"], "correcta": 1},
                {"secuencia": "⭐ ⭐ 🌙 ⭐ ⭐", "opciones": ["🌙", "⭐", "☀️"], "correcta": 0},
             ]},
            {"id": "m7_a3", "tipo": "seleccion", "titulo": "🔴 Difícil: encuentra el diferente",
             "puntos": 10, "categoria": "logica",
             "preguntas": [
                {"pregunta": "🍎 🍎 🍌 🍎  ¿Cuál es diferente?", "opciones": ["🍎", "🍌"], "correcta": 1},
                {"pregunta": "🔺 🔺 🔺 ⬛  ¿Cuál es diferente?", "opciones": ["🔺", "⬛"], "correcta": 1},
                {"pregunta": "3 - 6 - 9 - 10 - 15  ¿Cuál NO sigue el patrón de 3 en 3?", "opciones": ["9", "10", "15"], "correcta": 1},
             ]},
            {"id": "m7_a4", "tipo": "clasificar", "titulo": "Clasifica por tipo",
             "puntos": 10, "categoria": "logica",
             "categorias": ["Animales", "Frutas"],
             "items": [("Perro", "Animales"), ("Manzana", "Frutas"), ("Gato", "Animales"),
                       ("Plátano", "Frutas"), ("León", "Animales"), ("Uva", "Frutas")]},
            {"id": "m7_a5", "tipo": "memoria", "titulo": "Reto de memoria",
             "puntos": 10, "categoria": "logica",
             "pares": [("🔵", "Círculo"), ("🔺", "Triángulo"), ("⬛", "Cuadrado"), ("⭐", "Estrella")]},
            {"id": "m7_a6", "tipo": "laberinto", "titulo": "Laberinto lógico", "puntos": 10, "categoria": "logica"},
        ],
        "evaluacion": [
            {"pregunta": "🔵 🔴 🔵 🔴 🔵 __  ¿Qué sigue?", "opciones": ["🔵", "🔴", "🟢"], "correcta": 1},
            {"pregunta": "1 - 2 - 3 - __", "opciones": ["4", "6", "9"], "correcta": 0},
            {"pregunta": "2 - 4 - 6 - __", "opciones": ["7", "8", "9"], "correcta": 1},
            {"pregunta": "🍎 🍎 🍎 🍌  ¿Cuál es diferente?", "opciones": ["🍎", "🍌"], "correcta": 1},
            {"pregunta": "Comparar objetos significa...", "opciones": ["Ver semejanzas y diferencias", "Apagarlos", "Borrarlos"], "correcta": 0},
            {"pregunta": "Clasificar significa...", "opciones": ["Agrupar por una característica", "Sumar números", "Nada"], "correcta": 0},
            {"pregunta": "¿Cuál NO es una fruta?", "opciones": ["Manzana", "Perro", "Uva"], "correcta": 1},
            {"pregunta": "⭐ ⭐ 🌙 ⭐ ⭐ __  ¿Qué sigue?", "opciones": ["🌙", "⭐", "☀️"], "correcta": 1},
            {"pregunta": "5 - 10 - 15 - __", "opciones": ["18", "20", "25"], "correcta": 1},
            {"pregunta": "Un acertijo se resuelve mejor si...", "opciones": ["Pensamos con calma", "Respondemos sin pensar", "Lo ignoramos"], "correcta": 0},
        ],
    },
    # =================================================================================
    8: {
        "titulo": "Resolución de problemas",
        "icono": "🧩",
        "umbral": 210,
        "contenido": [
            ("Pensar antes de actuar",
             "Cuando tenemos un problema: primero pensamos qué pasó, luego imaginamos posibles soluciones, "
             "elegimos la mejor y la probamos."),
            ("Los pasos para resolver un problema",
             "1. Identificar el problema.\n2. Pensar posibles soluciones.\n3. Elegir la mejor.\n"
             "4. Probarla.\n5. Si no funciona, intentar otra."),
            ("Problemas de la vida real",
             "Todos los días aparecen pequeños problemas: no encontrar un archivo, que la computadora vaya lenta "
             "o recibir un mensaje sospechoso. ¡Con calma se resuelven!"),
        ],
        "actividades": [
            {"id": "m8_a1", "tipo": "problema", "titulo": "Pedro no encuentra su archivo",
             "puntos": 10, "categoria": "problema",
             "pregunta": "Pedro hizo una tarea en la computadora, pero ahora no encuentra el archivo. ¿Qué debería hacer primero?",
             "opciones": ["Buscarlo en la carpeta donde lo guardó o con el buscador", "Hacer la tarea de nuevo sin buscar", "Apagar la computadora"],
             "correcta": 0,
             "explicacion": "Antes de rehacer el trabajo conviene buscarlo en su carpeta o con el buscador de archivos."},
            {"id": "m8_a2", "tipo": "problema", "titulo": "María recibe un mensaje extraño",
             "puntos": 10, "categoria": "problema",
             "pregunta": "María recibe un mensaje de una persona desconocida que le pide información personal. ¿Qué debería hacer?",
             "opciones": ["No responder y avisar a un adulto de confianza", "Darle toda la información", "Enviarle una foto"],
             "correcta": 0,
             "explicacion": "Nunca se comparten datos con desconocidos. Lo correcto es no responder y avisar a un adulto."},
            {"id": "m8_a3", "tipo": "problema", "titulo": "La computadora está sin espacio",
             "puntos": 10, "categoria": "problema",
             "pregunta": "Una computadora ya no tiene espacio para guardar. ¿Qué acción ayuda a solucionarlo?",
             "opciones": ["Borrar archivos que ya no se usan o pasarlos a una USB", "Apagarla para siempre", "No hacer nada"],
             "correcta": 0,
             "explicacion": "Liberar espacio borrando lo que no sirve o pasándolo a una memoria USB soluciona el problema."},
            {"id": "m8_a4", "tipo": "problema", "titulo": "La computadora va muy lenta",
             "puntos": 10, "categoria": "problema",
             "pregunta": "La computadora está muy lenta con muchos programas abiertos. ¿Qué conviene hacer?",
             "opciones": ["Cerrar los programas que no se están usando", "Abrir más programas", "Golpearla"],
             "correcta": 0,
             "explicacion": "Cerrar los programas que no usamos libera memoria y la computadora va más rápido."},
            {"id": "m8_a5", "tipo": "ordenar", "titulo": "Ordena los pasos para resolver un problema",
             "puntos": 10, "categoria": "problema", "instruccion": "Ordena los pasos:",
             "items": ["Identificar el problema", "Pensar posibles soluciones",
                       "Elegir la mejor solución", "Probar la solución"]},
        ],
        "evaluacion": [
            {"pregunta": "El primer paso para resolver un problema es...", "opciones": ["Identificar el problema", "Elegir sin pensar", "Ignorarlo"], "correcta": 0},
            {"pregunta": "Si no encuentro un archivo debo...", "opciones": ["Buscarlo en su carpeta", "Rendirme", "Apagar todo"], "correcta": 0},
            {"pregunta": "Si un desconocido pide mis datos debo...", "opciones": ["No responder y avisar a un adulto", "Dárselos", "Publicarlos"], "correcta": 0},
            {"pregunta": "Si la computadora no tiene espacio puedo...", "opciones": ["Borrar lo que no uso o pasarlo a una USB", "Comprar otra pantalla", "Nada"], "correcta": 0},
            {"pregunta": "Si la PC va lenta con muchos programas...", "opciones": ["Cierro los que no uso", "Abro más", "La golpeo"], "correcta": 0},
            {"pregunta": "Después de identificar el problema debemos...", "opciones": ["Pensar posibles soluciones", "Apagar la PC", "Nada"], "correcta": 0},
            {"pregunta": "Al resolver un problema es importante...", "opciones": ["Pensar con calma", "Actuar sin pensar", "Enojarse"], "correcta": 0},
            {"pregunta": "Si una solución no funciona, debemos...", "opciones": ["Intentar otra", "Rendirnos", "Llorar"], "correcta": 0},
            {"pregunta": "Seguir los pasos en orden nos ayuda a...", "opciones": ["Resolver correctamente", "Perder tiempo", "Nada"], "correcta": 0},
            {"pregunta": "Pedir ayuda a un adulto cuando algo es difícil es...", "opciones": ["Una buena idea", "Algo malo", "Prohibido"], "correcta": 0},
        ],
    },
    # =================================================================================
    9: {
        "titulo": "Pensamiento computacional",
        "icono": "🔢",
        "umbral": 240,
        "contenido": [
            ("¿Qué es un algoritmo?",
             "Un algoritmo es una serie de pasos ordenados para lograr un objetivo. ¡Seguir instrucciones en el "
             "orden correcto es muy importante!"),
            ("Instrucciones y secuencias",
             "Una instrucción es una orden. Una secuencia es un conjunto de instrucciones en orden.\n\n"
             "Ejemplo: 'Preparar un vaso de agua'\n1. Tomar un vaso.\n2. Ponerlo bajo el grifo.\n"
             "3. Abrir el grifo.\n4. Llenar el vaso.\n5. Cerrar el grifo."),
            ("Descomposición y patrones",
             "Descomponer es dividir un problema grande en partes pequeñas y fáciles. Reconocer patrones "
             "(cosas que se repiten) nos ayuda a resolver más rápido."),
            ("Abstracción, condiciones y repeticiones",
             "• Abstracción: quedarnos con lo importante y dejar de lado lo que no sirve.\n"
             "• Condición: 'SI ocurre algo, ENTONCES hago una acción'.\n"
             "• Repetición: hacer varias veces la misma acción (un bucle)."),
        ],
        "actividades": [
            {"id": "m9_a1", "tipo": "ordenar", "titulo": "Algoritmo: preparar un vaso de agua",
             "puntos": 10, "categoria": "computacion", "instruccion": "Ordena el algoritmo:",
             "items": ["Tomar un vaso", "Colocar el vaso debajo del grifo", "Abrir el grifo",
                       "Llenar el vaso", "Cerrar el grifo"]},
            {"id": "m9_a2", "tipo": "ordenar", "titulo": "Algoritmo: lavarse las manos",
             "puntos": 10, "categoria": "computacion", "instruccion": "Ordena el algoritmo:",
             "items": ["Abrir el grifo", "Mojarse las manos", "Poner jabón",
                       "Frotar las manos", "Enjuagar y cerrar el grifo"]},
            {"id": "m9_a3", "tipo": "seleccion", "titulo": "Conceptos del pensamiento computacional",
             "puntos": 5, "categoria": "computacion",
             "preguntas": [
                {"pregunta": "Un algoritmo es...", "opciones": ["Pasos ordenados para lograr algo", "Un juguete", "Una fruta"], "correcta": 0},
                {"pregunta": "Descomponer un problema significa...", "opciones": ["Dividirlo en partes pequeñas", "Ignorarlo", "Borrarlo"], "correcta": 0},
                {"pregunta": "Una repetición (bucle) es...", "opciones": ["Hacer varias veces la misma acción", "Borrar todo", "Apagar"], "correcta": 0},
             ]},
            {"id": "m9_a4", "tipo": "relacionar", "titulo": "Relaciona el concepto",
             "puntos": 10, "categoria": "computacion",
             "pares": [("Pasos ordenados para un objetivo", "Algoritmo"),
                       ("Dividir en partes pequeñas", "Descomposición"),
                       ("SI ocurre algo, ENTONCES actúo", "Condición"),
                       ("Repetir una acción varias veces", "Repetición")]},
            {"id": "m9_a5", "tipo": "laberinto", "titulo": "Guía al personaje hasta la meta",
             "puntos": 10, "categoria": "computacion"},
            {"id": "m9_b1", "tipo": "bloques", "titulo": "🤖 Lleva el robot al tesoro",
             "puntos": 15, "categoria": "computacion",
             "instruccion": "Arma el programa con bloques para que el robot 🤖 llegue al tesoro 🎯. Usa AVANZAR y los giros.",
             "mapa": [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 0], [0, 0, 0, 0, 0]],
             "inicio": [0, 0], "meta": [4, 4], "mirando": "derecha"},
        ],
        "evaluacion": [
            {"pregunta": "Un algoritmo es...", "opciones": ["Pasos ordenados para lograr algo", "Un color", "Un sonido"], "correcta": 0},
            {"pregunta": "Descomponer un problema es...", "opciones": ["Dividirlo en partes pequeñas", "Hacerlo más grande", "Ignorarlo"], "correcta": 0},
            {"pregunta": "El orden de las instrucciones es...", "opciones": ["Muy importante", "Sin importancia", "Prohibido"], "correcta": 0},
            {"pregunta": "Un patrón es...", "opciones": ["Algo que se repite con un orden", "Un archivo", "Un cable"], "correcta": 0},
            {"pregunta": "Una condición dice...", "opciones": ["SI ocurre algo, ENTONCES hago una acción", "Nada", "Apaga la PC"], "correcta": 0},
            {"pregunta": "Una repetición (bucle) es...", "opciones": ["Repetir una acción varias veces", "Borrar", "Un virus"], "correcta": 0},
            {"pregunta": "Abstraer es...", "opciones": ["Quedarse con lo importante", "Complicar todo", "Nada"], "correcta": 0},
            {"pregunta": "Si cambiamos el orden de los pasos, el resultado...", "opciones": ["Puede salir mal", "Siempre es igual", "No importa"], "correcta": 0},
            {"pregunta": "Para lavarse las manos, ¿qué se hace primero?", "opciones": ["Abrir el grifo", "Poner jabón", "Secarse"], "correcta": 0},
            {"pregunta": "El pensamiento computacional ayuda a...", "opciones": ["Resolver problemas paso a paso", "Perder tiempo", "Nada"], "correcta": 0},
        ],
    },
    # =================================================================================
    10: {
        "titulo": "Introducción a la programación",
        "icono": "🧑‍💻",
        "umbral": 270,
        "contenido": [
            ("¿Qué es programar?",
             "Programar es darle instrucciones a una computadora para que haga una tarea. La computadora hace "
             "exactamente lo que le decimos, ¡por eso las instrucciones deben ser claras y estar en orden!"),
            ("¿Qué es un código?",
             "El código son las instrucciones escritas en un lenguaje que la computadora entiende. Puede escribirse "
             "con palabras o, para aprender, con bloques de colores que se unen."),
            ("Secuencias, condiciones y repeticiones",
             "• Secuencia: instrucciones una tras otra.\n"
             "• Condición: SI pasa algo, ENTONCES haz una acción.\n"
             "• Repetición: REPETIR una acción varias veces."),
            ("Variables (con un ejemplo)",
             "Una variable es como una cajita con un nombre donde guardamos un valor. Por ejemplo, la variable "
             "'puntos' puede guardar 10 y luego cambiar a 20."),
            ("Los errores son normales",
             "Cuando un programa no funciona hay un 'error' o 'bug'. Buscar y corregir errores se llama 'depurar' "
             "y es parte natural de programar. ¡No hay que frustrarse!"),
        ],
        "actividades": [
            {"id": "m10_a1", "tipo": "ordenar", "titulo": "Ordena los bloques: dibujar un cuadrado",
             "puntos": 10, "categoria": "programacion", "instruccion": "Ordena los bloques para dibujar un cuadrado (4 lados):",
             "items": ["Avanzar", "Girar", "Avanzar", "Girar", "Avanzar", "Girar", "Avanzar"]},
            {"id": "m10_a2", "tipo": "ordenar", "titulo": "Ordena el programa: saludar",
             "puntos": 10, "categoria": "programacion", "instruccion": "Ordena las instrucciones del programa:",
             "items": ["Iniciar el programa", "Pedir el nombre", "Mostrar 'Hola' + el nombre", "Terminar el programa"]},
            {"id": "m10_a3", "tipo": "seleccion", "titulo": "Conceptos de programación",
             "puntos": 5, "categoria": "programacion",
             "preguntas": [
                {"pregunta": "Programar es...", "opciones": ["Dar instrucciones a la computadora", "Apagar la PC", "Dibujar en papel"], "correcta": 0},
                {"pregunta": "Una variable es como...", "opciones": ["Una cajita que guarda un valor", "Un cable", "Una silla"], "correcta": 0},
                {"pregunta": "Un 'bug' es...", "opciones": ["Un error en el programa", "Un premio", "Un juego"], "correcta": 0},
             ]},
            {"id": "m10_a4", "tipo": "relacionar", "titulo": "Relaciona el bloque con lo que hace",
             "puntos": 10, "categoria": "programacion",
             "pares": [("AVANZAR", "Mover al personaje hacia adelante"),
                       ("GIRAR", "Cambiar de dirección"),
                       ("REPETIR", "Hacer algo varias veces"),
                       ("SI... ENTONCES", "Actuar solo si se cumple una condición")]},
            {"id": "m10_a5", "tipo": "seleccion", "titulo": "¿Qué instrucción falta?",
             "puntos": 10, "categoria": "programacion",
             "preguntas": [
                {"pregunta": "Para repetir 3 veces un salto usamos el bloque...", "opciones": ["REPETIR 3 veces: Saltar", "Saltar solo una vez", "Apagar"], "correcta": 0},
                {"pregunta": "Para actuar solo cuando hay un obstáculo usamos...", "opciones": ["SI hay obstáculo ENTONCES girar", "Avanzar siempre", "Nada"], "correcta": 0},
             ]},
            {"id": "m10_b1", "tipo": "bloques", "titulo": "🤖 Reto de programación: rescata el tesoro",
             "puntos": 15, "categoria": "programacion",
             "instruccion": "Programa al robot con bloques para llegar al tesoro. ¡Piensa la ruta antes de ejecutar!",
             "mapa": [[0, 0, 0, 1, 0], [1, 1, 0, 1, 0], [0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]],
             "inicio": [0, 0], "meta": [4, 0], "mirando": "derecha"},
        ],
        "evaluacion": [
            {"pregunta": "Programar es...", "opciones": ["Dar instrucciones a la computadora", "Comer", "Dormir"], "correcta": 0},
            {"pregunta": "El código es...", "opciones": ["Las instrucciones que la computadora entiende", "Una fruta", "Un cable"], "correcta": 0},
            {"pregunta": "Una secuencia es...", "opciones": ["Instrucciones una tras otra", "Un dibujo", "Un virus"], "correcta": 0},
            {"pregunta": "Una condición dice...", "opciones": ["SI pasa algo, ENTONCES haz una acción", "Nada", "Apaga"], "correcta": 0},
            {"pregunta": "Una repetición sirve para...", "opciones": ["Repetir una acción varias veces", "Borrar", "Apagar"], "correcta": 0},
            {"pregunta": "Una variable es...", "opciones": ["Una cajita que guarda un valor", "Un cable", "Una silla"], "correcta": 0},
            {"pregunta": "Un error en un programa se llama...", "opciones": ["Bug", "Premio", "Menú"], "correcta": 0},
            {"pregunta": "Corregir errores en un programa se llama...", "opciones": ["Depurar", "Apagar", "Borrar"], "correcta": 0},
            {"pregunta": "La computadora hace...", "opciones": ["Lo que le decimos con instrucciones claras", "Lo que quiere", "Nada"], "correcta": 0},
            {"pregunta": "Si mi programa falla, debo...", "opciones": ["Buscar el error y corregirlo", "Frustrarme y rendirme", "Apagar todo"], "correcta": 0},
        ],
    },
    # =================================================================================
    11: {
        "titulo": "Inteligencia artificial y tecnologías actuales",
        "icono": "🤖",
        "umbral": 300,
        "contenido": [
            ("¿Qué es la inteligencia artificial (IA)?",
             "La IA es tecnología que hace que las computadoras 'aprendan' de muchos ejemplos para realizar "
             "tareas que parecían solo humanas, como reconocer voces o imágenes."),
            ("IA que usamos todos los días",
             "• Asistentes virtuales que responden con la voz.\n• Reconocimiento de voz (dictar un mensaje).\n"
             "• Recomendaciones de videos y música.\n• Traducción automática de idiomas.\n"
             "• Reconocimiento de imágenes (reconocer una cara o un objeto en una foto)."),
            ("IA generativa (explicada fácil)",
             "Algunas IA pueden 'crear' cosas nuevas: textos, imágenes o dibujos, a partir de lo que les pedimos. "
             "Son útiles, pero pueden equivocarse."),
            ("Uso responsable de la IA",
             "• Verifica siempre la información que te da una IA; puede tener errores.\n"
             "• Cuida tu privacidad: no le des datos personales.\n"
             "• La IA es una herramienta; las decisiones importantes las tomamos las personas."),
            ("Tecnología y futuro",
             "La tecnología cambia muy rápido. Aprender a usarla bien y con responsabilidad nos abre muchas "
             "oportunidades para el futuro."),
        ],
        "actividades": [
            {"id": "m11_a1", "tipo": "clasificar", "titulo": "¿Usa inteligencia artificial?",
             "puntos": 15, "categoria": "ia",
             "categorias": ["Usa IA", "No usa IA"],
             "items": [("Un asistente de voz que responde preguntas", "Usa IA"),
                       ("Una calculadora simple", "No usa IA"),
                       ("Recomendaciones de videos según lo que ves", "Usa IA"),
                       ("Una linterna", "No usa IA"),
                       ("Traducir un texto automáticamente", "Usa IA"),
                       ("Un lápiz", "No usa IA")]},
            {"id": "m11_a2", "tipo": "relacionar", "titulo": "Relaciona el ejemplo de IA",
             "puntos": 10, "categoria": "ia",
             "pares": [("Responde con la voz", "Asistente virtual"),
                       ("Convierte tu voz en texto", "Reconocimiento de voz"),
                       ("Cambia un texto a otro idioma", "Traducción automática"),
                       ("Identifica objetos en una foto", "Reconocimiento de imágenes")]},
            {"id": "m11_a3", "tipo": "seleccion", "titulo": "Uso responsable de la IA",
             "puntos": 5, "categoria": "ia",
             "preguntas": [
                {"pregunta": "¿La información que da una IA siempre es correcta?", "opciones": ["Sí, siempre", "No, hay que verificarla"], "correcta": 1},
                {"pregunta": "¿Debo darle mis datos personales a una IA?", "opciones": ["No", "Sí, todos"], "correcta": 0},
                {"pregunta": "La IA es...", "opciones": ["Una herramienta que nos ayuda", "Una persona real", "Un juguete mágico"], "correcta": 0},
             ]},
            {"id": "m11_a4", "tipo": "seleccion", "titulo": "¿Verdadero o falso sobre la IA?",
             "puntos": 10, "categoria": "ia",
             "preguntas": [
                {"pregunta": "La IA aprende de muchos ejemplos.", "opciones": ["Verdadero", "Falso"], "correcta": 0},
                {"pregunta": "La IA nunca se equivoca.", "opciones": ["Verdadero", "Falso"], "correcta": 1},
                {"pregunta": "Las decisiones importantes las toman las personas.", "opciones": ["Verdadero", "Falso"], "correcta": 0},
             ]},
        ],
        "evaluacion": [
            {"pregunta": "La inteligencia artificial (IA) hace que las computadoras...", "opciones": ["Aprendan de ejemplos para hacer tareas", "Se apaguen solas", "No sirvan"], "correcta": 0},
            {"pregunta": "Un asistente virtual usa...", "opciones": ["Inteligencia artificial", "Una linterna", "Un lápiz"], "correcta": 0},
            {"pregunta": "Las recomendaciones de videos usan...", "opciones": ["IA", "Magia", "Nada"], "correcta": 0},
            {"pregunta": "La traducción automática...", "opciones": ["Usa IA", "No existe", "Es un juego"], "correcta": 0},
            {"pregunta": "La IA generativa puede...", "opciones": ["Crear textos o imágenes", "Cocinar", "Volar"], "correcta": 0},
            {"pregunta": "¿La información de una IA siempre es correcta?", "opciones": ["No, hay que verificar", "Sí, siempre", "Nunca sirve"], "correcta": 0},
            {"pregunta": "¿Debo dar datos personales a una IA?", "opciones": ["No", "Sí, todos", "Solo mi dirección"], "correcta": 0},
            {"pregunta": "Una calculadora simple...", "opciones": ["No usa IA", "Usa IA", "Es un robot"], "correcta": 0},
            {"pregunta": "La IA es principalmente...", "opciones": ["Una herramienta que nos ayuda", "Una persona", "Un ser vivo"], "correcta": 0},
            {"pregunta": "Las decisiones importantes las toman...", "opciones": ["Las personas", "Solo la IA", "Nadie"], "correcta": 0},
        ],
    },
    # =================================================================================
    12: {
        "titulo": "Gran reto final",
        "icono": "🏆",
        "umbral": 330,
        "contenido": [
            ("¡Llegaste al Gran Reto Final!",
             "En este módulo pondrás a prueba TODO lo que aprendiste en Primero Básico: dispositivos, uso de la "
             "computadora, teclado, archivos, Internet, seguridad, lógica, resolución de problemas, algoritmos, "
             "programación e inteligencia artificial."),
            ("¿Cómo funciona?",
             "Completa cada reto para ganar puntos. Al terminar todos los retos y aprobar la evaluación final, "
             "desbloquearás la insignia especial 🏆 'Experto Digital – Primero Básico'. ¡Mucho éxito!"),
        ],
        "actividades": [
            {"id": "m12_a1", "tipo": "clasificar", "titulo": "Reto 1: identifica componentes",
             "puntos": 10, "categoria": "juego",
             "categorias": ["Hardware", "Software"],
             "items": [("Mouse", "Hardware"), ("Juego educativo", "Software"), ("Teclado", "Hardware"),
                       ("Navegador", "Software"), ("Monitor", "Hardware"), ("Procesador de texto", "Software")]},
            {"id": "m12_a2", "tipo": "clasificar", "titulo": "Reto 2: organiza los archivos",
             "puntos": 10, "categoria": "juego",
             "categorias": ["Documentos", "Imágenes", "Videos"],
             "items": [("Tarea.docx", "Documentos"), ("Foto.jpg", "Imágenes"), ("Clip.mp4", "Videos"),
                       ("Carta.docx", "Documentos"), ("Paisaje.jpg", "Imágenes"), ("Baile.mp4", "Videos")]},
            {"id": "m12_a3", "tipo": "patron", "titulo": "Reto 3: problema lógico",
             "puntos": 10, "categoria": "juego",
             "patrones": [
                {"secuencia": "🟡 🟢 🟢 🟡 🟢 🟢", "opciones": ["🟡", "🟢", "🔴"], "correcta": 0},
                {"secuencia": "3 - 6 - 9 -", "opciones": ["10", "12", "13"], "correcta": 1},
             ]},
            {"id": "m12_a4", "tipo": "laberinto", "titulo": "Reto 4: resuelve el laberinto",
             "puntos": 10, "categoria": "juego"},
            {"id": "m12_a5", "tipo": "clasificar", "titulo": "Reto 5: ¿seguro o peligroso en Internet?",
             "puntos": 10, "categoria": "juego",
             "categorias": ["Seguro", "Peligroso"],
             "items": [("Dar tu contraseña a un desconocido", "Peligroso"),
                       ("Usar un enlace que te dio tu maestro", "Seguro"),
                       ("Publicar tu dirección de casa", "Peligroso"),
                       ("Cerrar sesión al terminar", "Seguro")]},
            {"id": "m12_a6", "tipo": "ordenar", "titulo": "Reto 6: crea un algoritmo",
             "puntos": 10, "categoria": "juego", "instruccion": "Ordena el algoritmo para preparar una mochila:",
             "items": ["Abrir la mochila", "Meter los cuadernos", "Meter la lonchera", "Cerrar la mochila"]},
            {"id": "m12_a7", "tipo": "relacionar", "titulo": "Reto 7: programación visual",
             "puntos": 10, "categoria": "juego",
             "pares": [("AVANZAR", "Mover adelante"), ("GIRAR", "Cambiar dirección"),
                       ("REPETIR", "Hacer varias veces"), ("SI... ENTONCES", "Actuar si se cumple algo")]},
            {"id": "m12_final", "tipo": "gran_reto", "titulo": "🏆 GRAN RETO FINAL",
             "puntos": 30, "categoria": "juego",
             "instruccion": "Encadena un reto de cada tema. ¡Responde bien para avanzar hasta la pantalla de victoria!",
             "pasos": [
                {"tema": "Componentes", "pregunta": "¿Cuál de estos es hardware?", "opciones": ["El mouse", "Un juego", "Una canción"], "correcta": 0},
                {"tema": "Archivos", "pregunta": "Una foto se guarda como archivo de tipo...", "opciones": ["Imagen (.jpg)", "Audio (.mp3)", "Documento (.docx)"], "correcta": 0},
                {"tema": "Internet seguro", "pregunta": "Dar tu contraseña a un desconocido es...", "opciones": ["Peligroso", "Seguro", "Recomendable"], "correcta": 0},
                {"tema": "Lógica", "pregunta": "2 - 4 - 6 - __  ¿Qué número sigue?", "opciones": ["7", "8", "9"], "correcta": 1},
                {"tema": "Algoritmos", "pregunta": "Un algoritmo es...", "opciones": ["Pasos ordenados para lograr algo", "Un color", "Un cable"], "correcta": 0},
                {"tema": "Programación", "pregunta": "Para mover al robot hacia adelante usamos el bloque...", "opciones": ["AVANZAR", "BORRAR", "APAGAR"], "correcta": 0},
                {"tema": "Inteligencia artificial", "pregunta": "Un asistente de voz que responde preguntas usa...", "opciones": ["Inteligencia artificial", "Una linterna", "Un lápiz"], "correcta": 0},
             ]},
        ],
        "evaluacion": [
            {"pregunta": "¿Qué parte usamos para hacer clic?", "opciones": ["Mouse", "Bocinas"], "correcta": 0},
            {"pregunta": "El mouse es...", "opciones": ["Hardware", "Software"], "correcta": 0},
            {"pregunta": "Un navegador es...", "opciones": ["Software", "Hardware"], "correcta": 0},
            {"pregunta": "Una foto se guarda como...", "opciones": ["Imagen (.jpg)", "Audio (.mp3)"], "correcta": 0},
            {"pregunta": "Dar tu contraseña a un desconocido es...", "opciones": ["Peligroso", "Seguro"], "correcta": 0},
            {"pregunta": "3 - 6 - 9 - __", "opciones": ["10", "12"], "correcta": 1},
            {"pregunta": "Un algoritmo es...", "opciones": ["Pasos ordenados para lograr algo", "Un color"], "correcta": 0},
            {"pregunta": "Programar es...", "opciones": ["Dar instrucciones a la computadora", "Dormir"], "correcta": 0},
            {"pregunta": "Un asistente de voz usa...", "opciones": ["Inteligencia artificial", "Una linterna"], "correcta": 0},
            {"pregunta": "¿Completaste todo Primero Básico?", "opciones": ["¡Sí, con esfuerzo!", "No lo sé"], "correcta": 0},
        ],
    },
}
