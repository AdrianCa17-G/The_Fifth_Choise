################################################################################
##  THE FIFTH CHOICE — Fan Visual Novel
##  Archivo: 00_definiciones.rpy   (FASE 0 — Núcleo del proyecto)
##  Motor: Ren'Py 8.5.3
##
##  Este archivo define personajes, variables globales, la pantalla de entrada
##  de nombre y documenta la lógica del Cálculo Secreto de finales.
##  No contiene narrativa: eso vive en 01_prologo.rpy en adelante.
################################################################################


################################################################################
##  1. PERSONAJES
################################################################################

## Protagonista. Sin sprite: nunca se muestra su rostro.
## El corchete [nombre_jugador] se interpola en tiempo real, así que el nombre
## cambia automáticamente en cuanto el jugador lo personaliza.
define mc = Character(
    "[nombre_jugador]",
    color="#F2F3F4",
    what_color="#EAECEE"
)

## Voz interna del protagonista (monólogo). Útil para el estilo DDLC.
define mc_pensamiento = Character(
    None,
    what_color="#AEB6BF",
    what_italic=True
)

## Narrador: sin nombre en la caja, solo texto.
define narrador = Character(
    None,
    what_color="#D5D8DC"
)

## Las quintillizas.
## `color` tiñe el nombre en la caja de diálogo.
## Si además quieres teñir el texto hablado, añade what_color a cada una.

define ichika  = Character("Ichika",  color="#FFB7C5")
define nino    = Character("Nino",    color="#C39BD3")
define miku    = Character("Miku",    color="#5DADE2")
define yotsuba = Character("Yotsuba", color="#58D68D")

define C_ITSUKI = "#EC7063"

define itsuki_inicio = Character("Estudiante Nueva", color=C_ITSUKI)
define itsuki        = Character("Itsuki",           color=C_ITSUKI)

## Habla colectiva (las cinco a la vez) y voces sin identificar.
define quintillizas = Character("Las quintillizas", color="#F4D03F")
define voz          = Character("???",              color="#95A5A6")

## NOTA DE ASSETS:
## En escenas grupales el protagonista aparece como silueta oscura.
## Cuando tengas el asset, descomenta y ajusta la ruta:
# image futaro_silueta = "images/sprites/futaro_silueta.webp"


################################################################################
##  2. VARIABLES
################################################################################

## --- Identidad del jugador ---------------------------------------------------
default nombre_jugador = "Futaro"

## --- Puntos de afinidad (INVISIBLES para el jugador) -------------------------
## Nunca se muestran en pantalla ni se comentan en el diálogo.
## Se acumulan a lo largo del Prólogo y los Capítulos 1 a 3.
default puntos_ichika  = 0
default puntos_nino    = 0
default puntos_miku    = 0
default puntos_yotsuba = 0
default puntos_itsuki  = 0

## --- Desempate ---------------------------------------------------------------
## Guarda el nombre de la primera chica con la que el jugador tuvo una decisión
## positiva. Se escribe UNA sola vez, en la primera elección con puntaje > 0.
default primera_conexion = ""
default primera_decision_hecha = False

## --- Progreso persistente (sobrevive entre partidas) -------------------------
## Se marcan True al alcanzar el final romántico correspondiente.
default persistent.ruta_ichika_completa  = False
default persistent.ruta_nino_completa    = False
default persistent.ruta_miku_completa    = False
default persistent.ruta_yotsuba_completa = False
default persistent.ruta_itsuki_completa  = False

## Se activa cuando las cinco rutas están completas.
default persistent.final_secreto_desbloqueado = False

## Opcional: registro de finales vistos, útil para una galería futura.
default persistent.final_malo_visto = False


