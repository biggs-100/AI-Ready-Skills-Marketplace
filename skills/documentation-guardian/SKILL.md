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

# 🛡️ SKILL: Documentation Guardian (Pro Max)

## 🎯 Propósito

Transformar el conocimiento técnico del sistema en documentación viva, precisa y visualmente impactante. Esta skill actúa como un **Auditor de la Verdad**, asegurando que cada cambio en el código tenga su contraparte documental correspondiente.

## 🔍 Cuándo Activar

- Al crear un nuevo módulo o directorio en `src/`.
- Al realizar cambios estructurales que afecten a `relationships.yaml`.
- Cuando se detectan términos nuevos en el código que no están en el glosario.
- Tras finalizar una sesión para generar el **Session Checkpoint**.

## 🛠️ Workflow Avanzado

### Paso 1: Auditoría de Coherencia (Inception)

Antes de escribir, analiza:

- `relationships.yaml` para detectar nuevas dependencias runtime.
- `.ai/context/glossary.yaml` para asegurar terminología consistente.
- Código fuente para extraer firmas de API y decoradores de seguridad.

### Paso 2: Generación Visual (Mermaid First)

Si el módulo tiene complejidad lógica o múltiples dependencias:

- Generar un diagrama de flujo o de arquitectura en **Mermaid** dentro del archivo `.md`.

### Paso 3: Aplicación de Plantillas

Utilizar los archivos en la carpeta `templates/` según la necesidad:

- `adr.md` para decisiones arquitectónicas.
- `module_readme.md` para documentación de sub-módulos.
- `openapi_spec.yaml` para contratos de API.

### Paso 4: Auditoría de "Blind Spots"

Escanear el código en busca de:

- Funciones sin docstrings (si se requiere).
- Términos técnicos no definidos en el manual.
- Diferencias entre el contrato de API y la implementación.

### Paso 5: Sincronización y Validación

- Ejecutar `py run.py sync` para actualizar el Manual RAG.
- Validar el formato con `markdownlint` (especialmente MD024, MD060, MD040).

## 📝 Plantillas Disponibles

- **ADR**: Ubicación: `templates/adr.md`
- **Module README**: Ubicación: `templates/module_readme.md`
- **OpenAPI 3.1**: Ubicación: `templates/openapi_spec.yaml`

## ✅ Checklist de Validación

- [ ] ¿El diagrama Mermaid refleja las dependencias en `relationships.yaml`?
- [ ] ¿Se han evitado "blind spots" terminológicos (Glosario sincronizado)?
- [ ] ¿La documentación explica el **POR QUÉ** más que el **QUÉ**?
- [ ] ¿Se han pasado las validaciones de `run.py validate`?

## 🚫 Anti-patrones

❌ Documentación redundante (explicar lo que el código ya dice).
❌ Diagramas Mermaid desincronizados con la realidad de las carpetas.
❌ Usar placeholders o "Lorem Ipsum".
❌ Olvidar sincronizar el RAG tras actualizar un archivo maestro.
