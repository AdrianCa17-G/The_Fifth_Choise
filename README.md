# The Fifth Choice — Estado del proyecto

Documento de contexto para retomar el desarrollo en una conversación nueva.
Última actualización: **prólogo cerrado por completo**. Sprites de las cinco
hermanas regenerados y limpiados, transforms reescritos (había un bug grave de
posición), guion corregido en continuidad y voz de personaje, y capa de audio
montada entera: 8 pistas, ambiente y 11 efectos con sus cues en el guion.

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
| `01_prologo.rpy` | ✅ Terminado (7 escenas, arte, sonido y revisión de guion) |
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

- **Miku**: Futaro comenta mal el libro de Sengoku y ella lo corrige sin
  levantar la vista — «es logística, las batallas las gana quien mueve el
  arroz» — y después se esconde detrás del libro al darse cuenta de que ha
  hablado. Cuatro líneas que encienden al personaje y plantan su ruta. Antes el
  libro era solo un objeto que señalaba el narrador.
- **Itsuki**: el reencuentro en el departamento ya establece la rivalidad.
- **Nino**: «el último duró cuatro días, también entró diciendo que venía a
  trabajar». Es la única vez del prólogo en que tiene razón y Futaro no sabe
  qué contestar.
- **Yotsuba**: su «…¿Verdad?» medio tono más bajo, con el rebote inmediato a
  «¡Digo, claro que sí!». La primera grieta de la armadura.

### Revisión de guion ya aplicada (no volver atrás)

- **Isanari no revela el número.** Dice «un tutor privado para su familia» y
  «hasta la graduación». Antes decía «sus hijas» y «hasta que se gradúen», en
  plural, y luego Futaro planificaba para «un alumno»: era un agujero, no un
  cálculo mal hecho. El «cinco veces la tarifa» es ahora la única pista.
- **«Quintillizas» se dice después de que entre la quinta.** Antes Nino lo
  soltaba con cuatro en pantalla y desactivaba el remate de «Cinco».
- **Futaro no se disculpa en el prólogo** y no grita insultos. Donde antes
  decía «lamento lo de esta mañana» ahora reafirma su postura, y el «¡niña
  malcriada!» pasó a un «baja la voz, ni siquiera sé tu nombre» dicho en frío.
  Su disculpa hay que guardarla para el arco, no gastarla el primer día.
- **El monólogo del instituto se reescribió** porque el fondo está vacío: ahora
  llega antes que nadie y prefiere los pasillos vacíos. Antes describía
  pasillos llenos de alumnos que no están en pantalla.
- **El reproche repetido de Itsuki se fusionó en una línea.** Se contaba tres
  veces: aula, azotea y departamento.
- **Raiha tiene un registro bajo** además del regañón, e Isanari genera
  fricción con Futaro. Antes ella solo gritaba y él no producía ninguna
  reacción en su hijo.

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
| cg_familia | Retrato familiar, primer vistazo de todo el juego, donde empieza todo, mas detalles abajo. Unificado en post, ya en WebP | Escena 1 |     
| cg_calificacion | Es bg_cuarto_mc, lo mismo, solo que hay un examen con una nota para que de sentido al dialogo de mc al inicio del prologo | Escena 1 |  
| cg_examen   | Dialogo entre mc y su docente, resaltando su inteligencia. 🔄 Rehecho | Escena 3 |   
| cg_itsuki_sentada  | Primer encuentro entre mc e Itsuki, aqui se desarrolla su dinámica | Escena 3 |         
| cg_itsuki_azotea | Segundo encuentro entre mc e Itsuki, un espacio de dialogo profundo entre ellos. 🔄 Rehecho | Escena 3 |     
| cg_manija_edificio | mc abriendo la puerta del departamento de las quintillizas | Escena 4 |    
| cg_ichika_puerta | Primer encuentro entre mc e Ichika | Escena 5 |          
| cg_nino_pasillo  | Primer encuentro entre mc y Nino. 🔄 Rehecho | Escena 5 |  
| cg_miku_sofa | Primer encuentro entre mc y Miku | Escena 5 |  
| cg_yotsuba_corriendo | Primer encuentro entre mc y Yotsuba | Escena 5 |  
| cg_itsuki_discusion  | Tercer encuentro entre Itsuki y mc, aunque aqui ya se intentan conocer mejor | Escena 5 |  
| cg_maruo_umbral | Padre de las quintillizas, establece las condiciones del trabajo con mc | Escena 6 |  
| cg_estudio_hermanas | Primera dinamica entre mc y las quintillizas, su sesión de estudio resulta un fracaso total | Escena 7 |  

**Rehechos en la última sesión** (`cg_examen`, `cg_itsuki_azotea`,
`cg_nino_pasillo`, y de paso `cg_ichika_puerta`, `cg_manija_edificio`,
`bg_instituto` y `bg_entrada_edificio`). Los tres primeros por errores propios
que conviene no repetir:

- **`cg_examen` venía con kanji inventado por toda la hoja.** La causa era que
  el prompt llevaba `text, english text, japanese text` en el campo positivo,
  arrastrados de cuando se creía que había campo negativo. Nombrar lo que no
  quieres es pedirlo. Ahora el papel se describe por lo que se ve: retícula de
  casillas vacías, cabecera, filas numeradas y un maru rojo. Estructura sin
  escritura.
- **`cg_itsuki_azotea` tenía a Futaro de frente y sin cara.** No hay LoRA suyo,
  así que el modelo lo resolvía como silueta negra; el parche en Gemini le dio
  rostro pero se llevó por delante el trazo. Se rehízo con él **de espaldas en
  primer término y desenfocado**, cortado por el borde del cuadro. Sin rostro no
  hay nada que el modelo pueda estropear.
- **`cg_nino_pasillo` era vertical**, y por eso salía con bandas negras a los
  lados y sin fondo visible, al revés que los de Itsuki, Miku y Yotsuba. Los CG
  van **siempre apaisados**, 1280×720. Es el mismo error de encuadre que costó
  el corte de piernas en los sprites.

