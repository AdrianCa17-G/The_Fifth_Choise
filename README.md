# The Fifth Choice

Fan visual novel basada en **Quintessential Quintuplets** (Go-toubun no Hanayome).
El jugador vive los eventos canónicos del anime y sus decisiones determinan con
cuál de las cinco quintillizas termina.

**Motor:** Ren'Py 8.5.3 · **Desarrollo:** Adrian (AdrianKiller17) · **Proyecto fan sin ánimo de lucro**

---

## Estado

| Fase | Archivo | Estado |
|---|---|---|
| 0 · Núcleo | `00_definiciones.rpy` | ✅ Terminado |
| 1 · Prólogo | `01_prologo.rpy` | ✅ Terminado — 7 escenas, arte y audio completos |
| 2 · Capítulo 1 | `02_capitulo1.rpy` | ⬜ Siguiente — bloqueado por 3 decisiones de diseño |
| 3 · Capítulo 2 | `03_capitulo2.rpy` | ⬜ Pendiente |
| 4 · Capítulo 3 | `04_capitulo3.rpy` | ⬜ Pendiente |
| 5 · Finales | `05_finales.rpy` | ⬜ Pendiente |
| — · Menú principal | `06_main_menu.rpy` | ✅ Terminado |

---

## Documentación

| Documento | Qué contiene |
|---|---|
| Este README | Estructura, sistemas de juego, personajes, progreso |
| [`docs/PROLOGO.md`](docs/PROLOGO.md) | Estado detallado del prólogo: escenas, guion, assets, problemas abiertos |
| [`docs/GUIA_ARTE.md`](docs/GUIA_ARTE.md) | Generación de imágenes: PixAI, LoRAs, prompts, estándar de sprites, scripts de post |
| [`docs/GUIA_AUDIO.md`](docs/GUIA_AUDIO.md) | Fuentes, licencias, escala de volumen, montaje |
| [`docs/GUIA_RENPY.md`](docs/GUIA_RENPY.md) | Trampas del motor ya encontradas y convenciones de código |
| [`CREDITOS.md`](CREDITOS.md) | Atribuciones, licencias de los assets y aviso de proyecto fan |

Las tres guías son **transversales**: valen para los tres capítulos que quedan,
no solo para el prólogo. Consultarlas antes de generar arte nuevo o tocar audio.

---

## Estructura del proyecto

```
Quintuplets/
└── The Fifth Choice/
    ├── README.md                       ← esta página
    ├── docs/
    │   ├── PROLOGO.md
    │   ├── GUIA_ARTE.md
    │   ├── GUIA_AUDIO.md
    │   └── GUIA_RENPY.md
    ├── herramientas/                    fuera de game/ — scripts de Python
    │   ├── normalizar_sprite.py
    │   ├── normalizar_extra.py
    │   ├── limpiar_halo.py
    │   └── escalar_cgs.py
    └── game/
        ├── audio/
        │   ├── bgm/                     8 pistas .ogg
        │   ├── sfx/                     12 efectos .mp3
        │   └── amb_viento.ogg
        ├── images/
        │   ├── bg/                      8 fondos, 1920×1080 WebP
        │   ├── cg/                      13 ilustraciones de escena
        │   ├── sprites/
        │   │   ├── ichika_sprites/
        │   │   ├── nino_sprites/
        │   │   ├── miku_sprites/
        │   │   ├── yotsuba_sprites/
        │   │   ├── itsuki_sprites/
        │   │   ├── raiha_sprites/
        │   │   └── isanari_sprites/
        │   ├── Fondo_Menu.png
        │   ├── Logo_Menu.png
        │   └── petal.png
        ├── fonts/
        │   ├── NotoSansJP-Regular.ttf    solo para el japonés de los créditos
        │   └── OFL.txt                   licencia, obligatorio distribuirla
        ├── 00_definiciones.rpy          ✅
        ├── 01_prologo.rpy               ✅
        ├── 06_main_menu.rpy             ✅
        ├── gui.rpy · options.rpy · screens.rpy
        │
        │   ── todavía no creados ──
        ├── 02_capitulo1.rpy             ← siguiente
        ├── 03_capitulo2.rpy
        ├── 04_capitulo3.rpy
        ├── 05_finales.rpy
        │
        │   ── generado por Ren'Py, no versionar ──
        ├── cache/  saves/  tl/  libs/  gui/
        └── *.rpyc
```

`cache/`, `saves/`, `tl/`, `libs/` y los `.rpyc` los crea y mantiene Ren'Py sola.
No deben subirse al repositorio: el `.gitignore` de la raíz ya los excluye.


### Qué va en cada `.rpy`

`00_definiciones.rpy` concentra **todo lo que no es narrativa**: personajes,
variables, imágenes compartidas (fondos y sprites), transforms, audio, funciones
de apoyo, la pantalla de nombre y `label start`.

Los archivos de capítulo contienen **solo su `label` y sus CG propios**. Un CG es
la ilustración de un momento concreto; si alguno acaba reutilizándose en otro
capítulo, se sube a definiciones.

`label start` vive en `00_definiciones.rpy` y en ningún otro sitio.

---

## Estructura narrativa

```
PRÓLOGO → CAPÍTULO 1 → CAPÍTULO 2 → CAPÍTULO 3 → CÁLCULO SECRETO → EPÍLOGO
```

Estilo narrativo tipo *Doki Doki Literature Club*: el sistema de puntos es
invisible y el jugador no elige a nadie explícitamente.

### Protagonista

Futaro Uesugi por defecto, nombre personalizable al inicio (`nombre_jugador`).
**Nunca se muestra su rostro.** En escenas grupales aparece como silueta oscura,
y en los CG se encuadra de espaldas, desenfocado y cortado por el borde.

