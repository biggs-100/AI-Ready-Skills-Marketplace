# ⚙️ Infraestructura: Skills Marketplace Factory

> **Gentleman Rule**: Los detalles técnicos de cómo se validan y distribuyen las skills mueren aquí. La lógica de negocio está en las Skills mismas.

## 🛠️ Adaptadores y Herramientas

- **Orquestador**: `run.py` (Python 3.10+)
- **Validación**: `markdownlint`, scripts internos de verificación.
- **Distribución**: Git (Sparse-checkout / URL cloning).

## 🚀 Implementación de Puertos

- **[SkillManager]**: Implementa la lógica de instalación remota y búsqueda en el catálogo.
- **[Validator]**: Implementa las reglas "Iron Law" para asegurar que ninguna skill rompa el estándar.

## ⚠️ Deuda Técnica y Acoplamiento

- **Librerías Críticas**: `pyyaml`, `gitpython`.
- **Estrategia de Cambio**: El sistema es agnóstico del contenido de las skills, lo que permite evolucionar las habilidades sin tocar el motor de distribución.

---
*Documentación generada bajo el estándar Gentleman v3.0.*
