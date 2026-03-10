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
    
    template_src = TEMPLATES_DIR / "skill_template_v2"
    if not template_src.exists():
        print("❌ Error: No se encuentra la plantilla v2.0 en templates/skill_template_v2")
        return 1

    shutil.copytree(template_src, dest)
    
    # Personalizar SKILL.md (Extraer y actualizar Frontmatter)
    skill_md_path = dest / "SKILL.md"
    content = skill_md_path.read_text(encoding="utf-8")
    
    # Regex simple para encontrar el frontmatter
    import re
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        frontmatter = yaml.safe_load(match.group(1)) or {}
        frontmatter['name'] = name
        new_frontmatter = yaml.dump(frontmatter, sort_keys=False)
        new_content = f"---\n{new_frontmatter}---\n" + content[match.end():]
        skill_md_path.write_text(new_content, encoding="utf-8")

    print(f"✅ Skill '{name}' (v2.0) creada con éxito en {dest}")
    return 0

def cmd_validate(name):
    skill_path = SKILLS_DIR / name
    if not skill_path.exists():
        print(f"❌ La skill '{name}' no existe.")
        return 1
    
    required_files = ["SKILL.md", "REFERENCE.md"]
    required_dirs = ["docs", "examples", "templates"]
    errors = []

    for f in required_files:
        if not (skill_path / f).exists():
            errors.append(f"Falta el archivo obligatorio: {f}")
    
    for d in required_dirs:
        if not (skill_path / d).is_dir():
            errors.append(f"Falta el directorio obligatorio: {d}/")

    if not errors:
        try:
            content = (skill_path / "SKILL.md").read_text(encoding="utf-8")
            import re
            match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
            if not match:
                errors.append("SKILL.md no tiene Frontmatter YAML")
            else:
                meta = yaml.safe_load(match.group(1))
                if not meta.get('name'): errors.append("Frontmatter no tiene 'name'")
                if not meta.get('triggers'): errors.append("Frontmatter no tiene 'triggers'")
        except Exception as e:
            errors.append(f"Error parseando Frontmatter: {e}")

    if errors:
        print(f"❌ Validación fallida para '{name}':")
        for err in errors:
            print(f"  - {err}")
        return 1
    else:
        print(f"✅ Skill '{name}' cumple con el estándar v2.0.")
        return 0

def cmd_list():
    if not SKILLS_DIR.exists():
        print("📋 No hay skills creadas aún.")
        return
    
    print("📋 Skills en desarrollo:")
    for item in SKILLS_DIR.iterdir():
        if item.is_dir():
            # Intentar leer descripción del SKILL.md
            desc = ""
            try:
                skill_md = item / "SKILL.md"
                if skill_md.exists():
                    content = skill_md.read_text(encoding="utf-8")
                    import re
                    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
                    if match:
                        meta = yaml.safe_load(match.group(1))
                        desc = f" - {meta.get('description', '')[:50]}..."
            except: pass
            print(f"  • {item.name}{desc}")

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
