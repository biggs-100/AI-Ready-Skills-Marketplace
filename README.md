# 🛠️ AI Skills Marketplace - Factory Edition

Este es un proyecto dedicado exclusivamente a la creación, testeo y distribución de **Skills** para la plantilla AI-Ready.

## 📁 Estructura del Proyecto

- `skills/`: Contiene todas las habilidades desarrolladas.
- `templates/`: Plantillas base para nuevas habilidades.
- `scripts/`: Herramientas de validación y empaquetado.
- `run.py`: Orquestador de desarrollo de skills.

## 🚀 Cómo crear una nueva Skill

Para empezar una nueva habilidad, ejecuta:

```bash
python run.py create <skill-name>
```

## 🧪 Cómo testear

Puedes validar la estructura y sintaxis de una skill con:

```bash
python run.py validate <skill-name>
```

## 📦 Distribución

Una vez terminada, la carpeta de la skill puede ser copiada al directorio `.ai/skills/market/` de cualquier proyecto compatible o servida vía URL de Git.
