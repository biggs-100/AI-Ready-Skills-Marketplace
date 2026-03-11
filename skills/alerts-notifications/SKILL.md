---
name: alerts-notifications
description: "Especialista en diseño e implementación de sistemas de alertas y notificaciones. Configura canales (email, SMS, push, webhooks) y gestiona reglas de enrutamiento inteligente."
version: 2.0.0
category: operations
triggers:
  keywords:
  - alertas
  - notificaciones
  - email
  - push notification
  - webhook
  file_patterns:
  - '*'
---

# SKILL: Alerts & Notifications

## 🎯 Propósito

Configurar notificaciones automáticas para eventos importantes del proyecto.

## 🔍 Cuándo Activar

- Usuario dice "notificaciones", "alerts", "alertas"
- Usuario quiere "Slack", "Discord", "Email"
- Usuario pide "monitoreo", "monitoring"
- Usuario necesita "webhooks"

## 🛠️ Proceso Paso a Paso

### Paso 1: Configurar Canales

```yaml
# .ai/alerts/config.yaml
channels:
  slack:
    webhook_url: ${SLACK_WEBHOOK_URL}
    channel: "#dev-notifications"
    enabled: true
  
  discord:
    webhook_url: ${DISCORD_WEBHOOK_URL}
    enabled: true
  
  email:
    smtp_server: smtp.gmail.com
    port: 587
    sender: notifications@project.com
    recipients:
      - dev@example.com
    enabled: false
```

### Paso 2: Definir Eventos

```yaml
events:
  commit:
    severity: "info"
    channels: ["slack"]
    message: "Nuevo commit: {message} por {author}"
  
  error:
    severity: "critical"
    channels: ["slack", "discord", "email"]
    message: "❌ Error en {service}: {error}"
  
  deploy:
    severity: "info"
    channels: ["slack"]
    message: "🚀 Desplegado a {environment}"
  
  test_fail:
    severity: "warning"
    channels: ["slack"]
    message: "⚠️ Tests fallidos en {branch}"
```

### Paso 3: Implementar Notificador

```python
# .ai/scripts/notifier.py
import os
import requests
from datetime import datetime

class Notifier:
    def __init__(self):
        self.slack_url = os.getenv("SLACK_WEBHOOK_URL")
        self.discord_url = os.getenv("DISCORD_WEBHOOK_URL")
    
    def send_slack(self, message, color="#36a64f"):
        if not self.slack_url:
            return
        
        payload = {
            "attachments": [{
                "color": color,
                "text": message,
                "ts": datetime.now().timestamp()
            }]
        }
        
        requests.post(self.slack_url, json=payload)
    
    def send_discord(self, message):
        if not self.discord_url:
            return
        
        payload = {"content": message}
        requests.post(self.discord_url, json=payload)
    
    def notify(self, event_type, data):
        messages = {
            "commit": f"📝 Commit: {data['message']} por {data['author']}",
            "error": f"❌ Error: {data['error']} en {data['service']}",
            "deploy": f"🚀 Deploy a {data['environment']}",
            "test_fail": f"⚠️ Tests fallidos en {data['branch']}"
        }
        
        message = messages.get(event_type, data.get("message", ""))
        self.send_slack(message)
        self.send_discord(message)
```

### Paso 4: Integrar con Watcher

```python
# .ai/scripts/watcher.py (modificado)
from .notifier import Notifier

class AIProjectWatcher:
    def __init__(self):
        self.notifier = Notifier()
    
    def on_error(self, error):
        self.notifier.notify("error", {
            "error": str(error),
            "service": "watcher"
        })
```

## ✅ Checklist de Validación

- [ ] Webhooks configurados
- [ ] Eventos definidos
- [ ] Notificador implementado
- [ ] Integración con watcher
- [ ] Pruebas de envío

## 🚫 Anti-patrones

❌ Notificar todo (spam)
❌ Exponer webhooks públicos
❌ Ignorar configuraciones
❌ No rotar secrets

## 📊 Métricas de Éxito

- **Entregas:** 100% exitosas
- **Latencia:** < 1s
- **Falsos positivos:** < 5%
- **Uso:** Solo eventos importantes

## 🧠 Ejemplos de Uso

### Ejemplo 1: Configurar Slack

**Usuario:** "Envía notificaciones a Slack"

**Proceso:**
1. Crear webhook en Slack
2. Configurar `.env` con webhook URL
3. Testear notificación
4. Confirmar recepción

**Resultado:**
```
✅ Slack configurado

Webhook: https://hooks.slack.com/...
Canal: #dev-notifications
Test: ✅ Recibido
```

### Ejemplo 2: Alerta de Error

**Automático cuando ocurre error:**
```
❌ Error en API: Connection timeout
Servicio: src/api/main.py:45
Tiempo: 2026-03-09 14:30:00
```

### Ejemplo 3: Notificación de Deploy

**Automático al desplegar:**
```
🚀 Deploy exitoso a producción
Entorno: production
Commit: abc123 feat: nueva funcionalidad
Tiempo: 2026-03-09 15:00:00
```

## 📝 Webhooks Populares

```python
# Slack
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/..."

# Discord
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/..."

# Microsoft Teams
TEAMS_WEBHOOK_URL = "https://outlook.office.com/webhook/..."

# Email (SendGrid)
SENDGRID_API_KEY = "SG..."
```

## ⚠️ Seguridad

- **Nunca** commitear webhooks URLs
- Usar variables de entorno siempre
- Rotar webhooks si se comprometen
- Validar origen de peticiones