import os
import re
import yaml
from pathlib import Path

ROOT = Path(__file__).parent.parent
SKILLS_DIR = ROOT / "skills"
OUTPUT_FILE = ROOT / "SKILLS_DIRECTORY.md"

def extract_frontmatter(content):
    match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1))
        except:
            return None
    return None

def main():
    skills = []
    for skill_path in SKILLS_DIR.iterdir():
        if skill_path.is_dir():
            skill_md = skill_path / "SKILL.md"
            if skill_md.exists():
                content = skill_md.read_text(encoding="utf-8")
                meta = extract_frontmatter(content)
                if meta:
                    skills.append({
                        "id": skill_path.name,
                        "name": meta.get("name", skill_path.name),
                        "description": meta.get("description", "Sin descripción."),
                        "category": meta.get("category", "Uncategorized"),
                        "version": meta.get("version", "1.0.0"),
                        "author": meta.get("author", "Unknown")
                    })

    # Sort skills by category then name
    skills.sort(key=lambda x: (x["category"], x["name"]))

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# 📚 Directorio de Habilidades (Skills Marketplace)\n\n")
        f.write("Este documento contiene el listado completo de habilidades disponibles en este marketplace, organizadas por categoría.\n\n")
        
        f.write("## 📋 Resumen Rápido\n\n")
        f.write("| Skill | Categoría | Versión | Descripción |\n")
        f.write("| :--- | :--- | :--- | :--- |\n")
        
        for s in skills:
            f.write(f"| [`{s['id']}`](#{s['id']}) | `{s['category']}` | `{s['version']}` | {s['description']} |\n")
        
        f.write("\n---\n\n")
        
        current_cat = ""
        for s in skills:
            if s["category"] != current_cat:
                current_cat = s["category"]
                f.write(f"## 📁 Categoría: {current_cat.capitalize()}\n\n")
            
            f.write(f"### <a name=\"{s['id']}\"></a> 🛠️ {s['name']}\n\n")
            f.write(f"- **ID:** `{s['id']}`\n")
            f.write(f"- **Versión:** `{s['version']}`\n")
            f.write(f"- **Autor:** {s['author']}\n")
            f.write(f"- **Descripción:** {s['description']}\n\n")
            f.write(f"[Ver documentación técnica](skills/{s['id']}/SKILL.md) | [Guía de Referencia](skills/{s['id']}/REFERENCE.md)\n\n")

    print(f"✅ Se ha generado la documentación en: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
