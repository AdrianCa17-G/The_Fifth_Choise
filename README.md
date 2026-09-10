# The Fifth Choice — Estado del proyecto

Documento de contexto para retomar el desarrollo en una conversación nueva.
Última actualización: Fase 0, Fase 1 y consolidación del pipeline de arte
(pesos de LoRA, estándar de sprites por IPD y corrección local en Gemini).

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
| `01_prologo.rpy` | ✅ Terminado (7 escenas) |
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

### Desviaciones del canon ya asumidas

Son decisiones cerradas, no errores. Conviene tenerlas presentes al escribir
diálogo para no contradecirlas en el texto:

- **Nino lleva el pelo corto desde el inicio.** Los LoRAs disponibles solo la
  generan así; se asume la inconsistencia con el anime en vez de pelear con la
  herramienta. Nunca describirla con el pelo largo en narración.
- **Miku es castaña, no azul pálido.** El LoRA no da el tono azul y no se
  corrige por prompt. El color `#5DADE2` sigue valiendo para su caja de
  diálogo; lo que cambia es el pelo en pantalla.

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

1. **Casa de los Uesugi** — presentación de Futaro por lo que le falta.   
   Deuda familiar, notas como única cosa que controla. Aparece Raiha. ✅ Terminado.
2. **La oferta** — Isanari propone el trabajo de tutor. Primer menú cosmético.  ✅ Terminado.
3. **Instituto Asaba** — profesor felicita por el examen; primer roce con 
   Itsuki (asiento y bento); azotea. Segundo menú cosmético.  ✅ Terminado.
4. **Camino al departamento** — Futaro calcula mal las premisas.  ✅ Terminado.
5. **La revelación** — conoce a las cinco. Orden: Ichika, Nino, Miku,  
   Yotsuba, e Itsuki de última (cambio deliberado respecto al anime, para que
   el prólogo cierre con golpe en vez de con enumeración). ✅ Terminado.
6. **El contrato** — Maruo. Aparece por primera vez la palabra «despedido», 
   semilla narrativa del Final Malo. ✅ Terminado.
7. **El primer intento** — clase fallida. Cada hermana se escapa a su manera. 
   Tercer menú cosmético. Cierra en fracaso, no en victoria. ✅ Terminado.

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
| bg_cuarto_mc | Cuarto de mc, aqui es donde va a terminar el dia |     
| bg_comedor | Cocina-comedor japonesa, donde hay reuniones familiares del mc |   
| bg_instituto | Donde estudia mc |   
| bg_aula | Aula donde esta mc con las quintillizas |         
| bg_azotea | Lugar donde itsuki y mc vuelven a discutir |       
| bg_edificio | Edificio de las quintillizas |     
| bg_entrada_edificio | Puerta a la entrada de la casa de las quintillizas |        
| bg_departamento | Casa por dentro de las quintillizas |

Todos estos bg ya son definitivos y son utilizados en el prologo, 
no solo serán usados ahi, sino en todo el desarrollo del juego.

### CGs o Artes de escena (`game/images/cg/`)

