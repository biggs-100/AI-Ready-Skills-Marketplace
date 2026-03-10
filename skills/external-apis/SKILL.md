# SKILL: External APIs Integration

## 🎯 Propósito

Integrar y consumir APIs externas en el proyecto.

## 🔍 Cuándo Activar

- Usuario dice "integrar API", "consumir servicio externo"
- Usuario menciona "webhook", "callback"
- Usuario necesita datos de APIs de terceros
- Usuario pide conectar servicios externos

## 🛠️ Proceso Paso a Paso

### Paso 1: Identificar API

Analizar:
- Endpoint de la API
- Método de autenticación (API Key, OAuth, JWT)
- Formato de datos (JSON, XML)
- Rate limits

### Paso 2: Crear Cliente API

```python
# src/external/api_client.py
import requests
from typing import Optional, Dict, Any

class APIClient:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    
    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        response = requests.get(
            f"{self.base_url}/{endpoint}",
            headers=self.headers,
            params=params
        )
        response.raise_for_status()
        return response.json()
    
    def post(self, endpoint: str, data: Dict) -> Dict:
        response = requests.post(
            f"{self.base_url}/{endpoint}",
            headers=self.headers,
            json=data
        )
        response.raise_for_status()
        return response.json()
```

### Paso 3: Configurar Variables de Entorno

```bash
# .env
EXTERNAL_API_KEY=your_api_key_here
EXTERNAL_API_URL=https://api.example.com
```

### Paso 4: Integrar en Servicio

```python
# src/modules/users/services.py
from external.api_client import APIClient
import os

class UserService:
    def __init__(self):
        self.api_client = APIClient(
            base_url=os.getenv("EXTERNAL_API_URL"),
            api_key=os.getenv("EXTERNAL_API_KEY")
        )
    
    def sync_with_external(self, user_id: str):
        """Sincroniza usuario con servicio externo"""
        data = {"user_id": user_id}
        return self.api_client.post("users/sync", data)
```

### Paso 5: Manejar Errores

```python
# src/external/error_handler.py
import logging
from requests.exceptions import RequestException

def handle_api_error(error: RequestException) -> Dict:
    """Maneja errores de API externa"""
    logging.error(f"API Error: {error}")
    
    if isinstance(error, requests.exceptions.Timeout):
        return {"error": "timeout", "retry": True}
    elif isinstance(error, requests.exceptions.HTTPError):
        return {"error": "http_error", "status": error.response.status_code}
    else:
        return {"error": "unknown", "retry": False}
```

## ✅ Checklist de Validación

- [ ] Cliente API creado
- [ ] Variables de entorno configuradas
- [ ] Integración en servicio existente
- [ ] Manejo de errores implementado
- [ ] Tests de integración creados

## 🚫 Anti-patrones

❌ Hardcodear API keys
❌ No manejar errores de red
❌ Ignorar rate limits
❌ No implementar retry logic

## 📊 Métricas de Éxito

- **Tiempo de respuesta:** < 500ms
- **Disponibilidad:** > 99.9%
- **Tasa de error:** < 0.1%
- **Rate limit:** Respetado siempre

## 🧠 Ejemplos de Uso

### Ejemplo 1: Integrar API de Pagos

**Usuario:** "Integra Stripe para pagos"

**Proceso:**
1. Instalar SDK: `pip install stripe`
2. Configurar API key en `.env`
3. Crear cliente de pagos
4. Implementar endpoint de checkout

**Resultado:**
```
✅ API Stripe integrada

Archivos creados:
- src/external/stripe_client.py
- src/modules/payments/services.py
- tests/test_stripe_integration.py

Endpoints creados:
- POST /payments/checkout
- POST /payments/webhook
```

### Ejemplo 2: Webhook de Notificaciones

**Usuario:** "Recibe webhooks de Slack"

**Proceso:**
1. Crear endpoint webhook
2. Validar firma de Slack
3. Procesar mensaje
4. Respond 200 OK

**Resultado:**
```
✅ Webhook de Slack configurado

Endpoint: POST /webhooks/slack
Validación: Firma HMAC
Procesamiento: Async queue
```

## 📝 Template de Cliente API

```python
# src/external/api_client.py
import os
import requests
from typing import Optional, Dict, Any
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class APIClient:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        # Retry strategy
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session = requests.Session()
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
    
    def request(self, method: str, endpoint: str, **kwargs) -> Dict:
        url = f"{self.base_url}/{endpoint}"
        response = self.session.request(
            method,
            url,
            headers=self.headers,
            **kwargs
        )
        response.raise_for_status()
        return response.json()
    
    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        return self.request("GET", endpoint, params=params)
    
    def post(self, endpoint: str, json: Optional[Dict] = None) -> Dict:
        return self.request("POST", endpoint, json=json)
    
    def put(self, endpoint: str, json: Optional[Dict] = None) -> Dict:
        return self.request("PUT", endpoint, json=json)
    
    def delete(self, endpoint: str) -> Dict:
        return self.request("DELETE", endpoint)
```

## ⚠️ Seguridad

- **Nunca** commitear API keys
- Usar variables de entorno siempre
- Implementar rotación de keys
- Loguear requests sin sensitive data