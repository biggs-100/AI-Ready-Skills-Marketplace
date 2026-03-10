---
name: "feature-weaver"
description: "Habilidad maestra para la creación de funcionalidades completas E2E (Backend + Frontend). Orquesta la creación de endpoints, modelos de datos, servicios y componentes UI en un solo flujo cohesivo."
version: "2.0.0"
category: "architecture"
author: "AI Master Factory"
triggers:
  keywords: ["crear funcionalidad", "implementar feature", "e2e feature", "nueva característica"]
  file_patterns: ["src/modules/**", "frontend/src/pages/**"]
---

# Skill: Feature Weaver 🕸️ (E2E Specialist)

## 🎯 Objetivo

Orquestar la implementación de una característica completa desde el contrato del Backend hasta la interfaz del Frontend, garantizando que ambos extremos hablen el mismo idioma y respeten las restricciones del SSOT.

## 🛠️ Workflow Maestro v2.0

### 1. Definición del Contrato (Pacto de Sangre)

Antes de codificar, la IA debe definir en `REFERENCE.md` de la feature:

- Los esquemas de entrada/salida (Deltas).
- Los endpoints involucrados.
- Las variables de estado compartidas.

### 2. Tejido del Backend (Core)

- Crear el modelo de datos en el módulo correspondiente.
- Implementar el endpoint usando FastAPI/Pydantic.
- Validar salud con `run.py validate`.

### 3. Tejido del Frontend (Vibración)

- Crear el servicio de API en el frontend.
- Implementar el componente UI siguiendo el estándar **UX Pro Max**.
- Conectar componentes con hooks reactivos.

### 4. Prueba de Integración

- Verificar la comunicación fluida entre capas.
- Confirmar que los tipos TypeScript coinciden con los esquemas Pydantic.

## 📚 Contenidos

- `docs/e2e-best-practices.md` - Guía de arquitectura limpia.
- `examples/full-crud-example.tsx` - Ejemplo de un CRUD completo.
- `templates/api-endpoint.py` - Boilerplate de backend.
- `templates/ui-component.tsx` - Boilerplate de frontend.

## ✅ Output esperado

Funcionalidad completa desplegada, testada y documentada en el Grafo de Arquitectura.
