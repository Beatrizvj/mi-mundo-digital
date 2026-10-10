"""Panel del Docente — Mi Mundo Digital.

Módulo autónomo que implementa TODA la pantalla del docente: gestión de
estudiantes, progreso, reportes en PDF y cambio de contraseña. Deliberadamente
separado de app.py para que las modificaciones de esta funcionalidad no toquen
las pantallas del estudiante (módulos, juegos, evaluaciones, puntos).

Convenciones (iguales a las de app.py): conexión a "encarta_educativa.db" por
operación, consultas parametrizadas, y uso de seguridad.registrar_evento para
dejar rastro de las acciones del docente.
"""
import datetime
import os
import re
import sqlite3
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, ttk

import pdf_simple
import seguridad

DB_PATH = "encarta_educativa.db"
GRADOS = {1: "Primero Básico", 2: "Segundo Básico", 3: "Tercero Básico"}


# ============================================================ acceso a datos
def _conectar():
    return sqlite3.connect(DB_PATH)


def listar_estudiantes(grado=None, busqueda=""):
    con = _conectar()
    try:
        sql = "SELECT id, nombre, grado, puntos FROM estudiantes WHERE 1=1"
        params = []
        if grado:
            sql += " AND grado=?"
            params.append(grado)
        if busqueda:
            sql += " AND nombre LIKE ?"
            params.append("%{}%".format(busqueda))
        sql += " ORDER BY nombre COLLATE NOCASE"
        return con.execute(sql, params).fetchall()
    finally:
        con.close()


def agregar_estudiante(nombre, grado):
    con = _conectar()
    try:
        cur = con.execute("INSERT INTO estudiantes (nombre, grado, puntos) VALUES (?, ?, 0)", (nombre, grado))
        con.commit()
        return cur.lastrowid
    finally:
        con.close()


def editar_estudiante(est_id, nombre, grado):
    con = _conectar()
    try:
        con.execute("UPDATE estudiantes SET nombre=?, grado=? WHERE id=?", (nombre, grado, est_id))
        con.commit()
    finally:
        con.close()


def eliminar_estudiante(est_id):
    con = _conectar()
    try:
        con.execute("DELETE FROM actividades_completadas WHERE estudiante_id=?", (est_id,))
        con.execute("DELETE FROM progreso WHERE estudiante_id=?", (est_id,))
        con.execute("DELETE FROM retos_diarios WHERE estudiante_id=?", (est_id,))
        con.execute("DELETE FROM estudiantes WHERE id=?", (est_id,))
        con.commit()
    finally:
        con.close()


def reiniciar_progreso(est_id):
    con = _conectar()
    try:
        con.execute("UPDATE estudiantes SET puntos = 0 WHERE id = ?", (est_id,))
        con.execute("DELETE FROM progreso WHERE estudiante_id = ?", (est_id,))
        con.commit()
    finally:
        con.close()


def progreso_detalle(est_id):
    """Resumen completo de un estudiante: módulos, evaluaciones e insignias.
    Importa app.py de forma diferida (no al cargar este módulo) para evitar un
    import circular, ya que app.py es quien abre este panel."""
    import app

    con = _conectar()
    try:
        fila = con.execute("SELECT nombre, grado, puntos, xp FROM estudiantes WHERE id=?", (est_id,)).fetchone()
        if fila is None:
            return None
        nombre, grado, puntos, xp = fila
        evaluaciones = con.execute(
            "SELECT tema, calificacion, completado FROM progreso "
            "WHERE estudiante_id=? AND tema LIKE 'Evaluación%' AND id IN "
            "(SELECT MAX(id) FROM progreso WHERE estudiante_id=? AND tema LIKE 'Evaluación%' GROUP BY tema) "
            "ORDER BY id",
            (est_id, est_id),
        ).fetchall()
    finally:
        con.close()

    modulos, prefijo, total = app.datos_grado(grado)
    completados = sum(1 for m in range(1, total + 1) if app.modulo_esta_completo(est_id, m, modulos, prefijo))
    porcentaje = round(completados / total * 100) if total else 0
    claves_insignias = app.obtener_insignias_estudiante(est_id)
    insignias = [app.INSIGNIAS_INFO.get(c, {}).get("nombre", c) for c in claves_insignias]

    return {
        "id": est_id,
        "nombre": nombre,
        "grado": grado,
        "grado_nombre": GRADOS.get(grado, "—"),
        "puntos": puntos,
        "xp": xp,
        "modulos_completados": completados,
        "total_modulos": total,
        "porcentaje": porcentaje,
        "evaluaciones": [(t, c, bool(a)) for (t, c, a) in evaluaciones],
        "insignias": insignias,
    }


