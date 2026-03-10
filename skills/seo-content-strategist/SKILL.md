---
name: "seo-content-strategist"
description: "Especialista en optimización de motores de búsqueda (SEO) y estrategia de contenido semántico. Asegura que la aplicación sea perfectamente indexable y relevante para los algoritmos modernos."
version: "2.0.0"
category: "marketing"
author: "AI Master Factory"
triggers:
  keywords: ["mejorar seo", "optimizar meta", "sitemap", "json-ld", "palabras clave"]
  file_patterns: ["frontend/src/pages/**/*.tsx", "frontend/src/components/layout/Header.tsx"]
---

# Skill: SEO Content Strategist 🚀

## 🎯 Objetivo

Transformar una aplicación técnicamente perfecta en un imán de tráfico orgánico. Se enfoca en la estructura semántica, la velocidad de rastreo y la relevancia del contenido.

## 🛠️ Workflow de Optimización SEO

### 1. Auditoría de Estructura Semántica (H1-H6)

- Verificar que cada página tenga un ÚNICO `<h1>`.
- Asegurar una jerarquía lógica de encabezados para facilitar el rastreo.
- Validar el uso de etiquetas alt descriptivas en todas las imágenes.

### 2. Generación de Metadatos Dinámicos

- Implementar títulos y meta-descripciones únicas por ruta.
- Configurar etiquetas Open Graph (OG) y Twitter Cards para redes sociales.
- Generar esquemas JSON-LD (Schema.org) para datos estructurados (Product, Article, Organization).

### 3. Rendimiento Crítico para Google (Core Web Vitals)

- Minimizar el Cumulative Layout Shift (CLS) ajustando dimensiones de imágenes.
- Asegurar que el contenido principal sea visible sin JS (SSR/Prerendering cuando sea posible).

## 📚 Contenidos

- `REFERENCE.md` - Checklist de validación SEO rápida.
- `docs/schema-standards.md` - Guía de implementación de JSON-LD.
- `examples/meta-component.tsx` - Componente de gestión de cabeceras SEO.

## ✅ Output esperado

Análisis de palabras clave, implementación de metadatos y reporte de "SEO Health Score" mejorado.
