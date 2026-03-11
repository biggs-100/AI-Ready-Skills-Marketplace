---
name: git-integration
description: "Especialista en automatización de flujos Git. Gestiona branches, merge strategies, generación de changelogs y automatización de tags y releases."
version: 2.0.0
category: devops
triggers:
  keywords:
  - git
  - branch
  - merge
  - release
  - changelog
  - tag
  file_patterns:
  - '*'
---

# SKILL: Git & GitHub Integration

## 🎯 Propósito

Integrar control de versiones y colaboración con GitHub.

## 🔍 Cuándo Activar

- Usuario dice "git", "commit", "push", "pull"
- Usuario menciona "pull request", "PR"
- Usuario quiere "branch", "merge"
- Usuario solicita "code review"

## 🛠️ Proceso Paso a Paso

### Paso 1: Configurar Git

```bash
# Configurar usuario
git config user.name "Tu Nombre"
git config user.email "tu@email.com"

# Configurar remote
git remote add origin https://github.com/usuario/repo.git
```

### Paso 2: Flujo de Trabajo Git

```
main
  |
  +-- feature/nueva-funcion
        |
        +-- commit, push
        |
        +-- PR a main
```

### Paso 3: Comandos Básicos

```bash
# Ver estado
git status

# Agregar cambios
git add .

# Commit
git commit -m "feat: descripción del cambio"

# Push
git push origin feature/branch

# Pull
git pull origin main
```

### Paso 4: Pull Requests

```bash
# Crear branch
git checkout -b feature/nueva-funcion

# Push al remote
git push -u origin feature/nueva-funcion

# Crear PR (desde GitHub CLI)
gh pr create --title "Nueva función" --body "Descripción"
```

### Paso 5: Code Review

```bash
# Descargar PR localmente
gh pr checkout 123

# Revisar cambios
git diff main...feature/branch

# Comentarios en PR
gh pr comment 123 --body "Comentario de revisión"
```

## ✅ Checklist de Validación

- [ ] Git configurado correctamente
- [ ] Remote configurado
- [ ] Branch strategy definida
- [ ] PR process documentado
- [ ] Code review establecido

## 🚫 Anti-patrones

❌ Commits sin mensaje descriptivo
❌ Push a main directamente
❌ Ignorar conflictos de merge
❌ No revisar PRs

## 📊 Métricas de Éxito

- **Commits por día:** > 5
- **PRs aprobados:** > 90%
- **Tiempo de review:** < 24h
- **Conflictos:** < 5%

## 🧠 Ejemplos de Uso

### Ejemplo 1: Crear Feature Branch

**Usuario:** "Crea branch para nueva función"

**Proceso:**
1. Verificar estado actual
2. Crear branch
3. Configurar tracking
4. Confirmar creación

**Resultado:**
```
✅ Branch creado exitosamente

Nombre: feature/usuarios-crud
Base: main
Tracking: origin/feature/usuarios-crud
```

### Ejemplo 2: Crear Pull Request

**Usuario:** "Crea PR para los cambios"

**Proceso:**
1. Push changes
2. Crear PR con título y descripción
3. Agregar reviewers
4. Confirmar creación

**Resultado:**
```
✅ Pull Request creado

Número: #123
Título: feat: CRUD de usuarios
URL: https://github.com/.../pull/123
Reviewers: @user1, @user2
```

### Ejemplo 3: Revisar Código

**Usuario:** "Revisa el PR #123"

**Proceso:**
1. Checkout del PR
2. Revisar cambios
3. Agregar comentarios
4. Aprobar o solicitar cambios

**Resultado:**
```
✅ Revisión completada

PR #123: feat: CRUD de usuarios
Cambios: 3 archivos, +45 -12
Comentarios: 2 sugerencias
Estado: Aprobado con sugerencias
```

## 📝 Git Flow

```bash
# Iniciar feature
git checkout main
git pull origin main
git checkout -b feature/nueva-funcion

# Desarrollar
git add .
git commit -m "feat: implementar nueva funcionalidad"

# Push
git push -u origin feature/nueva-funcion

# Crear PR (GitHub CLI)
gh pr create \
  --title "feat: nueva funcionalidad" \
  --body "Descripción detallada" \
  --reviewer @user1,@user2 \
  --label "feature,enhancement"

# Después de aprobación
git checkout main
git pull origin main
git merge feature/nueva-funcion
git push origin main
```

## ⚠️ Mejores Prácticas

- **Commits:** Mensajes descriptivos (Conventional Commits)
- **Branches:** `feature/`, `bugfix/`, `hotfix/`
- **PRs:** Título claro, descripción detallada
- **Reviews:** Mínimo 1 aprobador