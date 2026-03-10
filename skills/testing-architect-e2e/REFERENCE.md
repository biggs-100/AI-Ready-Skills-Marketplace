# Testing Architect E2E Reference 🧪⚡

## 🚀 Checklist de Pruebas Robustas

1. [ ] **Selectors**: ¿Se usan IDs únicos o `data-testid`?
2. [ ] **Waiters**: ¿Se evita `sleep()` en favor de `waitForSelector()`?
3. [ ] **Database Reset**: ¿Se limpia el estado antes de cada prueba?
4. [ ] **Navigation**: ¿Se prueba la respuesta en diferentes tamaños de pantalla (Mobile/Desktop)?
5. [ ] **API Validation**: ¿Se verifican las llamadas de red (Network intercepts)?
6. [ ] **Loading States**: ¿Se valida que aparezcan/desaparezcan los spinners de carga?
7. [ ] **Error UI**: ¿Se comprueba que el usuario reciba mensajes de error claros?
8. [ ] **Accessibility**: ¿Los elementos interactivos son accesibles vía teclado?
9. [ ] **Reports**: ¿Se generan reportes HTML automáticos en CI?
10. [ ] **Speed**: ¿La suite de pruebas corre en menos de 5 minutos?

## 🛠️ Comandos de Ejecución

- `npx playwright test`: Ejecuta todas las pruebas.
- `npx playwright show-report`: Visualiza los resultados del último test.

## 💡 Tip: Selectores Inteligentes

Evita usar clases CSS para los tests, ya que cambian con el diseño. Usa siempre `data-testid="submit-btn"` para que el test sea inmune a cambios estéticos.
