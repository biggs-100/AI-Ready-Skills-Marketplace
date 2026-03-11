---
name: testing-master-architect
description: Arquitecto maestro de calidad. Automatiza la generación de tests E2E, Unitarios e Integración, garantizando una cobertura >80% y cumplimiento de la "Ley de Hierro".
version: 2.1.0
category: quality
triggers:
  keywords:
    - generar tests
    - crear pruebas
    - test architect
    - cobertura
    - pytest
    - vitest
  file_patterns:
    - 'src/**/*.py'
    - 'src/**/*.ts'
    - 'src/**/*.tsx'
    - '.ai/sdd-changes/**/design.md'
dependencies:
  - validation
  - sdd-verify
---

# 🧪 SKILL: Testing Master Architect (Pro Max)

## 🎯 Propósito

Diseñar y ejecutar una estrategia de calidad total. Esta skill no solo genera stubs, sino que orquesta todo el ciclo de vida del testeo para que el proyecto mantenga su "Health Score" al 100%.

## 🔍 Cuándo Activar

- Al finalizar un diseño SDD para generar la base de pruebas.
- Tras crear un nuevo componente o endpoint.
- Cuando el `Health Score` baja debido a falta de cobertura.
- Antes de grandes refactorizaciones (Testing de Regresión).

## 🛠️ Workflow Avanzado

### Paso 1: Mapeo de Cobertura (Context Audit)

Analizar el estado actual del componente:

- Identificar dependencias en `relationships.yaml`.
- Leer firmas de funciones y modelos de datos (Pydantic/Zod).
- Determinar si existen "Blind Spots" en la lógica.

### Paso 2: Diseño de Estrategia E2E/Unit

Generar un plan de pruebas que cubra:

- **Happy Path**: El flujo normal de éxito.
- **Edge Cases**: Límites de datos, nulos, formatos inesperados.
- **Security Tests**: Errores de permisos (403), falta de tokens (401).

### Paso 3: Generación de Código de Test (Iron Standards)

Inyectar código listo para ejecutar con:

- Fixtures preconfiguradas.
- Mocking automático de bases de datos y APIs externas.
- Validaciones de esquema integradas.

### Paso 4: Ejecución y Validación

- Ejecutar los tests creados automáticamente.
- Verificar el reporte de cobertura.
- Si no se alcanza el 80%, sugerir casos adicionales.

### Paso 5: Registro en Gobernanza

- Guardar resultados en el log de validación.
- Actualizar `decisions_log.yaml` si se descubre un bug crítico durante el diseño.

## 📝 Plantillas Disponibles

- **Pytest Mock Factory**: `templates/pytest_factory.py`
- **Vitest Component Stub**: `templates/vitest_stub.tsx`

## ✅ Checklist de Calidad

- [ ] ¿Se cubren los 3 niveles: Unitario, Integración y E2E?
- [ ] ¿Los mocks evitan llamadas reales a producción?
- [ ] ¿La cobertura supera el umbral del 80% (Ley de Hierro)?
- [ ] ¿Se han incluido pruebas de validación de entradas?

---

*Garantía de Calidad mantenida por el Master Architect.*