# =================================================================== reportes
def _nombre_archivo_sugerido(prefijo):
    fecha = datetime.date.today().isoformat()
    return "{}_{}.pdf".format(prefijo, fecha)


def generar_reporte_individual(est_id, ruta):
    d = progreso_detalle(est_id)
    if d is None:
        raise ValueError("El estudiante ya no existe.")
    r = pdf_simple.PDFReporte()
    r.titulo("Reporte de progreso — {}".format(d["nombre"]))
    r.subtitulo(d["grado_nombre"])
    r.parrafo("Puntos: {}   ·   Módulos completados: {}/{}   ·   Progreso: {}%".format(
        d["puntos"], d["modulos_completados"], d["total_modulos"], d["porcentaje"]))
    r.espacio(6)
    r.subtitulo("Evaluaciones")
    if d["evaluaciones"]:
        r.tabla(["Evaluación", "Calificación", "Resultado"],
                [[t, "{}%".format(c), "Aprobada" if a else "No aprobada"] for (t, c, a) in d["evaluaciones"]],
                anchos=[330, 90, 92])
    else:
        r.parrafo("Sin evaluaciones realizadas todavía.")
    r.espacio(6)
    r.subtitulo("Insignias obtenidas")
    # los emoji del nombre de la insignia no existen en la fuente del PDF: se quitan para no imprimir «?»
    limpias = [re.sub(r"^[^\wÁÉÍÓÚÜÑáéíóúüñ]+", "", n) for n in d["insignias"]]
    r.parrafo(", ".join(limpias) if limpias else "Ninguna todavía.")
    r.pie_fecha()
    r.guardar(ruta)


def _tabla_resumen(r, titulo, filas_detalle):
    r.titulo(titulo)
    if not filas_detalle:
        r.parrafo("No hay estudiantes registrados.")
    else:
        r.tabla(["Nombre", "Grado", "Puntos", "Módulos", "Progreso"],
                [[d["nombre"], d["grado_nombre"], d["puntos"],
                  "{}/{}".format(d["modulos_completados"], d["total_modulos"]), "{}%".format(d["porcentaje"])]
                 for d in filas_detalle],
                anchos=[170, 110, 60, 80, 92])
    r.pie_fecha()


def generar_reporte_grado(grado, ruta):
    estudiantes = listar_estudiantes(grado=grado)
    detalles = [progreso_detalle(e[0]) for e in estudiantes]
    r = pdf_simple.PDFReporte()
    _tabla_resumen(r, "Reporte de {} — Todos los estudiantes".format(GRADOS.get(grado, "")), detalles)
    r.guardar(ruta)


def generar_reporte_general(ruta):
    estudiantes = listar_estudiantes()
    detalles = [progreso_detalle(e[0]) for e in estudiantes]
    r = pdf_simple.PDFReporte()
    _tabla_resumen(r, "Reporte general — Todos los estudiantes", detalles)
    r.guardar(ruta)