**Todavía pendientes:** `cg_yotsuba_corriendo` y `cg_itsuki_discusion` de la
escena de la presentación. Opcional: `cg_maruo_espaldas` para el cierre de la
escena 6; el prompt de Maruo ya está validado y sin rostro visible el LoRA no
puede feminizarlo.

### El retrato familiar

Composición hecha a partir de cuatro fuentes distintas (Isanari, la madre,
Futaro y Raiha), igualando el tamaño de las cabezas y unificando el color.
**La madre está en escala de grises** porque falleció; eso resuelve la
inconsistencia temporal (cuando murió, Futaro era niño y Raiha un bebé, y no
existen fotos de esa época). Va enmarcado y colgado en una pared en penumbra.
**Decisión tomada: no se regenera en PixAI.** Es el peor caso posible para esa
herramienta — cuatro figuras en un frame con necesidades de LoRA incompatibles
(Isanari pide 0.1 como adulto masculino, Raiha pide 0.3 para reconocerse, y los
LoRAs no se aplican por región), más una madre que no tiene LoRA y cuyo parecido
es lo único que sostiene la idea narrativa.

En su lugar se hizo un **pase de unificación en post**, que es lo que hace
creíble un composite: que todo el interior del marco pase por una sola capa
fotográfica. El orden importa:

1. Máscara del interior de la foto; el marco y el passepartout no se tocan.
2. Limpieza de los restos de subtítulo del fotograma original de Isanari (rayas
   horizontales claras sobre el fondo liso, de un subtítulo mal borrado).
3. Relleno del fleco cálido en la costura Isanari / Futaro, resto del recorte.
4. **Igualación de grano**, antes de añadir nada. Isanari traía halftone fuerte
   (nivel ~13) y Futaro estaba limpio (~2). Si se añade el grano común antes de
   este paso, a Isanari se le suma al que ya trae.
5. Realce leve de la madre, para que su blandura parezca decidida y no un
   escalado mal hecho.
6. Pase común: suavizado, dominante cálida, viñeta y un solo grano para las
   cuatro figuras.

**Ya no es el único PNG del set:** se exporta en WebP 95 como todo lo demás.

**Criterio de calidad para este CG en particular:** no debe parecerse al resto
del set. Los demás son plano cerrado, cámara con ángulo y luz dorada saturada;
este es una fotografía enmarcada *dentro* del mundo del juego. Si se alinea con
el lenguaje visual del set, deja de leerse como foto. El estándar es «convence
como fotografía», no «combina con los otros CG».

### Observación sobre los CGs

Hay algunos CGs que creo que solo serán uso único para el prologo, y otras
que observo se pueden reutilizar para el desarrollo de toda la historia y
el juego, pero debemos observar cuales serían útiles.

### Sprites (`game/images/sprites/`)

Son los únicos sprites usados hasta ahora en el prólogo, obviamente como es
corto no se usaron tantos sprites de cada persona, aquì mas me enfoqué en
pulir con todo esfuerzo los sprites de las quintillizas. Los de Raiha e Isanari
ya están rehechos y normalizados con el estándar del set.

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

Y los tres que no son hermanas, por la misma razón: si no están escritos, cada
render les pone otra ropa.

| Personaje | Pelo | Vestuario |
|---|---|---|
| Futaro | Negro corto, con un mechón levantado. | **Cárdigan gris claro abierto, manga larga, camisa blanca de cuello debajo, pantalón azul marino.** No es el blazer azul de las hermanas: son prendas distintas y no hay que mezclarlas. |
| Isanari | Rubio arena apagado, corto y en pinchos, gafas de sol apoyadas en la cabeza. Ojos marrones. Delgado y fibroso, **no musculado**. | Camiseta gris oscuro de manga corta, cinturón marrón, pantalón beige, zapatos marrones. |
| Raiha | Castaño oscuro muy largo, flequillo recto, coleta alta con lazo rosa. **Ojos marrones rojizos y piel clara.** | Camiseta de rayas blancas y rosa coral de manga corta, peto vaquero azul con bajos remangados, sandalias. |

Las dos marcas en negrita de Isanari y Raiha son correcciones que costaron
tandas: el modelo tira a hacerle a él cuerpo de gimnasio y a ella la piel
tostada, y ninguna de las dos cede sin tokens redundantes.

Al final me decidi por un formato png de los sprites en tamaño
760 x 930 en todos, para mantener balanceados. **Ese tamaño vale también para
Raiha e Isanari.** El 930 no es la altura del personaje sino la del encuadre, y
como todos se anclan con `yanchor 1.0` el borde inferior del lienzo es la misma
fila de pantalla para los tres. Lo que cambia en ellos no es el lienzo sino la
fila de la línea de ojos — ver más abajo.

| Personaje | Expresion | Archivo | Estado | Tamaño |
|---|---|---|---|---|
| Raiha | Sonriendo | `raiha_hablando.png` |  ✅ Terminado | 760 x 930 px |
| Raiha | Un poco molesta | `raiha_regano.png` |  ✅ Terminado | 760 x 930 px |
| Isanari | Sonrisa leve | `isanari_sonrisa.png` |  ✅ Terminado | 760 x 930 px |
| Isanari | Neutral | `isanari_neutral.png` |  ✅ Terminado | 760 x 930 px |
| Itsuki | Brazos cruzados (se usa como «seria») | `itsuki_molesta.png` |  ✅ Terminado | 760 x 930 px |
| Itsuki | Neutral real | `itsuki_neutral.png` |  🔄 Rehecho | 760 x 930 px |
| Itsuki | Sonriendo | `itsuki_sonrisa.png` |  🔄 Rehecho | 760 x 930 px |
| Itsuki | Sorpresa | `itsuki_sorpresa.png` |  🔄 Rehecho | 760 x 930 px |
| Itsuki | Timida | `itsuki_timida.png` |  🔄 Rehecho | 760 x 930 px |
| Yotsuba | Sonriendo | `yotsuba_sonrisa.png` |  🔄 Rehecho | 760 x 930 px |
| Miku | Aburrida | `miku_aburrida.png` |  ✅ Terminado | 760 x 930 px |
| Nino | Neutral | `nino_neutral.png` |  🔄 Rehecho | 760 x 930 px |
| Ichika | Neutral | `ichika_neutral.png` |  🔄 Rehecho | 760 x 930 px |
| Ichika | Sonriendo | `ichika_sonrisa.png` |  🔄 Rehecho | 760 x 930 px |
| Profesor / Madre / Maruo | 0 — no necesitan sprite | | ✅ Terminado | |

