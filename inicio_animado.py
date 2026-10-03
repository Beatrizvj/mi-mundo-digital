# -*- coding: utf-8 -*-
"""Encabezado animado de la pantalla de inicio de MI MUNDO DIGITAL.

Solo presentación visual: título con efecto 3D y entrada letra por letra, brillo suave que
recorre las letras, subtítulo, astronauta flotando, estrellas y símbolos tecnológicos muy
discretos. No contiene lógica del sistema ni accede a la base de datos.

Todo se dibuja con elementos del Canvas de Tkinter (sin dependencias externas); la única
imagen es el astronauta, que viene precalculado en PNG (astronauta_*.png).
"""
import math
import os
import random
import sys
import time
import tkinter as tk
import tkinter.font as tkfont

ALTOS_ASTRONAUTA = [192, 160, 128, 96]       # (el de 224 px no se usa: mover una imagen grande consume más procesador)
TITULO = "MI MUNDO DIGITAL"
SUBTITULO = "Aprende, descubre y crea en el mundo de la tecnología"
SIMBOLOS = ["</>", "{ }", "01", "π", "AI", "∑"]
INTERVALO_RAPIDO_MS = 40      # entrada y destello del título
INTERVALO_REPOSO_MS = 80      # el resto del tiempo (casi no consume procesador)


def _ruta(nombre):
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, nombre)


def _clamp(v, lo=0.0, hi=1.0):
    return lo if v < lo else hi if v > hi else v


def _mezcla(c1, c2, t):
    t = _clamp(t)
    r1, g1, b1 = int(c1[1:3], 16), int(c1[3:5], 16), int(c1[5:7], 16)
    r2, g2, b2 = int(c2[1:3], 16), int(c2[3:5], 16), int(c2[5:7], 16)
    return "#{:02x}{:02x}{:02x}".format(int(r1 + (r2 - r1) * t), int(g1 + (g2 - g1) * t), int(b1 + (b2 - b1) * t))


def _ease_out_back(p):
    c1 = 1.70158
    c3 = c1 + 1
    return 1 + c3 * (p - 1) ** 3 + c1 * (p - 1) ** 2


def _ease_out_cubic(p):
    return 1 - (1 - p) ** 3


