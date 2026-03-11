---
name: refactor-pro-active
description: "Especialista en refactorización proactiva de código. Identifica code smells, reduce complejidad ciclomática y aplica patrones de diseño para mejorar la mantenibilidad."
version: 2.0.0
category: quality
triggers:
  keywords:
  - refactorizar
  - code smell
  - clean code
  - modularizar
  - complejidad
  file_patterns:
  - '*'
---

# Skill: Refactor Pro-Active ⚙️

## 🎯 Objetivo

Identificar y proponer refactorizaciones automáticas para mejorar la mantenibilidad, legibilidad y performance del código. Su meta es mantener la Deuda Técnica del proyecto en niveles mínimos.

## 触发 Triggers

- "analizar code smells"
- "sugerir refactorización"
- "optimizar [archivo/módulo]"
- Detectado aumento en la complejidad ciclomática.
- Archivo supera las 300 líneas de código.

## 🛠️ Workflow

### 1. Detección de Patrones

La IA debe buscar:

- **Lógica Duplicada (DRY)**: Identificar bloques de código similares en diferentes módulos para extraerlos a utilidades.
- **Funciones Monolíticas**: Detectar funciones que intentan hacer más de una cosa y sugerir su división.
- **Acoplamiento Fuerte**: Identificar dependencias circulares o módulos que saben demasiado de otros.

### 2. Análisis de Mantenibilidad

- Verificar si las variables y funciones tienen nombres descriptivos (S.O.L.I.D.).
- Evaluar si el nivel de indentación es excesivo.
- Identificar falta de manejo de errores en bloques críticos.

### 3. Propuesta de Refactor

Generar un reporte con:

- **Ubicación**: Archivo y líneas.
- **Problema**: Descripción técnica de la deuda detectada.
- **Solución**: Refactorización sugerida con código de ejemplo.
- **Impacto**: Mejora esperada en mantenibilidad o performance.

## ✅ Output esperado

Un reporte técnico de refactorización con un plan de acción para limpiar el código.