Los sprites que dicen neutral son los sprites base de cada quintilliza,
algunas no tienen porque solo aparecieron poco tiempo en pantalla o sus
dialogos no encajarian con sus poses neutrales, ademas itsuki tiene un
sprite que aun no se ha utilizado "Itsuki Timida", debido al prologo, no
se encontró un momento exacto donde utilizarlo.

**Se resolvió la confusión `neutral` / `neutral2` de Itsuki.** El de brazos
cruzados pasó a llamarse `itsuki_molesta` y el neutral real ocupa
`itsuki_neutral`. El alias viejo `itsuki seria` ya no existe en el guion.

**Criterio adoptado para expresiones nuevas: generar solo contra guion
escrito**, nunca contra suposición. `itsuki_timida` se generó antes de tener la
escena y se quedó sin usar todo el prólogo. Las expresiones que falten a Nino,
Miku y Yotsuba se harán cuando el Capítulo 1 esté escrito y se sepa qué tonos
pide.

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
| `miku_aburrida` | 73,9 | 1,045 |
| `itsuki_molesta` (brazos cruzados) | 60,8 | 1,270 |
| `yotsuba_sonrisa` 🔄 | 76,4 | **1,011** |
| `nino_neutral` 🔄 | 71,3 | 1,083 |
| `ichika_neutral` 🔄 | 68,1 | 1,134 |
| `ichika_sonrisa` 🔄 (ojos cerrados) | 105,8 | 0,730 |
| `itsuki_sorpresa` 🔄 | 63,9 | 1,209 |
| `itsuki_timida` 🔄 | 61,6 | 1,254 |
| `itsuki_sonrisa` 🔄 | 53,9 | 1,431 |
| `itsuki_neutral` 🔄 | 48,7 | **1,584** |

Los marcados 🔄 se renormalizaron desde el render original. **Generar en
vertical 768 × 1280 importa mucho**: Yotsuba y Nino vinieron así y salieron a
escala 1,01 y 1,08, prácticamente sin reescalar. Las cuatro de Itsuki vinieron
apaisadas a 1280 × 720 y necesitaron hasta 1,58 de ampliación, con la pérdida
de nitidez que eso implica. Se compensa con realce con umbral, pero la
resolución perdida no vuelve.

**Ojos cerrados: el arco del `^_^` engaña.** En `ichika_sonrisa` los centroides
de los arcos quedan más separados que las pupilas y sobreestiman el IPD un 10%,
así que la cabeza salía pequeña. Se calibró comparando el perfil de silueta del
pelo contra su propio neutral, hasta dar con 0,730. Si vuelve a pasar, ese es
el método: medir el ancho de la silueta del pelo en varias filas alrededor de
la línea de ojos y ajustar hasta que coincida con otra expresión del mismo
personaje.

El margen superior de 199 px lo fija el lazo de Yotsuba, el accesorio más alto
del elenco. El corte inferior lo fija Itsuki: su render vino apaisado en
1280×720 y el marco la corta a media pierna, así que **todo el set quedó
cortado ahí**. Si se regenera a Itsuki en vertical con las rodillas visibles se
puede rehacer el set completo y recuperar el corte bajo la rodilla.

#### Personajes que no miden lo que las hermanas

Normalizar por IPD iguala el **tamaño de la cabeza**, no la altura. Para las
cinco hermanas basta porque miden lo mismo. Para un adulto y una niña no: hay
que mover además la línea de ojos, o los tres acaban con la cara a la misma
altura y la diferencia de estatura no existe.

Partiendo del set (IPD 77,2 con los ojos en 199) y de las alturas 178 / 165 /
138 cm, la escala del juego sale a **7,44 px por centímetro** y el suelo —donde
apoyan los pies las hermanas— cae en la fila **1348**, muy por debajo del
lienzo. De ahí:

| | escala sobre el render | fila de ojos | IPD final |
|---|---|---|---|
| Hermanas | referencia | 199 | 77,2 |
| Isanari | por IPD | **109** | 77,2 |
| Raiha | por altura | **388** | **68,3** |

A los tres el lienzo los corta a la misma altura física del suelo, unos 56 cm.
Eso es media pantorrilla en un adulto y por encima de la rodilla en una niña,
que es lo que pasaría en una foto real: la línea de corte es del encuadre, no
del personaje.

Tres cosas aprendidas aquí que conviene no volver a discutir:

- **Raiha no se normaliza por IPD.** Misma distancia entre pupilas significa
  misma cabeza, y una niña con cabeza de adolescente queda flotando respecto al
  suelo. Su IPD se deriva de la altura una sola vez (68,3) y luego se aplica
  igual a sus dos expresiones, para que la cara no cambie de tamaño al
  alternarlas.
- **Isanari a 109, el valor que da el cálculo**, aunque recorte 24 px de las
  puntas del pelo en el neutral y 17 en la sonrisa. Se probó dejarlo en 132 para
  no tocarle el pelo y quedaba casi a la altura de las hermanas: la diferencia
  de estatura se perdía entera. Con silueta de pelo en pinchos el recorte no se
  ve; que un adulto mida lo mismo que una cría de instituto sí.
- **109 es el techo del lienzo.** Para subirlo más habría que recortarle cráneo,
  no puntas. Si algún día se quiere más diferencia hay que cambiar el margen
  superior del set, no su escala: bajarle el IPD lo haría más pequeño, no más
  alto.

#### Huecos blancos: fondo o ropa

