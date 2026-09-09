# The Fifth Choice — Estado del proyecto

Documento de contexto para retomar el desarrollo en una conversación nueva.
Última actualización: sesión de desarrollo de Fase 0, Fase 1 y primeros assets.

---

## 1. Qué es

Fan visual novel basada en **Quintessential Quintuplets** (Go-toubun no Hanayome).
Motor: **Ren'Py 8.5.3**. Desarrollador: Adrian.

Concepto: el jugador vive los eventos canónicos del anime y sus decisiones
determinan con cuál de las cinco quintillizas termina. Estructura narrativa al
estilo *Doki Doki Literature Club*.

```
PRÓLOGO → CAPÍTULO 1 → CAPÍTULO 2 → CAPÍTULO 3 → CÁLCULO SECRETO → EPÍLOGO
```

El protagonista (Futaro Uesugi por defecto, nombre personalizable) **nunca
muestra el rostro**. En escenas grupales aparece como silueta oscura.

---

## 2. Estado de los archivos

| Archivo | Estado |
|---|---|
| `00_definiciones.rpy` | ✅ Terminado |
| `01_prologo.rpy` | ⬜ Pendiente - (7 escenas — 5/7 terminadas) |
| `02_capitulo1.rpy` | ⬜ Pendiente — siguiente tarea |
| `03_capitulo2.rpy` | ⬜ Pendiente |
| `04_capitulo3.rpy` | ⬜ Pendiente |
| `05_finales.rpy` | ⬜ Pendiente |
| `06_main_menu.rpy` | ✅ Ya existía |
| `script.rpy` | ❌ **Eliminado** (y su `.rpyc`) |

---

## 3. Fase 0 — `00_definiciones.rpy`

Contiene:

- **Personajes**: `mc` (protagonista dinámico), `mc_pensamiento` (monólogo
  interno en cursiva), `narrador` (sin nombre), y las cinco quintillizas con
  sus colores. También `quintillizas` (habla colectiva) y `voz` (sin identificar).
- **Variables**: `nombre_jugador`, los cinco `puntos_*`, `primera_conexion`,
  `primera_decision_hecha`, y las persistentes `persistent.ruta_*_completa` y
  `persistent.final_secreto_desbloqueado`.
- **Lógica del cálculo secreto** documentada en comentarios, con esqueleto de
  código listo para pegar en la Fase 5.
- **Helper `sumar_punto(chica, cantidad)`**: suma afinidad y registra
  automáticamente `primera_conexion` la primera vez. Úsalo siempre en los
  `menu` en lugar de sumar a mano — evita bugs de desempate.
- **Helper `rutas_completadas()`**: devuelve cuántas rutas lleva el jugador.
- **`screen pantalla_nombre`** + `label configurar_nombre`.
- **`label start`** — vive aquí y en ningún otro archivo. Llama a
  `configurar_nombre` y salta a `prologo`.

### Colores de los personajes

| Personaje | Color | Personalidad |
|---|---|---|
| Ichika | `#FFB7C5` | Actriz, coqueta |
| Nino | `#C39BD3` | Tsundere, protectora |
| Miku | `#5DADE2` | Tímida, historia |
| Yotsuba | `#58D68D` | Energética, noble |
| Itsuki | `#EC7063` | Seria, estudiosa |
| Narrador | `#D5D8DC` | — |

---

## 4. Sistema de finales

7 finales: 5 románticos, 1 malo, 1 secreto.

- **Umbral mínimo: 10 puntos.** Si ninguna chica llega, Final Malo (Futaro es
  despedido).
- **Orden de comparación**: ichika → nino → miku → yotsuba → itsuki.
- **Desempate**: gana `primera_conexion`; si está vacía o no participa del
  empate, prioridad canónica Ichika > Nino > Miku > Yotsuba > Itsuki.
- **Final secreto**: se desbloquea al completar las cinco rutas románticas.

### Calibración pendiente de decidir

Propuesta sobre la mesa, aún no confirmada: 3 decisiones puntuadas en el
prólogo (descartado, ver abajo) y 4 por capítulo, con valores de 1 a 3 puntos.
**Hay que fijar cuántas decisiones puntuadas tendrá cada capítulo antes de
escribir el Capítulo 1**, porque de eso depende que el umbral de 10 sea justo.

---

## 5. Fase 1 — `01_prologo.rpy`

**Decisión tomada: el prólogo NO otorga puntos.** Ninguna variable `puntos_*`
ni `primera_conexion` se toca. Los tres menús que hay son cosméticos: solo
cambian el diálogo inmediato y reconvergen.

Esto significa que **la primera decisión puntuada del juego está al inicio del
Capítulo 1**, y es la que escribirá `primera_conexion` y, por tanto, el
criterio de desempate de toda la partida.

