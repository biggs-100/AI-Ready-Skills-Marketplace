# API Documentation Reference 📚⚡

## 🚀 Checklist de Documentación Perfecta

1. [ ] **Summary**: ¿El endpoint tiene un título corto y descriptivo?
2. [ ] **Description**: ¿Se explica el "por qué" y el "qué" hace el endpoint?
3. [ ] **Examples**: ¿Los modelos Pydantic tienen un ejemplo de JSON válido?
4. [ ] **Errors**: ¿Están documentados los errores 401/403/404/500?
5. [ ] **Tags**: ¿Están agrupados los endpoints por módulos (Users, Agents, etc.)?
6. [ ] **Auth**: ¿Se especifica que requiere `X-API-Key`?
7. [ ] **Query Params**: ¿Todos los parámetros opcionales tienen descripción?
8. [ ] **Response Schema**: ¿La respuesta modelo es precisa?
9. [ ] **Service Mapping**: ¿Se menciona qué servicio de frontend usa este endpoint?
10. [ ] **Version**: ¿Se ha actualizado el número de versión de la API?

## 🛠️ Comandos de Doc

- `/docs`: URL por defecto para ver Swagger en local.
- `/redoc`: URL alternativa para ver documentación estática.

## 💡 Tip: Claridad

Usa siempre el campo `Field(description="...")` en Pydantic. Los agentes de IA (como yo) leemos esas descripciones para entender qué datos enviar sin tener que adivinar.