Al recortar hay que decidir qué blanco encerrado es fondo (transparente) y cuál
es ropa (opaco). El criterio del entorno no vale: el hueco entre los dedos está
rodeado de piel igual que la raya de la camiseta lo está de tela. Lo que separa
es la **pureza**:

- **Pureza ≥ 252** → fondo. Pilla los huecos del pelo y de los dedos en fuentes
  PNG, donde el fondo es 255 puro.
- **O bien pureza ≥ 250,5 con más de 1000 px** → fondo. Pilla los huecos grandes
  en fuentes JPEG de Gemini, donde el blanco baja a 251-253.

Todo lo demás se conserva. Ese margen no es un capricho: los dientes de Isanari
miden 250,1 y el brillo del ojo de Raiha 250,5, y con el umbral en 250 los dos
salían transparentes. Se veían como agujeros negros sobre fondo oscuro.

**CORRECCIÓN IMPORTANTE: la pureza sola NO basta.** Con Ichika la regla de
arriba borraba su camisa entera. Su camisa blanca mide 250,9–254,5 de pureza,
exactamente lo mismo que el fondo, y los dos parches del pecho (4151 y 3913 px)
cumplían «≥ 250,5 y más de 1000 px» al pie de la letra.

El discriminante que sí funciona es **el color del contorno, no la pureza del
hueco**. Un hueco de fondo de verdad está rodeado de piel o pelo, que son
cálidos; la ropa blanca y sus sombras son frías. La regla definitiva es que un
hueco encerrado se borra solo si cumple **las dos** condiciones:

- **Pureza media ≥ 253,5**, y
- **calidez del contorno (r − b) ≥ 20**.

Separación medida: hueco de pelo de Itsuki 254,8 / +66. Camisa de Ichika 253,7
/ +4. Dientes 250,9, protegidos por el filtro de pureza. No está al límite.

**Y el filtro de lineart del contorno se mide por luminancia, no por canal
mínimo.** Descartar la lineart con `min(r,g,b) > 120` parece razonable hasta
que llega el pelo rojo de Itsuki, cuyo canal mínimo ronda 70–111: el contorno
entero se descartaba, la prueba abortaba sin decidir y le quedaba un parche
blanco de 3445 px en el pelo, visible a leguas en el juego. Con `media > 70` se
quita la lineart negra sin tocar el pelo saturado. Área mínima del hueco: 40 px.

**Excepción conocida — Yotsuba.** Su paleta es amarillo, naranja y verde, así
que su cuello blanco está pegado al chaleco amarillo y mide cálido igual que el
pelo. La regla no puede distinguirlos y le comió una tira del cuello. Sobre un
PNG ya recortado hay que usar `--solo-halo`; desde el render original sí
funciona bien, porque ahí solo un hueco cumple las dos condiciones.

#### Halo blanco del contorno

Aparte de los huecos, hay un segundo defecto: el **halo**. Los recortes binarios
dejan los píxeles del borde con el blanco del fondo mezclado dentro del color, y
al componer sobre el fondo oscuro del apartamento se ve un contorno lechoso
alrededor del pelo. Yotsuba lo tenía: sus píxeles de borde promediaban RGB
(206, 190, 183).

Se corrige por **desmatteado**. El píxel guarda `C = a·C_real + (1−a)·255`, así
que se despeja `C_real`. No hace falta filtrar por color: si el píxel es blanco
de verdad, quitarle el blanco devuelve blanco y no cambia nada. Solo se excluyen
los alphas por debajo de 0,28, donde la división amplifica el ruido.

**Y al escalar hay que premultiplicar el alpha.** Si se reescala el RGBA sin
premultiplicar, Lanczos mezcla el RGB de los píxeles transparentes —que sigue
siendo el blanco del fondo— dentro del borde. Ya está corregido en el script.

Un aviso para no perder el tiempo: **la línea clara fina que se ve entre los
mechones no es halo, es el dibujo**. Escaneando el render crudo aparece un
píxel en (207, 168, 169) entre dos valores de rojo oscuro. Es la separación de
mechones que dibuja el modelo. Si se intenta quitar, se rompe el pelo.

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

Opciones añadidas: `--eje` para forzar el eje del cuerpo, `--huecos x,y;x,y`
para marcar a mano huecos de fondo por punto semilla, y `--sin-huecos` para
desactivar el borrado automático (el modo seguro para Yotsuba).

**Detección de ojos — dos trampas resueltas.** El umbral del azul subió a
`b−r > 60` y `b−g > 50`, y la búsqueda se restringe al 42% superior de la
figura. Con el umbral flojo, los brillos azules del **blazer de Ichika** son
más grandes que su iris y ganaban por tamaño: su neutral medía IPD 184 en vez
de 68. El iris está en b−r ≈ 80 y el blazer en 47, así que la separación es
amplia.

**Extensión inferior automática.** Si el render venía cortado por el borde del
frame y al normalizar el contenido se queda hasta 30 px corto, el script
prolonga la última fila. Ahí solo hay pierna y el corte lo marca el encuadre,
no el personaje. Es lo que resolvió el problema de los 24 px de `itsuki_timida`.

#### Herramienta: `limpiar_halo.py`

Trabaja sobre un sprite **ya normalizado** (760 × 930) sin tocar escala ni
posición. Hace dos cosas: el desmatteado del contorno y el borrado de huecos
encerrados con la regla del contorno cálido.

```
python limpiar_halo.py entrada.png salida.png
python limpiar_halo.py entrada.png salida.png --solo-halo
```

Se usa cuando el sprite ya está en el juego y no se tiene el render original.
Si se tiene el render, es mejor volver a pasar `normalizar_sprite.py`: el
resultado es más limpio porque trabaja antes de recortar y escalar.

*Nota para un posible sprite de Maruo:* la detección busca **azul** y él tiene
los ojos negros, así que habría que pasarle `--ojos` a mano. A cambio,
normalizarlo por IPD lo dejaría automáticamente más alto que las hermanas (un
adulto tiene menos cabeza en proporción al cuerpo), que es justo lo que
conviene para la escena del contrato.

