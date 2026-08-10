# Define-Challenge-Build (DCB)

> Metodología de planificación que separa el diseño (el Qué) de su implementación (el Cómo), y obliga a que ambos pasen por un proceso de cuestionamiento crítico antes de avanzar a la siguiente fase.

---

## 1. Qué es

**Define-Challenge-Build (DCB)** es una metodología de planificación cuyo núcleo es el **cuestionamiento estructurado**: ningún artefacto (ni la definición del proyecto, ni su plan de implementación) avanza a la siguiente fase sin haber sido sometido a una auditoría crítica que verifique que está bien planteado.

DCB es **agnóstica respecto a quién ejecuta cada rol**. Tanto el Define como el Challenge pueden ser llevados a cabo por personas humanas, por LLMs, o por una combinación de ambos — la metodología no depende de ninguna tecnología en particular para funcionar. De hecho, la combinación de ambos puede resultar en un Challenge superior a cualquiera de los dos por separado: la IA puede traer a la mesa información, precedentes o ángulos de riesgo que el humano no necesariamente conoce o tiene presentes en el momento, mientras que el humano aporta el juicio para decidir qué tan aplicable es esa información al contexto específico del proyecto. Ninguna de las tres combinaciones —solo humano, solo IA, o ambos— es la única forma "correcta" de ejecutar un Challenge; depende de qué recursos tenga disponibles cada equipo.

```
[Requerimientos] → [Define: "Qué"] → [Challenge #1] → [Definición Consolidada]
      → [Define: "Cómo" / Roadmap] → [Challenge #2] → [Build]
```

## 2. Qué NO es

DCB no es una metodología de ejecución y no compite con Scrum, Kanban o Waterfall. No dice cómo organizar sprints ni cómo gestionar un equipo — actúa **antes** de todo eso, estructurando cómo se define y valida un plan. Puedes definir tu proyecto con DCB y ejecutarlo después con la metodología de trabajo que prefieras.

El sistema más parecido a DCB es **Spec-Driven Development (SDD)**: ambos separan la especificación de la implementación. La diferencia es que DCB convierte el cuestionamiento en un paso **obligatorio y estructurado**, no una revisión opcional, y lo aplica dos veces: una sobre la Definición, otra sobre el Roadmap.

## 3. Objetivos

- Evitar que un plan mal definido o ambiguo avance a la fase de construcción sin ser detectado.
- Reducir el riesgo de construir sobre supuestos no verificados, sea quien sea (persona o IA) quien los generó.
- Separar claramente qué se está construyendo de cómo se va a construir, para que los cambios técnicos no obliguen a redefinir el objetivo del proyecto.

Aunque DCB es agnóstica en cuanto a *quién ejecuta* el Challenge, tiene un caso de uso particularmente fuerte cuando el contenido de la Definición o del Roadmap es *generado* por IA: el Challenge actúa como antídoto directo a los fallos característicos de un LLM —alucinación, exceso de confianza, y avance sobre supuestos no verificados— antes de que ese contenido llegue a la fase de Build.

## 4. Principio central: Desacoplamiento de Componentes

DCB prohíbe mezclar la meta del proyecto con su ejecución. Todo se divide en dos artefactos independientes:

| Artefacto | Pregunta que responde | Naturaleza |
|---|---|---|
| **Archivo de Definición** | El **Qué** | Estático — objetivos, reglas de negocio, alcance y restricciones del sistema |
| **Roadmap** | El **Cómo** | Dinámico y versionado — ruta técnica de implementación |

**¿Por qué separar?** Porque la tecnología, los tiempos y los imprevistos cambian constantemente durante el desarrollo, pero el objetivo del proyecto no debería cambiar solo porque cambió una decisión técnica. Si el Roadmap necesita mutar, la Definición permanece intacta.

## 5. El Flujo de Trabajo

DCB se ejecuta en tres etapas, cada una con su propio mecanismo de control:

