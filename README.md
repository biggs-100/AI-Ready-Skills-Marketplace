# 🛠️ AI Skills Marketplace — Elite Factory Edition

> **"La inteligencia no es solo código, es el racional acumulado detrás de cada decisión."** — *Elite Factory Vision*

Este repositorio es la **Forja de Inteligencia** para el ecosistema AI-Ready. Aquí no solo guardamos scripts; curamos habilidades de élite diseñadas para ser desacopladas, escalables y, sobre todo, justificadas por un racional técnico sólido.

## 🎯 Visión Estratégica (The "Why")

Las IAs suelen fallar por falta de contexto o por seguir patrones genéricos. Este marketplace existe para:

1. **Cerrar la Brecha de Contexto**: Cada skill inyecta años de mejores prácticas (Hexagonal, Clean Code) directamente en el proyecto del usuario.
2. **Gobernanza Automatizada**: Las habilidades actúan como guardianes que impiden la entrada de deuda técnica.
3. **Desacoplamiento Total**: Diseñadas bajo el principio de responsabilidad única, permitiendo que el orquestador las invoque solo cuando son estrictamente necesarias.

## 🏗️ Arquitectura de la Factoría

Mantenemos una estructura de capas para asegurar que el marketplace sea mantenible:

- **`skills/` (Dominio)**: El corazón de la factoría. Cada carpeta es una unidad de inteligencia independiente con su propia lógica y contratos.
- **`templates/` (Aplicación)**: Casos de uso base para la creación acelerada de nuevas habilidades.
- **`scripts/` & `run.py` (Infraestructura)**: El utillaje necesario para validar, empaquetar y distribuir la inteligencia.

---

## 🚀 Ciclo de Vida del Desarrollo

### 1. Creación con Racional

Para empezar una nueva habilidad basada en el estándar **Gentleman Edition**:

```bash
python run.py create <skill-name>
```

### 2. Validación "Iron Law"

No permitimos código sin integridad. Valida tu skill contra las reglas del marketplace:

```bash
python run.py validate <skill-name>
```

### 3. Distribución E2E

Las habilidades se sirven como **Micro-Inteligencias** que el orquestador principal puede instalar vía Git:

```bash
# En el proyecto destino:
python run.py skill-install <skill-name>
```

---

## 📔 Diario de Arquitectura

Consulta la evolución y decisiones críticas en nuestro [Architecture Journal](ARCHITECTURAL_JOURNAL.md).

## 📚 Catálogo de Habilidades

Explora el [Directorio Completo de Skills](SKILLS_DIRECTORY.md) para encontrar la herramienta exacta para tu desafío.

---
*Mantenido con rigor por Antigravity Orchestrator.*