| Archivo | Uso | En que escena |
|---|---|---|
| cg_familia | Retrato familiar, primer vistazo de todo el juego, donde empieza todo, mas detalles abajo | Escena 1 |     
| cg_calificacion | Es bg_cuarto_mc, lo mismo, solo que hay un examen con una nota para que de sentido al dialogo de mc al inicio del prologo | Escena 1 |  
| cg_examen   | Dialogo entre mc y su docente, resaltando su inteligencia | Escena 3 |   
| cg_itsuki_sentada  | Primer encuentro entre mc e Itsuki, aqui se desarrolla su dinámica | Escena 3 |         
| cg_itsuki_azotea | Segundo encuentro entre mc e Itsuki, un espacio de dialogo profundo entre ellos | Escena 3 |     
| cg_manija_edificio | mc abriendo la puerta del departamento de las quintillizas | Escena 4 |    
| cg_ichika_puerta | Primer encuentro entre mc e Ichika | Escena 5 |          
| cg_nino_pasillo  | Primer encuentro entre mc y Nino | Escena 5 |  
| cg_miku_sofa | Primer encuentro entre mc y Miku | Escena 5 |  
| cg_yotsuba_corriendo | Primer encuentro entre mc y Yotsuba | Escena 5 |  
| cg_itsuki_discusion  | Tercer encuentro entre Itsuki y mc, aunque aqui ya se intentan conocer mejor | Escena 5 |  
| cg_maruo_umbral | Padre de las quintillizas, establece las condiciones del trabajo con mc | Escena 6 |  
| cg_estudio_mesa | Primera dinamica entre mc y las quintillizas, su sesión de estudio resulta un fracaso total | Escena 7 |  

**Nomenclatura.** Los dos últimos se llamaban antes `cg_maruo_reunion` y
`cg_hermanas_estudiando`; los nombres reales en disco son los de la tabla.
El CG de la puerta tiene dos versiones (`ichika_puerta` y `ichika_puerta_v2`);
hay que fijar cuál se usa y borrar la otra antes de que el guion las mezcle.

**Ficha técnica de los dos CG más recientes:**

- `cg_maruo_umbral` — Maruo de frente, primer plano, contrapicado leve, fondo
  con lámpara, ladrillo y escalera. Fuente PNG de PixAI, sin realce de nitidez.
- `cg_estudio_mesa` — las cinco en fila detrás de la mesa baja durante la
  prueba de diagnóstico: Ichika dormida, Miku girada con audífonos, Yotsuba
  escribiendo, Itsuki concentrada en la hoja, Nino de brazos cruzados mirando a
  cámara. Generado en PixAI y corregido en Gemini (blazer de Nino, peinado de
  Ichika, tono de pelo de Miku). Fuente JPEG, con realce de nitidez.

**Pendientes de esta tabla:** faltan por generar los CG de Yotsuba e Itsuki de
la escena de la presentación (`cg_yotsuba_corriendo` y `cg_itsuki_discusion`).
Opcional: `cg_maruo_espaldas` para el cierre de la escena 6 («se dio la vuelta
y se fue»); el prompt de Maruo ya está validado y solo cambian los bloques de
encuadre y pose, y además es la opción segura porque sin rostro visible el LoRA
no puede feminizarlo.

### El retrato familiar

Composición hecha a partir de cuatro fuentes distintas (Isanari, la madre,
Futaro y Raiha), igualando el tamaño de las cabezas y unificando el color.
**La madre está en escala de grises** porque falleció; eso resuelve la
inconsistencia temporal (cuando murió, Futaro era niño y Raiha un bebé, y no
existen fotos de esa época). Va enmarcado y colgado en una pared en penumbra.
Es el unico asset en formato png no webp, estoy pensando si modificar 
nuevamente la imagen o dejarla tal como está.

### Observación sobre los CGs

Hay algunos CGs que creo que solo serán uso único para el prologo, y otras
que observo se pueden reutilizar para el desarrollo de toda la historia y
el juego, pero debemos observar cuales serían útiles.

### Sprites (`game/images/sprites/`)

Son los únicos sprites usados hasta ahora en el prólogo, obviamente como es
corto no se usaron tantos sprites de cada persona, aquì mas me enfoqué en
pulir con todo esfuerzo los sprites de las quintillizas, los sprites de 
raiha e Isanari aún debo modifcarlos ya que no están como quería.

Un solo atuendo por hermana: el **uniforme escolar**, también dentro del
departamento. Ahorra un set entero de cuerpos y nadie lo cuestiona. Lo que sí
hay que corregir de la versión anterior de este documento: **el uniforme no es
igual entre las cinco**. Lo único común es la falda verde plisada, y esa
diferencia es justo lo que las hace distinguibles en pantalla.

