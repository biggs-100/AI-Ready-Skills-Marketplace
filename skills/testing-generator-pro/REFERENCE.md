# Quick Reference: Testing Generator Pro ⚡

## 🚀 Comandos Rápidos

- `python run.py generate-tests --feature <name>`: Generar tests para una feature específica.
- `python run.py validate-tests`: Verificar que todos los archivos afectados tienen un test asociado.

## 🛠️ Atajos y Constantes

- **Test Dir**: `tests/`
- **Mocks Path**: `tests/conftest.py`

## 💡 Tips de Expertos

- Siempre revisa los `TODO` en los tests generados.
- Usa `pytest-mock` para aislar la lógica de negocio de la DB.
- No borres los tests de "Happy Path", son tu primera línea de defensa.
