---
name: "performance-optimizer-pro"
description: "Especialista en la optimización de velocidad, peso y eficiencia de recursos. Analiza cuellos de botella en el Backend y renderizado excesivo en el Frontend."
version: "2.0.0"
category: "performance"
author: "AI Master Factory"
triggers:
  keywords: ["optimizar velocidad", "mejorar carga", "reducir bundle", "query optimization"]
  file_patterns: ["frontend/src/**/*", "src/api/**/*.py"]
---

# Skill: Performance Optimizer Pro ⚡

## 🎯 Objetivo

Asegurar que la aplicación sea ultra-rápida y eficiente. Se enfoca en minimizar el tiempo de carga (LCP), reducir el peso de los assets y optimizar las consultas a la base de datos.

## 🛠️ Workflow de Optimización

### 1. Auditoría de Frontend (Vibración Rápida)

- **Lazy Loading**: Aplicar `React.lazy()` a rutas y componentes pesados.
- **Asset Optimization**: Verificar que las imágenes estén en formato WebP y los iconos sean SVGs optimizados.
- **Bundle Analysis**: Identificar librerías innecesarias o duplicadas.

### 2. Auditoría de Backend (Core Eficiente)

- **Database Indexing**: Analizar si las columnas usadas en `WHERE` o `JOIN` tienen índices.
- **Caching**: Identificar respuestas de API que pueden ser cacheadas (Redis/Memory).
- **Asincronía**: Mover tareas pesadas (envío de emails, procesamiento de imágenes) a Background Tasks.

### 3. Métricas de Éxito

- Reducción del tiempo de respuesta de la API (< 200ms).
- Puntuación de Lighthouse > 90 en todas las categorías.
- Reducción del tamaño del bundle JS inicial.

## 📚 Contenidos

- `REFERENCE.md` - Checklist de "Quick Wins" de rendimiento.
- `docs/performance-guidelines.md` - Patrones de diseño eficiente.
- `examples/optimized-component.tsx` - Ejemplo con Memo y Lazy.

## ✅ Output esperado

Parche de optimización con comparativa "Antes vs Después" en tiempo de carga y consumo de recursos.
