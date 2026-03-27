# Registro de Cambios

Los cambios del archivo se registran aquí para referencia del DM.

---

## 2026-03-27

### Archivo de Imágenes Integrado

Se procesó el correo electrónico "all dm images". Todas las imágenes fueron extraídas de los archivos .eml, nombradas y archivadas en el repositorio.

**Nueva estructura del directorio `images/`:**

| Carpeta | Contenido |
|---|---|
| `images/npcs/` | Alton, Commander Swan arm glyph, Grell, Jefferson Thomas (×2), Linus Larabee, Nemmerle, Raynor, Rusty, Simon, Walter (original) |
| `images/locations/` | Castleton, Croaking Fane, Linea Rubra (×2), Lockleed river gate, Nemmex Desert, Overlook Manor, Sloop Jon B, Stella Solis Snake Temple (×5), Tower of High Wizardry (×2), Walter's Kingdom (×6) |
| `images/creatures/` | Lil Sebastian, Lizardfolk, Rat vs Lizardman, Ratter, Ratter 2 |
| `images/events/` | Acolyte's Last Meal (The Keep), Cult behind Keep (×6), Massacre at Druid Enclave, Orcs at Threshold, Trouble with Trolls |
| `images/items/` | Taelendra's Leg, Valen's Bow |
| `images/maps/` | Hexcral (battle map) |
| `images/keep-on-borderlands/` | 12 fotos del módulo del Keep |

**Nuevos archivos creados a partir del contexto de las imágenes:**

*Ubicaciones:*
- `locations/croaking-fane.md` — templo con boca de rana; identificado como el sitio del módulo 2
- `locations/linea-rubra.md` — distrito ribereño en el Kingdom of the Rat
- `locations/nemmex-desert.md` — desierto con ruinas antiguas; donde Valen encontró el amuleto de araña
- `locations/stella-solis.md` — asentamiento en la región de Texas; bandera de Texas; administrado por Jefferson Thomas
- `locations/walters-kingdom.md` — el Kingdom of the Rat físico; identificado como un parque de atracciones pre-Reckoning inundado (carrusel, montaña rusa, estatua del fundador con figura de ratón)
- `maps/hexcral.md` — esquema del mapa de batalla Hexcral (mapa de terreno con rejilla hexagonal redonda)

*PNJs:*
- `npcs/jefferson-thomas.md` — Ranger de Tayhas; administra Stella Solis; conocido por Alton y Raynor
- `npcs/lil-sebastian.md` — guerrero rata acorazado; probablemente del Kingdom of the Rat
- `npcs/rusty.md` — alguacil de Swan en Threshold
- `npcs/simon-magistrate.md` — hermano de Linus Larabee; magistrado

**Archivos existentes actualizados** con referencias de imágenes: Alton, Commander Swan, Grell Hammerhand, King Walter, Linus Larabee, Nemmerle, Raynor, Taelendra, Valen, Castleton, Lockleed.

**Otras correcciones detectadas durante la integración:**
- "Krocking Fane" corregido a "Croaking Fane" en `campaign.md`
- Rusty añadido a los PNJs conocidos de `threshold.md`
- Referencias cruzadas añadidas entre los archivos de Stella Solis, Jefferson Thomas y Raynor
- `README.md` actualizado con `images/` y `maps/` en la estructura del repositorio

---

## 2026-03-13 — Archivo Inicializado

Archivo inicial creado. Contenido al momento de la creación:

- `campaign.md` — resumen, misión, grupo, hilos abiertos
- `sessions/session-001.md` — registro de la sesión 1 (con correcciones de las notas de entrega de Matt)
- `npcs/` — Alton, Commander Swan, Derek the Lesser, Dwarves (Castleton), Grell Hammerhand, King Walter, Linus Larabee, Nemmerle, Radamanthus, Raynor, Sangchris, Taelendra, Valen
- `locations/` — Castleton, Kingdom of the Rat, Lockleed, Regions, Threshold
- `items/` — Moongate, Staff of Healing
- `lore/` — archivos de lore del mundo
- `rules/` — archivos de referencia OSE
- `party/` — archivos de personajes

Se documentó el contexto del escenario en la Tierra post-Reckoning y los orígenes de LVNV y el tabardo. Se corrigió la confusión entre Swan y Taelendra (son personajes separados). Se registró que la gema de ónix del Moongate está desaparecida.
