---
name: "testing-architect-e2e"
description: "Especialista en la creación de suites de pruebas de punta a punta (End-to-End). Automatiza la validación de flujos de usuario reales integrando el Frontend con el Backend."
version: "2.0.0"
category: "quality"
author: "AI Master Factory"
triggers:
  keywords: ["crear tests", "añadir pruebas e2e", "validar flujo usuario", "testing playwright"]
  file_patterns: ["tests/e2e/**/*.spec.ts", "cypress/e2e/**/*.cy.js"]
---

# Skill: Testing Architect E2E 🧪

## 🎯 Objetivo

Garantizar que las funcionalidades ("features") entregadas por el sistema funcionen perfectamente en el navegador, validando la integración real entre todas las capas de la aplicación.

## 🛠️ Workflow de Testing v2.0

### 1. Definición de Escenarios (User Stories)

- Traducir la funcionalidad a pasos de usuario: "Dado que estoy en X, cuando hago Y, entonces sucede Z".
- Identificar casos de éxito, de error (Edge cases) y flujos alternativos.

### 2. Generación de Scripts de Prueba

- Crear selectores robustos (priorizando `data-testid`).
- Implementar aserciones que verifiquen tanto cambios visuales como persistencia en base de datos.
- Mocking de servicios externos si es necesario.

### 3. Orquestación y Reporte

- Ejecutar pruebas en modo headless.
- Generar capturas de pantalla o videos en caso de fallo.
- Validar el historial de logs para asegurar que no hubo errores silenciosos en el backend.

## 📚 Contenidos

- `REFERENCE.md` - Selectores comunes y patrones de aserción.
- `docs/testing-strategy.md` - Cuándo usar Unit vs E2E.
- `examples/login-flow.spec.ts` - Ejemplo de prueba de autenticación.

## ✅ Output esperado

Suite de pruebas operativa, pasando al 100% y reportada en el historial de validación del proyecto.
