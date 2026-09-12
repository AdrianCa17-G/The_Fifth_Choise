################################################################################
## 06_main_menu.rpy (v4)
## Menú principal - The Fifth Choice
## Cambios v4: botones con color por hermana, barra lateral, degradado y hover
################################################################################


# ==============================================================
# REGISTRO DE IMÁGENES
# ==============================================================
image main_menu_bg = "images/Fondo_Menu.png"
image main_menu_logo = "images/Logo_Menu.png"

# Sprites individuales (ponlos en game/images/sprites/)
image spr_ichika  = "images/sprites/ichika_nakano.png"
image spr_nino    = "images/sprites/nino_nakano.png"
image spr_miku    = "images/sprites/miku_nakano.png"
image spr_yotsuba = "images/sprites/yotsuba_nakano.png"
image spr_itsuki  = "images/sprites/itsuki_nakano.png"

# Pétalos de sakura (necesita images/petal.png — oval rosada pequeña ~15x10px)
image sakura_petals = SnowBlossom("images/petal.png", count=25, border=50)


# ==============================================================
# CONFIGURACIÓN Y GENERADORES DE DISPLAYABLES
# ==============================================================
init python:

    # ---------- Capa lateral (estilo Doki Doki Literature Club) ----------
    PANEL_ANCHO  = 520          # ancho total de la capa en píxeles
    PANEL_COLOR  = "#2B1B3F"    # violeta profundo, combina con el aula al atardecer
    PANEL_A_INI  = 0.88         # opacidad en el borde izquierdo (0.0 - 1.0)
    PANEL_A_FIN  = 0.00         # opacidad en el borde derecho
    PANEL_PASOS  = 48           # nº de tiras: más pasos = degradado más suave
    PANEL_ACENTO = "#FFB7C5"    # color de la línea de acento del borde

    def panel_lateral(color=None, a_ini=None, a_fin=None, ancho=None, pasos=None):
        """
        Columna vertical opaca a la izquierda que se desvanece hacia la derecha.
        Ren'Py no tiene degradados nativos: se apilan tiras de Solid con alpha
        decreciente.
        """
        color = color if color is not None else PANEL_COLOR
        a_ini = a_ini if a_ini is not None else PANEL_A_INI
        a_fin = a_fin if a_fin is not None else PANEL_A_FIN
        ancho = ancho if ancho is not None else PANEL_ANCHO
        pasos = pasos if pasos is not None else PANEL_PASOS

        alto  = config.screen_height
        base  = ancho // pasos
        resto = ancho % pasos

        args = []
        x = 0
        for i in range(pasos):
            t = i / float(pasos - 1)
            a = a_ini + (a_fin - a_ini) * t
            w = base + (1 if i < resto else 0)
            args.append((x, 0))
            args.append(Solid(color + "%02x" % int(round(a * 255)),
                            xsize=w, ysize=alto))
            x += w

        return Composite((ancho, alto), *args)


    # ---------- Colores de las quintillizas ----------
    QUINT_COLORES = {
        "ichika":  "#F2A0B8",   # rosa suave
        "nino":    "#E8637E",   # rosa intenso
        "miku":    "#6FC3D8",   # celeste
        "yotsuba": "#8CCB6E",   # verde
        "itsuki":  "#F0705A",   # coral
    }

    # ---------- Dimensiones de los botones ----------
    BOTON_ANCHO  = 400
    BOTON_ALTO   = 62
    BOTON_A_INI  = 0.42         # intensidad del degradado en hover (0.28 suave / 0.60 fuerte)
    BOTON_BARRA  = 5            # grosor de la barra lateral en hover

    def fondo_boton(color, a_ini=None, bar=None):
        """Barra sólida + degradado horizontal que se desvanece a la derecha."""
        a_ini = a_ini if a_ini is not None else BOTON_A_INI
        bar   = bar   if bar   is not None else BOTON_BARRA

        pasos  = 32
        partes = [(0, 0), Solid(color, xsize=bar, ysize=BOTON_ALTO)]
        base   = max(1, (BOTON_ANCHO - bar) // pasos)

        x = bar
        for i in range(pasos):
            t = i / float(pasos - 1)
            a = a_ini * (1.0 - t)
            partes.append((x, 0))
            partes.append(Solid(color + "%02x" % int(round(a * 255)),
                                xsize=base, ysize=BOTON_ALTO))
            x += base

        return Composite((BOTON_ANCHO, BOTON_ALTO), *partes)

    def barra_idle(color, bar=3):
        """Barra tenue en reposo, para que el ancho no salte al hacer hover."""
        return Composite((BOTON_ANCHO, BOTON_ALTO),
                        (0, 0), Solid(color + "55", xsize=bar, ysize=BOTON_ALTO))


# ==============================================================
# COMPONENTE DE BOTÓN
# ==============================================================
screen boton_menu(texto, accion, tono):
    $ c = QUINT_COLORES[tono]

    textbutton texto:
        action accion
        xysize (BOTON_ANCHO, BOTON_ALTO)
        padding (26, 12, 14, 12)
        background barra_idle(c)
        hover_background fondo_boton(c)
        text_style "tfch_button_text"
        text_hover_color c
        text_hover_outlines [(6, c + "55", 0, 0), (2, "#00000099", 0, 0)]
        at boton_slide
        # hover_sound "audio/sfx/hover.ogg"   # descomenta si tienes el sfx


# ==============================================================
# PANTALLA PRINCIPAL
# ==============================================================
screen main_menu():
    tag menu

    on "show"    action Play("music", "audio/bgm/main_theme.ogg", loop=True, fadeout=1.0)
    on "replace" action Play("music", "audio/bgm/main_theme.ogg", loop=True, fadeout=1.0)

    # --- FONDO ---
    add "main_menu_bg" fit "cover"

    # --- PÉTALOS DE SAKURA ---
    add "sakura_petals"

    # --- CAPA LATERAL DEGRADADA ---
    # Va aquí (antes de los sprites) para que las chicas queden por encima.
    # Si prefieres que la capa las tape, mueve este bloque debajo de los sprites.
    add panel_lateral() at panel_fadein

    # Línea fina de acento en el borde derecho de la capa
    add Solid(PANEL_ACENTO, xsize=2, ysize=config.screen_height):
        xpos PANEL_ANCHO
        alpha 0.30
        at panel_fadein

    # --- SPRITES individuales con entrada escalonada y flotación ---
    add "spr_ichika"  at sprite_anim(0.0, 0.0)  xalign 0.29 yalign 1.0
    add "spr_nino"    at sprite_anim(0.2, 0.4)  xalign 0.50 yalign 1.0
    add "spr_miku"    at sprite_anim(0.4, 0.8)  xalign 0.70 yalign 1.0
    add "spr_yotsuba" at sprite_anim(0.6, 1.2)  xalign 0.90 yalign 1.0
    add "spr_itsuki"  at sprite_anim(0.8, 1.6)  xalign 1.08 yalign 1.0

    # --- LOGO ---
    add "main_menu_logo":
        xalign 0.03
        yalign 0.03
        at logo_fadein

    # --- TAGLINE PRINCIPAL ---
    text "¿A quién elegirás?":
        xalign 0.65
        yalign 0.045
        color "#FFF8FC"
        size 30
        bold True
        outlines [
            (5, "#1B1026CC", 0, 0),
            (2, "#FF9FBE", 0, 0)
        ]
        at tagline_fadein

    # --- FRASE DECORATIVA ---
    text "Cinco sonrisas únicas, pero solo una será tu respuesta definitiva":
        xalign 0.69
        yalign 0.10
        color "#FFD9E6CC"
        size 20
        italic True
        outlines [(2, "#1B102688", 0, 0)]
        at tagline_fadein

    # --- PANEL DE BOTONES ---
    # La capa lateral ya hace de fondo, así que el frame va sin background.
    frame:
        xpos 90
        yalign 0.66
        xminimum 265
        background None
        padding (18, 18, 18, 18)

        vbox:
            spacing 6

            use boton_menu("Comenzar",  Start(),                 "ichika")
            use boton_menu("Cargar",    ShowMenu("load"),        "nino")
            use boton_menu("Opciones",  ShowMenu("preferences"), "miku")
            use boton_menu("Acerca de", ShowMenu("about"),       "yotsuba")
            use boton_menu("Salir",     Quit(confirm=True),      "itsuki")

    # --- VERSIÓN ---
    text "v1.0":
        xalign 0.98
        yalign 0.98
        color "#FFFFFF44"
        size 18


# ==============================================================
# TRANSFORMACIONES
# ==============================================================

# Botón: se desliza a la derecha al pasar el mouse
transform boton_slide:
    on idle:
        linear 0.18 xoffset 0
    on hover:
        linear 0.18 xoffset 14

# Capa lateral: entra deslizándose desde la izquierda
transform panel_fadein:
    alpha 0
    xoffset -60
    linear 0.9 alpha 1.0 xoffset 0

# Sprite: entrada desde abajo + flotación suave en loop (ease = sin lag)
transform sprite_anim(delay, float_offset):
    alpha 0
    yoffset 40
    pause delay
    linear 0.8 alpha 1.0 yoffset 0
    pause float_offset
    block:
        ease 2.2 yoffset -10
        ease 2.2 yoffset 0
        repeat

# Logo: fade in suave
transform logo_fadein:
    alpha 0
    pause 0.3
    linear 1.5 alpha 1.0

# Tagline: aparece después del logo
transform tagline_fadein:
    alpha 0
    pause 1.8
    linear 1.0 alpha 1.0


# ==============================================================
# ESTILO DEL TEXTO DE LOS BOTONES
# ==============================================================

style tfch_button_text:
    size              40
    color             "#F2EDF5"
    kerning           1.5
    text_align        0.0
    yalign            0.5
    insensitive_color "#FFFFFF33"
    outlines          [(2, "#00000099", 0, 0)]
    # Descomenta si añades una fuente redondeada en game/fonts/
    # font            "fonts/MPLUSRounded1c-Bold.ttf"