#### Referencia de vestuario y pelo (obligatoria para cualquier arte nueva)

| Hermana | Pelo | Vestuario |
|---|---|---|
| Ichika | Corto rosa pálido, flequillo en mechones separados de largo desigual con las puntas hacia dentro, silueta redondeada que se ahueca a los lados de la cara. Sin lazos. | Blazer azul marino con ribete blanco, camisa blanca, suéter amarillo atado a la cintura. |
| Nino | Corto, rosa más oscuro y apagado, lazos negros con verde a ambos lados de la cabeza. | Blazer azul marino con ribete blanco, camisa blanca abotonada, calcetas blancas altas. |
| Miku | Castaño, media melena. | Sudadera azul claro con capucha y cremallera, audífonos azules, medias oscuras. Sin blazer. |
| Yotsuba | Corto naranja, cinta verde en la cabeza. | Chaleco amarillo, camisa blanca de manga corta, lazo verde a cuadros. |
| Itsuki | Rojo intenso, muy largo (por debajo de la cintura), pasadores de estrella amarilla, un ahoge. | Chaleco rojo, camisa blanca de manga corta. Sin blazer. |

Al final me decidi por un formato png de los sprites en tamaño
760 x 930 en todos, para mantener balanceados, debo verificar si ese 
tamaño iría para los sprites de Raiha e Isanari.

| Personaje | Expresion | Archivo | Estado | Tamaño |
|---|---|---|---|---|
| Raiha | Sonriendo | `raiha_hablando.png` | Modificar | Pendiente |
| Raiha | Un poco molesta | `raiha_regano.png` | Modificar | Pendiente |
| Isanari | Sonrisa leve | `isanari_sonrisa.png` | Modificar | Pendiente |
| Isanari | Neutral | `isanari_neutral.png` | Modificar | Pendiente |
| Itsuki | Brazos cruzados (se usa como «seria») | `itsuki_neutral.png` |  ✅ Terminado | 760 x 930 px |
| Itsuki | Neutral real | `itsuki_neutral2.png` |  ✅ Terminado | 760 x 930 px |
| Itsuki | Sonriendo | `itsuki_sonrisa.png` |  ✅ Terminado | 760 x 930 px |
| Itsuki | Sorpresa | `itsuki_sorpresa.png` |  ✅ Terminado | 760 x 930 px |
| Itsuki | Timida | `itsuki_timida.png` |  ⚠️ Revisar | 760 x 930 px (24 px corta) |
| Yotsuba | Sonriendo | `yotsuba_sonrisa.png` |  ✅ Terminado | 760 x 930 px |
| Miku | Aburrida | `miku_aburrida.png` |  ✅ Terminado | 760 x 930 px |
| Nino | Neutral | `nino_neutral.png` |  ✅ Terminado | 760 x 930 px |
| Ichika | Neutral | `ichika_neutral.png` |  ✅ Terminado | 760 x 930 px |
| Ichika | Sonriendo | `Ichika_sonrisa.png` |  ✅ Terminado | 760 x 930 px |
| Profesor / Madre / Maruo | 0 — no necesitan sprite | | ✅ Terminado | |

Los sprites que dicen neutral son los sprites base de cada quintilliza, 
algunas no tienen porque solo aparecieron poco tiempo en pantalla o sus
dialogos no encajarian con sus poses neutrales, ademas itsuki tiene un 
sprite que aun no se ha utilizado "Itsuki Timida", debido al prologo, no
se encontró un momento exacto donde utilizarlo.

Como las cinco tienen la misma cara, el jugador las distingue por silueta.
Comprobar que peinado y accesorio se leen al 30% de tamaño.

#### Estándar del set — ya cerrado, no cambiar

Toda expresión nueva tiene que salir con estas cuatro constantes o rompe la
continuidad del elenco:

