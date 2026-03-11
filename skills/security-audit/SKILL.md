---
name: security-audit
description: "Especialista en auditoría profunda de seguridad bajo demanda. Realiza análisis exhaustivo de vulnerabilidades, inyecciones y configuraciones de seguridad."
version: 2.0.0
category: security
triggers:
  keywords:
  - auditoría seguridad
  - vulnerabilidad
  - pentest
  - owasp
  file_patterns:
  - '*'
---

# SKILL: Auditoría de Seguridad

## 🎯 Propósito

Evaluar preventivamente el código para detectar vulnerabilidades (OWASP Top 10), secretos expuestos y configuraciones inseguras antes de un despliegue.

## 🔍 Cuándo Activar

- Antes de cada commit a la rama principal.
- Cuando se agrega una nueva funcionalidad que maneja datos sensibles o autenticación.
- El usuario pide un "security check".

## 📋 Pre-requisitos

- Leer `security.yaml`, `core_constraints.yaml` y `project_constraints.yaml`.
- Herramientas de escaneo (SCA, SAST).

## 🛠️ Proceso Paso a Paso

### Paso 1: Scan de Secretos

Buscar preventivamente API keys, tokens o passwords hardcodeados usando regex o herramientas dedicadas.

### Paso 2: Auditoría de Auth/Authz

Verificar que cada endpoint nuevo tenga protección de autenticación y checks de permisos adecuados.

### Paso 3: Validación de Datos (Injection)

Asegurar que todo input de usuario esté sanitizado y validado vía Pydantic. Verificar que no haya SQL Injection.

### Paso 4: Revisión de Dependencias

Ejecutar herramientas como `pip-audit` o `npm audit` para detectar CVEs en las bibliotecas del proyecto.

### Paso 5: Reporte de Hallazgos

Documentar vulnerabilidades encontradas y proponer remediación inmediata.

## ✅ Checklist de Validación

- [ ] No hay secretos en el código fuente.
- [ ] Los endpoints están protegidos por defecto.
- [ ] Todas las dependencias son seguras.
- [ ] Se loguean eventos de auditoría (login, fallos de auth).

## 🚫 Anti-patrones

❌ Asumir que el framework es seguro por defecto.
❌ Ocultar fallos de seguridad en vez de fijarlos.
❌ No validar el tamaño de los inputs (DoS).
