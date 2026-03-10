---
name: release-notes-gen
description: Especialista en release notes gen
version: 2.0.0
category: general
triggers:
  keywords:
  - release notes gen
  file_patterns:
  - '*'
---

# Skill: Release Notes Generator 🚀

## 🎯 Objetivo

Generar notas de versión (Release Notes) profesionales y estructuradas analizando los cambios recientes en el repositorio (Git logs).

## 触发 Triggers

- "generar notas de versión"
- "release notes"
- "¿qué hay de nuevo en esta versión?"
- "preparar release"

## 🛠️ Workflow

### 1. Extracción de Datos

Ejecuta el siguiente comando para obtener los cambios desde el último tag (o los últimos 20 commits si no hay tags):

```bash
git log --pretty=format:"%s (%h)" -n 20
```

### 2. Clasificación

Clasifica los commits según los siguientes prefijos:

- **🚀 Features**: `feat: ...`, `feature: ...`
- **🐛 Bug Fixes**: `fix: ...`, `bug: ...`
- **⚡ Performance**: `perf: ...`
- **📂 Refactors**: `refactor: ...`
- **📝 Docs**: `docs: ...`

### 3. Generación del Documento

Crea un archivo llamado `docs/history/RELEASE_vX.X.X.md` con el siguiente formato:

```markdown
# 📦 Release Notes - v[VER] ([FECHA])

## 🌟 Resumen Ejecutivo
[Breve descripción del impacto de esta versión]

## 🚀 Lo Nuevo
- [Feature 1]
- [Feature 2]

## 🐛 Correcciones
- [Bug fix 1]

## 🛠️ Cambios Internos
- [Refactor/Performance]
```

### 4. Sincronización

Al finalizar, ejecuta `python run.py sync` para que el cerebro registre la nueva documentación.

## ✅ Output esperado

Un nuevo archivo en `docs/history/` y un resumen para el usuario.
