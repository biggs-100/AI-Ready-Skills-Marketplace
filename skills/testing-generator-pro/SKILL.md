---
name: "testing-generator-pro"
description: "Generador automático de stubs de tests (Pytest/Jest) basado en documentos de diseño SDD. Asegura una cobertura inicial del 80% siguiendo los patrones del proyecto."
version: "2.0.0"
category: "quality"
author: "AI Master Factory"
triggers:
  keywords: ["generar tests", "crear stubs de prueba", "test scaffolding", "generar casos de prueba"]
  file_patterns: [".ai/sdd-changes/**/design.md", "openspec/changes/**/design.md"]
---

# Skill: Testing Generator Pro 🧪

## 🎯 Objetivo

Eliminar la fricción de escribir el "boileplate" de los tests. Esta skill lee la estrategia de testing de un documento de diseño y genera los archivos `.py` o `.ts` necesarios con los casos de prueba ya definidos pero marcados como `TODO`.

## 🛠️ Workflow de Generación

### 1. Análisis de Estrategia SDD

- Lee la sección `## Testing Strategy` del documento de diseño.
- Identifica los archivos afectados en `## File Changes`.
- Determina el framework adecuado (Pytest para Python, Vitest/Jest para TS).

### 2. Creación de Scaffolding

- Genera archivos en la carpeta `tests/` imitando la estructura de `src/`.
- Inyecta los imports necesarios (fixtures, mocks).
- Crea funciones de prueba con decoradores adecuados (ej: `@pytest.mark.asyncio`).

### 3. Inyección de Casos de Borde

- Agrega automáticamente tests para:
  - Entradas nulas/vacías.
  - Errores de validación (400 Bad Request).
  - Fallos de permisos (403 Forbidden).

## 📚 Contenidos

- `REFERENCE.md` - Comandos para lanzar la generación.
- `docs/test-patterns.md` - Guía de patrones de testing del proyecto.
- `examples/pytest-stub.py` - Ejemplo de stub generado para un endpoint FastAPI.

## ✅ Output esperado

Archivos de test creados en la ruta correspondiente con cobertura inicial de escenarios de éxito y error.
