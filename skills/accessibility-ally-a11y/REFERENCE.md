# A11Y Reference ♿⚡

## 🚀 Checklist de Inclusión (10 Puntos)

1. [ ] **Focus Indicators**: ¿Es visible y claro el indicador de foco al navegar con TAB?
2. [ ] **Alt Text**: ¿Todas las imágenes tienen `alt` (vacío `alt=""` solo si es decorativa)?
3. [ ] **Form Labels**: ¿Cada `input` tiene un `<label>` asociado mediante `htmlFor`?
4. [ ] **Color Contrast**: ¿El texto tiene suficiente contraste contra el fondo?
5. [ ] **Semantic Tags**: ¿Se usan botones `<button>` para acciones y enlaces `<a>` para navegación?
6. [ ] **ARIA Labels**: ¿Los iconos sin texto tienen un `aria-label` descriptivo?
7. [ ] **Landmarks**: ¿La página está dividida en `<header>`, `<main>` y `<footer>`?
8. [ ] **Heading Order**: ¿Los títulos siguen un orden lógico sin saltarse niveles?
9. [ ] **Interactive Size**: ¿Los botones tienen un área táctil de al menos 44x44px?
10. [ ] **Language**: ¿El elemento `<html>` tiene el atributo `lang` correcto?

## 🛠️ Herramientas de Auditoría

- `WAVE Browser Extension`: Para análisis visual de errores.
- `axe-core`: Motor de pruebas para automatización.
- `NVDA / VoiceOver`: Lectores de pantalla reales para pruebas de usuario.

## 💡 Tip: Simplicidad

La mejor accesibilidad es el HTML semántico puro. Un `<button>` nativo ya tiene manejo de teclado y roles ARIA integrados. Úsalo siempre antes de intentar convertir un `<div>` en un botón.
