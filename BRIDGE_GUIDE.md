# 🌉 Guía del Puente: Factory -> Projects

Esta guía explica cómo distribuir las habilidades desarrolladas en esta factoría a tus proyectos basados en la **AI-Ready Project Template**.

## 🚀 Método 1: Instalación Manual (Local)

Si estás trabajando en la misma máquina, puedes copiar la carpeta de la skill directamente:

1. Identifica la skill en `skills/[skill-id]`.
2. Cópiala a la carpeta `.ai/skills/market/` de tu proyecto destino.
3. Registra la skill en el `index.yaml` del proyecto destino (o deja que el `skill_manager.py` lo haga por ti si usas el comando de instalación).

## 📡 Método 2: Instalación vía CLI (Recomendado)

En el proyecto destino, utiliza el comando que configuramos:

```bash
# Formato actual (Local Path)
python run.py skill-install c:/Users/USER/Desktop/app_plantilla/ai-skills-marketplace/skills/release-notes-gen

# Formato futuro (Git)
python run.py skill-install https://github.com/tu-usuario/ai-skills-marketplace.git?path=skills/release-notes-gen
```

## 🛠️ Mantenimiento de Skills

- **Versionado**: Cada skill tiene un campo `version` en su `metadata.yaml`. Asegúrate de incrementarlo al hacer cambios críticos.
- **Validación**: Antes de distribuir, ejecuta siempre `python run.py validate [skill-name]` en esta factoría para evitar errores de parseo en el proyecto destino.

---
*Factory v1.0 | Diseñado para la escalabilidad de inteligencia.*