No es una decisión estética sino técnica: no existe LoRA de Futaro, así que
cualquier intento de generarlo de frente sale como silueta negra o con la cara
rota. Sin rostro no hay nada que el modelo pueda estropear.

---

## Las cinco quintillizas

| Personaje | Color | Personalidad |
|---|---|---|
| Ichika | `#FFB7C5` rosa | Actriz, coqueta, la primera en actuar |
| Nino | `#C39BD3` morado | Tsundere, protectora, la más intensa |
| Miku | `#5DADE2` azul | Tímida, historia, desarrollo lento |
| Yotsuba | `#58D68D` verde | Energética, noble, la más dulce |
| Itsuki | `#EC7063` rojo | Seria, estudiosa, rivalidad → amor |

Como las cinco tienen la misma cara, el jugador las distingue por silueta.
Cualquier expresión nueva tiene que leerse al 30 % de tamaño.

### Itsuki tiene dos objetos de personaje

El protagonista no sabe su nombre hasta la escena 5 del prólogo, cuando ella se
lo grita. Hasta entonces la caja de diálogo dice **«Estudiante Nueva»**
(`itsuki_inicio`); a partir de ahí, `itsuki`. El color va en la constante
`C_ITSUKI` para que los dos no puedan desincronizarse.

### Desviaciones del canon — decisiones cerradas

No son errores. Conviene tenerlas presentes al escribir diálogo para no
contradecirlas en el texto:

- **Nino lleva el pelo corto desde el inicio.** Los LoRAs disponibles solo la
  generan así. Nunca describirla con el pelo largo en narración.
- **Miku es castaña, no azul pálido.** El LoRA no da el tono azul. El color
  `#5DADE2` sigue valiendo para su caja de diálogo; lo que cambia es el pelo.

---

## Sistema de finales

Siete finales: cinco románticos, uno malo y uno secreto.

| Final | Condición |
|---|---|
| Ichika / Nino / Miku / Yotsuba / Itsuki | Más puntos con ella, mínimo 10 |
| Final Malo | Ninguna alcanza 10 puntos → Futaro es despedido |
| Final Secreto | Completar las cinco rutas románticas |

### Cálculo secreto

Los puntos son **invisibles**: no se muestran, no se comentan en diálogo y no hay
menú de selección. Se resuelven al cerrar el Capítulo 3.

- **Umbral mínimo: 10 puntos.** Castiga al jugador disperso.
- **Orden de comparación:** ichika → nino → miku → yotsuba → itsuki.
- **Desempate:** gana `primera_conexion`, la primera chica con la que el jugador
  tuvo una decisión positiva. Si está vacía o no participa del empate, se aplica
  la prioridad canónica del orden anterior.

La lógica completa, con el esqueleto de código listo para la Fase 5, está
documentada en comentarios dentro de `00_definiciones.rpy`.

### Reglas al escribir decisiones

Usar **siempre** el helper, nunca sumar a mano:

```renpy
$ sumar_punto("miku", 2)
```

Es lo único que garantiza que `primera_conexion` se escriba una sola vez y que
el desempate de toda la partida quede bien fijado.

**El prólogo no otorga puntos.** Sus tres menús son cosméticos: cambian el
diálogo inmediato y reconvergen. La primera decisión puntuada del juego está al
inicio del Capítulo 1.

---

## Herramientas

| Para qué | Herramienta |
|---|---|
| Motor | Ren'Py 8.5.3 |
| Generación de imágenes | PixAI (modelo base Tsubaki.2) |
| Corrección local de imágenes | Gemini |
| Post de sprites y CG | Scripts propios de Python (`herramientas/`) con pillow, numpy y scipy |
| Música | 魔王魂 y DOVA-SYNDROME |
| Efectos de sonido | 効果音ラボ |
| Ambiente | Springin' Sound Stock |
| Edición de audio | Audacity |
| Tipografía japonesa | Noto Sans JP (SIL OFL 1.1), solo para los créditos |
| Asistencia de código y guion | Claude |

Detalles de configuración en [`docs/GUIA_ARTE.md`](docs/GUIA_ARTE.md) y
[`docs/GUIA_AUDIO.md`](docs/GUIA_AUDIO.md).

---

## Siguiente paso — Capítulo 1

El guion está bloqueado por **tres decisiones de diseño** que hay que cerrar
antes de escribir una sola línea:

1. **Cuántas decisiones puntuadas tendrá cada capítulo y con qué valores.**
   De esto depende que el umbral de 10 sea alcanzable sin ser trivial.
2. **Cuál es la primera decisión puntuada del juego.** Escribe
   `primera_conexion` y con ella el desempate de toda la partida: es la decisión
   de diseño más pesada del capítulo.
3. **La contradicción de Maruo.** Él promete despido si una hermana reprueba;
   el Final Malo se dispara por afinidad baja. Son dos condiciones distintas y
   el juego solo ejecuta la segunda. Propuesta sobre la mesa: que la afinidad
   represente «logró llegar a ellas y por eso estudian», y narrar el Final Malo
   como el despido que Maruo anunció.

En arte, el criterio ya está fijado: **generar expresiones solo contra guion
escrito**, nunca contra suposición. `itsuki_timida` se generó antes de tener la
escena y se quedó sin usar todo el prólogo.

---

## Notas

- Proyecto fan **gratuito**. No monetizar nunca.
- Trabajar un archivo `.rpy` por sesión.
- Probar en Ren'Py después de cada fase antes de continuar.
- Ante un error, copiar el `traceback` completo.
- **Guardar la semilla** de cada fondo, CG y sprite que funcione. Es lo único
  del trabajo de arte que no se puede recuperar después.