- Lienzo **760 × 930 px**, PNG RGBA con transparencia real.
- Línea de ojos en la fila **y = 199**.
- Distancia interpupilar (IPD) ya escalada: **77,2 px**.
- Eje horizontal: **el centro de la falda** (eje del cuerpo), no el centro del
  bounding box, porque los brazos y el pelo suelto lo desplazan.

La normalización se hace por **distancia interpupilar**, que es lo único que no
depende del peinado, la pose ni los accesorios. Normalizar por altura de lienzo
o por bounding box fue el error original: las cinco medían 630×930 pero cada
una estaba a una escala distinta por dentro y en pantalla no parecían
quintillizas. Escalas aplicadas a partir del IPD crudo medido:

| Render | IPD crudo | Escala |
|---|---|---|
| `nino_neutral` (referencia del set) | 74,2 | 1,040 |
| `miku_aburrida` | 73,9 | 1,045 |
| `yotsuba_sonrisa` | 70,6 | 1,093 |
| `ichika` (ambas) | 68,1 | 1,133 |
| `itsuki` (brazos cruzados) | 60,8 | 1,270 |

El margen superior de 199 px lo fija el lazo de Yotsuba, el accesorio más alto
del elenco. El corte inferior lo fija Itsuki: su render vino apaisado en
1280×720 y el marco la corta a media pierna, así que **todo el set quedó
cortado ahí**. Si se regenera a Itsuki en vertical con las rodillas visibles se
puede rehacer el set completo y recuperar el corte bajo la rodilla.

**Recorte de fondo.** El blanco de PixAI se quita por flood fill desde el
borde, pero además hay que eliminar los huecos de fondo *encerrados* entre
mechones de pelo: quedan opacos y aparecen como manchas blancas sobre el fondo
del juego. Se distinguen de la ropa blanca por pureza — el fondo es blanco puro
(≥ 254 en los tres canales) y la camisa siempre trae algo de sombra. Los
recortadores automáticos de terceros no hacen esto: dejan los parches y encima
motas oscuras en el contorno del pelo.

#### Herramienta: `normalizar_sprite.py`

Vive **fuera de `game/`**, en una carpeta `herramientas`; no es un script de
Ren'Py. Requiere Python de python.org con `pillow`, `numpy` y `scipy`.

```
python normalizar_sprite.py entrada.png salida.png
```

Quita el fondo, detecta el iris azul, mide el IPD y deja el sprite con las
constantes de arriba. Si la imagen ya viene recortada, la aplana sobre blanco,
la vuelve a recortar bien y limpia motas sueltas. Con los ojos cerrados la
detección falla: hay que pasar `--ojos x1,y1,x2,y2` copiando las coordenadas de
las pupilas de otra versión del mismo render. Las tres constantes están al
inicio del archivo y no se tocan.

*Nota para un posible sprite de Maruo:* la detección busca **azul** y él tiene
los ojos negros, así que habría que pasarle `--ojos` a mano. A cambio,
normalizarlo por IPD lo dejaría automáticamente más alto que las hermanas (un
adulto tiene menos cabeza en proporción al cuerpo), que es justo lo que
conviene para la escena del contrato.

---

### Transiciones

`pj(x)` . Coloca el sprite anclado al borde inferior en la posición horizontal
que se le pase; sin argumento cae en el centro (`x=0.5`). Como las cinco
comparten lienzo y anclaje, **un solo transform sirve para todas**, sin zoom ni
offset por personaje:

```renpy
transform pj(x=0.5):
    xanchor 0.5
    yanchor 1.0
    xpos x
    ypos 1.0
```

Valores que reparten bien a las cinco en la escena de presentación:

```renpy
show ichika neutral at pj(0.13)
show nino neutral at pj(0.31)
show miku aburrida at pj(0.5)
show yotsuba sonrisa at pj(0.69)
show itsuki seria at pj(0.87)
```

