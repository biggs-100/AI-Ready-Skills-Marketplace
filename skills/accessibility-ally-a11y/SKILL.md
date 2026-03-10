---
name: "accessibility-ally-a11y"
description: "Especialista en accesibilidad web (A11Y) y cumplimiento de los estándares WCAG. Asegura que la aplicación sea inclusiva y utilizable por personas con diversas capacidades."
version: "2.0.0"
category: "quality"
author: "AI Master Factory"
triggers:
  keywords: ["mejorar accesibilidad", "cumplimiento wcag", "aria labels", "contraste colores", "navegación teclado"]
  file_patterns: ["frontend/src/pages/**/*.tsx", "frontend/src/components/**/*.tsx"]
---

# Skill: Accessibility Ally (A11Y) ♿

## 🎯 Objetivo

Garantizar que nadie se quede fuera. Esta skill transforma una interfaz visual en una experiencia navegable para lectores de pantalla, teclados y usuarios con daltonismo.

## 🛠️ Workflow de Inclusión

### 1. Auditoría de Navegación por Teclado

- Asegurar que todos los elementos interactivos sean "focuseables".
- Implementar indicadores de foco claros y visibles.
- Verificar el orden lógico de tabulación (`tabindex`).

### 2. Semántica y Atributos ARIA

- Validar el uso de etiquetas HTML semánticas (`<main>`, `<nav>`, `<section>`).
- Enriquecer elementos con `aria-label`, `aria-describedby` y roles específicos cuando sea necesario.
- Asegurar que los formularios tengan etiquetas `<label>` correctamente vinculadas.

### 3. Contraste y Percepción Visual

- Auditar los ratios de contraste de color (mínimo 4.5:1 para texto normal).
- Asegurar que el color no sea el único medio para transmitir información.
- Proporcionar textos alternativos (`alt`) significativos para imágenes.

## 📚 Contenidos

- `REFERENCE.md` - Guía rápida de roles ARIA y estados.
- `docs/a11y-standards.md` - Checklist detallada WCAG 2.1.
- `examples/accessible-form.tsx` - Ejemplo de formulario perfecto para lectores de pantalla.

## ✅ Output esperado

Reporte de cumplimiento A11Y y parches de código para resolver barreras de accesibilidad detectadas.