################################################################################
##  3. LÓGICA DEL CÁLCULO SECRETO  (documentación — se implementa en FASE 5)
################################################################################
##
##  CUÁNDO SE EJECUTA
##  Al cerrar el Capítulo 3, antes del epílogo. El jugador no ve ningún número,
##  ningún menú de selección y ninguna pista explícita del sistema.
##
##  PASO 1 — UMBRAL MÍNIMO
##  mayor = max(puntos_ichika, puntos_nino, puntos_miku, puntos_yotsuba,
##              puntos_itsuki)
##  Si mayor < 10  ->  FINAL MALO (Futaro es despedido). Fin del cálculo.
##  El umbral castiga al jugador disperso: repartir atención entre las cinco
##  sin comprometerse con ninguna no debe premiarse.
##
##  PASO 2 — SELECCIÓN DE GANADORA
##  Se recorren las candidatas SIEMPRE en este orden fijo:
##      ichika -> nino -> miku -> yotsuba -> itsuki
##  Se conserva la primera que alcance el valor `mayor`.
##  Comparar con `>` (no con `>=`) garantiza que, ante empate, prevalezca la
##  primera del orden; el desempate real se resuelve en el Paso 3.
##
##  PASO 3 — DESEMPATE
##  Se construye la lista `empatadas` con todas las chicas cuyo puntaje == mayor.
##  a) Si len(empatadas) == 1        -> esa es la ganadora.
##  b) Si primera_conexion está en `empatadas` -> gana primera_conexion.
##     (La primera decisión positiva del jugador desempata: quien llegó antes
##      al corazón del protagonista.)
##  c) Si primera_conexion está vacía o no participa del empate -> se aplica la
##     prioridad canónica: Ichika > Nino > Miku > Yotsuba > Itsuki.
##
##  PASO 4 — MARCADO PERSISTENTE
##  Al entrar al final romántico X se ejecuta:
##      $ persistent.ruta_X_completa = True
##
##  PASO 5 — DESBLOQUEO DEL FINAL SECRETO
##  Tras marcar la ruta, se evalúa:
##      if (persistent.ruta_ichika_completa and persistent.ruta_nino_completa
##          and persistent.ruta_miku_completa and persistent.ruta_yotsuba_completa
##          and persistent.ruta_itsuki_completa):
##          $ persistent.final_secreto_desbloqueado = True
##  Con la bandera activa, el Final Secreto (polígamo) se ofrece DESPUÉS del
##  quinto final romántico, no antes: es una recompensa por completar el juego.
##
##  ESQUELETO DE REFERENCIA PARA FASE 5 (05_finales.rpy)
##  ------------------------------------------------------------------------
##  label calculo_secreto:
##      python:
##          candidatas = [
##              ("ichika",  puntos_ichika),
##              ("nino",    puntos_nino),
##              ("miku",    puntos_miku),
##              ("yotsuba", puntos_yotsuba),
##              ("itsuki",  puntos_itsuki),
##          ]
##          mayor = max(p for _, p in candidatas)
##          if mayor < 10:
##              ganadora = "ninguna"
##          else:
##              empatadas = [n for n, p in candidatas if p == mayor]
##              if len(empatadas) == 1:
##                  ganadora = empatadas[0]
##              elif primera_conexion in empatadas:
##                  ganadora = primera_conexion
##              else:
##                  ganadora = empatadas[0]   # ya viene en orden canónico
##      if ganadora == "ninguna":
##          jump final_malo
##      jump expression "final_" + ganadora
##  ------------------------------------------------------------------------
##
##  HELPER SUGERIDO PARA LAS DECISIONES (Capítulos 1 a 3)
##  Evita repetir la lógica de primera_conexion en cada choice:
##      $ sumar_punto("miku", 2)
##  Implementación disponible más abajo, en la sección 4.
##
################################################################################


################################################################################
##  4. FUNCIONES DE APOYO
################################################################################

init python:

    def sumar_punto(chica, cantidad=1):
        """
        Suma afinidad y registra la primera conexión del jugador.
        Uso dentro de un choice:  $ sumar_punto("nino", 2)
        """
        store_var = "puntos_" + chica
        setattr(store, store_var, getattr(store, store_var) + cantidad)

        if cantidad > 0 and not store.primera_decision_hecha:
            store.primera_conexion = chica
            store.primera_decision_hecha = True

    def rutas_completadas():
        """Cuántas rutas románticas lleva completadas el jugador (0 a 5)."""
        return sum([
            persistent.ruta_ichika_completa,
            persistent.ruta_nino_completa,
            persistent.ruta_miku_completa,
            persistent.ruta_yotsuba_completa,
            persistent.ruta_itsuki_completa,
        ])


