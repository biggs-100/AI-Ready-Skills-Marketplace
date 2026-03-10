# SKILL: Performance Tuning

## 🎯 Propósito

Identificar, diagnosticar y resolver cuellos de botella de rendimiento para asegurar latencias bajas y alta eficiencia en el sistema.

## 🔍 Cuándo Activar

- Se reportan "tiempos de respuesta lentos".
- Uso de CPU/Memoria elevado.
- El usuario pide "optimizar" una funcionalidad existente.

## 📋 Pre-requisitos

- Acceso a logs de performance o trazas de DB.
- Leer `relationships.yaml` para identificar queries complejas.

## 🛠️ Proceso Paso a Paso

### Paso 1: Identificación

Usar `EXPLAIN ANALYZE` en la base de datos para encontrar queries lentas o loops N+1.

### Paso 2: Optimización de Datos

Agregar índices necesarios (usar `CONCURRENTLY` en producción) o refactorizar queries.

### Paso 3: Caching

Implementar estrategias de cache (Redis) para datos de alta lectura y baja escritura.

### Paso 4: Paralelismo y Async

Refactorizar llamadas secuenciales a servicios externos usando `asyncio.gather` o background workers.

### Paso 5: Validación

Comparar las métricas de respuesta "Antes vs Después".

## ✅ Checklist de Validación

- [ ] La latencia P95 ha disminuido.
- [ ] No se han introducido race conditions en el proceso de optimización.
- [ ] El uso de cache tiene una estrategia de invalidación correcta.

## 🚫 Anti-patrones

❌ Optimización prematura sin datos de profiling.
❌ Cachear datos altamente volátiles o sensibles (PII).
❌ Olvidar que el cache también puede fallar.
