# The_Fifth_Choise
Juego RenPy, Fangame de las quintillizas

# 📖 GUÍA COMPLETA — The Fifth Choice
## Fan Visual Novel — Quintessential Quintuplets
### Motor: Ren'Py 8.5.3 | Desarrollado por: Adrian

---

## 🗂️ ESTRUCTURA DEL PROYECTO

```
Quintuplets/
└── The Fifth Choice/
    └── game/
        ├── images/
        │   ├── sprites/
        │   │   ├── ichika_menu.webp
        │   │   ├── nino_menu.webp
        │   │   ├── miku_menu.webp
        │   │   ├── yotsuba_menu.webp
        │   │   └── itsuki_menu.webp
        │   ├── bg/              ← fondos de escenas
        │   ├── Fondo_Menu.png   ✅ listo
        │   ├── Logo_Menu.png    ✅ listo
        │   └── petal.png        ✅ listo
        ├── audio/
        │   └── bgm/
        │       └── main_theme.ogg  ✅ listo
        ├── 00_definiciones.rpy  ← FASE 0 (pendiente)
        ├── 01_prologo.rpy       ← FASE 1 (pendiente)
        ├── 02_capitulo1.rpy     ← FASE 2 (pendiente)
        ├── 03_capitulo2.rpy     ← FASE 3 (pendiente)
        ├── 04_capitulo3.rpy     ← FASE 4 (pendiente)
        ├── 05_finales.rpy       ← FASE 5 (pendiente)
        ├── 06_main_menu.rpy     ✅ LISTO
        ├── options.rpy          ← por defecto de Ren'Py
        ├── screens.rpy          ← por defecto de Ren'Py
        └── gui.rpy              ← por defecto de Ren'Py
```

---

## 🎮 DISEÑO DEL JUEGO

### Concepto
Fan VN "What If" donde el jugador vive los eventos canónicos del anime
pero sus decisiones determinan con cuál quintilliza termina.
Estilo narrativo: Doki Doki Literature Club (DDLC).

### Estructura narrativa
```
PRÓLOGO → CAPÍTULO 1 → CAPÍTULO 2 → CAPÍTULO 3 → CÁLCULO SECRETO → EPÍLOGO/FINAL
```

### Protagonista
- Nombre por defecto: Futaro Uesugi
- El jugador puede personalizarlo al inicio
- Nunca se muestra su rostro ni sprite
- En escenas grupales aparece como silueta oscura (shadow asset)
- Variable: `nombre_jugador`

### Las 5 quintillizas
| Personaje | Color de texto | Personalidad |
|-----------|---------------|--------------|
| Ichika  | `#FFB7C5` rosa    | Actriz, coqueta, primera en actuar |
| Nino    | `#C39BD3` morado  | Tsundere, protectora, la más intensa |
| Miku    | `#5DADE2` azul    | Tímida, historia, desarrollo lento |
| Yotsuba | `#58D68D` verde   | Energética, noble, la más dulce |
| Itsuki  | `#EC7063` rojo    | Seria, estudiosa, rivalidad → amor |

---

## 🏆 SISTEMA DE FINALES (7 en total)

| Final | Condición |
|-------|-----------|
| Final Ichika  | Más puntos con Ichika (mín. 10 pts) |
| Final Nino    | Más puntos con Nino (mín. 10 pts) |
| Final Miku    | Más puntos con Miku (mín. 10 pts) |
| Final Yotsuba | Más puntos con Yotsuba (mín. 10 pts) |
| Final Itsuki  | Más puntos con Itsuki (mín. 10 pts) |
| Final Malo    | Ninguna tiene ≥ 10 puntos → Futaro es despedido |
| Final Secreto | Completar las 5 rutas románticas → polígamo jajaja |

---

## ⚙️ SISTEMA DE PUNTOS (Cálculo Secreto)

- Las variables de puntos son **invisibles** para el jugador
- Se calculan al final del Capítulo 3
- Umbral mínimo: **10 puntos** con al menos una chica
- En caso de empate: gana quien tuvo la primera decisión positiva
- Si empate vacío: prioridad Ichika → Nino → Miku → Yotsuba → Itsuki

### Variables de puntos
```
default puntos_ichika  = 0
default puntos_nino    = 0
default puntos_miku    = 0
default puntos_yotsuba = 0
default puntos_itsuki  = 0
default primera_conexion = ""
default primera_decision_hecha = False
```

### Variables persistentes (Final Secreto)
```
default persistent.ruta_ichika_completa  = False
default persistent.ruta_nino_completa    = False
default persistent.ruta_miku_completa    = False
default persistent.ruta_yotsuba_completa = False
default persistent.ruta_itsuki_completa  = False
default persistent.final_secreto_desbloqueado = False
```

---

## 📝 PROMPTS POR FASE

### ▶ FASE 0 — `00_definiciones.rpy`

