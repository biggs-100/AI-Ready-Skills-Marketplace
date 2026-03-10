# SKILL: Integración con Herramientas Externas

## 🎯 Propósito

Interactuar con herramientas de desarrollo externas (Git, Docker, APIs, servicios cloud).

## 🔍 Cuándo Activar

- Usuario menciona "git", "commit", "push"
- Usuario menciona "docker", "container", "deploy"
- Usuario necesita ejecutar comandos del sistema
- Usuario solicita interacción con APIs externas

## 📋 Pre-requisitos

- Acceso a shell del sistema
- Herramientas instaladas (git, docker, etc.)
- Permisos adecuados

## 🛠️ Proceso Paso a Paso

### Paso 1: Identificar Herramienta

Analizar la solicitud:
- Git → Control de versiones
- Docker → Contenedores
- API → Servicios externos
- Cloud → AWS/GCP/Azure

### Paso 2: Verificar Disponibilidad

Comprobar si la herramienta está instalada:
```bash
git --version
docker --version
```

### Paso 3: Ejecutar Comando

Usar `bash` tool para ejecutar comandos seguros:
```bash
# Git
git status
git diff
git log

# Docker
docker ps
docker logs [container]

# APIs (curl)
curl -X GET https://api.example.com/health
```

### Paso 4: Procesar Resultado

Interpretar la salida y responder al usuario:
- Mostrar resumen de cambios
- Identificar errores
- Sugerir acciones correctivas

### Paso 5: Documentar Acción

Registrar en `.ai/memory/commands.log` si es necesario:
```yaml
- date: 2026-03-09
  command: git commit -m "feat: ..."
  result: success
  output: "[resumen]"
```

## ✅ Checklist de Validación

- [ ] Herramienta verificada y disponible
- [ ] Comando ejecutado con éxito
- [ ] Resultado interpretado correctamente
- [ ] Respuesta clara al usuario
- [ ] Acciones documentadas si es necesario

## 🚫 Anti-patrones

❌ Ejecutar comandos destructivos sin confirmación
❌ Ignorar errores en la salida
❌ Ejecutar comandos sin verificar contexto
❌ No hacer backup antes de cambios críticos

## 📊 Métricas de Éxito

- **Comandos ejecutados:** Cantidad de operaciones
- **Tasa de éxito:** % de comandos que funcionan
- **Tiempo de respuesta:** Velocidad de ejecución
- **Satisfacción del usuario:** Confirmación de éxito

## 🧠 Ejemplos de Uso

### Ejemplo 1: Operaciones Git

**Usuario:** "¿Qué archivos he modificado?"

**Proceso:**
1. Ejecutar `git status`
2. Parsear salida
3. Mostrar archivos modificados, agregados, eliminados
4. Sugerir próximo paso (commit, stash, etc.)

### Ejemplo 2: Docker Logs

**Usuario:** "¿Por qué el container falla?"

**Proceso:**
1. Ejecutar `docker ps -a`
2. Identificar container fallido
3. Ejecutar `docker logs [container]`
4. Analizar errores
5. Sugerir solución

### Ejemplo 3: API Health Check

**Usuario:** "Verifica si la API está arriba"

**Proceso:**
1. Ejecutar `curl -X GET http://localhost:8000/health`
2. Verificar código de respuesta
3. Mostrar resultado
4. Sugerir acciones si está caída