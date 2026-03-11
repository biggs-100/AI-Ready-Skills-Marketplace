---
name: documentation-guardian
description: El guardián definitivo de la verdad técnica. Asegura que la documentación y el código nunca diverjan mediante automatización y validación.
version: 2.1.0
category: quality
triggers:
  keywords:
    - documentar
    - actualizar docs
    - generar readme
    - crear adr
    - experto en documentación
  file_patterns:
    - '**/*.md'
    - '**/*.yaml'
    - 'src/**/*.py'
    - 'src/**/*.ts'
dependencies:
  - sync-graph
  - glossary-checker
---

# 🛡️ SKILL: Documentation Guardian (Elite Edition)

> "El guardián no solo vigila el código, vigila el racional que lo habita."

## 🎯 Propósito

Esta skill asegura que la documentación técnica sea un activo vivo, estructurado y siempre sincronizado con el código, utilizando principios de **Elite Programming** y Clean Architecture.
Esta skill no solo explica el "qué", sino que blinda el **"Por qué"** y asegura la integridad de las capas de Clean Architecture.

## 🔍 Cuándo Activar

- Al crear o modificar módulos en `src/`.
- Al tomar decisiones técnicas que impacten el largo plazo (ADRs).
- Tras finalizar una sesión para actualizar el **Architecture Decision Journal**.

## 🛠️ Workflow Avanzado (Gentleman Way)

### Paso 1: Clasificación de Capas (Boundary Detection)

Antes de generar el README, identifica dónde reside el código:

- **Dominio**: Reglas de negocio puras. Usar `template_domain.md`.
- **Aplicación**: Casos de uso y orquestación. Usar `template_application.md`.
- **Infraestructura**: Adaptadores y detalles técnicos. Usar `template_infrastructure.md`.

### Paso 2: El Diario Arquitectónico (Context Preservation)

Cada decisión importante debe ser brevemente reseñada en `.ai/ARCHITECTURAL_JOURNAL.md` para mantener la narrativa histórica del proyecto.

### Paso 3: ADRs con Racional Exhaustivo

Al crear un ADR usando `adr.md`, es **obligatorio**:

1. Listar el **Gentleman Choice**: ¿Qué alternativas se descartaron y por qué?
2. Análisis de **Desacoplamiento**: ¿Esta decisión rompe la independencia de las capas?
3. Puntuar el impacto en **Deuda Técnica**.

### Paso 4: Generación Visual de Fronteras

Representar con Mermaid los límites entre capas, no solo el flujo de datos.

### Paso 5: Sincronización y Validación RAG

- Ejecutar `py run.py sync`.
- Validar formato y lints.

## 📝 Plantillas Disponibles

- **Architecture Journal**: `templates/architecture_journal.md`
- **ADR Advanced**: `templates/adr.md`
- **Domain README**: `templates/template_domain.md`
- **App README**: `templates/template_application.md`
- **Infra README**: `templates/template_infrastructure.md`

## ✅ Checklist "Gentleman"

- [ ] ¿El ADR incluye alternativas descartadas?
- [ ] ¿Se ha actualizado el Diario Arquitectónico?
- [ ] ¿El README del módulo identifica correctamente su capa (Dom/App/Infra)?
- [ ] ¿Se explica el **POR QUÉ** detrás de la arquitectura?

## 🚫 Anti-patrones

❌ Mezclar lógica de dominio con detalles de infraestructura en el mismo README.
❌ Ignorar las consecuencias negativas de una decisión técnica.
❌ Dejar el Diario Arquitectónico desactualizado más de 2 sesiones.
