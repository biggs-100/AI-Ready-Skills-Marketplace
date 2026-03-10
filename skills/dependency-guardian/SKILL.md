---
name: "dependency-guardian"
description: "Especialista en mantenimiento, seguridad y salud de las dependencias del proyecto. Mantiene el stack tecnológico actualizado y libre de vulnerabilidades."
version: "2.0.0"
category: "devops"
author: "AI Master Factory"
triggers:
  keywords: ["actualizar librerías", "auditoría npm", "pip audit", "vulnerabilidad", "package update"]
  file_patterns: ["package.json", "requirements.txt", "pyproject.toml"]
---

# Skill: Dependency Guardian 🛡️

## 🎯 Objetivo

Asegurar que el proyecto nunca se detenga por una librería rota o insegura. Actúa como el sistema inmunitario del código, detectando y neutralizando amenazas en las dependencias externas.

## 🛠️ Workflow de Mantenimiento

### 1. Auditoría de Seguridad (Vulnerability Scan)

- Ejecutar `npm audit` y `pip-audit` periódicamente.
- Identificar CVEs (Common Vulnerabilities and Exposures) que afecten al proyecto.
- Generar parches de actualización automáticos para dependencias críticas.

### 2. Gestión de Ciclo de Vida (Update Strategy)

- Identificar dependencias con versiones "deprecated" u obsoletas.
- Evaluar el impacto de actualizaciones "breaking changes" antes de aplicarlas.
- Proponer alternativas más ligeras o seguras a librerías actuales.

### 3. Compliance Legal (License Audit)

- Verificar que ninguna librería use licencias prohibidas (ej: GPL en proyectos comerciales cerrados).
- Generar inventarios de licencias para reportes de cumplimiento.

## 📚 Contenidos

- `REFERENCE.md` - Comandos rápidos de auditoría.
- `docs/update-policy.md` - Política de actualización semántica (Major/Minor/Patch).
- `examples/audit-report.md` - Ejemplo de reporte de seguridad profesional.

## ✅ Output esperado

Auditoría completa de dependencias, remediación de vulnerabilidades y actualización segura del stack.