################################################################################
##  5. PANTALLA DE ENTRADA DE NOMBRE
################################################################################

screen pantalla_nombre():

    modal True
    zorder 200

    ## Fondo sobrio. Si prefieres reutilizar el arte del menú, comenta la línea
    ## siguiente y descomenta la de Fondo_Menu.png.
    add "#0B0B10"
    # add "Fondo_Menu.png"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 780
        xpadding 60
        ypadding 50
        background Solid("#15151FE6")

        vbox:
            spacing 26
            xalign 0.5

            text "Antes de empezar…":
                size 24
                color "#8E9AAF"
                xalign 0.5

            text "¿Cuál es tu nombre?":
                size 44
                color "#FFFFFF"
                xalign 0.5

            input:
                value VariableInputValue("nombre_jugador", returnable=True)
                length 16
                allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZáéíóúÁÉÍÓÚñÑüÜ '-"
                size 38
                color "#FFB7C5"
                xalign 0.5

            text "Deja «Futaro» si prefieres vivir la historia tal como fue.":
                size 19
                color "#6C7A89"
                italic True
                xalign 0.5

            textbutton "Continuar":
                xalign 0.5
                text_size 26
                action Return(True)

    ## Enter también confirma.
    key "K_RETURN" action Return(True)


label configurar_nombre:

    call screen pantalla_nombre

    python:
        nombre_jugador = nombre_jugador.strip()
        if not nombre_jugador:
            nombre_jugador = "Futaro"

    return


################################################################################
##  6. PUNTO DE ENTRADA
################################################################################
##  IMPORTANTE: `label start` vive AQUÍ y en ningún otro archivo.
##  01_prologo.rpy debe abrir con `label prologo:` — si define su propio
##  `label start`, Ren'Py lanzará un error de etiqueta duplicada.
################################################################################

label start:

    call configurar_nombre

    jump prologo


################################################################################
##  7. PROPUESTA DE ARRANQUE DEL PRÓLOGO  (borrador para FASE 1)
################################################################################
##
##  TONO: frío, cotidiano, ligeramente amargo. Nada de romance todavía.
##  El prólogo debe vender el problema (dinero, deuda, orgullo), no a las chicas.
##
##  ESCENA 1 — Pantalla en negro, solo texto
##      El protagonista se presenta por lo que le falta, no por lo que es:
##      una deuda familiar, una beca que sostener, un padre ausente en horarios
##      imposibles. Cierra con la idea de que estudiar es lo único que controla.
##
##  ESCENA 2 — Instituto Asaba, azotea o aula vacía
##      Primer contacto hostil con una de las quintillizas (canónicamente
##      Itsuki, por el incidente del asiento y el bento). El jugador aún no sabe
##      que son cinco. Sin puntos en juego: esta escena solo instala el conflicto.
##
##  ESCENA 3 — La oferta
##      El profesor / Maruo plantea el trabajo de tutor: paga muy por encima del
##      mercado, cliente único, condición innegociable — las cinco deben
##      graduarse. Aquí aparece por primera vez la palabra «despedido», que es
##      la semilla narrativa del Final Malo.
##
##  ESCENA 4 — La revelación
##      Puerta del apartamento. Cinco rostros idénticos. Corte a negro y título.
##
##  PRIMERA DECISIÓN CON PUNTAJE:
##      Colocarla al final del Prólogo, cuando el jugador decide a quién dirigir
##      la palabra primero. Esa elección escribe `primera_conexion` y, por tanto,
##      define el criterio de desempate de toda la partida sin que él lo sepa.
##      Ejemplo:
##          menu:
##              "Hablarle a la que parece más accesible.":
##                  $ sumar_punto("yotsuba", 1)
##              "Buscar a la que ya conozco.":
##                  $ sumar_punto("itsuki", 1)
##
################################################################################
