---
name: "internationalization-master"
description: "Especialista en internalización (i18n) y localización (l10n). Automatiza el soporte multi-idioma y asegura la adaptación cultural de la aplicación."
version: "2.0.0"
category: "globalization"
author: "AI Master Factory"
triggers:
  keywords: ["añadir idioma", "traducir", "soporte i18n", "localización", "multi-language"]
  file_patterns: ["frontend/src/locales/**/*.json", "frontend/src/i18n.ts"]
---

# Skill: Internationalization Master 🌍

## 🎯 Objetivo

Hacer que tu aplicación hable el idioma de tus usuarios, sin importar dónde estén. Automatiza la extracción de cadenas, la traducción contextual y el manejo de formatos regionales (fechas, monedas).

## 🛠️ Workflow de Globalización

### 1. Extracción y Centralización

- Identificar textos harcodeados en componentes y moverlos a diccionarios JSON.
- Implementar hooks de traducción (ej: `useTranslation()`).
- Estructurar archivos por namespaces (common, dashboard, settings).

### 2. Traducción Inteligente

- Utilizar IA para pre-traducir cadenas manteniendo términos técnicos inalterados.
- Gestionar pluralización y variables dinámicas dentro de las traducciones.
- Validar la longitud de los textos traducidos para evitar roturas de UI.

### 3. Adaptación Regional (l10n)

- Formatear números y monedas según el locale activo.
- Configurar el manejo de fechas con librerías como `date-fns` o `Intl`.
- Soporte para idiomas RTL (derecha a izquierda) si es requerido.

## 📚 Contenidos

- `REFERENCE.md` - Formatos de traducción y pluralización.
- `docs/i18n-best-practices.md` - Guía de nombrado de llaves.
- `examples/locales-en.json` - Estructura de diccionario estándar.

## ✅ Output esperado

Infraestructura i18n configurada, diccionarios actualizados y aplicación multi-idioma lista.