### Estructura del prólogo (7 escenas)

1. **Casa de los Uesugi** — presentación de Futaro por lo que le falta.   ✅ Terminado
   Deuda familiar, notas como única cosa que controla. Aparece Raiha.
2. **La oferta** — Isanari propone el trabajo de tutor. Primer menú cosmético.  ✅ Terminado
3. **Instituto Asaba** — profesor felicita por el examen; primer roce con  ✅ Terminado
   Itsuki (asiento y bento); azotea. Segundo menú cosmético.
4. **Camino al departamento** — Futaro calcula mal las premisas.  ✅ Terminado
5. **La revelación** — conoce a las cinco. Orden: Ichika, Nino, Miku,  ✅ Terminado
   Yotsuba, e Itsuki de última (cambio deliberado respecto al anime, para que
   el prólogo cierre con golpe en vez de con enumeración).
6. **El contrato** — Maruo. Aparece por primera vez la palabra «despedido»,
   semilla narrativa del Final Malo.
7. **El primer intento** — clase fallida. Cada hermana se escapa a su manera.
   Tercer menú cosmético. Cierra en fracaso, no en victoria.

Termina con `jump cap1_inicio`.

### Anzuelos sembrados para recoger después

- **Miku**: Futaro alcanza a leer el lomo de un libro sobre el período Sengoku.
  Gancho listo para su ruta en el Capítulo 1.
- **Itsuki**: el reencuentro en el departamento ya establece la rivalidad.

### Personajes secundarios definidos en este archivo

`isanari`, `raiha`, `maruo`, `profe`. Si prefieres centralizarlos, muévelos a
`00_definiciones.rpy`.

---

## 6. Assets creados

Todos en 1920×1080, WebP salvo indicación.

### Fondos (`game/images/bg/`)

| Archivo | Uso |
|---|---|
| `bg_escritorio.webp` | Cuarto de Futaro con el resultado `1位` marcado en rojo sobre la hoja |
| `bg_cuarto_futaro.webp` | El mismo cuarto sin la marca |
| `bg_comedor.webp` | Cocina-comedor japonesa, escena de la cena |
| `bg_foto_familiar_marco.png` | Retrato familiar enmarcado (ver abajo) |

Los demás fondos del prólogo siguen siendo **placeholders `Solid()`** de
colores planos definidos al inicio de `01_prologo.rpy`: `bg_casa`,
`bg_instituto`, `bg_aula`, `bg_azotea`, `bg_calle`, `bg_calle_noche`,
`bg_departamento`, `bg_negro`. Sustituir línea a línea según se generen.

### El retrato familiar

Composición hecha a partir de cuatro fuentes distintas (Isanari, la madre,
Futaro y Raiha), igualando el tamaño de las cabezas y unificando el color.
**La madre está en escala de grises** porque falleció; eso resuelve la
inconsistencia temporal (cuando murió, Futaro era niño y Raiha un bebé, y no
existen fotos de esa época). Va enmarcado y colgado en una pared en penumbra.

### Sprites (`game/images/sprites/`)

| Archivo | Notas |
|---|---|
| `raiha_hablando.png` | 650×951 |
| `raiha_regano.png` | 650×992 |
| `isanari_neutral.png` | 850x1169 |
| `isanari_sonriendo.png` | 880x1112 |

---

### Nombres de imagen: con espacio, no con guion bajo

```renpy
image raiha hablando    = "sprites/raiha_hablando.webp"
image raiha sorprendida = "sprites/raiha_sorprendida.webp"
```

Así Ren'Py trata `raiha` como etiqueta y el resto como atributo, y
`show raiha sorprendida` **sustituye** el sprite en lugar de apilar dos.

### Transiciones

`with dissolve` **solo en la primera aparición**. En los cambios de expresión
posteriores, `show` pelado — si no, hace un fundido cruzado entre las dos caras
y parece que parpadea.

---

## 8. Plan de sprites del prólogo

Un solo atuendo para las cinco: **uniforme escolar**, también en el
departamento. Ahorra un set entero de cuerpos y nadie lo cuestiona.

| Personaje | Caras necesarias |
|---|---|
| Itsuki | 4 — seria, molesta, sorprendida, casi-sonrisa |
| Ichika | 3 — sonrisa, neutral, ojos cerrados |
| Nino | 2 — molesta, neutral |
| Yotsuba | 2 — sonrisa amplia, sorprendida |
| Miku | 2 — mirada baja, levantando la vista |
| Raiha | 2 —  sonriendo, un poco molesta | ✅ Terminado
| Isanari | 2 — sonrisa socarrona, neutral | ✅ Terminado
| Maruo | 1 — severo (no sonríe nunca) |
| Profesor / madre | 0 — no necesitan sprite | ✅ Terminado