### 5.1 Define
Se extraen los requerimientos del proyecto y se redacta una primera propuesta del **Archivo de Definición**. Esta etapa se repite después para generar el **Roadmap**, pero solo una vez que la Definición ha sido consolidada.

### 5.2 Challenge
El corazón de la metodología. El artefacto recién generado (Definición o Roadmap) es sometido a una auditoría crítica antes de ser aceptado, ejecutada por personas expertas, por LLMs con roles específicos (seguridad, escalabilidad, base de datos, negocio, etc.), o ambos.

El Challenge se aplica **dos veces**:

1. **Sobre la Definición**: verifica que el "Qué" sea correcto, completo y libre de ambigüedades antes de diseñar ninguna solución técnica sobre él.
2. **Sobre el Roadmap**: verifica que el "Cómo" sea coherente con la Definición ya aprobada y técnicamente viable, antes de liberarlo para su ejecución.

Solo tras superar el Challenge correspondiente, un artefacto se considera consolidado.

### 5.3 Build
Con la Definición blindada y el Roadmap validado, se ejecuta la implementación. Si surgen imprevistos que afectan al Roadmap, este puede versionarse y volver a pasar por un nuevo Challenge — sin tocar la Definición, salvo que el imprevisto revele que el "Qué" original era inviable, en cuyo caso el proceso retorna explícitamente a la fase de Define.

## 6. Cuándo usarla

- Vas a usar una IA (u otro equipo) para diseñar o planear un sistema, no solo para generar código puntual.
- El proyecto tiene requerimientos ambiguos o cambiantes.
- Trabajas solo y necesitas un mecanismo externo de verificación porque no tienes con quién contrastar decisiones.
- El costo de construir sobre un diseño equivocado es alto.

## 7. Cuándo NO usarla

- Tareas puntuales o acotadas (una función suelta, un snippet, un fix menor).
- Prototipos rápidos o experimentos donde el objetivo es explorar, no blindar un diseño.
- Proyectos donde el "Qué" es trivial o ya está completamente claro.

## 8. Pros y riesgos

**Pros**
- Reduce el riesgo de construir sobre alucinaciones o supuestos no verificados.
- El Roadmap puede cambiar sin comprometer el objetivo del proyecto.
- Da trazabilidad: cada Roadmap referencia qué parte de la Definición está implementando.

**Riesgos**
- **El Challenge se puede volver teatro.** Si quien lo ejecuta —humano o IA— no tiene autoridad real para bloquear el artefacto, el proceso se convierte en un trámite que se aprueba sin fricción real, y la metodología pierde su propósito por completo.
- **Falsa sensación de seguridad.** Un artefacto "consolidado tras Challenge" puede hacer que el equipo baje la guardia durante el Build, cuando en realidad el Challenge solo redujo el riesgo, no lo eliminó.
- **Costo de disciplina.** Requiere que el equipo resista la tentación de saltarse el Challenge cuando hay presión de tiempo — precisamente cuando más falta hace.

## 9. Artefactos de la Metodología

### 9.1 Archivo de Definición (El Qué)
Documento maestro y estático. Detalla de forma conceptual los objetivos, reglas de negocio, alcance y restricciones del sistema. Una vez consolidado tras el Challenge, no debería modificarse salvo que se descubra una inviabilidad estructural.

### 9.2 Roadmap (El Cómo)
Uno o varios documentos dinámicos y versionados que trazan la ruta técnica de implementación, siempre bajo referencia directa a la Definición aprobada.

### 9.3 Prompts de Challenge
Instrucciones especializadas por rol (seguridad, escalabilidad, base de datos, negocio, etc.) usadas para auditar la Definición y el Roadmap. *(En desarrollo — próxima incorporación al repositorio.)*

## 10. Cómo separar la Definición de los Roadmaps

La separación no es solo conceptual, debe ser física. Reglas prácticas:

