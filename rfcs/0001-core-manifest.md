# RFC 0001: Core Manifest v0.1

## Summary
Defines the required JSON-HD manifest fields, payload references, integrity hooks, versioning, and extensibility.

## Motivation
Implementers need a stable, minimal contract that is independent of any container profile (ZIP, HDF5, etc.).

## Proposal
Adopt `SPEC.md` as the normative Core manifest description for v0.1-draft, and keep JSON Schema in `schemas/` aligned.

## Open questions
- Canonicalization rules for `manifestHash` (profile-specific vs core-wide)
- Required vs optional payload hashes in v1.0
