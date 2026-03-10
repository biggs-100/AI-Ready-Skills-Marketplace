"""
🛠️ Skills Factory — El orquestador para crear y validar nuevas habilidades AI.
"""

import sys
import os
import shutil
import yaml
from pathlib import Path

ROOT = Path(__file__).parent
SKILLS_DIR = ROOT / "skills"
TEMPLATES_DIR = ROOT / "templates"

def cmd_help():
    print("""
╔══════════════════════════════════════════════════════════════╗
║          🛠️  AI Skills Factory — Developer CLI                ║
╚══════════════════════════════════════════════════════════════╝

  Uso: python run.py <comando> [argumentos...]

  create <name>    ✨ Crear una nueva skill desde la plantilla
  validate <name>  🧪 Validar estructura y metadatos de una skill
  list             📋 Listar todas las skills en desarrollo
  help             ❓ Mostrar esta ayuda
""")

def cmd_create(name):
    if not name:
        print("❌ Error: Debes especificar un nombre para la skill.")
        return 1
    
    dest = SKILLS_DIR / name
    if dest.exists():
        print(f"⚠️ La skill '{name}' ya existe.")
        return 1
    
    template_src = TEMPLATES_DIR / "skill_template"
    if not template_src.exists():
        # Crear template básico si no existe
        template_src.mkdir(parents=True, exist_ok=True)
        (template_src / "SKILL.md").write_text("# Skill: [Nombre]\nInstrucciones aquí...", encoding="utf-8")
        (template_src / "metadata.yaml").write_text("id: placeholder\ncategory: tools\ntriggers:\n  keywords: []", encoding="utf-8")

    shutil.copytree(template_src, dest)
    
    # Personalizar metadata.yaml
    meta_path = dest / "metadata.yaml"
    with open(meta_path, "r", encoding="utf-8") as f:
        meta = yaml.safe_load(f) or {}
    
    meta['id'] = name
    with open(meta_path, "w", encoding="utf-8") as f:
        yaml.dump(meta, f, sort_keys=False)

    print(f"✅ Skill '{name}' creada con éxito en {dest}")
    return 0

def cmd_validate(name):
    skill_path = SKILLS_DIR / name
    if not skill_path.exists():
        print(f"❌ La skill '{name}' no existe.")
        return 1
    
    required_files = ["SKILL.md", "metadata.yaml"]
    errors = []

    for f in required_files:
        if not (skill_path / f).exists():
            errors.append(f"Falta el archivo obligatorio: {f}")
    
    if not errors:
        try:
            with open(skill_path / "metadata.yaml", "r", encoding="utf-8") as f:
                meta = yaml.safe_load(f)
            if not meta.get('id'): errors.append("metadata.yaml no tiene 'id'")
            if not meta.get('triggers'): errors.append("metadata.yaml no tiene 'triggers'")
        except Exception as e:
            errors.append(f"Error parseando metadata.yaml: {e}")

    if errors:
        print(f"❌ Validación fallida para '{name}':")
        for err in errors:
            print(f"  - {err}")
        return 1
    else:
        print(f"✅ Skill '{name}' es válida y lista para el Marketplace.")
        return 0

def cmd_list():
    if not SKILLS_DIR.exists():
        print("📋 No hay skills creadas aún.")
        return
    
    print("📋 Skills en desarrollo:")
    for item in SKILLS_DIR.iterdir():
        if item.is_dir():
            print(f"  • {item.name}")

def main():
    if len(sys.argv) < 2:
        cmd_help()
        return

    command = sys.argv[1].lower()
    args = sys.argv[2:]

    if command == "create":
        sys.exit(cmd_create(args[0] if args else None))
    elif command == "validate":
        sys.exit(cmd_validate(args[0] if args else None))
    elif command == "list":
        cmd_list()
    else:
        cmd_help()

if __name__ == "__main__":
    main()
