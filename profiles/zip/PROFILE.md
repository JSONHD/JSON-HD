# JSON-HD ZIP Profile (v0.1-draft)

## Summary
A `.jsonhd` file is a ZIP container with required entries:
- `/manifest.json` (required)
- `/payload/**` (recommended location for embedded payload files)

Optional:
- `/schemas/**`
- `/provenance/**`
- `/signatures/**`

## Resolution rules
- `ref.type = "path"` paths are resolved relative to the ZIP root.
- ZIP Profile supports `ref.type`: `path`, `uri` (external), and (optionally) `byteRange`.

## Constraints
- ZIP entries SHOULD use forward slashes.
- `manifest.json` SHOULD be stored uncompressed for fast access.
- Payload entries MAY be compressed.

## Conformance tests
A ZIP profile package MUST:
- contain `/manifest.json`
- have all `path` refs resolvable as ZIP entries
- match `size` if provided
- match `hash` if provided
