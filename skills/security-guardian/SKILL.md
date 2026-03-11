---
name: security-guardian
description: Guardián proactivo de seguridad y privacidad. Escanea datos sensibles (PII), busca secretos y garantiza el cumplimiento de políticas de seguridad en tiempo real.
version: 2.1.0
category: security
triggers:
  keywords:
    - seguridad
    - auditoria
    - pii
    - privacidad
    - cifrado
    - scan
  file_patterns:
    - 'src/modules/users/**'
    - 'src/modules/auth/**'
    - '**/repositories/**'
    - '**/services/**'
    - '.env*'
dependencies:
  - validation
  - sync-graph
---

# 🛡️ SKILL: Security Guardian (Pro Max)

## 🎯 Propósito

Actuar como la máxima autoridad en seguridad y privacidad de datos dentro del proyecto. No solo detecta vulnerabilidades, sino que garantiza que el manejo de información sensible (PII) cumpla con los estándares GDPR y OWASP.

## 🔍 Cuándo Activar

- Al modificar archivos que manejen datos de usuarios (PII).
- Antes de realizar commits que involucren configuraciones de red o API externas.
- Cuando se detecta un posible hardcodeo de secretos.
- Al integrar nuevas librerías de terceros (Análisis de vulnerabilidades de dependencias).

## 🛠️ Workflow Avanzado

### Paso 1: Escaneo de Sensibilidad (Privacy Scan)

Identificar si el archivo en edición maneja:

- Datos personales (Emails, IDs, Contraseñas).
- Secretos (API Keys, Tokens).
- Si pertenecen a un módulo con la advertencia `[pii_context]`.

### Paso 2: Validación de Blindaje (Shielding)

Verificar que:

- No haya registros de logs que contengan datos sensibles.
- Las contraseñas usen algoritmos de hashing modernos (Argon2, bcrypt).
- Las comunicaciones externas estén cifradas (TLS/SSL).

### Paso 3: Análisis Estático de Vulnerabilidades (SAST)

Buscar patrones de:

- Inyección SQL/NoSQL.
- Cross-Site Scripting (XSS).
- Broken Access Control (Insecure Direct Object References).

### Paso 4: Reporte y Mitigación

Sugerir parches inmediatos para:

- Enmascaramiento de datos.
- Rotación de secretos expuestos.
- Implementación de políticas de CORS más restrictivas.

### Paso 5: Sincronización del "Contexto de Seguridad"

- Actualizar `security.yaml` si se introducen nuevos vectores de ataque o protecciones.
- Ejecutar `py run.py validate` para confirmar que el Health Score no se vea afectado.

## 📝 Plantillas Disponibles

- **Security ADR**: `templates/security_decision.md`
- **Secret Scan Policy**: `docs/secret_policy.md`

## ✅ Checklist de Seguridad

- [ ] ¿Se han enmascarado los datos PII en todos los logs?
- [ ] ¿Se ha verificado la ausencia de secretos en el historial de Git?
- [ ] ¿El endpoint requiere autenticación robusta?
- [ ] ¿Se han validado y sanitizado todas las entradas de usuario?

---

*Gobernanza de Seguridad activada por el Guardián.*
