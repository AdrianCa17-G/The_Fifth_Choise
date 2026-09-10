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
6. **El contrato** — Maruo. Aparece por primera vez la palabra «despedido», ✅ Terminado
   semilla narrativa del Final Malo.
7. **El primer intento** — clase fallida. Cada hermana se escapa a su manera. ✅ Terminado
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
| cg_maruo_reunion | Padre de las quintillizas, establece las condiciones del trabajo con mc | Escena 6 |  
| cg_hermanas_estudiando | Primera dinamica entre mc y las quintillizas, su sesión de estudio resulta un fracaso total | Escena 7 |  

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

Un solo atuendo para las cinco: **uniforme escolar**, también en el
departamento. Ahorra un set entero de cuerpos y nadie lo cuestiona.

Al final me decidi por un formato png de los sprites en tamaño
760 x 930 en todos, para mantener balanceados, debo verificar si ese 
tamaño iría para los sprites de Raiha e Isanari.

| Personaje | Expresion | Archivo | Estado | Tamaño |
|---|---|---|---|---|
| Raiha | Sonriendo | `raiha_hablando.png` | Modificar | Pendiente |
| Raiha | Un poco molesta | `raiha_regano.png` | Modificar | Pendiente |
| Isanari | Sonrisa leve | `isanari_sonrisa.png` | Modificar | Pendiente |
| Isanari | Neutral | `isanari_neutral.png` | Modificar | Pendiente |
| Itsuki | Neutral | `itsuki_neutral.png` |  ✅ Terminado | 760 x 930 px |
| Itsuki | Sonriendo | `itsuki_sonrisa.png` |  ✅ Terminado | 760 x 930 px |
| Itsuki | Molesta | `itsuki_molesta.png` |  ✅ Terminado | 760 x 930 px |
| Itsuki | Sorprendida | `itsuki_sorprendida.png` |  ✅ Terminado | 760 x 930 px |
| Itsuki | Timida | `itsuki_timida.png` |  ✅ Terminado | 760 x 930 px |
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

---

### Transiciones

`pj` . Hace que el sprite del personaje aparezca exactamente en el 
centro de la pantalla

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
