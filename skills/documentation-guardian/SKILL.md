---
name: documentation-guardian
description: El guardián definitivo de la verdad técnica. Asegura que la documentación y el código nunca diverjan mediante automatización y validación.
version: 2.1.0
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

## 🔍 Activación

| Disparador | Acción Requerida |
| :--- | :--- |
| **Módulos `src/`** | Generación de README por capas |
| **Decisiones ADR** | Documentación de alternativas y racional |
| **Fin de Sesión** | Sincronización del Architecture Journal |

---

## 🛠️ Workflow Elite

| Fase | Tarea | Herramienta |
| :--- | :--- | :--- |
| **1. Clasificar** | Detectar frontera (Dom/App/Infra) | `templates/template_*.md` |
| **2. Narrar** | Registrar en el historial técnico | `ARCHITECTURAL_JOURNAL.md` |
| **3. Decidir** | Documentar ADR con racional | `templates/adr.md` |
| **4. Sincronizar** | Refrescar RAG Nexus | `run.py sync` |

---

## ✅ Checklist Elite

- [ ] ¿Se ha actualizado el Journal histórico?
- [ ] ¿El README especifica su capa (Dom/App/Infra)?
- [ ] ¿Se explica el **"Por Qué"** de la arquitectura?
- [ ] ¿El ADR incluye alternativas descartadas?

---
*Elite Standard v3.0.*
