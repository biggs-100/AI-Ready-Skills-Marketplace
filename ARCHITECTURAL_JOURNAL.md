# 📔 Architecture Decision Journal — Skills Marketplace

## 🧭 Visión Estratégica

Consolidar un repositorio centralizado de "Micro-Inteligencias" (Skills) que sigan el estándar **Elite Edition**: Desacopladas, con racional explícito y orientadas a Clean Architecture.

---

## 📅 MARZO 2026

### Resumen de Evolución

Lanzamiento oficial del marketplace y transición al estándar **v3.0 (Elite Edition)**. Se ha refactorizado la skill fundamental `documentation-guardian` para actuar como el estándar de oro del repositorio.

#### ⚡ Decisiones Críticas

- **[ADR-001] Distributed Intelligence**: Se decidió que las skills no compartan código entre sí para maximizar el desacoplamiento. -> *Impacto: Desacoplamiento Máximo.*
- **[ADR-002] Git-Based Installation**: Se implementó la instalación vía Git Sparse-checkout en el orquestador principal. -> *Impacto: Instalación ligera y selectiva.*
- **[ADR-003] Gentleman Standards**: Inclusión obligatoria de "Por qué" y "Alternativas" en todos los documentos de diseño. -> *Impacto: Reducción de deuda técnica por obsolescencia de contexto.*

#### 🏗️ Estado de las Capas (Marketplace Factory)

- **Dominio (Skills)**: 32+ habilidades migradas al estándar básico. Comienzo de la migración de skills core al estándar Gentleman (v3.0).
- **Aplicación (Templates)**: Plantillas actualizadas para incluir `REFERENCE.md` y `metadata.yaml` obligatorio.
- **Infraestructura (Scripts)**: `run.py` actualizado para soportar validaciones cruzadas y empaquetado automático.

---
*Mantenido por el Orquestador para preservar la herencia técnica del proyecto.*
