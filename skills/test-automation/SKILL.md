---
name: test-automation
description: "Especialista en automatización básica de tests. Configura frameworks de testing, genera fixtures y establece runners de CI para ejecución continua."
version: 2.0.0
category: quality
triggers:
  keywords:
  - test automatizado
  - pytest
  - jest
  - ci test
  - automatizar tests
  file_patterns:
  - '*'
---

# SKILL: Test Automation - Tests Automáticos y CI/CD

## 🎯 Propósito

Ejecutar, generar y mantener tests automáticos para asegurar calidad del código.

## 🔍 Cuándo Activar

- Usuario dice "ejecutar tests", "correr tests", "testear"
- Usuario menciona "coverage", "cobertura de código"
- Usuario pide "CI/CD", "integración continua"
- Antes de commits o deployments

## 📋 Pre-requisitos

- Framework de tests instalado (pytest, jest, etc.)
- Configuración de CI/CD (GitHub Actions, GitLab CI)
- Acceso a métricas de cobertura

## 🛠️ Proceso Paso a Paso

### Paso 1: Analizar Estado Actual

```bash
# Ver tests existentes
find tests/ -name "*.py" -o -name "*.ts" -o -name "*.js"

# Ver cobertura actual
coverage report 2>/dev/null || echo "Sin coverage configurado"
```

### Paso 2: Ejecutar Tests

```bash
# Python
pytest tests/ -v --tb=short

# JavaScript/TypeScript
npm test

# Cobertura
pytest --cov=src --cov-report=html
```

### Paso 3: Analizar Resultados

**Métricas a recolectar:**
- Tests totales
- Tests pasados
- Tests fallidos
- Cobertura de código (%)
- Tiempo de ejecución

### Paso 4: Generar Reporte

```bash
# Reporte de cobertura
coverage html

# Reporte de pytest
pytest --html=report.html
```

### Paso 5: Integración CI/CD

**GitHub Actions (ejemplo):**
```yaml
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: pytest tests/ -v --cov=src
```

## ✅ Checklist de Validación

- [ ] Todos los tests ejecutados
- [ ] Cobertura calculada
- [ ] Reportes generados
- [ ] CI/CD configurado
- [ ] Umbrales de calidad cumplidos

## 🚫 Anti-patrones

❌ Commit sin ejecutar tests
❌ Ignorar tests fallidos
❌ No medir cobertura de código
❌ Omitir CI/CD en producción

## 📊 Métricas de Éxito

- **Tests ejecutados:** 100% de suites
- **Tasa de pase:** >95%
- **Cobertura:** >80% (core), >60% (general)
- **Tiempo CI:** <5 minutos

## 🧠 Ejemplos de Uso

### Ejemplo 1: Ejecutar Todos los Tests

**Usuario:** "Ejecuta todos los tests"

**Proceso:**
1. Detectar framework (pytest, jest, etc.)
2. Ejecutar `pytest tests/ -v`
3. Analizar resultados
4. Mostrar resumen

**Resultado:**
```
✅ Tests ejecutados exitosamente

Total: 45 tests
Pasados: 45 ✅
Fallados: 0
Tiempo: 2.3s
Cobertura: 85%
```

### Ejemplo 2: Generar Tests para Nuevo Endpoint

**Usuario:** "Crea tests para el endpoint de usuarios"

**Proceso:**
1. Analizar endpoint existente
2. Generar casos de prueba
3. Escribir tests
4. Ejecutar y verificar

**Resultado:**
```
✅ Tests generados para POST /users

Archivos creados:
- tests/test_users_api.py
- tests/test_users_auth.py

Casos de prueba:
- POST /users (happy path) ✅
- POST /users (invalid data) ✅
- POST /users (auth fail) ✅
- GET /users (list) ✅
- GET /users/{id} (not found) ✅
```

### Ejemplo 3: Configurar CI/CD

**Usuario:** "Configura CI/CD con GitHub Actions"

**Proceso:**
1. Crear `.github/workflows/ci.yml`
2. Configurar triggers (push, PR)
3. Definir pasos de test
4. Agregar badge al README

**Resultado:**
```
✅ CI/CD configurado

Archivo: .github/workflows/ci.yml
Triggers: push, pull_request
Steps:
  - Checkout code
  - Setup Python 3.11
  - Install dependencies
  - Run tests
  - Upload coverage

Badge añadido al README:
![CI](https://github.com/.../workflows/CI/badge.svg)
```

## 📝 Template de GitHub Actions

```yaml
name: CI

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pytest pytest-cov
    
    - name: Run tests with coverage
      run: |
        pytest tests/ -v --cov=src --cov-report=xml
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
        flags: unittests
        name: codecov-umbrella
    
    - name: Upload test results
      if: always()
      uses: actions/upload-artifact@v3
      with:
        name: test-results
        path: |
          htmlcov/
          report.html