---

### Transiciones y transforms

**Regla del archivo: todo `show` lleva SIEMPRE su posición**, aunque solo
cambie el tinte. Esto no es estilo, es lo único que impide que vuelva un bug
que costó una sesión entera encontrar.

#### El bug de los sprites encimados

`at` **reemplaza el transform entero, no lo suma.** Cuando se escribía
`show nino at habla`, no se le añadía el tinte a la posición: se la quitaba.
Ren'Py intenta salvarlo heredando el estado del transform anterior, y lo que
hereda es el estado **en ese instante exacto**.

El transform de movimiento usaba `ease t xcenter x` con `t = 1` segundo. Si el
jugador hacía clic a los 200 ms, el sprite iba por el 20% del recorrido, el
siguiente `show ... at habla` congelaba ese 20% y ya no se movía nunca más. De
ahí los sprites encimados y las regresiones rotas.

La causa de fondo es una asimetría de Ren'Py que conviene tener grabada:

> **Un clic salta una transición a su estado final. Un clic NO adelanta una
> animación ATL.** Por eso el movimiento tiene que ser una transición, nunca un
> `ease` dentro del transform.

#### Los transforms actuales

```renpy
define X_ICHIKA  = 0.13
define X_NINO    = 0.31
define X_MIKU    = 0.50
define X_YOTSUBA = 0.69
define X_ITSUKI  = 0.87

transform pj(x=0.5):
    xanchor 0.5
    yanchor 1.0
    xpos x
    ypos 1.0
    zoom 1.0
    matrixcolor TintMatrix("#ffffff")

transform pj_habla(x=0.5):
    xanchor 0.5
    yanchor 1.0
    xpos x
    ypos 1.0
    ease 0.25 zoom 1.01 matrixcolor TintMatrix("#ffffff")

transform pj_calla(x=0.5):
    xanchor 0.5
    yanchor 1.0
    xpos x
    ypos 1.0
    ease 0.25 zoom 0.99 matrixcolor TintMatrix("#a0a0a0")

define mover = MoveTransition(0.8)
```

`pj_mueve`, `habla` y `calla` **ya no existen**. Reafirmar la posición absoluta
en cada `show` hace que una transición interrumpida se autocorrija en la línea
siguiente.

#### Movimientos y entradas

```renpy
show ichika at pj(0.25)
with mover

show nino neutral at pj(0.75)
with dissolve
```

Primero el desplazamiento de quien ya estaba, después la entrada del nuevo con
`dissolve`. Se encadenan solas sin clic de por medio.

**Trampa de `MoveTransition`:** sus parámetros `enter` y `leave` esperan un
**transform con la posición de partida** (`offscreenright` y similares), no una
transición. Pasarles `dissolve` no falla al cargar el juego — revienta en
tiempo de render con `AttributeError: 'NoneType' object has no attribute
'style'`, ya dentro de la escena. Por eso `mover` va pelado y las entradas se
resuelven aparte.

Para salidas, `hide <tag>` con `moveoutleft`. Antes se movía el sprite a
`xcenter -0.5` y se quedaba cargado fuera de pantalla.

#### Otras transiciones

`with dissolve` para cambios de escena entre BG y CG. `with fade` para saltos de
tiempo y cortes duros. `disolucion_lenta = Dissolve(1.2)` sigue definida pero ya
no se usa en el prólogo.

---

## 9. Generación de imágenes — configuración que funciona

**Plataformas: PixAI** para generar y **Gemini** para composiciones y
correcciones locales sobre imágenes ya generadas. PixAI en cuenta gratuita,
10.000 créditos diarios que no caducan.

- **Modelo base por defecto: Tsubaki.2**
- El LoRA debe coincidir con el modelo base o no hace nada y gasta créditos en
  silencio. Es el fallo más caro de la plataforma.
- **El campo negativo depende del modelo base, no de la cuenta.** Con Tsubaki.2
  no aparece, y de ahí venía la idea de que la cuenta gratuita no lo tenía. Con
  Haruka v2 sí existe, y además **viene relleno con un negativo por defecto**
  que conviene revisar: trae `simple background` y `transparent background`, que
  pelean directamente contra el fondo blanco liso que se pide para los sprites,
  y `cropped`, que pelea contra el encuadre de cuerpo entero. Ahí es donde salían
  los marcos decorativos y los textos japoneses de la nada.
- **Cuando hay campo negativo, úsalo para lo que el positivo no puede.** Cosas
  como `handcuffs, chains, jewelry, frame, border, multiple views, 2girls,
  dark skin` se atacan mucho mejor desde ahí.
- **Sin campo negativo, todo va en positivo y describiendo el resultado
  visible**, nunca lo que se quiere evitar.

### Compatibilidad de LoRA y modelo base

Los LoRA de la comunidad no son todos del mismo linaje y ahí se pierden créditos:

- **Tsubaki.2 es SD 1.5.** El LoRA de serie de Gotoubun que se usa es de esta
  familia.
- **Los LoRA marcados «Illustrious XL» son SDXL.** Con Tsubaki.2 no hacen nada.
  PixAI autoselecciona **Haruka v2** (SDXL) al cargarlos, que no es coincidencia
  exacta pero sí compatible: el LoRA engancha, aunque rinde por debajo de su
  valor nominal. Por eso el LoRA de Raiha se usó a **0.85** y no a 0.75.
- **Consecuencia:** al cambiar de base también se pierde el LoRA de serie, que
  es de Tsubaki. Con un LoRA de personaje Illustrious se va **sin LoRA de
  serie**; el de personaje ya trae su estilo dentro.

### LoRA de personaje encontrados