- **Un único Archivo de Definición por proyecto.** Vive en la raíz del repositorio y es la fuente de verdad del "Qué". No se fragmenta por módulo ni por sprint.
- **Un Roadmap por unidad de entrega**, no un Roadmap monolítico para todo el proyecto. Una unidad de entrega puede ser un módulo, una feature grande, o un milestone técnico (ej. `roadmap-auth.md`, `roadmap-pagos.md`). Esto permite auditar, versionar y ejecutar cada Roadmap de forma independiente, sin bloquear al resto del proyecto si uno cambia.
- **Cada Roadmap referencia explícitamente las secciones de la Definición que implementa** (ej. "Implementa Definición §3.2 Reglas de Autenticación y §4.1 Roles de Usuario"). Esto mantiene la trazabilidad y permite detectar rápidamente si un Roadmap se desvió del "Qué" aprobado.
- **La Definición no contiene detalles de implementación** (stack, librerías, endpoints, esquemas de base de datos). Si un detalle técnico se filtra a la Definición, es señal de que ese contenido pertenece a un Roadmap.
- **El Roadmap no redefine objetivos de negocio.** Si al construirlo se descubre que la Definición es ambigua o inviable, el Roadmap no debe "resolverlo por su cuenta" — el proceso vuelve explícitamente a la fase de Define sobre el Archivo de Definición.
- **Versionado independiente.** La Definición se versiona por revisiones mayores (v1, v2, v3 — cada una pasa de nuevo por Challenge). Los Roadmaps se versionan con mayor frecuencia (v1.1, v1.2...) porque absorben los imprevistos normales del Build sin tocar la Definición.

## 11. Estructura de Proyecto Recomendada

```
mi-proyecto/
├── DEFINITION.md                 # El Qué — único, estático, fuente de verdad
├── CHALLENGE_LOG.md               # Historial de Challenges aplicados a la Definición (roles, hallazgos, resolución)
│
├── roadmaps/
│   ├── roadmap-auth/
│   │   ├── v1.md                  # Primera versión consolidada del Roadmap
│   │   ├── v1.1.md                # Re-versionado tras un imprevisto en Build
│   │   └── challenge-log.md       # Historial de Challenges aplicados a este Roadmap
│   ├── roadmap-pagos/
│   │   ├── v1.md
│   │   └── challenge-log.md
│   └── roadmap-notificaciones/
│       ├── v1.md
│       └── challenge-log.md
│
├── prompts/
│   └── challenge/
│       ├── seguridad.md           # Prompt de rol: Challenge de seguridad
│       ├── escalabilidad.md       # Prompt de rol: Challenge de escalabilidad
│       ├── base-de-datos.md       # Prompt de rol: Challenge de base de datos
│       └── negocio.md             # Prompt de rol: Challenge de negocio
│
└── src/                            # Código, construido a partir de los roadmaps consolidados
```

**Por qué esta estructura funciona:**
- La Definición está aislada en la raíz — cualquiera (humano o LLM) que necesite entender el "Qué" del proyecto la encuentra sin revisar código ni roadmaps.
- Cada carpeta en `roadmaps/` es autocontenida: tiene su propio historial de versiones y su propio log de Challenge, facilitando auditar un módulo sin ruido del resto del proyecto.
- Los `challenge-log.md` dejan rastro de *quién* (humano o qué rol de LLM) cuestionó *qué*, y cómo se resolvió — esto le da trazabilidad real a la metodología, más allá de la referencia cruzada a la Definición.
- Los prompts de Challenge son reutilizables entre roadmaps y entre proyectos, por lo que viven en su propia carpeta versionable.

## 12. Roadmaps como Spec-Driven Development hiperespecífico

El Spec-Driven Development (SDD) parte de una premisa simple: se escribe una especificación antes de escribir código, y el código se genera o se valida contra esa especificación. DCB lleva esta idea un paso más allá en la fase de Roadmap.

Un Roadmap dentro de DCB no es una especificación general de alto nivel — es, en la práctica, **una especificación hiperespecífica de ejecución**: ya pasó por un ciclo de Define, ya fue cuestionado por Challenge, y ya está atada por referencia directa a una Definición aprobada. Para cuando el Roadmap llega al Build, ya no queda ambigüedad de negocio ni de diseño pendiente de resolver — solo queda ejecución.

