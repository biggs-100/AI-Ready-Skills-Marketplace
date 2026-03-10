# i18n Reference 🌍⚡

## 🚀 Checklist de Localización (10 Puntos)

1. [ ] **No Hardcoded Strings**: ¿Se han extraído todos los textos a archivos JSON?
2. [ ] **Descriptive Keys**: ¿Las llaves son legibles (ej: `auth.login.submit`)?
3. [ ] **Pluralization**: ¿Se manejan correctamente los casos singular/plural?
4. [ ] **Interpolation**: ¿Las variables se pasan dinámicamente (`welcome, {{name}}`)?
5. [ ] **Date Formats**: ¿Las fechas usan el estándar `Intl` o similar?
6. [ ] **Currency symbols**: ¿La moneda cambia según el locale configurado?
7. [ ] **UI Overflow**: ¿Se ha probado el diseño con idiomas largos (ej: Alemán)?
8. [ ] **Fallback Language**: ¿Hay un idioma por defecto si falta una traducción?
9. [ ] **Directionality**: ¿La UI soporta LTR/RTL si el idioma lo requiere?
10. [ ] **Contextual AI Translation**: ¿Se han revisado las traducciones automáticas?

## 🛠️ Herramientas Sugeridas

- `react-i18next`: Librería estándar para React.
- `Lokalise / Transifex`: Para gestión profesional de traducciones.
- `i18n-ally (VSCode Extension)`: Para ver traducciones inline.

## 💡 Tip: Llaves

Usa "Natural Keys" o "Nested Keys". Las llaves anidadas (`dashboard: { title: "..." }`) ayudan a organizar el código conforme la app crece a miles de cadenas.
