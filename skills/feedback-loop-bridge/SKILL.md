---
name: "feedback-loop-bridge"
description: "Puente de aprendizaje automático que analiza logs de errores y feedback del sistema para extraer lecciones aprendidas y actualizar la memoria del agente."
version: "2.0.0"
category: "core"
author: "AI Master Factory"
triggers:
  keywords: ["analizar logs", "extraer lecciones", "aprender del error", "feedback loop"]
  file_patterns: ["logs/*.log", ".ai/last_impact_report.json"]
---

# Skill: Feedback Loop Bridge 🔄

## 🎯 Objetivo

Cerrar el ciclo de aprendizaje. Esta skill procesa los rastros de fallos y éxitos para actualizar `.ai/memory/lessons_learned.yaml` y el BrainDB, asegurando que el agente no repita los mismos errores.

## 🛠️ Workflow de Aprendizaje

### 1. Ingesta de Logs

- Escanea archivos `.log` en busca de excepciones (Stack Traces).
- Analiza `last_impact_report.json` para ver si el impacto real coincidió con el planeado.

### 2. Destilación de Lecciones

- Identifica el componente causante del error.
- Formula una regla de prevención (ej: "Siempre validar X antes de llamar a Y").
- Categoriza el impacto (Bajo, Medio, Crítico).

### 3. Actualización de Memoria

- Inyecta la nueva lección en `lessons_learned.yaml`.
- Sincroniza con el Engram para que esté disponible en futuras sesiones.

## 📚 Contenidos

- `REFERENCE.md` - Guía de comandos de extracción.
- `docs/log-analysis-patterns.md` - Cómo interpretar trazas de error comunes.
- `examples/lesson-entry.yaml` - Formato estándar de una lección aprendida.

## ✅ Output esperado

Nuevas entradas en la memoria del proyecto y actualización del Knowledge Graph.