`pj_mueve` . Hace que el sprite del personaje se mueva con una transicion
desde una coordenada hasta otra coordenada, generalmente en x, en un
determinado tiempo, estas coordenas las coloca el jugador.

`habla` . Hace que el sprite del personaje se agrande un poco su zoom,
haciendo alusion a que esta hablando.

`calla` . Hace que el sprite del personaje se tiña de una sombra negra y baje
un poco su zoom, haciendo alusion a que no esta hablando.

`with dissolve`. Crea una transicion suave para cambio de escenas, ya sea
en BGs o en CGs.

` Definir dissolve`. Dura 1.2 segundos
define disolucion_lenta = Dissolve(1.2).

`with fade`. Realiza un fundido en tres pasos secuenciales, ya sea
en BGs o en CGs.

OJO. Aqui hay que analizar en donde usar dissolve y en donde fade, ya que las
puse al azar, segun yo están todas bien pero no se si están con el uso adecuado.

---

## 9. Generación de imágenes — configuración que funciona

**Plataformas: PixAI** para generar y **Gemini** para composiciones y
correcciones locales sobre imágenes ya generadas. PixAI en cuenta gratuita,
10.000 créditos diarios que no caducan.

- **Modelo base: Tsubaki.2**
- El LoRA debe coincidir con el modelo base o no hace nada y gasta créditos en
  silencio. Es el fallo más caro de la plataforma.
- **La cuenta gratuita de PixAI no tiene campo de prompt negativo separado.**
  Todo va en un solo campo, así que lo que se quiere evitar hay que expresarlo
  en positivo. Esto invalida el bloque «negativo» que traía la versión anterior
  de este documento.

### Pesos de LoRA — ya calibrados

| Caso | LoRA de serie | LoRA de personaje |
|---|---|---|
| Personaje individual (sprite o CG) | 0.3 | 0.7 – 0.8 |
| CG de grupo con las cinco | 0.3 | Ninguno |
| Maruo u otro adulto masculino | 0.1 | Ninguno |

- **0.3 es el techo del LoRA de serie**, no ~0.65 como decía la versión
  anterior. Por encima aparece un artefacto constante: una **banda blanca sobre
  el fleco**. A 0.3 desaparece; si reaparece, bajar a 0.2.
- **Sí se apilan LoRAs** (serie + personaje) para figuras individuales. Lo que
  no se puede es aplicar LoRAs individuales **por región**: en un CG de grupo
  contaminan a las cinco, así que en grupo se va solo con el de serie y se
  describe a cada hermana **por rasgos, no por nombre**.
- Con Maruo, el LoRA de serie a 0.2–0.3 le feminiza y envejece el rostro, le da
  volumen al pelo y le contagia ojos azules. A 0.1 se comporta.

### Resoluciones y postproducción

- **CG y fondos:** generar a **1280×720** (o lo que devuelva la herramienta) y
  escalar a 1920×1080 con Lanczos. Generar directo a 1920 produce composiciones
  duplicadas. Si la fuente es JPEG, aplicar realce de nitidez **con umbral** —
  el umbral evita amplificar los bloques de compresión en las zonas planas.
  Guardar en WebP calidad 95.
- **Sprites:** generar **siempre en vertical, 768×1280**, nunca apaisado. Un
  render apaisado corta las piernas demasiado arriba y arrastra a todo el
  elenco. Encuadre de cuerpo entero que llegue al menos por debajo de la
  rodilla, fondo blanco liso, sin sombra proyectada en el suelo. Los sprites
  **no** pasan por el flujo de escalado de arriba: van por
  `normalizar_sprite.py`.

### Fórmula de prompt que funciona (bloques en este orden)

1. `single seamless illustration, one continuous frame, widescreen visual novel CG, masterpiece, best quality, official anime screencap, go-toubun no hanayome style`
2. **Encuadre** — hay que forzarlo con tokens redundantes; el modelo tiende al
   plano medio centrado y a la figura de pie.
