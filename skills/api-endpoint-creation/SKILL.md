# SKILL: Crear Endpoint API (FastAPI)

## 🎯 Propósito

Crear un endpoint REST siguiendo arquitectura limpia con validación, manejo de errores y tests.

## 🔍 Cuándo Activar

- Usuario dice: "crear endpoint para [entidad]" o "nueva ruta API".
- Se menciona nueva funcionalidad de API.
- Se requiere exponer lógica de negocio al frontend o clientes externos.

## 📋 Pre-requisitos

- Framework: FastAPI detectado (ver `src/api/main.py`).
- Estructura: Existe `src/api/` y `src/modules/`.
- Contexto: Leer `architecture.yaml` y `security.yaml`.

## 📝 Ejemplos de Uso

### Ejemplo 1: Endpoint para CRUD de Usuarios

**Usuario pide:** "Crea un endpoint para crear usuarios"

**Proceso:**
1. Identificar módulo: `users`
2. Definir contrato: POST /users con email, password, nombre
3. Crear schema: `UserCreateRequest` en `src/modules/users/schemas.py`
4. Implementar servicio: `UserService.create_user()`
5. Crear endpoint: `POST /users` en `src/api/users.py`
6. Tests: Happy path (201) y errores (400, 409)

### Ejemplo 2: Endpoint con Autenticación

**Usuario pide:** "Añade ruta para perfil de usuario"

**Proceso:**
1. Requerir token JWT
2. Inyectar dependencia de auth
3. Validar permisos (usuario propio o admin)
4. Retornar datos de perfil (sin password)

### Ejemplo 3: Endpoint con Paginación

**Usuario pide:** "Lista tareas con paginación"

**Proceso:**
1. Definir parámetros: `page`, `limit`, `sort`
2. Validar límites máximos (ej: limit <= 100)
3. Aplicar filtros y paginación en repositorio
4. Retornar formato: `{data: [...], pagination: {...}}`

## 🛠️ Proceso Paso a Paso

### Paso 1: Análisis de Impacto

```bash
# Verificar si ya existe ruta similar
grep -r "@router.get\|@router.post" src/api/
```

### Paso 2: Definir el Contrato

Antes de escribir código, definir el método, path, auth y permisos en una breve nota mental o comentario.

### Paso 3: Crear Schema (Pydantic)

Ubicar en `src/modules/[modulo]/schemas.py` o similar.

```python
from pydantic import BaseModel, EmailStr, Field

class ResourceCreateRequest(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    # ... otros campos
```

### Paso 4: Implementar Lógica en el Servicio

No poner lógica de negocio en el endpoint. Usar `src/modules/[modulo]/services/`.

### Paso 5: Crear el Endpoint

Usar `APIRouter` y dependencias inyectadas.

```python
@router.post("/", status_code=201)
def create_something(data: ResourceCreateRequest, service: MyService = Depends()):
    return service.create(data)
```

### Paso 6: Crear Tests

Escribir tests en `tests/` cubriendo happy path y errores (400, 401, etc.).

### Paso 7: Sincronizar Contexto

Actualizar `relationships.yaml` y `docs/api/openapi.yaml`.

## ✅ Checklist de Validación

- [ ] Endpoint usa Pydantic para validación.
- [ ] Códigos HTTP son semánticamente correctos (201 para POST, etc.).
- [ ] Hay manejo de excepciones explícito (HTTPException).
- [ ] Tests cubren happy path y errores.
- [ ] relationships.yaml actualizado.

## 🚫 Anti-patrones


❌ NO repetir este error detectado por aprendizaje: Error recurrente relacionado con: 'olvidó importar'
❌ NO repetir este error detectado por aprendizaje: Error recurrente relacionado con: 'importar datetime'
❌ NO poner lógica de negocio en el endpoint.
❌ NO retornar modelos de DB directamente (usar schemas de respuesta).
❌ NO olvidar validación de entrada.

## 📊 Métricas de Éxito

- El endpoint aparece en `/docs`.
- Los tests de integración pasan al 100%.
- El grafo de conocimiento refleja la nueva ruta.
