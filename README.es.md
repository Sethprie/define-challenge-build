# Define-Challenge-Build (DCB)

> Metodología de planificación que separa el diseño (el Qué) de su implementación (el Cómo). Ambos pasan por un cuestionamiento crítico obligatorio antes de avanzar a la siguiente fase.

---

## 1. Qué es

Define-Challenge-Build (DCB) es una metodología de planificación de proyectos de software. Separa la definición de un proyecto (el Qué) de su plan de implementación (el Cómo), y exige que cada uno pase por una auditoría crítica —el Challenge— antes de avanzar a la siguiente fase.

Su núcleo es ese Challenge: ningún artefacto, ni la Definición ni el Roadmap, avanza a construcción sin haber sido cuestionado primero.

El Challenge puede ejecutarse de tres formas:

* **Solo expertos humanos.**
* **Solo IA.**
* **Expertos humanos + IA**, combinados. Esta es la forma recomendada: la IA aporta información, precedentes o riesgos que un experto no siempre tiene presentes en el momento, y el experto aporta el criterio para filtrar qué tan aplicable es eso al proyecto real.

```
[Requerimientos] → [Define: "Qué"] → [Challenge #1] → [Definición Consolidada]
      → [Define: "Cómo" / Roadmap] → [Challenge #2] → [Build]

```

## 2. Qué NO es

DCB no es una metodología de ejecución. No compite con Scrum, Kanban ni Waterfall, y no dice cómo organizar sprints ni gestionar un equipo. Actúa antes de eso: define cómo se valida un plan, no cómo se ejecuta.

Es similar al Spec-Driven Development (SDD): ambos separan especificación de implementación. La diferencia es que en DCB el Challenge es un paso obligatorio, no una revisión opcional, y se aplica dos veces: sobre la Definición y sobre el Roadmap.

## 3. Objetivos

* Que un plan mal definido o ambiguo no llegue a construcción sin ser detectado.
* Reducir el riesgo de construir sobre supuestos sin verificar.
* Separar qué se construye de cómo se construye, para que un cambio técnico no obligue a redefinir el objetivo del proyecto.

Cuando el contenido de la Definición o el Roadmap lo genera una IA, el Challenge funciona como control directo contra sus fallos típicos: alucinación, exceso de confianza y avance sobre supuestos sin verificar.

## 4. Principio central: desacoplamiento de componentes

DCB separa la meta del proyecto de su ejecución en dos artefactos independientes:

| Artefacto | Responde a | Naturaleza |
| --- | --- | --- |
| **Archivo de Definición** | El Qué | Estático — objetivos, reglas de negocio, alcance y restricciones |
| **Roadmap** | El Cómo | Dinámico y versionado con git — ruta técnica de implementación |

Si el Roadmap cambia, la Definición se mantiene intacta.

## 5. El flujo de trabajo

### 5.1 Define

Se extraen los requerimientos y se redacta una primera propuesta del Archivo de Definición. Una vez que la Definición queda consolidada, esta misma etapa se repite para generar el Roadmap.

### 5.2 Challenge

El artefacto recién generado —Definición o Roadmap— se audita antes de aceptarse, con expertos, IA, o ambos combinados (ver sección 1).

Se aplica dos veces:

1. **Sobre la Definición** — verifica que el "Qué" esté completo y sin ambigüedades.
2. **Sobre el Roadmap** — verifica que el "Cómo" sea coherente con la Definición aprobada y técnicamente viable.

Un artefacto se considera consolidado cuando supera su Challenge correspondiente.

### 5.3 Build

Con la Definición blindada y el Roadmap validado, se construye. Si surge un imprevisto que afecta al Roadmap, se corrige el archivo y vuelve a pasar por Challenge, sin tocar la Definición. Si el imprevisto revela que el "Qué" original era inviable, se vuelve a Define.

## 6. Cuándo usarla

* Vas a usar IA para diseñar o planear un sistema, no solo para generar código puntual.
* El proyecto tiene requerimientos ambiguos o cambiantes.
* Trabajas solo y necesitas un mecanismo externo de verificación.
* Construir sobre un diseño equivocado te sale caro.

## 7. Cuándo no usarla

* Tareas puntuales o acotadas: una función suelta, un snippet, un fix menor.
* Prototipos rápidos donde el objetivo es explorar, no blindar un diseño.
* Proyectos donde el "Qué" ya está completamente claro.

## 8. Pros y riesgos

**Pros**

* Reduce el riesgo de construir sobre alucinaciones o supuestos sin verificar.
* El Roadmap cambia sin comprometer el objetivo del proyecto.
* Da trazabilidad: cada Roadmap referencia qué parte de la Definición implementa.

**Riesgos**

