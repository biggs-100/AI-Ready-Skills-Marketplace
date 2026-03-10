import os
import yaml
import re
from pathlib import Path

ROOT = Path(r"c:\Users\USER\Desktop\app_plantilla\ai-skills-marketplace")
SKILLS_DIR = ROOT / "skills"

def validate_skill(name):
    skill_path = SKILLS_DIR / name
    required_files = ["SKILL.md", "REFERENCE.md"]
    required_dirs = ["docs", "examples", "templates"]
    errors = []

    for f in required_files:
        if not (skill_path / f).exists():
            errors.append(f"Falta el archivo: {f}")
    
    for d in required_dirs:
        if not (skill_path / d).is_dir():
            errors.append(f"Falta el directorio: {d}/")

    if not errors:
        try:
            skill_md = skill_path / "SKILL.md"
            content = skill_md.read_text(encoding="utf-8")
            match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
            if not match:
                errors.append("SKILL.md no tiene Frontmatter YAML")
            else:
                meta = yaml.safe_load(match.group(1))
                if not meta.get('name'): errors.append("Frontmatter no tiene 'name'")
                if not meta.get('triggers'): errors.append("Frontmatter no tiene 'triggers'")
        except Exception as e:
            errors.append(f"Error parseando Frontmatter: {e}")

    return errors

if __name__ == "__main__":
    skills = [d.name for d in SKILLS_DIR.iterdir() if d.is_dir()]
    report = []
    
    print(f"Buscando skills en: {SKILLS_DIR}")
    print(f"Total skills encontradas: {len(skills)}")
    
    for s in skills:
        errors = validate_skill(s)
        if errors:
            report.append(f"❌ {s}: {', '.join(errors)}")
        else:
            report.append(f"✅ {s}: OK")
            
    for line in report:
        print(line)
