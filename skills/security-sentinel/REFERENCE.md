# Security Sentinel Reference 🛡️⚡

## 🚀 Checklist de Seguridad (Zero Trust)

1. [ ] **No Secrets**: ¿Se han movido todas las API Keys a `.env`?
2. [ ] **SQL Injection**: ¿Todas las queries usan parámetros?
3. [ ] **Auth Check**: ¿El endpoint tiene validación de JWT/Session?
4. [ ] **Input Validation**: ¿Se usa Pydantic `Field` con regex/límites?
5. [ ] **HTTPS/CORS**: ¿La configuración de CORS es restrictiva?
6. [ ] **Sensitive Data**: ¿Se ocultan passwords/hashes en el JSON de respuesta?
7. [ ] **Rate Limiting**: ¿Hay protección contra fuerza bruta?
8. [ ] **Error Handling**: ¿Los errores son genéricos (sin revelar internals)?
9. [ ] **Dependencies**: ¿Están actualizadas las librerías críticas?
10. [ ] **Watcher**: ¿El AI Watcher ha reportado violaciones de seguridad?

## 🛠️ Comandos de Escaneo

- `py run.py security-scan`: Ejecuta un escaneo estático de código.
- `py run.py check-secrets`: Busca credenciales expuestas en el historial.

## 💡 Tip: Validación Estricta

Usa siempre `StrictStr` o validaciones de longitud en Pydantic para evitar desbordamientos de búfer lógicos o DoS por payloads gigantes.
