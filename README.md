# Define-Challenge-Build (DCB)

> Metodología de planificación que separa el diseño (el Qué) de su implementación (el Cómo). Ambos pasan por un cuestionamiento crítico obligatorio antes de avanzar a la siguiente fase.

---

## 1. Qué es

DCB tiene un solo núcleo: ningún artefacto —ni la definición del proyecto ni su plan de implementación— avanza a construcción sin haber sido auditado críticamente primero.

El Challenge se puede ejecutar de tres formas:
- **Solo expertos humanos.**
- **Solo IA.**
- **Expertos humanos + IA**, combinados. Esta es la forma recomendada: la IA aporta información, precedentes o riesgos que un experto no siempre tiene presentes en el momento, y el experto aporta el criterio para filtrar qué tan aplicable es eso al proyecto real.

```
[Requerimientos] → [Define: "Qué"] → [Challenge #1] → [Definición Consolidada]
      → [Define: "Cómo" / Roadmap] → [Challenge #2] → [Build]
```

## 2. Qué NO es

DCB no es una metodología de ejecución. No compite con Scrum, Kanban ni Waterfall, y no dice cómo organizar sprints ni gestionar un equipo. Actúa antes de eso: define cómo se valida un plan, no cómo se ejecuta.

Es similar al Spec-Driven Development (SDD): ambos separan especificación de implementación. La diferencia es que en DCB el Challenge es un paso obligatorio, no una revisión opcional, y se aplica dos veces: sobre la Definición y sobre el Roadmap.

## 3. Objetivos

- Que un plan mal definido o ambiguo no llegue a construcción sin ser detectado.
- Reducir el riesgo de construir sobre supuestos sin verificar.
- Separar qué se construye de cómo se construye, para que un cambio técnico no obligue a redefinir el objetivo del proyecto.

Cuando el contenido de la Definición o el Roadmap lo genera una IA, el Challenge actúa como control directo contra sus fallos típicos: alucinación, exceso de confianza, avance sobre supuestos sin verificar.

## 4. Principio central: desacoplamiento de componentes

DCB separa la meta del proyecto de su ejecución en dos artefactos independientes:

| Artefacto | Responde a | Naturaleza |
|---|---|---|
| **Archivo de Definición** | El Qué | Estático — objetivos, reglas de negocio, alcance y restricciones |
| **Roadmap** | El Cómo | Dinámico y versionado — ruta técnica de implementación |

Si el Roadmap cambia, la Definición se mantiene intacta.

## 5. El flujo de trabajo

### 5.1 Define
Se extraen los requerimientos y se redacta una primera propuesta del Archivo de Definición. La misma etapa se repite después para generar el Roadmap, una vez que la Definición está consolidada.

### 5.2 Challenge
El artefacto recién generado —Definición o Roadmap— se audita antes de aceptarse, con expertos, IA, o ambos combinados (ver §1).

Se aplica dos veces:

1. **Sobre la Definición** — verifica que el "Qué" esté completo y sin ambigüedades.
2. **Sobre el Roadmap** — verifica que el "Cómo" sea coherente con la Definición aprobada y técnicamente viable.

Un artefacto se considera consolidado cuando supera su Challenge correspondiente.

### 5.3 Build
Con la Definición blindada y el Roadmap validado, se construye. Si surge un imprevisto que afecta al Roadmap, se versiona y vuelve a pasar por Challenge, sin tocar la Definición. Si el imprevisto revela que el "Qué" original era inviable, se vuelve a Define.

## 6. Cuándo usarla

- Vas a usar IA para diseñar o planear un sistema, no solo para generar código puntual.
- El proyecto tiene requerimientos ambiguos o cambiantes.
- Trabajás solo y necesitás un mecanismo externo de verificación.
- Construir sobre un diseño equivocado te sale caro.

## 7. Cuándo no usarla

- Tareas puntuales o acotadas: una función suelta, un snippet, un fix menor.
- Prototipos rápidos donde el objetivo es explorar, no blindar un diseño.
- Proyectos donde el "Qué" ya está completamente claro.

## 8. Pros y riesgos

**Pros**
- Reduce el riesgo de construir sobre alucinaciones o supuestos sin verificar.
- El Roadmap cambia sin comprometer el objetivo del proyecto.
- Da trazabilidad: cada Roadmap referencia qué parte de la Definición implementa.

**Riesgos**
- Si quien ejecuta el Challenge no tiene autoridad real para bloquear el artefacto, se vuelve un trámite sin fricción real.
- Un artefacto "consolidado tras Challenge" puede dar falsa sensación de seguridad durante el Build.
- Requiere disciplina para no saltarse el Challenge bajo presión de tiempo.

## 9. Artefactos de la metodología

### 9.1 Archivo de Definición (el Qué)
Documento maestro y estático. Objetivos, reglas de negocio, alcance y restricciones del sistema. No se modifica tras consolidarse, salvo inviabilidad estructural.

### 9.2 Roadmap (el Cómo)
Documentos dinámicos y versionados que trazan la ruta técnica de implementación, referenciando siempre a la Definición aprobada.

