# Define-Challenge-Build (DCB)

> Metodología de planificación y arquitectura de software guiada por especificaciones, que utiliza Modelos de Lenguaje Grande (LLMs) y un sistema estructurado de cuestionamiento para validar el diseño antes de la ejecución.

---

## 1. Definición

**Define-Challenge-Build (DCB)** es una metodología de desarrollo de software cuyo núcleo es el **cuestionamiento estructurado**: ningún artefacto (ni la definición del proyecto, ni su plan de implementación) avanza a la siguiente fase sin haber sido sometido a una auditoría crítica que verifique que está bien planteado.

A diferencia de otras metodologías guiadas por especificaciones, DCB no asume que la primera versión generada por un LLM es correcta. En cambio, obliga a que **cada artefacto sobreviva un proceso de Challenge** —revisión por humanos expertos y/o por LLMs con roles específicos— antes de ser considerado válido.

```
[Requerimientos] → [Define: Generación del "Qué"] → [Challenge #1] → [Definición Consolidada]
      → [Define: Generación del "Cómo" / Roadmap] → [Challenge #2] → [Build]
```

---

## 2. Principio central: Desacoplamiento de Componentes

DCB prohíbe mezclar la meta del proyecto con su ejecución. Todo se divide en dos artefactos independientes:

| Artefacto | Pregunta que responde | Naturaleza |
|---|---|---|
| **Archivo de Definición** | El **Qué** | Estático — objetivos, reglas de negocio, alcance y restricciones del sistema |
| **Roadmap** | El **Cómo** | Dinámico y versionado — ruta técnica de implementación |

**¿Por qué separar?** Porque la tecnología, los tiempos y los imprevistos cambian constantemente durante el desarrollo, pero el objetivo del proyecto no debería cambiar solo porque cambió una decisión técnica. Si el Roadmap necesita mutar, la Definición permanece intacta. Esto evita que un cambio de herramienta o de cronograma contamine el propósito original del proyecto.

---

## 3. El Flujo de Trabajo

DCB se ejecuta en tres etapas, cada una con su propio mecanismo de control:

### 3.1 Define
Se extraen los requerimientos del cliente o del negocio y se introducen a un LLM para redactar la primera propuesta del **Archivo de Definición**. Esta etapa también se repite, en un segundo momento, para generar el **Roadmap**, pero solo después de que la Definición ha sido consolidada.

### 3.2 Challenge
Este es el corazón real de la metodología. El artefacto recién generado (ya sea la Definición o el Roadmap) es sometido a una auditoría crítica antes de ser aceptado. El Challenge puede ejecutarse mediante:

- **Humanos expertos** (revisión manual por especialistas del dominio).
- **LLMs con roles específicos** (seguridad, escalabilidad, base de datos, negocio, etc.), cada uno cuestionando el artefacto desde su ángulo particular.

El Challenge se aplica **dos veces** en el ciclo completo:

1. **Challenge sobre la Definición**: verifica que el "Qué" sea correcto, completo y libre de ambigüedades antes de que se diseñe ninguna solución técnica sobre él.
2. **Challenge sobre el Roadmap**: verifica que el "Cómo" sea coherente con la Definición ya aprobada y técnicamente viable, antes de liberarlo al equipo de desarrollo.

Solo tras superar el Challenge correspondiente, un artefacto pasa a considerarse consolidado.

### 3.3 Build
Con la Definición blindada y el Roadmap validado, el equipo de desarrollo ejecuta la implementación. Si durante el Build surgen imprevistos que afectan al Roadmap, este puede versionarse y volver a pasar por un nuevo Challenge — sin necesidad de tocar la Definición, salvo que el imprevisto revele que el "Qué" original era inviable, en cuyo caso el proceso retorna explícitamente a la fase de Define.

---

## 4. Propuesta de Valor

- **Mitigación de alucinaciones**: el cuestionamiento cruzado (humano y/o multi-LLM) neutraliza errores comunes de generación de contenido por IA, evitando que una definición o un roadmap defectuoso avance sin ser detectado.
- **Arquitectura flexible**: al desacoplar el Qué del Cómo, los cambios tecnológicos o de cronograma no comprometen el objetivo del proyecto — solo el Roadmap muta y se re-versiona.
- **Consenso técnico previo**: automatiza y estructura la fase más lenta del desarrollo (planeación y documentación), garantizando que exista acuerdo técnico antes de escribir una sola línea de código.
- **Trazabilidad**: cada Roadmap puede referenciar explícitamente qué sección de la Definición está implementando, facilitando auditorías futuras.

---

## 5. Artefactos de la Metodología

### 5.1 Archivo de Definición (El Qué)
Documento maestro y estático. Detalla de forma conceptual (y, cuando aplica, matemática) los objetivos, reglas de negocio, alcance y restricciones del sistema. Una vez consolidado tras el Challenge, no debería modificarse salvo que se descubra una inviabilidad estructural.

### 5.2 Roadmap (El Cómo)
Uno o varios documentos dinámicos y versionados que trazan la ruta técnica de implementación. Evolucionan a medida que el desarrollo avanza y enfrenta imprevistos, siempre bajo referencia directa a la Definición aprobada.

### 5.3 Prompts de Challenge
Conjunto de instrucciones especializadas (por rol: seguridad, escalabilidad, base de datos, negocio, etc.) utilizadas para auditar tanto la Definición como el Roadmap. *(Pendiente de documentar en detalle.)*
