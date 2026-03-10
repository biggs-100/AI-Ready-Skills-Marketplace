# Engram Master Curator Reference 🧠⚡

## 🚀 Proceso de Limpieza Cerebral

1. [ ] **Redundancy**: ¿Hay dos engrams que digan lo mismo? Eliminar el más antiguo.
2. [ ] **Validity**: ¿Esta lección sigue siendo válida con la versión de librerías actual?
3. [ ] **Clarity**: ¿La descripción de la lección es entendible por un agente nuevo?
4. [ ] **Tags**: ¿Están bien categorizados (ej: `ux`, `api`, `auth`)?
5. [ ] **Consistency**: ¿El engram contradice el `master_instructions.yaml` actual?
6. [ ] **Pruning**: ¿Hay fragmentos sobre tareas fallidas que no aportan aprendizaje?
7. [ ] **Significance**: ¿La lección es lo suficientemente importante para persistir?
8. [ ] **Update**: ¿Se debe actualizar una skill basada en este aprendizaje?
9. [ ] **Archive**: Mover lecciones de versiones deprecadas a `archives/`.
10. [ ] **Sync**: Ejecutar `py run.py sync` tras cada curaduría manual.

## 🛠️ Comandos de Memoria

- `py run.py memory-viz`: Visualiza la conexión entre fragmentos.
- `py run.py memory-prune`: Escanea y sugiere fragmentos para borrar.

## 💡 Tip: Consolidación

Si detectas 3 o más engrams sobre el mismo error de código, es hora de crear una **Regla IDE** nueva en lugar de depender solo de la memoria.
