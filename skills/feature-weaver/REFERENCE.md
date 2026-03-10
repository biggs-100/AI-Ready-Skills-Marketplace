# Feature Weaver Reference ⚡

## 🚀 Checklist de Perfección (10 Puntos)

1. [ ] ¿El endpoint usa Pydantic para validación?
2. [ ] ¿El frontend usa TypeScript (sin 'any')?
3. [ ] ¿El componente UI tiene hover effects y transiciones?
4. [ ] ¿Se han manejado los estados de carga (Loading) y error?
5. [ ] ¿El nombre de la ruta sigue la convención kebab-case?
6. [ ] ¿Se ha actualizado el `relationships.yaml`?
7. [ ] ¿La fuente es 'Outfit'?
8. [ ] ¿Se usa HSL para colores dinámicos?
9. [ ] ¿Hay al menos un test unitario para la lógica nueva?
10. [ ] ¿El Orquestador ha validado con `run.py validate`?

## 🛠️ Comandos de Tejido

- `py run.py weave --dry-run`: Simula la creación de la feature.
- `py run.py weave --force`: Crea los archivos desde templates.

## 💡 Tip: Contrato Primero

Siempre genera el archivo `types.ts` en el frontend basado en el `schema.py` del backend para evitar errores de comunicación.