# ======================================================================== UI
class PanelDocente:
    """Construye y maneja la ventana del Panel del Docente."""

    def __init__(self, app_instance):
        self.app = app_instance
        self.root = app_instance.root
        self.font_family = getattr(app_instance, "font_family", "Segoe UI")
        self.bg_color = getattr(app_instance, "bg_color", "#EEF2F7")
        self.primary_color = getattr(app_instance, "primary_color", "#4F46E5")
        self.secondary_color = getattr(app_instance, "secondary_color", "#0D9488")
        self.accent_color = getattr(app_instance, "accent_color", "#F59E0B")
        self.text_dark = getattr(app_instance, "text_dark", "#0F172A")
        self.text_muted = getattr(app_instance, "text_muted", "#64748B")
        self.danger_color = "#EF4444"

        self.grado_filtro = None   # None = todos
        self.busqueda_var = None

        self.win = tk.Toplevel(self.root)
        self.win.title("Panel del Docente")
        self.win.geometry("900x620")
        self.win.minsize(820, 560)
        self.win.configure(bg=self.bg_color)
        self.win.grab_set()

        self._construir_header()
        self.body = tk.Frame(self.win, bg=self.bg_color)
        self.body.pack(fill="both", expand=True, padx=20, pady=(0, 15))

        self.mostrar_estudiantes()

    # --------------------------------------------------------------- chrome
    def _boton_nav(self, parent, texto, comando):
        return tk.Button(parent, text=texto, font=(self.font_family, 10, "bold"),
                         bg="white", fg=self.text_dark, bd=0, padx=12, pady=8,
                         activebackground="#E2E8F0", cursor="hand2", command=comando)

    def _construir_header(self):
        header = tk.Frame(self.win, bg=self.bg_color)
        header.pack(fill="x", padx=20, pady=15)
        tk.Label(header, text="📊 Panel de Control Docente", font=(self.font_family, 16, "bold"),
                 bg=self.bg_color, fg=self.primary_color).pack(side="left")

        nav = tk.Frame(self.win, bg=self.bg_color)
        nav.pack(fill="x", padx=20)
        botones = [
            ("👨‍🎓 Estudiantes", self.mostrar_estudiantes),
            ("📊 Progreso", self.mostrar_progreso),
            ("📄 Reportes PDF", self.mostrar_reportes),
            ("🔐 Cambiar contraseña", self.mostrar_cambiar_password),
            ("🚪 Cerrar sesión", self.cerrar_sesion),
        ]
        for texto, cmd in botones:
            self._boton_nav(nav, texto, cmd).pack(side="left", padx=(0, 8), pady=(0, 10))

    def _limpiar_body(self):
        for w in self.body.winfo_children():
            w.destroy()

    def _titulo_seccion(self, texto):
        tk.Label(self.body, text=texto, font=(self.font_family, 13, "bold"),
                 bg=self.bg_color, fg=self.text_dark).pack(anchor="w", pady=(0, 10))

    def cerrar_sesion(self):
        self.win.destroy()

    # ---------------------------------------------------------- Estudiantes
    def mostrar_estudiantes(self):
        self._limpiar_body()
        self._titulo_seccion("👨‍🎓 Gestión de estudiantes")

        barra = tk.Frame(self.body, bg=self.bg_color)
        barra.pack(fill="x", pady=(0, 10))

        tk.Label(barra, text="Buscar:", font=(self.font_family, 10), bg=self.bg_color).pack(side="left")
        self.busqueda_var = tk.StringVar()
        entry = tk.Entry(barra, textvariable=self.busqueda_var, font=(self.font_family, 10), width=22)
        entry.pack(side="left", padx=(6, 16))
        self.busqueda_var.trace_add("write", lambda *_: self._refrescar_tabla())

        tk.Label(barra, text="Grado:", font=(self.font_family, 10), bg=self.bg_color).pack(side="left")
        self.combo_grado = ttk.Combobox(barra, state="readonly", width=16,
                                        values=["Todos"] + [GRADOS[g] for g in (1, 2, 3)])
        self.combo_grado.current(0)
        self.combo_grado.pack(side="left", padx=(6, 16))
        self.combo_grado.bind("<<ComboboxSelected>>", lambda *_: self._refrescar_tabla())

        frame_tabla = tk.Frame(self.body, bg=self.bg_color)
        frame_tabla.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(frame_tabla, columns=("ID", "Nombre", "Grado", "Puntos"),
                                 show="headings", height=14)
        for col, w, anchor in (("ID", 50, "center"), ("Nombre", 320, "w"),
                               ("Grado", 140, "center"), ("Puntos", 100, "center")):
            self.tree.heading(col, text=col if col != "Nombre" else "Nombre del estudiante")
            self.tree.column(col, width=w, anchor=anchor)
        self.tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.bind("<Double-1>", lambda *_: self._ver_progreso_seleccionado())

        acciones = tk.Frame(self.body, bg=self.bg_color)
        acciones.pack(fill="x", pady=12)
        self._boton(acciones, "➕ Agregar", self.secondary_color, self._agregar_estudiante).pack(side="left", padx=4)
        self._boton(acciones, "✏️ Editar", self.primary_color, self._editar_estudiante).pack(side="left", padx=4)
        self._boton(acciones, "🗑️ Eliminar", self.danger_color, self._eliminar_estudiante).pack(side="left", padx=4)
        self._boton(acciones, "📊 Ver progreso", self.accent_color, self._ver_progreso_seleccionado).pack(side="left", padx=4)
        self._boton(acciones, "🔄 Reiniciar progreso", "#64748B", self._reiniciar_progreso).pack(side="left", padx=4)

        self._refrescar_tabla()

    def _boton(self, parent, texto, color, comando):
        return tk.Button(parent, text=texto, font=(self.font_family, 10, "bold"), bg=color, fg="white",
                         bd=0, padx=12, pady=8, cursor="hand2", command=comando)

    def _refrescar_tabla(self):
        grado_sel = self.combo_grado.get()
        grado = None
        for g, nombre in GRADOS.items():
            if nombre == grado_sel:
                grado = g
        for item in self.tree.get_children():
            self.tree.delete(item)
        for est_id, nombre, grado_bd, puntos in listar_estudiantes(grado, self.busqueda_var.get().strip()):
            self.tree.insert("", "end", values=(est_id, nombre, GRADOS.get(grado_bd, "—"), puntos))

    def _estudiante_seleccionado(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("Atención", "Selecciona un estudiante de la lista.", parent=self.win)
            return None
        valores = self.tree.item(sel)["values"]
        return valores[0]  # id

    def _agregar_estudiante(self):
        resultado = _dialogo_estudiante(self.win, self, "Agregar estudiante")
        if resultado is None:
            return
        nombre, grado = resultado
        est_id = agregar_estudiante(nombre, grado)
        seguridad.registrar_evento("DOCENTE_ESTUDIANTE_AGREGADO", "id={} grado={}".format(est_id, grado))
        self._refrescar_tabla()

    def _editar_estudiante(self):
        est_id = self._estudiante_seleccionado()
        if est_id is None:
            return
        actual = next((e for e in listar_estudiantes() if e[0] == est_id), None)
        if actual is None:
            return
        resultado = _dialogo_estudiante(self.win, self, "Editar estudiante",
                                        nombre_inicial=actual[1], grado_inicial=actual[2])
        if resultado is None:
            return
        nombre, grado = resultado
        editar_estudiante(est_id, nombre, grado)
        seguridad.registrar_evento("DOCENTE_ESTUDIANTE_EDITADO", "id={}".format(est_id))
        self._refrescar_tabla()

    def _eliminar_estudiante(self):
        est_id = self._estudiante_seleccionado()
        if est_id is None:
            return
        if not messagebox.askyesno(
            "Confirmar eliminación",
            "¿Eliminar a este estudiante? Se borrará también su progreso, puntos e insignias.\n"
            "Esta acción no se puede deshacer.",
            parent=self.win,
        ):
            return
        eliminar_estudiante(est_id)
        seguridad.registrar_evento("DOCENTE_ESTUDIANTE_ELIMINADO", "id={}".format(est_id))
        self._refrescar_tabla()

    def _reiniciar_progreso(self):
        est_id = self._estudiante_seleccionado()
        if est_id is None:
            return
        if not messagebox.askyesno("Confirmar", "¿Reiniciar el puntaje y el progreso de este estudiante?",
                                   parent=self.win):
            return
        reiniciar_progreso(est_id)
        seguridad.registrar_evento("DOCENTE_REINICIO_PROGRESO", "estudiante_id={}".format(est_id))
        messagebox.showinfo("Éxito", "Progreso reiniciado correctamente.", parent=self.win)
        self._refrescar_tabla()

    def _ver_progreso_seleccionado(self):
        est_id = self._estudiante_seleccionado()
        if est_id is None:
            return
        self.mostrar_progreso(est_id)

    # ------------------------------------------------------------- Progreso
    def mostrar_progreso(self, est_id=None):
        self._limpiar_body()
        self._titulo_seccion("📊 Progreso del estudiante")

        selector = tk.Frame(self.body, bg=self.bg_color)
        selector.pack(fill="x", pady=(0, 12))
        tk.Label(selector, text="Estudiante:", font=(self.font_family, 10), bg=self.bg_color).pack(side="left")

        estudiantes = listar_estudiantes()
        etiquetas = ["{} ({})".format(n, GRADOS.get(g, "—")) for (_i, n, g, _p) in estudiantes]
        combo = ttk.Combobox(selector, state="readonly", width=40, values=etiquetas)
        combo.pack(side="left", padx=8)

        detalle = tk.Frame(self.body, bg=self.bg_color)
        detalle.pack(fill="both", expand=True, pady=10)

        def pintar(d):
            for w in detalle.winfo_children():
                w.destroy()
            if d is None:
                tk.Label(detalle, text="Selecciona un estudiante para ver su progreso.",
                         font=(self.font_family, 10), bg=self.bg_color, fg=self.text_muted).pack(anchor="w")
                return
            tk.Label(detalle, text="{}  —  {}".format(d["nombre"], d["grado_nombre"]),
                     font=(self.font_family, 13, "bold"), bg=self.bg_color, fg=self.primary_color).pack(anchor="w")
            resumen = ("⭐ Puntos: {puntos}   ·   📘 Módulos completados: {mc}/{tm}   ·   "
                      "📈 Progreso: {pct}%   ·   🧪 XP: {xp}").format(
                puntos=d["puntos"], mc=d["modulos_completados"], tm=d["total_modulos"],
                pct=d["porcentaje"], xp=d["xp"])
            tk.Label(detalle, text=resumen, font=(self.font_family, 10), bg=self.bg_color,
                     fg=self.text_dark, wraplength=780, justify="left").pack(anchor="w", pady=(6, 14))

            tk.Label(detalle, text="Evaluaciones realizadas", font=(self.font_family, 11, "bold"),
                     bg=self.bg_color, fg=self.text_dark).pack(anchor="w")
            if d["evaluaciones"]:
                tabla = ttk.Treeview(detalle, columns=("Eval", "Calif", "Res"), show="headings", height=6)
                tabla.heading("Eval", text="Evaluación")
                tabla.heading("Calif", text="Calificación")
                tabla.heading("Res", text="Resultado")
                tabla.column("Eval", width=440, anchor="w")
                tabla.column("Calif", width=100, anchor="center")
                tabla.column("Res", width=120, anchor="center")
                for t, c, a in d["evaluaciones"]:
                    tabla.insert("", "end", values=(t, "{}%".format(c), "Aprobada" if a else "No aprobada"))
                tabla.pack(anchor="w", pady=(4, 14), fill="x")
            else:
                tk.Label(detalle, text="Sin evaluaciones realizadas todavía.", font=(self.font_family, 10),
                         bg=self.bg_color, fg=self.text_muted).pack(anchor="w", pady=(4, 14))

            tk.Label(detalle, text="Insignias obtenidas", font=(self.font_family, 11, "bold"),
                     bg=self.bg_color, fg=self.text_dark).pack(anchor="w")
            texto_insignias = ", ".join(d["insignias"]) if d["insignias"] else "Ninguna todavía."
            tk.Label(detalle, text=texto_insignias, font=(self.font_family, 10), bg=self.bg_color,
                     fg=self.text_dark, wraplength=780, justify="left").pack(anchor="w", pady=(4, 14))

            self._boton(detalle, "📄 Generar PDF de este estudiante", self.primary_color,
                       lambda: self._exportar_individual(d["id"], d["nombre"])).pack(anchor="w")

        def al_elegir(*_):
            idx = combo.current()
            if idx < 0:
                return
            pintar(progreso_detalle(estudiantes[idx][0]))

        combo.bind("<<ComboboxSelected>>", al_elegir)

        if est_id is not None:
            for i, e in enumerate(estudiantes):
                if e[0] == est_id:
                    combo.current(i)
                    break
            pintar(progreso_detalle(est_id))
        else:
            pintar(None)

    # -------------------------------------------------------------- Reportes
    def mostrar_reportes(self):
        self._limpiar_body()
        self._titulo_seccion("📄 Reportes PDF")
        tk.Label(self.body, text="Elige el reporte que quieres generar. Se te pedirá dónde guardarlo.",
                 font=(self.font_family, 10), bg=self.bg_color, fg=self.text_muted).pack(anchor="w", pady=(0, 16))

        opciones = tk.Frame(self.body, bg=self.bg_color)
        opciones.pack(fill="x")

        self._boton(opciones, "👤 Reporte de un estudiante", self.primary_color,
                   self._reporte_individual_dialogo).pack(fill="x", pady=4)
        self._boton(opciones, "📗 Reporte — Primero Básico", self.secondary_color,
                   lambda: self._reporte_grado(1)).pack(fill="x", pady=4)
        self._boton(opciones, "📘 Reporte — Segundo Básico", self.secondary_color,
                   lambda: self._reporte_grado(2)).pack(fill="x", pady=4)
        self._boton(opciones, "📙 Reporte — Tercero Básico", self.secondary_color,
                   lambda: self._reporte_grado(3)).pack(fill="x", pady=4)
        self._boton(opciones, "🗂️ Reporte general (todos los estudiantes)", self.accent_color,
                   self._reporte_general).pack(fill="x", pady=4)

    def _pedir_destino(self, sugerido):
        return filedialog.asksaveasfilename(
            parent=self.win, title="Guardar reporte PDF", defaultextension=".pdf",
            initialfile=sugerido, filetypes=[("Documento PDF", "*.pdf")],
        )

    def _reporte_individual_dialogo(self):
        estudiantes = listar_estudiantes()
        if not estudiantes:
            messagebox.showinfo("Sin estudiantes", "Todavía no hay estudiantes registrados.", parent=self.win)
            return
        etiquetas = ["{} ({})".format(n, GRADOS.get(g, "—")) for (_i, n, g, _p) in estudiantes]
        top = tk.Toplevel(self.win)
        top.title("Elegir estudiante")
        top.configure(bg=self.bg_color)
        top.grab_set()
        tk.Label(top, text="Selecciona el estudiante:", font=(self.font_family, 10, "bold"),
                 bg=self.bg_color).pack(padx=20, pady=(16, 6))
        combo = ttk.Combobox(top, state="readonly", width=38, values=etiquetas)
        combo.pack(padx=20, pady=6)
        combo.current(0)

        def confirmar():
            idx = combo.current()
            est_id, nombre = estudiantes[idx][0], estudiantes[idx][1]
            top.destroy()
            self._exportar_individual(est_id, nombre)

        tk.Button(top, text="Generar PDF", font=(self.font_family, 10, "bold"), bg=self.primary_color,
                 fg="white", bd=0, padx=14, pady=8, command=confirmar).pack(pady=16)

    def _exportar_individual(self, est_id, nombre):
        sugerido = _nombre_archivo_sugerido("reporte_" + "".join(c for c in nombre if c.isalnum() or c == " ").strip().replace(" ", "_"))
        ruta = self._pedir_destino(sugerido)
        if not ruta:
            return
        try:
            generar_reporte_individual(est_id, ruta)
        except OSError as exc:
            messagebox.showerror("No se pudo guardar", "No se pudo escribir el archivo:\n{}".format(exc), parent=self.win)
            return
        seguridad.registrar_evento("DOCENTE_REPORTE_PDF", "individual estudiante_id={}".format(est_id))
        messagebox.showinfo("Listo", "Reporte guardado en:\n{}".format(ruta), parent=self.win)

    def _reporte_grado(self, grado):
        ruta = self._pedir_destino(_nombre_archivo_sugerido("reporte_" + GRADOS[grado].lower().replace(" ", "_")))
        if not ruta:
            return
        try:
            generar_reporte_grado(grado, ruta)
        except OSError as exc:
            messagebox.showerror("No se pudo guardar", "No se pudo escribir el archivo:\n{}".format(exc), parent=self.win)
            return
        seguridad.registrar_evento("DOCENTE_REPORTE_PDF", "grado={}".format(grado))
        messagebox.showinfo("Listo", "Reporte guardado en:\n{}".format(ruta), parent=self.win)

    def _reporte_general(self):
        ruta = self._pedir_destino(_nombre_archivo_sugerido("reporte_general"))
        if not ruta:
            return
        try:
            generar_reporte_general(ruta)
        except OSError as exc:
            messagebox.showerror("No se pudo guardar", "No se pudo escribir el archivo:\n{}".format(exc), parent=self.win)
            return
        seguridad.registrar_evento("DOCENTE_REPORTE_PDF", "general")
        messagebox.showinfo("Listo", "Reporte guardado en:\n{}".format(ruta), parent=self.win)

    # ------------------------------------------------------ Cambiar contraseña
    def mostrar_cambiar_password(self):
        self._limpiar_body()
        self._titulo_seccion("🔐 Cambiar contraseña del docente")

        forma = tk.Frame(self.body, bg=self.bg_color)
        forma.pack(anchor="w", pady=10)

        def campo(etiqueta):
            tk.Label(forma, text=etiqueta, font=(self.font_family, 10), bg=self.bg_color).pack(anchor="w", pady=(10, 2))
            e = tk.Entry(forma, show="*", font=(self.font_family, 10), width=30)
            e.pack(anchor="w")
            return e

        e_actual = campo("Contraseña actual:")
        e_nueva = campo("Nueva contraseña:")
        e_confirmar = campo("Confirmar nueva contraseña:")

        def guardar():
            almacenado = seguridad.obtener_hash_docente()
            if almacenado is None or not seguridad.verificar_password(e_actual.get(), almacenado):
                seguridad.registrar_evento("DOCENTE_CAMBIO_PASSWORD_FALLIDO", "contraseña actual incorrecta")
                messagebox.showerror("Error", "La contraseña actual es incorrecta.", parent=self.win)
                return
            nueva, confirmar_val = e_nueva.get(), e_confirmar.get()
            if nueva != confirmar_val:
                messagebox.showwarning("No coinciden", "La nueva contraseña y su confirmación no coinciden.",
                                       parent=self.win)
                return
            ok, msg = seguridad.validar_password_nueva(nueva)
            if not ok:
                messagebox.showwarning("Contraseña débil", msg, parent=self.win)
                return
            seguridad.guardar_password_docente(nueva)
            seguridad.registrar_evento("DOCENTE_PASSWORD_CAMBIADA")
            messagebox.showinfo("Contraseña actualizada", "La contraseña se cambió correctamente.", parent=self.win)
            e_actual.delete(0, "end")
            e_nueva.delete(0, "end")
            e_confirmar.delete(0, "end")

        tk.Button(forma, text="Guardar nueva contraseña", font=(self.font_family, 10, "bold"),
                 bg=self.primary_color, fg="white", bd=0, padx=14, pady=9, cursor="hand2",
                 command=guardar).pack(anchor="w", pady=18)


def _dialogo_estudiante(parent, panel, titulo, nombre_inicial="", grado_inicial=1):
    """Modal con Nombre + Grado. Devuelve (nombre, grado) o None si se cancela."""
    resultado = {}
    top = tk.Toplevel(parent)
    top.title(titulo)
    top.configure(bg=panel.bg_color)
    top.grab_set()
    top.resizable(False, False)

    tk.Label(top, text="Nombre y apellido:", font=(panel.font_family, 10, "bold"),
             bg=panel.bg_color).pack(padx=20, pady=(18, 4), anchor="w")
    entry_nombre = tk.Entry(top, font=(panel.font_family, 10), width=32)
    entry_nombre.insert(0, nombre_inicial)
    entry_nombre.pack(padx=20)

    tk.Label(top, text="Grado:", font=(panel.font_family, 10, "bold"),
             bg=panel.bg_color).pack(padx=20, pady=(14, 4), anchor="w")
    combo_grado = ttk.Combobox(top, state="readonly", width=29, values=[GRADOS[g] for g in (1, 2, 3)])
    combo_grado.current(grado_inicial - 1 if grado_inicial in (1, 2, 3) else 0)
    combo_grado.pack(padx=20)

    def confirmar():
        ok, valor = seguridad.validar_nombre(entry_nombre.get())
        if not ok:
            messagebox.showwarning("Nombre no válido", valor, parent=top)
            return
        grado = combo_grado.current() + 1
        resultado["nombre"], resultado["grado"] = valor, grado
        top.destroy()

    def cancelar():
        top.destroy()

    botones = tk.Frame(top, bg=panel.bg_color)
    botones.pack(pady=18)
    tk.Button(botones, text="Guardar", font=(panel.font_family, 10, "bold"), bg=panel.primary_color,
             fg="white", bd=0, padx=14, pady=8, command=confirmar).pack(side="left", padx=6)
    tk.Button(botones, text="Cancelar", font=(panel.font_family, 10), bg="#E2E8F0", fg=panel.text_dark,
             bd=0, padx=14, pady=8, command=cancelar).pack(side="left", padx=6)

    top.wait_window()
    if "nombre" not in resultado:
        return None
    return resultado["nombre"], resultado["grado"]


def abrir(app_instance):
    """Punto de entrada llamado desde app.py."""
    PanelDocente(app_instance)