| Personaje | LoRA | Base | Fuerza |
|---|---|---|---|
| Ichika | 中野一花 サンプル(アニメ)Tsubaki.2バージョン | **Tsubaki.2 nativo** | 0.8 |
| Nino | 中野二乃 アニメ(サンプル)Tsubaki.2バージョン | **Tsubaki.2 nativo** | 0.8 |
| Miku | 中野三玖 アニメ(サンプル)Tsubaki.2バージョン | **Tsubaki.2 nativo** | 0.8 |
| Yotsuba | 中野四葉 サンプル(アニメ)Tsubaki.2バージョン | **Tsubaki.2 nativo** | 0.8 |
| Itsuki | 中野五月 サンプル(アニメ)Tsubaki.2バージョン | **Tsubaki.2 nativo** | 0.8 |
| Raiha | «Raiha Uesugi - The Quintessential Quintuplets», trigger `raihau, hair bow, striped shirt, blue overalls` | Illustrious XL → usar Haruka v2 | 0.7 – 0.85 |

**Las cinco hermanas tienen LoRA propio y nativo de Tsubaki.2.** No hace falta
cambiar de modelo base ni subirles la fuerza, al contrario que con Raiha.

Con LoRA de personaje **hay que quitar la redundancia del prompt**, no sumarla:
competir con él es lo que rompe el parecido. Y ojo, el de Raiha trae los ojos
turquesa del anime; se corrigen a marrón por prompt sin pelea.

**Futaro no tiene LoRA**, y esa es la razón de fondo de que salga como silueta
negra cada vez que se le pide de frente. La solución no es prompting: es
encuadrarlo de espaldas, desenfocado y cortado por el borde. Sin rostro no hay
nada que estropear, y el cárdigan gris con el pelo negro corto lo identifican de
sobra.

### Pesos de LoRA — ya calibrados

| Caso | LoRA de serie | LoRA de personaje |
|---|---|---|
| Sprite individual de una hermana | **Ninguno** | 0.8 |
| CG individual | 0.3 | 0.7 – 0.8 |
| CG de grupo con las cinco | 0.3 | Ninguno |
| Maruo u otro adulto masculino | 0.1 | Ninguno |

**Corrección respecto a la versión anterior: los sprites de las hermanas se
generan SOLO con su LoRA de personaje**, sin el de serie. Es lo que se venía
haciendo en la práctica y lo que mantiene la consistencia del set; añadir el de
serie ahora metería un cambio de estilo justo en la hermana que se intenta
emparejar. Encaja además con lo ya sabido: el LoRA de personaje trae su propio
estilo dentro y el de serie encima solo suma riesgo.

**Las cinco quintillizas SÍ tienen LoRA propio**, y además nativo de Tsubaki.2,
no de Illustrious. Enganchan a su valor nominal sin tener que subirles la fuerza
para compensar, al contrario que el de Raiha. Con LoRA de personaje nativo, la
semilla deja de ser crítica para mantener el parecido entre expresiones —
conviene apuntarla igual, pero ya no obliga a rehacer sets enteros.

**Tsubaki.2 no tiene campo negativo ni ajustes avanzados** salvo la semilla. No
hay pasos ni CFG que tocar, así que el prompt es la única palanca: de ahí que
haya que meter tokens redundantes en la expresión y el encuadre.

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

### Herramientas de post (`herramientas/`, fuera de `game/`)

Cuatro scripts de Python, todos con `pillow`, `numpy` y `scipy`. No son scripts de
Ren'Py y no deben vivir dentro de `game/`.

| Script | Qué hace |
|---|---|
| `normalizar_sprite.py` | Recorta el fondo y normaliza un sprite de hermana al estándar del set (760 × 930, ojos en 199, IPD 77,2). Opciones: `--ojos`, `--eje`, `--huecos`, `--sin-huecos`. |
| `limpiar_halo.py` | Sobre un sprite **ya normalizado**: quita el halo blanco del contorno por desmatteado y borra huecos encerrados. `--solo-halo` para Yotsuba. |
| `normalizar_extra.py` | Lo mismo para Isanari y Raiha, con sus filas de ojos propias y el modo por altura de Raiha. |
| `escalar_cgs.py` | Pasa un lote de CG y fondos a 1920×1080 con Lanczos y WebP 95. Aplica realce de nitidez **solo a las fuentes JPEG** y con umbral. |

**Detección de ojos:** los scripts buscan **iris azul**. Isanari y Raiha los
tienen marrones, así que con ellos hay que pasar las coordenadas a mano. Lo
mismo valdría para un futuro sprite de Maruo, que los tiene negros.

**Saturación de referencia del set:** los CG aprobados están entre **68 y 84** de
saturación media. Los que salgan muy por debajo se corrigen en el escalado, no
regenerando — salvo que el contenido justifique el color bajo (una puerta de
madera o un portal de hormigón no tienen color que sacar y forzarlo solo mete
ruido).

---

## 9 bis. Audio — montado y cerrado

Ocho pistas, un ambiente y once efectos. Los cues ya están escritos en
`01_prologo.rpy`; solo falta ir soltando archivos en las carpetas.

### Estructura de carpetas y nombres

```
game/audio/bgm/   hogar, cena, cotidiano, incomodo,
                  extraneza, caos, contrato, derrota   (.ogg)
game/audio/       amb_viento.ogg
                  sfx_*.mp3   (11 efectos)
```

Los BGM se declaran con nombre corto (`define audio.hogar = "audio/bgm/hogar.ogg"`)
porque la carpeta ya lleva el prefijo. Los efectos mantienen `sfx_`.

### Las ocho pistas elegidas

| Cue | Pista | Fuente |
|---|---|---|
| `hogar` | ピアノ34「静寂の世界へ」 | 魔王魂 |
| `cena` | アコースティック04 | 魔王魂 |
| `cotidiano` | ピアノ25「Cookie Cookie」 | 魔王魂 |
| `incomodo` | Zany Escape (Kobat) | DOVA |
| `extraneza` | 日曜の午後 (KK) | DOVA |
| `caos` | Busy As A Bee (ハモおた) | DOVA |
| `contrato` | Night Shade Story (shimtone) | DOVA |
| `derrota` | ピアノ09 | 魔王魂 |
| `amb_viento` | 風 孤独感 | Springin' Sound Stock |

