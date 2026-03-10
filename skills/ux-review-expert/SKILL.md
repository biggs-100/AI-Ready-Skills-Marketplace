---
name: "ux-review-expert"
description: "Auditor de diseño especializado en el estándar UX Pro Max v2.0. Garantiza que cada elemento visual cumpla con los estándares premium de tipografía, color y movimiento."
version: "2.0.0"
category: "design"
author: "AI Master Factory"
triggers:
  keywords: ["ux review", "diseño", "ui audit", "estética", "estilos"]
  file_patterns: ["**/*.css", "**/*.tsx", "**/*.html", "**/*.jsx"]
---

# Skill: UX Review Expert (Pro Max v2.0) 🎨

## 🎯 Objetivo

Garantizar que cada elemento visual del proyecto cumpla con los estándares de diseño premium de la plantilla. Actúa como el filtro de calidad estética final para evitar interfaces genéricas o inconsistentes.

## 🛠️ Workflow

### 1. Auditoría de Fundamentos

La IA debe verificar:

- **Tipografía**: La fuente principal DEBE ser `Outfit`.
- **Colores**: Prohibido el uso de nombres de colores genéricos o HEX planos. Usar HSL.
- **Bordes**: `border-radius` > 8px obligatorio.

### 2. Chequeo de Efectos Premium

- **Glassmorphism**: Backdrop blur de al menos 12px.
- **Micro-animaciones**: Transiciones en hover y estados activos.

## 📚 Contenidos

- `REFERENCE.md` - Guía rápida de tokens visuales.
- `docs/ux-standard.md` - Definición detallada del estilo.
- `examples/premium-button.css` - Ejemplo de CSS correcto.
