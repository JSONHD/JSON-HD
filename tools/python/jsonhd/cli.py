import argparse
import json
from pathlib import Path

from jsonhd.validate import validate_manifest, validate_payload_refs

def main():
    p = argparse.ArgumentParser(prog="jsonhd", description="JSON-HD tooling (draft)")
    p.add_argument("manifest", help="Path to manifest.json")
    args = p.parse_args()

    manifest_path = Path(args.manifest)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    validate_manifest(manifest, start_dir=manifest_path.parent)
    validate_payload_refs(manifest, base_dir=manifest_path.parent)

    print("OK: manifest is valid and payload refs resolve")

if __name__ == "__main__":
    main()