3. **Personaje** — `1girl, solo, only one person in the entire image` + nombre +
   rasgos + expresión.
4. **Pose y vestuario.**
5. **Background** — copiar literal entre CG para mantener la continuidad del
   departamento.
6. **Iluminación** + `deep focus, entire scene in sharp detail, clean lineart, natural hands with five fingers`.

### Reglas de prompting aprendidas

- **Nunca escribir «without X» ni «no X»**: el modelo ignora la negación
  gramatical y genera X.
- **Excepción:** las etiquetas tipo danbooru sí funcionan aunque suenen a
  negación (`no humans`, `plain hair with no ribbons`). Son etiquetas
  entrenadas, no negaciones. La regla sigue valiendo para todo lo demás.
- Los descriptores difíciles (largo de pelo, estar sentada, expresión no
  sonriente) necesitan **2–3 tokens redundantes distintos**.
- Para expresiones serias funcionan mejor los conceptos en positivo
  (`calm neutral`, `subdued`, `closed mouth`) que las negaciones.
- Generar tandas de prueba con **steps bajos** antes de gastar créditos.

### Estilo visual del set de CG

Todos los CG comparten este lenguaje. Cualquier CG nuevo debe cumplirlo o
desentona:

- **Plano cerrado y cámara con ángulo.** Nada de plano medio centrado y
  frontal: picado, contrapicado o dutch angle según la escena, con la figura
  ocupando casi todo el alto del frame.
- **El fondo se sugiere, no se describe entero.** Dos o tres elementos
  reconocibles (ladrillo, escalera, acuario, lámpara) y el resto recortado o
  desenfocado. Describir la sala completa produce una ilustración de catálogo
  de muebles.
- **Luz dorada muy saturada** en todos. Es lo que da unidad al set; un CG en
  tonos fríos canta aunque el encuadre sea perfecto.
- **Bandas de brillo horizontales muy marcadas en el pelo.** Lo trae el LoRA de
  serie y es parte de la firma visual del set: no hay que corregirlo.
- **Excepción:** los CG de grupo van en **plano frontal, las cinco en fila a la
  misma profundidad**. Es la disposición que mejor tolera el modelo, porque
  cada cara ocupa su propio espacio horizontal y no compiten. Las
  composiciones a distintas profundidades son más cinematográficas y mucho más
  frágiles.

### CG de grupo — separar a las cinco

Ichika, Nino e Itsuki están las tres en la gama rosa-roja y el modelo las
promedia. Se separan así:

- **Ichika:** `short light pink hair, pastel pink hair, soft baby pink hair, plain hair with no ribbons`
- **Nino:** `short reddish pink hair, darker rose pink hair, large black and green ribbons tied on both sides of her head, twin ribbons, prominent hair ribbons`
- **Itsuki:** `very long bright red hair, deep crimson red hair, vivid red hair reaching past her waist, long flowing hair, waist length hair`

Ojo: `one strand of hair sticking up` para el ahoge de Itsuki tiende a generar
**dos** ahoges. Con el pelo rojo y las estrellas ya se distingue de sobra, así
que se puede omitir.

Yotsuba en manga corta necesita redundancia: `short sleeve white shirt, bare arms, sleeves ending above the elbow`.
El token que más trabaja es `bare arms`, porque describe el resultado visible
en vez del corte de la manga.

**Contaminación de vestuario:** con cinco figuras los atributos se difunden
entre vecinas (el chaleco rojo de Itsuki se le pasa a Nino, que están pegadas).
Se mitiga engordando el vestuario del afectado con redundancia y encerrando el
atributo en su dueña (`red vest only on this girl`). Si aun así falla, se
corrige en Gemini.

**Jerarquía de qué defender cuando no sale todo:** primero que sean cinco,
luego los colores de pelo, luego las poses, y el vestuario al final. Un blazer
mal asignado se nota mucho menos que una sexta hermana.

