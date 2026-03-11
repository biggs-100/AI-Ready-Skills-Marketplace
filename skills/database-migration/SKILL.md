---
name: database-migration
description: "Especialista en el diseño, generación y ejecución segura de migraciones de base de datos. Soporta rollback, verificación de integridad y generación de scripts SQL/ORM para PostgreSQL, SQLite y MySQL."
version: 2.0.0
category: devops
triggers:
  keywords:
  - migración
  - alterar tabla
  - nueva columna
  - schema change
  - alembic
  file_patterns:
  - '*'
---

# SKILL: Crear Migración de Base de Datos

## 🎯 Propósito

Generar migraciones seguras con rollback, validación de integridad y sin pérdida de datos.

## 🔍 Cuándo Activar

- Usuario pide: "modificar tabla", "añadir columna", "crear índice" o "nueva tabla".
- Se detectan cambios en los modelos ORM.

## 📋 Pre-requisitos

- Acceso a herramientas de migración (Alembic/Prisma).
- Leer `relationships.yaml` para entender quién usa las tablas afectadas.
- Leer `security.yaml` por temas de PII.

## 🛠️ Proceso Paso a Paso

### Paso 1: Analizar Impacto

Evaluar el riesgo (Bajo, Medio, Alto) según el tipo de cambio. Evitar locks largos en tablas grandes.

### Paso 2: Generar Migración

```bash
# Alembic
alembic revision --autogenerate -m "descripcion_del_cambio"
```

### Paso 3: Revisar el script de Migración

Asegurarse de que tenga tanto `upgrade()` como `downgrade()`. Verificar nombres snake_case.

### Paso 4: Probar Rollback localmente

Aplicar la migración y revertirla inmediatamente para confirmar que el `downgrade` funciona perfecto.

### Paso 5: Actualizar Código

Actualizar modelos ORM, Repositorios y Schemas para reflejar el cambio en la DB.

### Paso 6: Sincronizar Contexto

Ejecutar `python run.py sync` para actualizar el grafo de relaciones de datos.

## ✅ Checklist de Validación

- [ ] La migración es reversible (tiene DOWN).
- [ ] Se usó `CONCURRENTLY` para nuevos índices en tablas grandes.
- [ ] No hay pérdida de datos en el proceso.
- [ ] Se han actualizado los modelos ORM.
- [ ] relationships.yaml refleja el nuevo schema.

## 🚫 Anti-patrones

❌ NO borrar columnas sin antes haber actualizado el código que las usa.
❌ NO ejecutar migraciones sin probar el rollback primero.
❌ NO hardcodear IDs específicos en migraciones de datos.

## 📊 Métricas de Éxito

- Migración aplicada sin errores en entorno local.
- Rollback exitoso.
- Cero tiempo de inactividad (zero-downtime) en proyecciones.