Esto tiene una consecuencia práctica para equipos que usan agentes de codificación basados en LLM (como Claude Code u otros): un Roadmap consolidado en DCB puede entregarse **directamente** a un agente como su especificación de trabajo, con una probabilidad mucho mayor de que el resultado sea correcto al primer intento, porque:

- Las decisiones de arquitectura y alcance ya fueron discutidas y cerradas en Define + Challenge, no se toman "sobre la marcha" durante el Build.
- El agente no tiene que inferir intención de negocio — esa intención vive en la Definición referenciada, no en la cabeza de quien escribió el prompt.
- Cada paso del Roadmap puede escribirse como una tarea atómica y verificable, exactamente el formato que un agente de codificación necesita para minimizar errores acumulados entre pasos.
- Si el agente encuentra una inconsistencia durante el Build, el protocolo ya está definido: se re-versiona el Roadmap (o, si el problema es de fondo, se regresa a Define sobre la Definición) — el agente no decide por su cuenta cómo resolver la ambigüedad.

En otras palabras, dentro de DCB el Roadmap **es** el spec de SDD, pero llevado a un nivel de granularidad y validación previa que un spec tradicional normalmente no alcanza — lo cual encaja de forma natural con flujos de trabajo agénticos donde el "constructor" es una IA.

## 13. Ejemplo de Uso

Proyecto: una plataforma de reservas de canchas deportivas para un club.

**Paso 1 — Define (Definición):**
Se recogen los requerimientos del cliente (reglas de reserva, roles de usuario, política de cancelaciones, restricciones legales) y se le pide a un LLM que redacte la primera versión de `DEFINITION.md`, con secciones como "§2 Roles de Usuario", "§3 Reglas de Reserva y Cancelación", "§4 Restricciones Legales (horarios, aforo)".

**Paso 2 — Challenge sobre la Definición:**
El borrador se somete a Challenge usando los prompts de `prompts/challenge/`:
- El rol de *negocio* detecta que no se especificó qué pasa si dos usuarios reservan la misma cancha en el mismo instante (condición de carrera de negocio, no técnica).
- El rol de *legal/restricciones* detecta que falta definir el manejo de cancelaciones por lluvia en canchas al aire libre.

Los hallazgos se registran en `CHALLENGE_LOG.md`, se corrige la Definición, y se repite el Challenge hasta que no queden objeciones abiertas. La Definición queda consolidada como v1.

**Paso 3 — Define (Roadmap):**
Con la Definición blindada, se genera `roadmaps/roadmap-reservas/v1.md`, que referencia explícitamente "Implementa Definición §3 y §4" y detalla, por ejemplo, el uso de bloqueos a nivel de base de datos para resolver la condición de carrera de reservas simultáneas.

**Paso 4 — Challenge sobre el Roadmap:**
Este Roadmap pasa por Challenge de *base de datos* y de *escalabilidad*. El rol de base de datos objeta que el mecanismo de bloqueo propuesto no escala bien con múltiples canchas concurrentes, y sugiere una alternativa. Se ajusta el Roadmap a v1.1 y se vuelve a auditar hasta quedar consolidado.

**Paso 5 — Build:**
El Roadmap `v1.1` consolidado se entrega directamente a un agente de codificación (o a un equipo humano) como spec de ejecución, siguiendo la lógica de la sección 12. Durante el Build surge un imprevisto (la librería de bloqueos elegida no soporta el motor de base de datos del cliente): se re-versiona el Roadmap a `v1.2` y se documenta el cambio en su `challenge-log.md`, sin tocar en ningún momento `DEFINITION.md`, porque el "Qué" del proyecto no cambió — solo cambió el "Cómo".

---

## Estado del proyecto

DCB está en desarrollo activo. Los prompts de Challenge por rol se están formalizando como plantillas reutilizables. Feedback, crítica y casos de uso son bienvenidos.

## Licencia

Este proyecto está bajo licencia [MIT](./LICENSE).