* Si quien ejecuta el Challenge no tiene autoridad real para bloquear el artefacto, se vuelve un trámite sin fricción real.
* Un artefacto "consolidado tras Challenge" puede dar una falsa sensación de seguridad durante el Build.
* Requiere disciplina para no saltarse el Challenge bajo presión de tiempo.

## 9. Artefactos de la metodología

### 9.1 Archivo de Definición (el Qué)

Documento maestro y estático: objetivos, reglas de negocio, alcance y restricciones del sistema. No se modifica tras consolidarse, salvo inviabilidad estructural.

### 9.2 Roadmap (el Cómo)

Documento dinámico que traza la ruta técnica de implementación, sin depender de referencias a un archivo concreto de Definición.

Cada Roadmap vive en un único archivo, y su nombre debe ser descriptivo — nunca genérico como `roadmap.md`, porque una misma feature puede terminar con varios roadmaps. Convención recomendada:

* `roadmap-<feature>.md` cuando la entrega se resuelve en un solo roadmap.
* `roadmap-<feature>-<slice>.md` cuando la feature se divide en varios — por capa técnica (`roadmap-auth-backend.md`, `roadmap-auth-frontend.md`) o por sub-entrega.

El historial de cambios se sigue con git (commits), no duplicando el archivo por versión. La excepción es cuando el proyecto no usa ningún sistema de control de versiones: en ese caso sí conviene agregar además un sufijo v1, v2, v3, etc., para distinguir versiones.

*Estructura recomendada del archivo de Roadmap:*

Cada Roadmap es autocontenido y debe estructurarse internamente con:

* **Definición:** una breve descripción inicial del problema específico que resuelve ese roadmap y qué parte de la Definición aprobada cubre, sin nombrar archivos ni anclarlo a un documento externo.
* **Fases y Tareas Atómicas:** desglose paso a paso (ej. Backend, Frontend) organizado con casillas de verificación (`- [ ]`) para el seguimiento del Build.

### 9.3 Prompts de Challenge

Instrucciones para auditar la Definición y el Roadmap. Este repositorio no incluye prompts de ejemplo: deben redactarse según los riesgos reales de cada proyecto.

## 10. Cómo separar la Definición de los Roadmaps

* **Un único Archivo de Definición por proyecto**, en la raíz del repositorio. No se fragmenta por módulo ni por sprint.
* **Una o más Roadmaps por unidad de entrega** (módulo, feature, milestone técnico). Una feature puede resolverse con un único roadmap vertical, o dividirse en varios — por capa técnica (backend, frontend) o por sub-entrega — según convenga; lo que nunca se hace es un roadmap monolítico que cubra todo el sistema.
* **Cada Roadmap es autocontenido** y describe la entrega que implementa sin depender de referencias a otros artefactos.
* **Nombre de archivo descriptivo.** Cada roadmap se nombra según la convención de la sección 9.2 (`roadmap-<feature>.md` o `roadmap-<feature>-<slice>.md`), nunca de forma genérica.
* **La Definición no lleva detalles de implementación** — stack, librerías, endpoints, esquemas de base de datos.
* **El Roadmap no redefine objetivos de negocio.** Si al construirlo aparece que la Definición es ambigua o inviable, se vuelve a Define.
* **Versionado con git.** Definición y Roadmaps son archivos únicos; cada cambio se registra como un commit, y ese historial es el que muestra la evolución del artefacto. Solo si el proyecto no usa git u otro control de versiones tiene sentido nombrar archivos como v1, v2, v3.

## 11. Estructura de proyecto recomendada

```
mi-proyecto/
├── definition.md                  # El Qué — único, estático, fuente de verdad
├── CHALLENGE_LOG.md               # Historial de Challenges sobre la Definición
│
├── roadmaps/
│   ├── roadmap-auth/
│   │   ├── roadmap-auth-backend.md
│   │   ├── roadmap-auth-frontend.md
│   │   └── challenge-log.md
│   ├── roadmap-pagos/
│   │   ├── roadmap-pagos.md
│   │   └── challenge-log.md
│   └── roadmap-notificaciones/
│       ├── roadmap-notificaciones.md
│       └── challenge-log.md
│
├── prompts/
│   └── challenge/
│       └── ...                    # Prompts escritos por el equipo (ver sección 9.3)
│
└── src/                            # Código construido a partir de los roadmaps consolidados

```

La Definición vive aislada en la raíz, así se puede consultar sin revisar código ni roadmaps. Cada carpeta en `roadmaps/` es autocontenida: agrupa los roadmaps de una misma feature —uno solo o varios, según si conviene dividirla— junto con un log de Challenge compartido. Los cambios sobre cada archivo de roadmap a lo largo del tiempo se siguen con git, no con archivos duplicados. El `challenge-log.md` registra quién cuestionó qué roadmap y cómo se resolvió.

