# JSON-HD (High Definition Metadata)

JSON-HD is a hybrid metadata container format: a **human-readable JSON manifest** plus **efficient payload storage** (binary and/or files), designed for interoperability, integrity, and partial access.

Think: “JSON for meaning + structured payloads for scale.”

## What you get
- A canonical **manifest.json** you can parse instantly (discovery + indexing).
- Payloads stored efficiently (ZIP profile today, HDF5 profile next).
- Strong linking from manifest → payloads (URIs, byte ranges, dataset paths).
- Built-in integrity hooks (hashes, sizes, validation rules).
- Extensible by design (namespaced extensions, forward-compatible parsing).

## Status
- **Core Spec:** v0.1 (draft)
- **ZIP Profile:** v0.1 (draft, reference samples included)
- **HDF5 Profile:** planned (RFC in progress)

## Quick start (ZIP profile)
A `.jsonhd` file is a ZIP container with:
- `/manifest.json` (required)
- `/payload/**` (payload files)
- optional `/schemas/**`, `/signatures/**`, `/provenance/**`

### Minimal example
See: `samples/zip-minimal/`

## Repo map
- `SPEC.md` — Core spec (normative language: MUST/SHOULD/MAY)
- `profiles/` — Packaging profiles (ZIP, HDF5, etc.)
- `schemas/` — JSON Schemas for manifest validation
- `samples/` — Test vectors (canonical examples)
- `tools/` — Reference tooling (CLI validators/builders)

## Contributing
See `CONTRIBUTING.md`. We use lightweight RFCs in `rfcs/`.

## License
Apache-2.0 (see LICENSE).