```
Actúa como desarrollador experto en Ren'Py y guionista de novelas visuales.
Estamos construyendo la fan VN "The Fifth Choice" basada en Quintessential
Quintuplets, estilo DDLC (Prólogo, 3 Capítulos, Epílogo).
7 finales: 5 románticos, 1 malo, 1 secreto (polígamo, desbloqueable).

Genera el archivo 00_definiciones.rpy con exactamente esto:

1. PERSONAJES con Character():
   - mc = Character("[nombre_jugador]") — protagonista dinámico sin sprite
   - Ichika  → color #FFB7C5
   - Nino    → color #C39BD3
   - Miku    → color #5DADE2
   - Yotsuba → color #58D68D
   - Itsuki  → color #EC7063
   - Narrador → sin nombre, color #D5D8DC

2. VARIABLES con default:
   - nombre_jugador = "Futaro"
   - puntos_ichika/nino/miku/yotsuba/itsuki = 0
   - primera_conexion = ""
   - primera_decision_hecha = False
   - persistent.ruta_X_completa = False (para las 5)
   - persistent.final_secreto_desbloqueado = False

3. LÓGICA DEL CÁLCULO SECRETO en comentarios (#):
   - Umbral mínimo 10 puntos para evitar Final Malo
   - Orden de comparación: ichika→nino→miku→yotsuba→itsuki
   - Desempate por primera_conexion, si vacío gana Ichika
   - Lógica de desbloqueo del final secreto con persistent

4. INPUT DE NOMBRE al inicio:
   - Screen que pregunta el nombre antes del prólogo
   - Default "Futaro", acepta nombre personalizado

Entrega solo código limpio listo para copiar.
Al final agrega en comentarios propuesta breve del inicio del Prólogo.
```

---

### ▶ FASE 1 — `01_prologo.rpy`

```
Actúa como desarrollador experto en Ren'Py y guionista de VN.
Continuamos con "The Fifth Choice" (fan VN de Quintessential Quintuplets).

El archivo 00_definiciones.rpy ya existe con todos los personajes,
variables de puntos y sistema de cálculo secreto.

Genera el archivo 01_prologo.rpy con:

CONTEXTO: El prólogo adapta el inicio del anime. Futaro recibe la
propuesta de su padre de trabajar como tutor. Conoce a las 5 hermanas
por primera vez en el hotel. Tono: presentación de personajes, algo
caótico y cómico como el anime.

ESTRUCTURA:
- label prologo: punto de entrada
- Presentación de cada hermana con su personalidad característica
- Al menos 2 decisiones simples que sumen puntos suavemente (máx 3 pts)
- Registrar primera_conexion y primera_decision_hecha
- Al final: jump cap1_inicio

REGLAS TÉCNICAS:
- El protagonista usa Character("[nombre_jugador]") ya definido
- Nunca mostrar sprite del protagonista
- Usar narrador para descripciones de escena
- Comentarios explicando cada bloque
- Código modular y limpio

Entrega solo el código listo para copiar.
```

---

### ▶ FASE 2 — `02_capitulo1.rpy`

```
Actúa como desarrollador experto en Ren'Py y guionista de VN.
Continuamos con "The Fifth Choice". Ya existen:
00_definiciones.rpy y 01_prologo.rpy

Genera el archivo 02_capitulo1.rpy con:

CONTEXTO: Primer capítulo como tutor. Eventos canónicos del anime
adaptados: primeras sesiones de estudio, momentos individuales con
cada hermana, tensión inicial que se va suavizando.

ESTRUCTURA:
- label cap1_inicio: punto de entrada
- 3 Main Events (escenas principales con todas)
- Al menos 4 decisiones que sumen puntos (máx 5 pts cada una)
- 1 escena individual con cada hermana (5 en total, según puntos acumulados)
- Al final: jump cap2_inicio

REGLAS TÉCNICAS:
- Mantener coherencia con personajes ya definidos
- Nunca mostrar sprite del protagonista
- Comentarios explicando la lógica de puntos en cada decisión
- Código modular

Entrega solo el código listo para copiar.
```

---

### ▶ FASE 3 — `03_capitulo2.rpy`

```
Actúa como desarrollador experto en Ren'Py y guionista de VN.
Continuamos con "The Fifth Choice". Ya existen:
00_definiciones.rpy, 01_prologo.rpy, 02_capitulo1.rpy

Genera el archivo 03_capitulo2.rpy con:

CONTEXTO: Las relaciones se profundizan. Eventos más personales e
íntimos con cada hermana. El jugador empieza a sentir hacia quién
se inclina. Tono más romántico y emotivo.

ESTRUCTURA:
- label cap2_inicio: punto de entrada
- 3 Main Events más dramáticos/emotivos
- Al menos 5 decisiones con mayor impacto (máx 8 pts cada una)
- Escenas 1 a 1 más íntimas con cada hermana
- Al final: jump cap3_inicio

REGLAS TÉCNICAS:
- Decisiones deben sentirse más importantes que el capítulo 1
- Nunca mostrar sprite del protagonista
- Comentarios explicando puntos

Entrega solo el código listo para copiar.
```

