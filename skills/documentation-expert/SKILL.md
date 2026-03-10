# Skill: Documentation Expert ✍️

## 🎯 Objetivo

Transformar el código y la arquitectura del sistema en documentación técnica de alta calidad, coherente y fácil de entender, tanto para humanos como para otros agentes de IA.

## 触发 Triggers

- "documentar módulo [nombre]"
- "generar guia técnica"
- "explicar flujo de [función]"
- "crear README"
- "actualizar documentación"

## 🛠️ Workflow

### 1. Análisis de Contexto

Antes de escribir, la IA debe:

- Leer el archivo `relationships.yaml` para entender las dependencias del módulo.
- Escanear el código fuente para extraer clases, funciones y sus decoradores.
- Revisar si existen ADRs (Architectural Decision Records) que justifiquen el diseño actual.

### 2. Estructura de Documentación Estándar

Cada módulo documentado debe seguir este esquema:

- **Resumen Ejecutivo**: ¿Qué hace este módulo en una frase?
- **Arquitectura**: Diagrama Mermaid de flujo o de clases.
- **Puntos de Entrada**: Detalle de APIs, rutas o funciones públicas.
- **Ejemplos de Uso**: Snippets de código claros y probados.
- **Seguridad y Observabilidad**: Mención de validaciones y logs implementados.

### 3. Calidad de Código (Docstrings)

Si se solicita "docstrings", la IA debe:

- Aplicar formato Google Style o NumPy Style según la convención del proyecto.
- Incluir tipos de datos, excepciones lanzadas y valores de retorno.

### 4. Sincronización Cerebral

Tras generar o actualizar un archivo `.md`:

- Verificar que el archivo esté en la carpeta `docs/`.
- Sugerir al usuario ejecutar `python run.py sync` para actualizar el Manual RAG.

## ✅ Output esperado

Archivos Markdown profesionales y actualizados, o código fuente con docstrings enriquecidos.