**Total: 18 caras y 8 cuerpos.**

La «casi-sonrisa» de Itsuki es específica del prólogo y la más importante: sin
ella se cae el momento de la azotea.

Como las cinco tienen la misma cara, el jugador las distingue por silueta.
Comprobar que peinado y accesorio se leen al 30% de tamaño.

---

## 9. Generación de imágenes — configuración que funciona

**Plataforma: PixAI.** Cuenta gratuita, 10.000 créditos diarios que no caducan.

- **Modelo base: Tsubaki.2**
- **LoRA: `(Tsubaki.2) go-toubun no hanayome`, fuerza ~0.65**
- El LoRA debe coincidir con el modelo base o no hace nada y gasta créditos en
  silencio. Es el fallo más caro de la plataforma.
- No apilar LoRAs. El de Gotoubun solo basta para fondos.
- Generar a **1344×768** y ampliar después. Generar directo a 1920 produce
  composiciones duplicadas.

### Plantilla de prompt para fondos

```
masterpiece, best quality, absurdres, scenery, indoors, no humans,
[DESCRIPCIÓN DE LA ESCENA],
soft lighting, bright colors, pastel colors, soft shading,
detailed background, anime background art, wide shot
```

Negativo:

```
1girl, 1boy, person, face, hands, text, english text, watermark,
signature, thick outlines, dark, gloomy, desaturated, realistic,
blurry, lowres, jpeg artifacts
```

El `no humans` positivo + `1girl, 1boy, person` negativo es lo que evita que
meta un personaje en el fondo.

Para el cuarto de Futaro añadir: `sparse room, bare walls, worn furniture,
old books, shabby, few belongings`. Los generadores tienden a hacer
habitaciones demasiado acogedoras, y la casa es de una familia que cuenta el
dinero.

**Guardar la semilla** de cada fondo que funcione. Es lo que hace que doce
fondos parezcan del mismo juego.

### Lo que no funciona

Quitar personajes de fotogramas del anime por clonado o inpainting clásico.
Se intentó con un fotograma del comedor y falla: detrás de los personajes hay
ollas, muebles, patas de mesa y sombras que no son repetitivas, y no hay
franjas limpias de las que copiar. Para eso hace falta inpainting generativo
(la herramienta de edición de PixAI) o generar el fondo desde cero.

---

## 10. Trampas de Ren'Py ya encontradas

- **`label start` duplicado.** Vive solo en `00_definiciones.rpy`. Los demás
  archivos usan `label prologo`, `label cap1_inicio`, etc.
- **Borrar el `.rpyc` junto al `.rpy`.** Si eliminas un archivo y dejas su
  compilado, Ren'Py lo sigue cargando y el error reaparece idéntico. Es la
  causa número uno de «lo borré y sigue fallando».
- **Imágenes en `game/images/bg/`** con ruta explícita: `"bg/archivo.webp"`.
- **Nombres de archivo** sin espacios, sin tildes, en minúsculas. Ren'Py
  distingue mayúsculas en Linux y Android; funciona en Windows y revienta al
  exportar.
- **Las pantallas se dibujan por encima de los sprites**, así que la caja de
  diálogo nunca queda tapada por un personaje.

---

## 11. Problemas conocidos

- **Cambio de ropa de Raiha.** El sprite `hablando` lleva camiseta de rayas y
  el `sorprendida` jersey de cuello alto: vienen de escenas distintas del
  anime. En la escena de la cena van seguidos en la misma conversación, que es
  el peor caso. Opciones: buscar la expresión en una escena con la ropa
  correcta, o asumirlo.
- **Coleta cortada** en `raiha_sorprendida`: ya salía fuera de cuadro en el
  fotograma original, no hay nada que recuperar.
- **La madre en el retrato familiar** viene de una foto de artbook de 340 px de
  ancho, ampliada. Como sprite en escena funciona; en primer plano se notaría.
- **Composición del comedor**: la mesa está centrada y adelantada. Los sprites
  hay que colocarlos a los lados (`xalign 0.2` / `0.8`) o quedan plantados
  encima del mueble.

---

## 12. Siguiente paso

Escribir **`02_capitulo1.rpy`**. Antes de empezar hay que decidir:

1. Cuántas decisiones puntuadas tendrá el capítulo y con qué valores, para
   calibrar el umbral de 10.
2. Cuál es la primera decisión puntuada del juego — la que escribirá
   `primera_conexion` y definirá el desempate de toda la partida.

Recordar usar siempre `$ sumar_punto("chica", n)` dentro de los `menu`.