### 9.3 Prompts de Challenge
Instrucciones para auditar la Definición y el Roadmap. Este repositorio no incluye prompts de ejemplo: escribilos vos mismo, según los riesgos reales de tu proyecto.

## 10. Cómo separar la Definición de los Roadmaps

- **Un único Archivo de Definición por proyecto**, en la raíz del repositorio. No se fragmenta por módulo ni por sprint.
- **Un Roadmap por unidad de entrega** (módulo, feature, milestone técnico), no uno monolítico.
- **Cada Roadmap referencia qué secciones de la Definición implementa** (ej. "Implementa Definición §3.2 y §4.1").
- **La Definición no lleva detalles de implementación** — stack, librerías, endpoints, esquemas de base de datos.
- **El Roadmap no redefine objetivos de negocio.** Si al construirlo aparece que la Definición es ambigua o inviable, se vuelve a Define.
- **Versionado independiente.** Definición: v1, v2, v3 (cada una pasa por Challenge). Roadmaps: v1.1, v1.2... (absorben imprevistos del Build sin tocar la Definición).

## 11. Estructura de proyecto recomendada

```
mi-proyecto/
├── DEFINITION.md                 # El Qué — único, estático, fuente de verdad
├── CHALLENGE_LOG.md               # Historial de Challenges sobre la Definición
│
├── roadmaps/
│   ├── roadmap-auth/
│   │   ├── v1.md
│   │   ├── v1.1.md
│   │   └── challenge-log.md
│   ├── roadmap-pagos/
│   │   ├── v1.md
│   │   └── challenge-log.md
│   └── roadmap-notificaciones/
│       ├── v1.md
│       └── challenge-log.md
│
├── prompts/
│   └── challenge/
│       └── ...                    # Prompts escritos por el equipo (ver §9.3)
│
└── src/                            # Código construido a partir de los roadmaps consolidados
```

La Definición aislada en la raíz se encuentra sin revisar código ni roadmaps. Cada carpeta en `roadmaps/` es autocontenida: tiene su propio historial de versiones y su propio log de Challenge. Los `challenge-log.md` registran quién cuestionó qué y cómo se resolvió.

## 12. Roadmaps como Spec-Driven Development hiperespecífico

Un Roadmap dentro de DCB ya pasó por Define, ya fue cuestionado en Challenge, y ya está atado a una Definición aprobada. Al llegar al Build no queda ambigüedad de negocio ni de diseño pendiente — solo ejecución.

Para equipos que usan agentes de codificación (Claude Code u otros), esto significa que un Roadmap consolidado se le puede entregar directamente al agente como spec de trabajo:

- Las decisiones de arquitectura y alcance ya se cerraron en Define + Challenge, no se toman durante el Build.
- El agente no infiere intención de negocio — vive en la Definición referenciada.
- Cada paso del Roadmap es una tarea atómica y verificable.
- Si el agente encuentra una inconsistencia, el protocolo ya existe: re-versionar el Roadmap, o volver a Define si el problema es de fondo.

## 13. DCB y Vertical Slice Architecture

DCB combina bien con Vertical Slice Architecture (VSA): organizar el sistema por feature de punta a punta en vez de por capa técnica horizontal.

Una feature de VSA es un Roadmap de DCB. Ambos referencian la misma Definición central.

Aplicar DCB por feature trae:

- **Challenge más acotado.** Auditar una sola feature es más rápido que auditar todo el sistema junto.
- **Paralelización real.** Distintas features pueden estar en distintas etapas de DCB al mismo tiempo.
- **Cambios contenidos.** Re-versionar el Roadmap de una feature no afecta al resto.
- **Trazabilidad feature por feature.**

## 14. Ejemplo de uso

Proyecto: una plataforma de reservas de canchas deportivas para un club.

**Paso 1 — Define (Definición).**
Se recogen los requerimientos del cliente (reglas de reserva, roles de usuario, cancelaciones, restricciones legales) y se redacta la primera versión de `DEFINITION.md`.

**Paso 2 — Challenge sobre la Definición.**
El equipo (expertos + IA) audita el borrador:
- Falta especificar qué pasa si dos usuarios reservan la misma cancha en el mismo instante.
- Falta definir el manejo de cancelaciones por lluvia en canchas al aire libre.

Se registra en `CHALLENGE_LOG.md`, se corrige, se repite hasta no tener objeciones abiertas. La Definición queda consolidada como v1.

**Paso 3 — Define (Roadmap).**
Se genera `roadmaps/roadmap-reservas/v1.md`, que referencia "Implementa Definición §3 y §4" y detalla el uso de bloqueos a nivel de base de datos para resolver la condición de carrera.

**Paso 4 — Challenge sobre el Roadmap.**
Se objeta que el mecanismo de bloqueo propuesto no escala bien con múltiples canchas concurrentes. Se ajusta a v1.1 y se vuelve a auditar.

**Paso 5 — Build.**
El Roadmap v1.1 se entrega directamente a un agente de codificación como spec de ejecución. Durante el Build aparece un imprevisto (la librería elegida no soporta el motor de base de datos del cliente): se re-versiona a v1.2, documentado en `challenge-log.md`, sin tocar `DEFINITION.md`.