### Maruo — ficha de prompt

Adulto joven de treinta y pocos, delgado, cara estrecha de mandíbula suave,
ojos pequeños y negros de párpado caído, pelo negro muy corto con matiz
verdoso solo en los brillos y flequillo recto. Traje negro, camisa blanca,
corbata azul **sólida** (sin rayas). Trazo más plano que el de las hermanas.

```
young adult man in his early thirties, soft rounded jawline, plain simple face,
small narrow eyes, drooping half lidded eyes, black eyes, dark black eyes,
very short black hair, pure black hair, jet black hair with faint dark green
highlights, low volume hair, matte hair with minimal highlights,
simple flat shading on the face
```

El LoRA tira fuerte hacia los ojos azules de las hermanas: los tres tokens
redundantes de negro no son opcionales.

### Corrección local en Gemini — flujo validado

Para arreglar detalles de un CG ya generado sin volver a tirar tandas:

- Se le dan **dos imágenes**: el CG y el sprite de referencia del personaje a
  corregir.
- Se **numera cada cambio** («CHANGE 1», «CHANGE 2») y se identifica al
  personaje **por posición y rasgos, no por nombre**.
- Se enumera **explícitamente todo lo que debe quedar igual**: las otras
  hermanas, la mesa, el fondo, la iluminación.
- Se insiste en igualar grosor de línea, sombreado plano y gradación de color, y
  en que la edición parezca pintada en la misma pasada.
- Se pide la imagen completa al mismo encuadre y resolución.

**Riesgo:** cada pasada reinterpreta la imagen entera y puede **deshacer
correcciones anteriores** (pasó dos veces con el chaleco rojo de Nino). Además
el trazo se ablanda y el fondo pierde definición con cada iteración. Máximo dos
o tres ediciones encadenadas; a partir de ahí, quedarse con la mejor versión y
aceptar el detalle menor. Gemini comprime en JPEG y eso **no se recupera**: el
escalado y el realce devuelven definición aparente al trazo, pero el detalle
que se comió el JPEG no vuelve, y subir el WebP por encima de 95 solo guarda
los artefactos con más fidelidad.

### Bloque de fondo del departamento

Para CG donde se ve la sala completa, versión luz de tarde (la de la mayoría
del set). Copiar **literal** entre CG:

```
indoors, double height loft apartment living room, exposed red brick wall,
black metal staircase with glass railing leading to a second floor landing,
long horizontal built in aquarium glowing under the staircase, green aquatic
plants and a fish inside the tank, dark wooden cabinets covering the back wall,
white leather three seater sofa with cushions, low dark wood coffee table,
white shaggy rug, black leather armchair, small round table lamp,
dining table with dark chairs behind the sofa, kitchen counter on the right
with hanging pendant lights, dark hardwood floor, floor to ceiling window on
the left, low wide steps beside the window, dark wooden interior door in the
back wall,
warm late afternoon sunlight streaming through the tall window, long light rays
across the floor, soft warm shadows, teal glow from the aquarium, soft shading,
anime background art
```

**Noche:** el ventanal es lo único que delata la hora. Si el encuadre apunta a
la pared del fondo (la de la puerta interior), el ventanal queda fuera de plano
y el interior puede estar bien iluminado sin contradecir la noche. En ese caso
el segundo párrafo pasa a:

```
warm interior lighting, all indoor lamps turned on, glowing pendant lights over
the counter, bright evenly lit room, teal glow from the aquarium, soft warm
shadows on the floor, soft shading, bright colors, anime background art
```

Si hace falta una versión nocturna de `bg_departamento` sin regenerarla,
Ren'Py la da con un tinte sobre el mismo archivo:

```renpy
image bg departamento_noche = im.MatrixColor(
    "images/bg/bg_departamento.webp",
    im.matrix.tint(0.72, 0.76, 1.0) * im.matrix.brightness(-0.08)
)
```

