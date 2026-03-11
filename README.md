# 🛠️ Elite Skills Marketplace

> **"Micro-Inteligencias desacopladas para el ecosistema AI-Ready."**

Repositorio central de habilidades (Skills) diseñadas bajo el estándar Elite: modulares, con racional técnico y listas para instalar.

---

## 🚀 Uso Rápido

```bash
python run.py skill-list-remote       # Ver catálogo
python run.py skill-install <nombre> # Instalar skill
```

---

## 🏗️ Estructura Elite

- **`skills/`**: Directorio de habilidades instalables.
- **`templates/`**: Estructuras base para nuevas skills.
- **`docs/`**: Racional de infraestructura.

---

## 📖 Documentación
- [**Directorio de Skills**](SKILLS_DIRECTORY.md): Lista completa de capacidades.
- [**Architecture Journal**](ARCHITECTURAL_JOURNAL.md): Evolución de la forja.
- [**Guía de Contribución**](CONTRIBUTING.md): Cómo crear skills Elite.

---
*Elite Factory v3.0.*

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
