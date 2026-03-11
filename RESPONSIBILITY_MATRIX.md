# 🗺️ Matriz de Responsabilidad de Skills

> **Propósito:** Eliminar ambigüedad sobre cuándo usar cada skill, especialmente en dominios con múltiples opciones.

---

## 🔒 Seguridad

| Skill | Rol | Cuándo Usarla | Estado |
| :--- | :--- | :--- | :---: |
| **`security-guardian`** | Guardián proactivo en tiempo real | Escanear PII, buscar secretos en código, enforcement de políticas | ✅ Activa |
| **`security-sentinel`** | Auditor pre-despliegue | Auditoría OWASP completa antes de cada release/deploy | ✅ Activa |
| **`security-audit`** | Deep-dive manual | Auditoría manual profunda solicitada por el Tech Lead | ⚠️ Legacy — Usar `security-sentinel` |

---

## ⚡ Performance

| Skill | Rol | Cuándo Usarla | Estado |
| :--- | :--- | :--- | :---: |
| **`performance-optimizer-pro`** | Análisis automático + recomendaciones | Optimización de velocidad, peso y eficiencia de recursos | ✅ Activa |
| **`performance-tuning`** | Ajuste manual de parámetros | Tuning específico de queries, caches o configs | ⚠️ Legacy — Usar `performance-optimizer-pro` |

---

## 📝 Documentación

| Skill | Rol | Cuándo Usarla | Estado |
| :--- | :--- | :--- | :---: |
| **`documentation-guardian`** (v3.0) | Guardián de verdad técnica con triggers | Automatización de docs, validación, Mermaid, auditoría de blind spots | ✅ Activa |
| **`api-documentation-genius`** | Especialista en API docs | Swagger, OpenAPI, ejemplos de código para endpoints | ✅ Activa |
| **`documentation-expert`** | Documentador general | Documentación general básica | ⚠️ Legacy — Usar `documentation-guardian` |

---

## 🧪 Testing

| Skill | Rol | Cuándo Usarla | Estado |
| :--- | :--- | :--- | :---: |
| **`testing-master-architect`** (v2.1) | Orquestador maestro de testing | Generación completa de tests E2E + Unitarios + Integración | ✅ Activa |
| **`testing-architect-e2e`** | Especialista E2E | Solo pruebas End-to-End (flujos de usuario) | ✅ Activa |
| **`testing-generator-pro`** | Generador de stubs desde SDD | Generar cobertura inicial del 80% desde documentos de diseño | ✅ Activa |
| **`test-automation`** | Automatización general | Automatización básica de tests | ⚠️ Legacy — Usar `testing-master-architect` |

---

## 🏗️ Integración

| Skill | Rol | Cuándo Usarla | Estado |
| :--- | :--- | :--- | :---: |
| **`external-service-integration`** | Integrar servicios externos completos | Flujo completo de integración con APIs externas | ✅ Activa |
| **`external-apis`** | Consumir APIs simples | Llamadas HTTP simples a APIs externas | ⚠️ Legacy — Usar `external-service-integration` |

---

## 📋 Guía Rápida de Decisión

```
¿Necesitas escanear seguridad?
  ├── ¿Es antes de un deploy? → security-sentinel
  └── ¿Es monitoreo continuo/PII? → security-guardian

¿Necesitas tests?
  ├── ¿Suite completa desde cero? → testing-master-architect
  ├── ¿Solo E2E? → testing-architect-e2e
  └── ¿Stubs desde SDD? → testing-generator-pro

¿Necesitas documentación?
  ├── ¿API/Swagger? → api-documentation-genius
  └── ¿Docs generales + validación? → documentation-guardian
```

---

## ⚠️ Skills Marcadas como Legacy

Las skills con estado `⚠️ Legacy` siguen funcionando pero **no son recomendadas** para nuevas tareas. Su funcionalidad está incluida en la skill activa correspondiente.

| Legacy | Reemplazada por |
| :--- | :--- |
| `security-audit` | `security-sentinel` |
| `performance-tuning` | `performance-optimizer-pro` |
| `documentation-expert` | `documentation-guardian` |
| `test-automation` | `testing-master-architect` |
| `external-apis` | `external-service-integration` |

---
*Elite Factory v3.0 — Matriz de Responsabilidad*
