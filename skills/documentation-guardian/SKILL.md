---
name: documentation-guardian
description: El guardián definitivo de la verdad técnica. Asegura que la documentación y el código nunca diverjan mediante automatización y validación.
version: 3.0.0
category: quality
triggers:
  keywords:
    - documentar
    - actualizar docs
    - generar readme
    - crear adr
    - experto en documentación
  file_patterns:
    - '**/*.md'
    - '**/*.yaml'
    - 'src/**/*.py'
    - 'src/**/*.ts'
dependencies:
  - sync-graph
  - glossary-checker
---

# 🛡️ Documentation Guardian — Elite Edition

```text
   _____ _    _          _____  _____ _____   
  / ____| |  | |   /\   |  __ \|  __ \_   _|  
 | |  __| |  | |  /  \  | |__) | |  | || |    
 | | |_ | |  | | / /\ \ |  _  /| |  | || |    
 | |__| | |__| |/ ____ \| | \ \| |__| || |_   
  \_____|\____//_/    \_\_|  \_\_____/_____|  
```

> **"Vigila el racional técnico que habita en el código."**

---

## 🎯 Propósito Elite

Asegura que la documentación sea un activo vivo y estructurado, blindando el **"Por Qué"** arquitectónico sobre el simple "Qué" del código.

---

## 🔍 Activación y Disparadores

| Evento | Acción en el Ecosistema |
| :--- | :--- |
| **Módulos `src/`** | Generación de READMEs clasificados por capas. |
| **Decisiones Técnicas** | Creación de ADRs con alternativas y racional. |
| **Puntos de Control** | Sincronización del Architecture Decision Journal. |

---

## 🛠️ Workflow Elite (Step-by-Step)

| Fase | Tarea | Detalle Técnico |
| :--- | :--- | :--- |
| **1. Clasificación** | Detectar frontera | Clasifica entre Dominio, Aplicación o Infraestructura. |
| **2. Documentación** | Generar README | Usa plantillas `template_*.md` para inyectar reglas Elite. |
| **3. Narrativa** | Actualizar Journal | Registra el impacto histórico en `ARCHITECTURAL_JOURNAL.md`. |
| **4. Decisión** | Crear ADR | Documenta alternativas descartadas y deuda técnica. |
| **5. Nexus** | Sync RAG | Ejecuta `run.py sync` para actualizar la memoria de la IA. |

---

## 📝 Plantillas del Guardián

| Plantilla | Propósito |
| :--- | :--- |
| **`template_domain.md`** | Lógica de negocio pura (Elite Rule: 0 dependencias). |
| **`template_application.md`** | Casos de uso y orquestación de procesos. |
| **`template_infrastructure.md`** | Implementaciones técnicas y adaptadores externos. |
| **`adr.md`** | Registro histórico de decisiones y racional. |
| **`architecture_journal.md`** | Bitácora narrativa de evolución del proyecto. |

---

## ✅ Checklist de Integridad

- [ ] ¿Se ha actualizado el Journal técnico de la sesión?
- [ ] ¿El README especifica claramente su capa (Dom/App/Infra)?
- [ ] ¿Existe un ADR para cada cambio arquitectónico significativo?
- [ ] ¿Se han documentado las alternativas descartadas (Elite Choice)?

---
*Elite Standard v3.0 | Preservando el Nexus de Conocimiento.*