No sustituye a un fondo pintado de noche —los rayos del ventanal siguen ahí,
solo que azulados—, pero para escenas de paso resuelve sin gastar créditos.

### Plantilla de prompt para fondos

```
masterpiece, best quality, absurdres, scenery, indoors, no humans,
[DESCRIPCIÓN DE LA ESCENA],
soft lighting, bright colors, pastel colors, soft shading,
detailed background, anime background art, wide shot
```

El que hace el trabajo es `no humans`: es etiqueta danbooru entrenada, no una
negación gramatical, y por eso sí funciona dentro del prompt positivo. La lista
de negativos que traía este documento (`1girl, 1boy, person, face, hands, text,
watermark…`) **ya no aplica**: la cuenta gratuita no tiene campo negativo
separado, y escribir esos términos en el campo único los invoca en vez de
evitarlos. Si aun así se cuela una figura, la vía es reforzar en positivo
(`empty room, unoccupied, scenery only`) o cambiar la semilla.

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
- **Al reemplazar un sprite hay que borrar `game/cache`** o Ren'Py sigue
  mostrando la versión vieja. Es el equivalente del `.rpyc` para las imágenes:
  pasas media hora normalizando un sprite y en pantalla no cambia nada.

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
- **`itsuki_timida` quedó 24 px corta por abajo** (su render venía cortado más
  arriba): con `yanchor 1.0` flota ese pelín respecto a las otras cuatro.
- **El pelo de Miku no coincide entre CG y sprite.** En los CG quedó castaño
  oscuro tras la corrección en Gemini; el sprite sigue en castaño claro. Hay
  que decidir cuál manda, porque si no la inconsistencia se arrastra a todo el
  juego.
- **Nombres de sprites de Raiha.** El problema del cambio de ropa habla de
  `raiha_sorprendida`, pero la tabla de sprites solo registra
  `raiha_hablando` y `raiha_regano`. Antes de rehacerlos hay que fijar de una
  vez qué expresiones existen y cómo se llaman.
- **`Ichika_sonrisa.png` empieza por mayúscula**, contra la regla de la sección
  10. Funciona en Windows y revienta al exportar a Linux o Android. Renombrar
  ahora, que solo lo referencia el prólogo.

---

## 12. Siguiente paso

El proyecto avanza por dos frentes que no se bloquean entre sí.

### Guion — escribir `02_capitulo1.rpy`

Antes de empezar hay que decidir:

1. Cuántas decisiones puntuadas tendrá el capítulo y con qué valores, para
   calibrar el umbral de 10.
2. Cuál es la primera decisión puntuada del juego — la que escribirá
   `primera_conexion` y definirá el desempate de toda la partida.

Recordar usar siempre `$ sumar_punto("chica", n)` dentro de los `menu`.

### Arte — cerrar el prólogo

En orden, porque el primero desbloquea a los demás:

1. **Definir qué expresiones necesita cada hermana en el prólogo y generar las
   que falten.** Nino, Miku y Yotsuba tienen una sola cada una. La lista sale
   del guion de `01_prologo.rpy`, que ya está escrito: es cuestión de barrerlo
   y anotar cada cambio de tono.
2. Generar los CG de Yotsuba e Itsuki para completar la escena de la
   presentación.
3. Rehacer los sprites de Raiha e Isanari con el estándar del set (760 × 930,
   línea de ojos en 199, IPD 77,2).
4. Decidir el tono de pelo de Miku —CG o sprite— y unificar.
5. Opcional: `cg_maruo_espaldas` para el cierre de la escena 6.
6. Opcional: regenerar a Itsuki en vertical con las rodillas visibles y rehacer
   el set completo para ganar pierna en las cinco. Es la única forma de subir
   el corte inferior, y cuanto más tarde se haga, más sprites hay que rehacer.
