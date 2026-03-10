---
name: "security-sentinel"
description: "Especialista en auditoría de seguridad preventiva. Escanea código, configuraciones y endpoints buscando vulnerabilidades (OWASP, inyecciones, fallos de auth) antes del despliegue."
version: "2.0.0"
category: "security"
author: "AI Master Factory"
triggers:
  keywords: ["auditoría seguridad", "scan vulnerabilidades", "revisar auth", "security check"]
  file_patterns: ["src/api/**/*.py", ".env*", "frontend/src/services/*.ts"]
---

# Skill: Security Sentinel 🛡️

## 🎯 Objetivo

Identificar, prevenir y mitigar riesgos de seguridad en el ciclo de vida del desarrollo. Actúa como un guardián que bloquea el despliegue de código vulnerable.

## 🛠️ Workflow de Auditoría

### 1. Análisis de Capa de Datos e Inyección

- Verificar que ninguna consulta SQL se construya mediante concatenación de strings.
- Validar el uso de ORMs o sentencias preparadas.
- Buscar sanitización de entradas en modelos Pydantic/Zod.

### 2. Auditoría de Autenticación y Autorización

- Revisar que los endpoints críticos tengan el decorador de dependencia `Depends(get_current_user)` o equivalente.
- Validar la expiración y robustez de los tokens JWT.
- Verificar permisos mínimos (Principle of Least Privilege).

### 3. Fuga de Información y Secretos

- Escanear archivos para evitar el hardcodeo de llaves API, contraseñas o datos sensibles.
- Revisar que las respuestas de error no expongan trazas de stack (Stacktraces) en producción.

### 4. Seguridad en Frontend

- Verificar protecciones contra XSS (Cross-Site Scripting).
- Revisar configuraciones de CORS y CSP (Content Security Policy).

## 📚 Contenidos

- `REFERENCE.md` - Checklist de endurecimiento (Hardening).
- `docs/security-policy.md` - Estándares de seguridad del proyecto.
- `examples/secure-endpoint.py` - Ejemplo de endpoint blindado.

## ✅ Output esperado

Reporte de riesgos categorizado por severidad (Crítica, Alta, Media, Baja) con parches de código sugeridos.
