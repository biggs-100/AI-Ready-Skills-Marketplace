---
name: "api-documentation-genius"
description: "Especialista en redacción técnica y documentación de APIs. Mantiene Swagger, manuales y ejemplos de código sincronizados con la realidad del servidor."
version: "2.0.0"
category: "documentation"
author: "AI Master Factory"
triggers:
  keywords: ["documentar api", "swagger update", "explicar endpoint", "guía de integración"]
  file_patterns: ["src/api/**/*.py", "docs/api/*.md"]
---

# Skill: API Documentation Genius 📚

## 🎯 Objetivo

Hacer que la API sea fácil de entender y consumir por otros humanos o IAs. Se encarga de que no haya "magia negra" en el código y que cada parámetro, respuesta y error esté documentado con claridad.

## 🛠️ Workflow de Documentación

### 1. Enriquecimiento de OpenAPI (FastAPI)

- Añadir `description`, `summary` y `response_description` a cada decorador de ruta.
- Usar `json_schema_extra` en los modelos Pydantic para proveer ejemplos reales de entrada.
- Documentar todos los códigos de estado posibles (200, 201, 400, 401, 403, 404, 500).

### 2. Creación de Guías de Integración

- Escribir ejemplos detallados de uso usando `curl`, Python (`requests`) y TypeScript (`fetch`).
- Explicar el flujo de autenticación (ej: cómo obtener y usar el `X-API-Key`).

### 3. Sincronización de Manuales

- Mantener archivos Markdown en `docs/api/` alineados con los cambios en `src/api/main.py`.

## 📚 Contenidos

- `REFERENCE.md` - Glosario de términos y códigos de estado.
- `docs/doc-standards.md` - Cómo escribir buena documentación técnica.
- `examples/example-curl.sh` - Snippets listos para copiar y pegar.

## ✅ Output esperado

Documentación interactiva (Swagger/Redoc) completa y guías de integración Markdown listas para compartir.