**`hogar` suena exactamente dos veces en todo el prólogo**: bajo el retrato
familiar y en «Bien. Que sea difícil». Es el tema de Futaro. Si sonara también
durante la cena dejaría de ser un tema y sería fondo — por eso existe `cena`
como pista aparte.

### Los cuatro silencios

Son la parte que más rinde y la que más se olvida:

- **El monólogo de apertura.** Hace que la entrada de `hogar` signifique algo.
- **`cg_manija_edificio`.** Dos segundos de nada antes de la revelación.
- **Antes de que aparezca Maruo**, con `fadeout 0.3`. Corte seco: aquí el juego
  deja de ser una comedia.
- **Desde que sale del edificio hasta «Bien. Que sea difícil».** «Despedido.»
  cae en seco. La música vuelve cuando decide no rendirse, no antes.

### Reparto medido de cada pista

Se midió cuántas líneas de diálogo cubre cada cue, y ahí aparecieron dos errores
que no se ven leyendo el guion: `caos` sonaba **5 líneas** (una pista de 2:52
desperdiciada) y había un `cotidiano` de **6 líneas** que no daba tiempo ni a
entrar con su propio fundido. Corregido:

| Cue | Líneas |
|---|---|
| extraneza | 73 |
| cena | 52 |
| caos | 46 |
| azotea (solo viento) | 38 |
| incomodo | 30 |
| derrota | 26 + 25 en silencio |
| contrato | 21 |
| hogar (inicio) | 19 |
| cotidiano ×2 | 12 y 11 |
| hogar (final) | 7 |

Tres decisiones de montaje que salieron de esa medición:

- **`caos` arranca en el portazo de Itsuki**, a la vez que el golpe, no después
  de «Quintillizas». Antes `extraneza` cargaba con 114 líneas y con seis ánimos
  distintos.
- **La azotea va sin música, solo viento.** Ahí los dos están callados sin saber
  qué decirse: no es la bronca del aula, es lo contrario. Resolvió de paso que
  `incomodo` tuviera que servir a dos escenas opuestas, y sin gastar una pista.
- **`derrota` se corta antes del portazo de Nino.** Las cuatro puertas suenan
  sobre silencio, que pesa más, y la pista deja de dar cinco vueltas.

### Los once efectos

Todos de 効果音ラボ salvo el viento. Términos de búsqueda en japonés, que es lo
único que entiende su buscador:

| Momento | Buscar |
|---|---|
| Papel sobre la mesa (esc. 2) | `書類を置く` |
| Timbre del instituto | `学校のチャイム` |
| Silla del aula | `椅子を引く` |
| Interfono del edificio | `インターホン` |
| Manija antes de entrar | `ドアノブ` |
| Puerta al abrir Ichika | `ドアを開ける` |
| Yotsuba corriendo | `走る足音` |
| Portazo de Itsuki | `ドアを勢いよく開ける` |
| Bolsa del supermercado | `レジ袋` |
| Repartir la hoja | `紙をめくる` |
| Las cuatro puertas (esc. 7) | `ドアを閉める` |

**Volúmenes ya ajustados en el guion**: 0,4 para papel y silla; 0,6–0,7 para
puertas y timbres; **1,0 solo para el portazo de Itsuki**, que es a propósito el
sonido más alto del prólogo. Las cuatro puertas de la escena 7 usan el mismo
archivo sin variar nada: la repetición idéntica es lo que hace que la última
suene más sola que la primera.

### Licencias — resumido

| Sitio | Condición |
|---|---|
| 魔王魂 | CC BY 4.0. Crédito **obligatorio**: `音楽：魔王魂`. Autoriza el cifrado para creación de juegos |
| DOVA-SYNDROME | Uso en juegos permitido. Gestionan su propio Content ID y no reclaman. **Pasa a llamarse OpenTracks el 15/09/2026** |
| PeriTune | Crédito opcional. Prohibido registrar en Content ID |
| 効果音ラボ | Sin crédito, informe ni enlace. Empaquetar en el juego permitido |
| Springin' Sound Stock | Crédito opcional. Uso comercial y venta de juegos permitidos |

**Apuntar título y autor de cada pista según se descarga**, no la URL —
DOVA cambia de nombre en septiembre y los enlaces pueden romperse.

### Notas técnicas

- **OGG para todo lo que cicle**, MP3 vale para los efectos puntuales. El MP3
  mete un silencio en el punto de bucle; un golpe de puerta no cicla, un viento
  sí.
- `renpy.music.register_channel("ambiente", "sfx", loop=True)` está en el
  `init python` del prólogo. Sin ese canal, el viento cortaría la música.
- **El viento se alargó a mano en Audacity.** El original dura 4 s y un ciclo
  tan corto se reconoce enseguida. Se repitió 7 veces hasta 35 s y se le
  aplicaron fundidos de un segundo en los extremos. Queda un bajón de volumen
  cada 35 s, imperceptible porque va por debajo del diálogo.

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
- **`at` reemplaza el transform entero, no lo suma.** Ver la sección de
  transiciones. Es la trampa más cara que ha dado este proyecto.
- **Un clic salta una transición; un clic NO adelanta una animación ATL.** De
  ahí que el movimiento tenga que ser transición y no `ease`.
- **`MoveTransition(enter=...)` pide un transform de posición, no una
  transición.** Y no falla al cargar: revienta en tiempo de render, ya dentro
  de la escena, con un `AttributeError` que no menciona el parámetro culpable.
- **Renombrar un `define audio.X` obliga a renombrar todos sus `play`.** Al
  reorganizar las carpetas se acortaron tres `play music` sin tocar sus
  `define`, y el archivo quedó a medias: cinco pistas con prefijo y tres sin él,
  apuntando a nombres inexistentes.

---

## 11. Problemas conocidos

- ~~**Cambio de ropa de Raiha**~~ y ~~**coleta cortada**~~ — resueltos. Sus dos
  sprites se generaron de cero con la misma semilla, mismo vestuario y la coleta
  completa. `raiha_sorprendida` ya no existe: las expresiones son `hablando` y
  `regano`.