class EncabezadoInicio:
    EXTRUSION = ["#1B1747", "#24206A", "#2E2A88", "#3A35A3"]      # capas de profundidad (de más lejos a más cerca)

    def __init__(self, app, canvas, c_top, c_bot):
        self.root = app.root
        self.c = canvas
        self.ff = app.font_family
        self.c_top, self.c_bot = c_top, c_bot
        self.t0 = time.time()
        self._visible = False       # el reloj de la animación arranca en el primer dibujo real
        self.activo = False
        self._job = None
        self.imgs = {}
        for alto in ALTOS_ASTRONAUTA:
            try:
                self.imgs[alto] = tk.PhotoImage(master=self.root, file=_ruta("astronauta_%d.png" % alto))
            except tk.TclError:
                pass            # sin imagen la pantalla funciona igual
        self._reiniciar_items()

    # ------------------------------------------------------------------ utilidades
    def _reiniciar_items(self):
        self.letras = []
        self.sub_id = None
        self.chispas = []
        self.estrellas = []
        self.simbolos = []
        self.astro = None
        self.fugaz = None
        self._cuadro = 0
        self._ult_ambiente = -10.0
        self._titulo_sucio = True
        self.w = self.h = self.oy = 0

    def _fondo(self, y):
        return _mezcla(self.c_top, self.c_bot, _clamp(y / max(1, self.h)))

    # ------------------------------------------------------------------ dibujo
    def dibujar(self, w, h, oy, tarjetas_izq):
        """Crea los elementos del encabezado (se llama cada vez que se redibuja la pantalla)."""
        c = self.c
        if not self._visible:
            self._visible = True
            self.t0 = time.time()
        self._reiniciar_items()
        self.w, self.h, self.oy = w, h, oy
        cx = w // 2

        # ---- título ----
        disponibles = set(tkfont.families(self.root))
        fam = "Segoe UI Black" if "Segoe UI Black" in disponibles else self.ff
        peso = "normal" if fam == "Segoe UI Black" else "bold"
        track = 3
        sz = 42
        while True:
            f = tkfont.Font(root=self.root, family=fam, size=sz, weight=peso)
            anchos = [f.measure(ch) for ch in TITULO]
            total = sum(anchos) + track * (len(TITULO) - 1)
            if total <= w - 400 or sz <= 24:
                break
            sz -= 2
        x_ini = cx - total / 2.0
        y_t = 62 + oy
        x = x_ini
        idx = 0
        for ch, aw in zip(TITULO, anchos):
            if ch != " ":
                ext = []
                for k, col in zip((4, 3, 2, 1), self.EXTRUSION):
                    ext.append((c.create_text(x + k * 0.8, y_t + k, text=ch, anchor="w", font=(fam, sz, peso),
                                              fill=self._fondo(y_t)), k, col))
                main = c.create_text(x, y_t, text=ch, anchor="w", font=(fam, sz, peso), fill=self._fondo(y_t))
                nuevo = idx < 8
                self.letras.append({
                    "x": x, "i": len(self.letras), "ext": ext, "main": main,
                    "base": "#FFFFFF" if nuevo else "#FDE047",
                    "brillo": "#FFE9A8" if nuevo else "#FFFFFF", "y": None, "col": None,
                })
            x += aw + track
            idx += 1
        self._titulo_rect = (x_ini - 24, 24 + oy, x_ini + total + 24, 100 + oy)

        # ---- subtítulo y destellos ----
        fs = tkfont.Font(root=self.root, family=self.ff, size=14)
        sw = fs.measure(SUBTITULO)
        self.sub_id = c.create_text(cx, 106 + oy, text=SUBTITULO, font=(self.ff, 14), fill=self._fondo(106 + oy))
        for lado in (-1, 1):
            xs = cx + lado * (sw / 2.0 + 28)
            self.chispas.append((c.create_text(xs, 106 + oy, text="✦", font=(self.ff, 13), fill=self._fondo(106 + oy)),
                                 lado, xs))
        obst = [self._titulo_rect, (cx - sw / 2.0 - 60, 94 + oy, cx + sw / 2.0 + 60, 122 + oy),
                (w - 170, 0, w, 186), (0, 0, 150, 74), (cx - 190, 138 + oy, cx + 190, 166 + oy)]

        # ---- astronauta (izquierda), del tamaño más grande que quepa ----
        for alto in ALTOS_ASTRONAUTA:
            img = self.imgs.get(alto)
            if img is None:
                continue
            iw, ih = img.width(), img.height()
            x0, y0 = 6, 62 + oy
            derecha, abajo = x0 + iw, y0 + ih
            cabe_titulo = derecha <= self._titulo_rect[0] - 10
            cabe_tarjetas = abajo <= 182 + oy or derecha <= tarjetas_izq - 6
            if cabe_titulo and cabe_tarjetas and abajo <= h - 70:
                item = c.create_image(x0 - iw - 60, y0, image=img, anchor="nw")
                self.astro = {"id": item, "x": x0, "y": y0, "iw": iw}
                obst.append((x0 - 10, y0 - 10, derecha + 10, abajo + 10))
                break

        # ---- estrellas y símbolos tecnológicos (posiciones fijas por tamaño de ventana) ----
        rnd = random.Random(2024 + w)
        def libre(px, py, margen=0):
            return all(not (r[0] - margen <= px <= r[2] + margen and r[1] - margen <= py <= r[3] + margen) for r in obst)
        for _ in range(34):
            for _intento in range(25):
                px, py = rnd.uniform(10, w - 10), rnd.uniform(8, 178 + oy)
                if libre(px, py, 6):
                    break
            else:
                continue
            r = rnd.choice((1, 1, 1.5, 2))
            it = c.create_oval(px - r, py - r, px + r, py + r, fill=self._fondo(py), outline="")
            self.estrellas.append({"id": it, "y": py, "fase": rnd.uniform(0, 6.28), "vel": rnd.uniform(0.8, 2.2),
                                   "ret": rnd.uniform(0.3, 1.8), "col": None})
        puestos = []
        for sim in SIMBOLOS:
            for _intento in range(60):
                px, py = rnd.uniform(40, w - 40), rnd.uniform(14, 170 + oy)
                if libre(px, py, 22) and all(abs(px - qx) > 110 or abs(py - qy) > 40 for qx, qy in puestos):
                    puestos.append((px, py))
                    it = c.create_text(px, py, text=sim, font=("Consolas", 15, "bold"), fill=self._fondo(py))
                    self.simbolos.append({"id": it, "x": px, "y": py, "fase": rnd.uniform(0, 6.28),
                                          "ret": rnd.uniform(0.8, 2.0)})
                    break
        self._actualizar(time.time() - self.t0)

    # ------------------------------------------------------------------ animación
    def iniciar(self):
        if self.activo:
            return
        self.activo = True
        self._tick()

    def _tick(self):
        self._job = None
        try:
            if not self.c.winfo_exists():
                self.activo = False
                return
            if self.root.state() == "iconic":          # ventana minimizada: no se anima nada
                self._job = self.root.after(500, self._tick)
                return
            rapido = self._actualizar(time.time() - self.t0)
        except tk.TclError:
            self.activo = False
            return
        self._job = self.root.after(INTERVALO_RAPIDO_MS if rapido else INTERVALO_REPOSO_MS, self._tick)

    def _actualizar(self, t):
        c = self.c
        oy = self.oy
        self._cuadro += 1
        entrando = t < 3.2                      # durante la entrada se actualiza todo en cada cuadro
        lento = entrando or (t - self._ult_ambiente) >= 0.8      # lo decorativo (estrellas, símbolos) cambia poco a poco
        if lento:
            self._ult_ambiente = t
        y_t = 62 + oy
        fondo_t = self._fondo(y_t)

        # --- Título: entrada letra por letra y, después, un brillo que recorre las letras de vez en cuando.
        #     Fuera de esos momentos no se toca nada (así casi no consume procesador).
        entrada_fin = 0.2 + 0.065 * len(self.letras) + 0.7
        ciclo = 4.8
        barrido = None
        if self.letras and t > entrada_fin + 0.4:
            fase = (t - entrada_fin - 0.4) % ciclo
            if fase < 1.5:
                x_min, x_max = self.letras[0]["x"], self.letras[-1]["x"]
                barrido = x_min - 90 + (x_max - x_min + 180) * (fase / 1.5)
        if t < entrada_fin + 0.2 or barrido is not None or self._titulo_sucio:
            self._titulo_sucio = barrido is not None
            for l in self.letras:
                p = _clamp((t - (0.2 + 0.065 * l["i"])) / 0.65)
                e = _ease_out_back(p) if p < 1 else 1.0
                yoff = (1 - e) * -48
                f = 0.0
                if barrido is not None:
                    f = max(0.0, 1 - abs(l["x"] - barrido) / 70.0) ** 2
                    yoff -= 2.5 * f
                a = _clamp(p * 1.8)
                yy = round(y_t + yoff, 1)
                if l["y"] != yy:
                    l["y"] = yy
                    c.coords(l["main"], l["x"], yy)
                    for it, k, _col in l["ext"]:
                        c.coords(it, l["x"] + k * 0.8, yy + k)
                objetivo = _mezcla(l["base"], l["brillo"], f)
                claro = _mezcla(objetivo, "#FFFFFF", 0.6)      # al aparecer pasa por un tono claro (evita marrones apagados)
                col = _mezcla(fondo_t, claro, a / 0.55) if a < 0.55 else _mezcla(claro, objetivo, (a - 0.55) / 0.45)
                if col != l["col"]:
                    l["col"] = col
                    c.itemconfigure(l["main"], fill=col)
                if a < 1 or t < entrada_fin + 0.3:
                    for it, _k, colx in l["ext"]:
                        c.itemconfigure(it, fill=_mezcla(fondo_t, colx, a))

        # --- Subtítulo y destellos
        if self.sub_id is not None:
            ps = _clamp((t - 1.3) / 0.8)
            if ps < 1 or self._cuadro <= 1:
                ys = 106 + oy + (1 - _ease_out_cubic(ps)) * 10
                c.coords(self.sub_id, self.w // 2, ys)
                c.itemconfigure(self.sub_id, fill=_mezcla(self._fondo(106 + oy), "#E0E7FF", ps))
                for it, _lado, xs in self.chispas:
                    c.coords(it, xs, ys)
            if lento:
                for k, (it, _lado, _xs) in enumerate(self.chispas):
                    tw = 0.5 + 0.5 * math.sin(t * 2.2 + k * 1.7)
                    c.itemconfigure(it, fill=_mezcla(self._fondo(106 + oy), "#FCD34D", ps * (0.45 + 0.55 * tw)))

        # --- Astronauta: entra deslizándose y luego flota suavemente
        if self.astro is not None:
            a = self.astro
            pa = _clamp((t - 0.15) / 1.1)
            xo = -(a["iw"] + 60) * (1 - _ease_out_cubic(pa))
            pos = (round(a["x"] + xo), round(a["y"] + 6 * math.sin(t * 1.55) * pa))
            if pos != a.get("pos"):                  # solo se redibuja si se movió al menos 1 píxel
                a["pos"] = pos
                c.coords(a["id"], pos[0], pos[1])

        if lento:
            # --- Estrellas que titilan
            for s in self.estrellas:
                pin = _clamp((t - 0.4 - s["ret"] * 0.4) / 1.2)
                b = pin * (0.25 + 0.75 * (0.5 + 0.5 * math.sin(t * s["vel"] + s["fase"])))
                col = _mezcla(self._fondo(s["y"]), "#FFFFFF", b * 0.9)
                if col != s["col"]:
                    s["col"] = col
                    c.itemconfigure(s["id"], fill=col)
            # --- Símbolos tecnológicos (muy tenues, flotan despacio)
            for s in self.simbolos:
                pin = _clamp((t - 1.0 - s["ret"] * 0.3) / 1.2)
                c.coords(s["id"], s["x"], s["y"] + 4 * math.sin(t * 0.8 + s["fase"]))
                if pin < 1 or self._cuadro <= 1:
                    c.itemconfigure(s["id"], fill=_mezcla(self._fondo(s["y"]), "#E9E5FF", 0.26 * pin))

        # --- Estrella fugaz ocasional, rasante por la parte alta de la pantalla
        self._fugaz(t)
        return entrando or barrido is not None or self.fugaz is not None

    def _fugaz(self, t):
        c = self.c
        inicio, periodo, dur = 4.0, 9.0, 0.9
        if self.w < 700 or t < inicio:
            return
        k = int((t - inicio) // periodo)
        tau = (t - inicio) % periodo
        if tau > dur:
            if self.fugaz:
                for it in self.fugaz:
                    c.delete(it)
                self.fugaz = None
            return
        u = tau / dur
        x0 = self.w * 0.12 + ((k * 97) % 100) / 100.0 * max(60, self.w - 180 - 320 - self.w * 0.12)
        y0 = 12 + self.oy * 0.3
        cabeza = (x0 + u * 300, y0 + u * 18)
        cola = (cabeza[0] - 62, cabeza[1] - 3.7)
        brillo = 1 - abs(2 * u - 1) ** 2
        fondo = self._fondo(cabeza[1])
        if not self.fugaz:
            self.fugaz = [c.create_line(0, 0, 0, 0, width=1), c.create_line(0, 0, 0, 0, width=2),
                          c.create_oval(0, 0, 0, 0, outline="")]
        l1, l2, pto = self.fugaz
        mid = ((cola[0] + cabeza[0]) / 2, (cola[1] + cabeza[1]) / 2)
        c.coords(l1, cola[0], cola[1], mid[0], mid[1])
        c.coords(l2, mid[0], mid[1], cabeza[0], cabeza[1])
        c.coords(pto, cabeza[0] - 2, cabeza[1] - 2, cabeza[0] + 2, cabeza[1] + 2)
        c.itemconfigure(l1, fill=_mezcla(fondo, "#FFFFFF", brillo * 0.35))
        c.itemconfigure(l2, fill=_mezcla(fondo, "#FFFFFF", brillo * 0.7))
        c.itemconfigure(pto, fill=_mezcla(fondo, "#FFFFFF", brillo))