## 12. Roadmaps como Spec-Driven Development hiperespecífico

Un Roadmap dentro de DCB ya pasó por Define, ya fue cuestionado en Challenge, y ya está atado a una Definición aprobada. Al llegar al Build no queda ambigüedad de negocio ni de diseño pendiente — solo ejecución.

Para equipos que usan agentes de codificación (Claude Code u otros), esto significa que un Roadmap consolidado se le puede entregar directamente al agente como spec de trabajo:

* Las decisiones de arquitectura y alcance ya se cerraron en Define + Challenge, no se toman durante el Build.
* El agente no infiere intención de negocio — esa intención vive en la Definición referenciada.
* Cada paso del Roadmap es una tarea atómica y verificable.
* Si el agente encuentra una inconsistencia, el protocolo ya existe: corregir el Roadmap (dejándolo registrado en git), o volver a Define si el problema es de fondo.

## 13. DCB y Vertical Slice Architecture

DCB combina bien con Vertical Slice Architecture (VSA): organizar el sistema por feature de punta a punta en vez de por capa técnica horizontal.

Una feature de VSA se traduce en uno o más Roadmaps de DCB, todos referenciando la misma Definición central. Dividir una feature en varios roadmaps —por ejemplo, separando backend y frontend dentro de la misma carpeta— no rompe el principio de VSA: la feature sigue siendo la unidad de entrega y de Challenge, solo que su Cómo queda repartido en piezas más pequeñas y fáciles de auditar por separado.

Aplicar DCB por feature trae:

* **Challenge más acotado.** Auditar una sola feature es más rápido que auditar todo el sistema junto.
* **Paralelización real.** Distintas features pueden estar en distintas etapas de DCB al mismo tiempo.
* **Cambios contenidos.** Corregir el Roadmap de una feature no afecta al resto.
* **Trazabilidad feature por feature.**

## 14. Ejemplo de uso

Proyecto: una plataforma de reservas de canchas deportivas para un club.

**Paso 1 — Define (Definición).**
Se recogen los requerimientos del cliente (reglas de reserva, roles de usuario, cancelaciones, restricciones legales) y se redacta la primera versión de la Definición.

**Paso 2 — Challenge sobre la Definición.**
El equipo (expertos + IA) audita el borrador y detecta vacíos:

* Falta especificar qué pasa si dos usuarios reservan la misma cancha en el mismo instante.
* Falta definir el manejo de cancelaciones por lluvia en canchas al aire libre.

Se registra en `CHALLENGE_LOG.md`, se corrige, y se repite hasta no tener objeciones abiertas. La Definición queda consolidada.

**Paso 3 — Define (Roadmap con definición y tareas).**
Se genera `roadmaps/roadmap-reservas/roadmap-reservas.md`:

```markdown
# Roadmap: Reservas de Canchas
## 1. Definición
- **Qué resuelve:** Implementa la lógica de bloqueo y registro de turnos referenciando la Definición, sección 3.
- **Alcance:** Excluye pagos online por ahora; solo reserva operativa interna.

## 2. Fases y Tareas
### Fase 1: Backend (.NET)
- [ ] Crear endpoint de reserva asegurando bloqueo de concurrencia.
### Fase 2: Frontend (Next.js)
- [ ] Construir vista de calendario y botón de confirmación.

```

> Los roadmaps deben ser siempre deterministas: nada de "por confirmar" ni de cosas que se pretenda agregar más adelante, para eso está el Challenge. Tampoco pueden contener referencias a otros roadmaps ni a la Definición. Los cambios posteriores sobre el mismo archivo son exclusivos para correcciones, no para agregar contenido nuevo; ese historial queda en git. Si se quiere ampliar el feature de un roadmap ya completado, se hace un roadmap aparte.
>
> El roadmap es para decisiones de diseño y contrato del sistema, no un log de cada ajuste fino hecho sobre la marcha.

**Paso 4 — Challenge sobre el Roadmap.**
Se objeta que el mecanismo de bloqueo propuesto no escala bien con múltiples canchas concurrentes. Se corrige `roadmap-reservas.md` y se vuelve a auditar; el cambio queda documentado en `challenge-log.md` y registrado como commit en git.

**Paso 5 — Build.**
El Roadmap consolidado se entrega directamente a un agente de codificación como spec de ejecución. Durante el Build aparece un imprevisto (la librería elegida no soporta el motor de base de datos del cliente): se corrige `roadmap-reservas.md`, se documenta el motivo en `challenge-log.md`, y el cambio queda versionado en git, sin tocar la Definición.