- **La madre en el retrato familiar** viene de una foto de artbook de 340 px de
  ancho, ampliada. Como sprite en escena funciona; en primer plano se notaría.
- **Composición del comedor**: la mesa está centrada y adelantada. Los sprites
  hay que colocarlos a los lados (`xalign 0.2` / `0.8`) o quedan plantados
  encima del mueble.
- ~~**`itsuki_timida` quedó 24 px corta**~~ — resuelto. El script prolonga la
  última fila cuando el render venía cortado por el borde del frame.
- **El pelo de Miku no coincide entre CG y sprite.** En los CG quedó castaño
  oscuro tras la corrección en Gemini; el sprite sigue en castaño claro. Hay
  que decidir cuál manda, porque si no la inconsistencia se arrastra a todo el
  juego.
- ~~**Nombres de sprites de Raiha**~~ — cerrado: `raiha_hablando` y
  `raiha_regano`, nada más.
- ~~**`Ichika_sonrisa.png` con mayúscula**~~ — resuelto al regenerarla:
  `ichika_sonrisa.png`.
- **Las gafas de Isanari cambian de sitio entre sus dos sprites**: caladas sobre
  los ojos en el `neutral`, subidas a la frente en la `sonrisa`. Decisión
  tomada: se asume. Es un secundario y casi nadie lo va a registrar. Lo único
  que conviene evitar es alternarlos en réplicas consecutivas, que es donde el
  salto sí se ve.
- **Los sprites vienen con luz de estudio plana y los fondos con luz cálida.**
  Se nota sobre todo con el comedor: el blanco de la camiseta de Raiha es más
  frío que cualquier blanco de la habitación, y a Isanari le queda un contorno
  rojizo en el brazo que no viene de ninguna luz de la escena. Se arregla con un
  tinte cálido por escena aplicado a los sprites, no al fondo. No hay que
  regenerar nada.
- **El fondo del comedor está pintado con una cámara mucho más lejana que la de
  los personajes.** Isanari de cuerpo entero queda a un palmo de la campana
  extractora y encoge la habitación. En esa cocina conviene colocarlo hacia el
  hueco de la puerta, o reservar ese fondo para planos donde él no salga entero.
- ~~**Contradicción texto-imagen en la escena 2**~~ — resuelto: el narrador ya
  no dice que Isanari se sentó.
- ~~**Composición del comedor**~~ — aplicado: Raiha e Isanari a 0,20 y 0,73, y
  Raiha sola a 0,30.
- **El corte inferior del set sigue fijado por Itsuki.** Sus cuatro renders
  nuevos volvieron a venir apaisados en 1280 × 720. Nino y Yotsuba sí vinieron
  verticales y se ve la diferencia de nitidez. Para subir el corte hay que
  regenerar a Itsuki en vertical y rehacer las cinco.
- **El lazo de Yotsuba viene cortado en el propio render**: hay verde en la fila
  0 del PNG original de PixAI. No es la normalización. Para tenerlo entero hay
  que regenerar con más margen arriba.
- **La falda de `itsuki_neutral` es olivácea.** Color medio (92, 102, 74) frente
  a (90, 118, 63) del resto del set. Alternar esa expresión con otra en la misma
  escena hace que la falda cambie de tono en pantalla. Se corrige en post con un
  ajuste de tono sobre la región verde, sin regenerar.
- **Maruo promete una condición que el juego no ejecuta.** Dice que si una
  hermana reprueba, despedido en el acto. Pero el Final Malo se dispara porque
  ninguna llegó a 10 puntos de afinidad: son dos condiciones distintas. Hay que
  decidirlo antes de escribir el Capítulo 1, porque cambia lo que significan los
  puntos. Lo más limpio es que la afinidad represente «logró llegar a ellas y
  por eso estudian», y narrar el Final Malo como el despido que Maruo anunció.
- **Itsuki dice que acaba de transferirse** y que las materias son más difíciles.
  Sus cuatro hermanas van al mismo instituto, así que se transfirieron todas.
  Es coherente, pero conviene que lo sea a propósito y no por descuido.

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

### Arte — el prólogo ya está cerrado

Fondos, CG y sprites están completos y al mismo estándar. Lo que queda es
opcional o depende del Capítulo 1:

1. ~~Expresiones que faltan a Nino, Miku y Yotsuba~~ — **aplazado a propósito**.
   Se generarán contra el guion del Capítulo 1 cuando esté escrito, no antes.
   La lección de `itsuki_timida` es que generar contra suposición produce arte
   que no se usa.
2. ~~Generar los CG de Yotsuba e Itsuki~~ — hechos.
3. ~~Rehacer los sprites de Raiha e Isanari~~ — hecho.
4. Decidir el tono de pelo de Miku —CG o sprite— y unificar.
5. Corregir la falda olivácea de `itsuki_neutral`.
6. Aplicar el tinte cálido por escena a los sprites.
7. Opcional: `cg_maruo_espaldas` para el cierre de la escena 6.
8. Opcional: variante de tarde de `bg_instituto` y de noche de
   `bg_departamento`. La segunda se resuelve con `MatrixColor` sin gastar
   créditos.
9. Opcional: regenerar a Itsuki en vertical y rehacer el set para ganar pierna
   en las cinco. Cuanto más tarde, más sprites hay que rehacer.

### Audio — solo falta descargar

Los cues están escritos y las pistas elegidas. Queda bajar los archivos, ir
comprobando la costura del bucle de cada uno, y rellenar la tabla de créditos.
Vigilar sobre todo dos: `cotidiano` (ピアノ25) en el instituto, que es la que
menos claro está, y `incomodo` (Zany Escape) en el aula.

### Guardar las semillas

Lo único de todo este trabajo que no se puede recuperar después. Sin la semilla,
volver a un encuadre ya aprobado cuesta tandas enteras. Conviene apuntarla junto
al archivo —en el nombre o en una nota— para los sprites de Isanari y Raiha y
para los fondos y CG rehechos.
