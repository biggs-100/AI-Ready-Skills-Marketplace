# SKILL: Integrar Servicio Externo

## 🎯 Propósito

Integrar APIs de terceros o servicios externos de forma resiliente, asegurando el manejo de errores, reintentos (retry) y seguridad de credenciales.

## 🔍 Cuándo Activar

- Se necesita consumir una API externa (Stripe, Twilio, OpenAI, etc.).
- El usuario pide "conectar" el sistema con otro servicio.

## 📋 Pre-requisitos

- Documentación técnica del servicio externo.
- Credenciales de API (a manejar vía env vars).
- Biblioteca de cliente HTTP (ej. `httpx`).

## 🛠️ Proceso Paso a Paso

### Paso 1: Documentar Dependencia

Registrar el servicio en `config/dependencies/external_services.yaml` incluyendo timeouts y políticas de reintento.

### Paso 2: Gestión de Secretos

Asegurar que las API Keys estén en `.env` (ignorado por git) o en un gestor de secretos.

### Paso 3: Crear Cliente Resiliente

Implementar el cliente usando patrones de reintento (ej. `tenacity`) y manejo de timeouts.

### Paso 4: Implementar Fallback

Definir qué hacer si el servicio externo falla (usar cache, retornar error controlado, usar valor por defecto).

### Paso 5: Sincronizar Relaciones

Actualizar `relationships.yaml` para incluir la dependencia externa.

## ✅ Checklist de Validación

- [ ] No hay secretos en el código.
- [ ] Se implementó lógica de reintento con backoff exponencial.
- [ ] El servicio tiene timeouts configurados.
- [ ] Existe un test de integración (mockeando la respuesta del servicio).

## 🚫 Anti-patrones

❌ NO hardcodear API keys.
❌ NO hacer llamadas síncronas que bloqueen el hilo principal si la app es async.
❌ NO olvidar el manejo de Rate Limits.
