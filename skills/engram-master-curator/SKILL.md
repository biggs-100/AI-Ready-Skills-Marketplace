---
name: "engram-master-curator"
description: "Especialista en la gestión y refinamiento de la memoria persistente del sistema (Engram). Optimiza el aprendizaje de la IA eliminando redundancias y consolidando lecciones clave."
version: "2.0.0"
category: "core"
author: "AI Master Factory"
triggers:
  keywords: ["limpiar memoria", "consolidar engram", "resumen de aprendizaje", "mantenimiento cerebral"]
  file_patterns: [".ai/brain/**/*.jsonl", ".ai/brain/metadata.yaml"]
---

# Skill: Engram Master Curator 🧠

## 🎯 Objetivo

Mantener la salud cognitiva del sistema. Asegura que la IA recupere solo la información más relevante, precisa y actualizada, evitando la degradación del contexto por datos obsoletos.

## 🛠️ Workflow de Curaduría

### 1. Auditoría de Fragmentos

- Identificar engrams que contradicen reglas actuales de la arquitectura.
- Detectar duplicados o lecciones que ya han sido superadas por mejores prácticas.

### 2. Consolidación de Conocimiento

- Fusionar fragmentos atómicos en "Lecciones Maestras".
- Extraer patrones recurrentes para convertirlos en nuevas reglas permanentes en `master_instructions.yaml`.

### 3. Indexación y Búsqueda

- Optimizar los metadatos de los fragmentos para mejorar la recuperación RAG.
- Categorizar lecciones por dominio (UX, Backend, Security, etc.).

## 📚 Contenidos

- `REFERENCE.md` - Guía de etiquetado de memoria.
- `docs/memory-lifecycle.md` - Cómo se crea y destruye un Engram.
- `templates/lesson-template.md` - Estructura ideal de una lección aprendida.

## ✅ Output esperado

Un "Mapa de Conocimiento" actualizado y una base de datos de memoria optimizada (sin ruido).
