# Skill: UX Review Expert (Pro Max v2.0) 🎨

## 🎯 Objetivo

Garantizar que cada elemento visual del proyecto cumpla con los estándares de diseño premium de la plantilla. Actúa como el filtro de calidad estética final para evitar interfaces genéricas o inconsistentes.

## 触发 Triggers

- "revisar diseño de [componente]"
- "auditoría UX/UI"
- "validar estilos"
- "check visual"
- Cambio detectado en archivos `.css`, `.tsx`, `.html`

## 🛠️ Workflow

### 1. Auditoría de Fundamentos

La IA debe verificar:

- **Tipografía**: La fuente principal DEBE ser `Outfit`. Si no se encuentra, marcar como error crítico.
- **Colores**: Prohibido el uso de nombres de colores genéricos (`red`, `blue`) o HEX planos sin variables. Deben usarse variables CSS o HSL curadas.
- **Bordes**: Verificar que los contenedores tengan `border-radius` mayor a 8px (estilo moderno suavizado).

### 2. Chequeo de Efectos Premium

- **Glassmorphism**: Buscar implementaciones de `backdrop-filter: blur()` y transparencias sutiles en modales y headers.
- **Micro-animaciones**: Verificar la presencia de transiciones suaves en hover y estados activos.
- **Sombras**: Asegurar el uso de sombras suaves (sombras de 3 o 4 capas) en lugar de sombras negras duras.

### 3. Reporte de Desviaciones

Generar una tabla con:

- **Elemento**: Selector CSS o componente.
- **Error**: Qué regla del UX Pro Max incumple.
- **Fix sugerido**: El snippet de código corregido.

## ✅ Output esperado

Un reporte de auditoría visual detallado con sugerencias de código listas para aplicar.
