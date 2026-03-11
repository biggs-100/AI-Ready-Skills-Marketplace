# 🔌 Capa de Infraestructura: [Nombre del Módulo]

> **Gentleman Rule**: Los detalles técnicos (DB, HTTP Clients, Frameworks) mueren aquí. Implementamos las interfaces de la Aplicación.

## 🛠️ Adaptadores y Herramientas

- **Persistencia**: [SQLAlchemy, Prisma, etc.]
- **Integración**: [Axios, Boto3, etc.]
- **Framework**: [FastAPI, NestJS, etc.]

## 🚀 Implementación de Puertos

- **[SqlUserRepository]**: Implementa `IUserRepository`.
- **[S3FileStorage]**: Implementa `IFileStorage`.

## ⚠️ Deuda Técnica y Acoplamiento

- **Librerías Críticas**: [Lista de dependencias externas pesadas]
- **Estrategia de Cambio**: [¿Qué tan difícil es cambiar la DB?]

---
*Capa de detalles técnicos y adaptadores.*