---

### ▶ FASE 4 — `04_capitulo3.rpy`

```
Actúa como desarrollador experto en Ren'Py y guionista de VN.
Continuamos con "The Fifth Choice". Ya existen los archivos anteriores.

Genera el archivo 04_capitulo3.rpy con:

CONTEXTO: Capítulo final antes del epílogo. El clímax emocional.
Decisiones de alto peso. Al final ejecuta el Cálculo Secreto.

ESTRUCTURA:
- label cap3_inicio: punto de entrada
- 2 Main Events de alto impacto dramático
- Al menos 4 decisiones cruciales (máx 12 pts cada una)
- label calculo_final: implementa la lógica completa del cálculo secreto
  * Verifica umbral mínimo (10 pts) → si no: jump final_malo
  * Determina ganadora con max() y diccionario de puntos
  * Aplica regla de desempate con primera_conexion
  * Verifica persistent para final secreto
  * Deriva al final correspondiente con jump

REGLAS TÉCNICAS:
- El calculo_final debe estar bien comentado línea a línea
- Nunca mostrar sprite del protagonista

Entrega solo el código listo para copiar.
```

---

### ▶ FASE 5 — `05_finales.rpy`

```
Actúa como desarrollador experto en Ren'Py y guionista de VN.
Continuamos con "The Fifth Choice". Ya existen todos los archivos anteriores.

Genera el archivo 05_finales.rpy con los 7 finales:

FINALES ROMÁNTICOS (uno por hermana):
- label final_ichika / final_nino / final_miku / final_yotsuba / final_itsuki
- Cada uno: escena emotiva de confesión + epílogo de boda breve
- Al terminar: persistent.ruta_X_completa = True
- Verificar si las 5 son True → persistent.final_secreto_desbloqueado = True

FINAL MALO:
- label final_malo
- Futaro es despedido, las hermanas lo rechazan, tono triste
- Sin activar ningún persistent

FINAL SECRETO:
- label final_secreto
- Solo accesible si persistent.final_secreto_desbloqueado = True
- Las 5 hermanas aparecen juntas, tono cómico/romántico
- Boda polígama, ending gracioso

REGLAS TÉCNICAS:
- Cada final debe tener su propia personalidad y tono
- Nunca mostrar sprite del protagonista
- Al final de cada label: return

Entrega solo el código listo para copiar.
```

---

## 🎨 ASSETS PENDIENTES

### Sprites de personajes (escenas)
Generar en Leonardo.ai / Stable Diffusion:
- Cada chica en poses: normal, feliz, sorprendida, molesta, sonrojada
- Fondo transparente, estilo anime, 800x1400px
- Formato: .webp

### Fondos de escena (backgrounds)
```
- Salón de clases (día / noche)
- Habitación hotel (primera escena)
- Apartamento Nakano (sala, comedor)
- Parque / exterior
- Pasillo escuela
```
Generar con IA, 1280x720px, estilo anime, sin personajes.

### Silueta del protagonista
- Asset de sombra/silueta para escenas donde debe "aparecer"
- Figura masculina en negro semitransparente
- Mismas dimensiones que sprites de chicas

---

## 🛠️ HERRAMIENTAS USADAS

| Para qué | Herramienta |
|----------|------------|
| Motor del juego | Ren'Py 8.5.3 |
| Sprites / Fondos | Leonardo.ai / Stable Diffusion |
| Música | Suno.ai → exportar .ogg |
| Voces (opcional) | ElevenLabs |
| Edición imágenes | GIMP / Photoshop / Canva |
| Conversión audio | Audacity / CloudConvert |
| IA para código | Claude (claude.ai) |

---

## 📌 NOTAS IMPORTANTES

1. El juego es un **fan project gratuito** — no monetizar jamás
2. Trabajar **un archivo .rpy por sesión** en Claude
3. Cada prompt nuevo mencionar qué archivos ya existen
4. Testear en Ren'Py después de cada fase antes de continuar
5. Si hay error, copiar el `traceback` y pasárselo a Claude

---

## ✅ PROGRESO

- [x] Menú principal (`06_main_menu.rpy`)
- [ ] Definiciones del sistema (`00_definiciones.rpy`)
- [ ] Prólogo (`01_prologo.rpy`)
- [ ] Capítulo 1 (`02_capitulo1.rpy`)
- [ ] Capítulo 2 (`03_capitulo2.rpy`)
- [ ] Capítulo 3 + Cálculo (`04_capitulo3.rpy`)
- [ ] Los 7 finales (`05_finales.rpy`)

