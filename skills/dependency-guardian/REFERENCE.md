# Dependency Guardian Reference 🛡️⚡

## 🚀 Comandos de Supervivencia

| Tarea | Backend (Python) | Frontend (Node.js) |
| :--- | :--- | :--- |
| **Auditoría** | `pip-audit` | `npm audit` |
| **Listado Outdated** | `pip list --outdated` | `npm outdated` |
| **Actualización** | `pip install --upgrade <pkg>` | `npm update` |
| **Limpieza** | `pip-autoremove` | `npm prune` |

## 🛡️ Checklist de Salud (10 Puntos)

1. [ ] **No Overkill**: ¿Hay librerías gigantes instaladas para tareas pequeñas?
2. [ ] **Lock Files**: ¿Existen y están sincronizados `package-lock.json` o `poetry.lock`?
3. [ ] **Dev Dependencies**: ¿Las librerías de testing están correctamente en `devDependencies`?
4. [ ] **License Check**: ¿Todas las librerías permiten uso comercial?
5. [ ] **Direct Imports**: ¿Se importan librerías que no están en el `package.json`?
6. [ ] **Node Version**: ¿El proyecto especifica los motores de Node/Python compatibles?
7. [ ] **Security Fixes**: ¿Se han aplicado todos los parches de seguridad recomendados?
8. [ ] **Duplicate Pkgs**: ¿Hay múltiples versiones de la misma librería instaladas?
9. [ ] **Dead Code**: ¿Hay dependencias del `package.json` que no se usan en el código?
10. [ ] **Vendor Lock-in**: ¿Es fácil sustituir una dependencia clave si falla?

## 💡 Tip: Actualización

Nunca actualices "Major versions" (`1.x` -> `2.x`) masivamente. Hazlo una por una y corre los tests de regresión después de cada cambio.
