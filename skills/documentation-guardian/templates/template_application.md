# ⚙️ Capa de Aplicación: [Nombre del Módulo]

> **Elite Rule**: Aquí residen los Casos de Uso. Esta capa orquesta el dominio pero no conoce la infraestructura.

## 🏃 Casos de Uso

- **[Caso de Uso 1]**: [Flujo de pasos]
- **[Caso de Uso 2]**: [Flujo de pasos]

## 🔌 Puertos (Interfaces)

Esta capa define cómo se comunica con el exterior mediante abstracciones:

- **[IRepository]**: Definición para persistencia.
- **[IExternalService]**: Definición para integraciones.

## 🚦 Orquestación

```mermaid
sequenceDiagram
    participant App as Aplicación (Svc)
    participant Dom as Dominio (Entidad)
    participant Infra as Infraestructura (Repo)
    
    App->>Dom: Operación de negocio
    Dom-->>App: Resultado
    App->>Infra: Persistir cambio
```

---
*Capa de orquestación (Casos de Uso).*
