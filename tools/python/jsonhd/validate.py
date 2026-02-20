import json
from pathlib import Path
import jsonschema

def _find_repo_root(start_dir: Path) -> Path:
    cur = start_dir.resolve()
    for _ in range(10):
        if (cur / "schemas").is_dir() and (cur / "SPEC.md").exists():
            return cur
        if cur.parent == cur:
            break
        cur = cur.parent
    raise FileNotFoundError("Could not locate repo root (missing schemas/ and SPEC.md).")

def _load_schema(repo_root: Path, rel_path: str) -> dict:
    schema_path = repo_root / "schemas" / rel_path
    return json.loads(schema_path.read_text(encoding="utf-8"))

def validate_manifest(manifest: dict, start_dir: Path) -> None:
    repo_root = _find_repo_root(start_dir)
    schema = _load_schema(repo_root, "manifest.schema.json")
    resolver = jsonschema.RefResolver.from_schema(schema)
    jsonschema.validate(instance=manifest, schema=schema, resolver=resolver)

def validate_payload_refs(manifest: dict, base_dir: Path) -> None:
    for p in manifest.get("payloads", []):
        ref = p.get("ref", {})
        if ref.get("type") == "path":
            path = ref.get("path")
            if not path:
                raise ValueError(f"Payload {p.get('name')} missing ref.path")
            target = (base_dir / path).resolve()
            if not target.exists():
                raise FileNotFoundError(f"Missing payload file: {target}")
