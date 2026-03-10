# SKILL: Fine-tuning con QLoRA

## 🎯 Propósito

Realizar ajustes finos eficientes en modelos de lenguaje (LLMs) utilizando la técnica QLoRA para adaptar el modelo a tareas específicas con bajo consumo de VRAM.

## 🔍 Cuándo Activar

- Se necesita mejorar el desempeño del modelo en un dominio específico.
- El usuario solicita "entrenar" o "ajustar" un modelo localmente.

## 📋 Pre-requisitos

- GPU con al menos 8GB VRAM (para modelos de parámetros ~7B).
- Dataset preparado y validado.
- Librerías instaladas: `transformers`, `peft`, `bitsandbytes`.

## 🛠️ Proceso Paso a Paso

### Paso 1: Configuración del Entorno

Instalar dependencias: `uv pip install torch transformers peft bitsandbytes datasets accelerate`.

### Paso 2: Carga Cuantizada (4-bit)

Configurar `BitsAndBytesConfig` para cargar el modelo base optimizado para memoria.

### Paso 3: Configuración de Adaptadores LoRA

Definir los `target_modules` (usualmente los layers de atención) y los hiperparámetros de LoRA (r, alpha).

### Paso 4: Ejecutar Entrenamiento

Usar un entrenador (como `SFTTrainer`) para correr el proceso asegurando el guardado frecuente de checkpoints.

## ✅ Checklist de Validación

- [ ] El modelo carga sin errores de Out of Memory (OOM).
- [ ] La pérdida (loss) disminuye durante el entrenamiento.
- [ ] Los adaptadores se guardan correctamente por separado del modelo base.

## 🚫 Anti-patrones

❌ NO intentar entrenar sin cuantización si la VRAM es limitada.
❌ NO usar datasets sin filtrar o ruidosos.
