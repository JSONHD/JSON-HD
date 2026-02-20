# JSON-HD Core Specification (v0.1-draft)

## 0. Normative language
The key words **MUST**, **SHOULD**, **MAY** are to be interpreted as in RFC 2119.

## 1. Purpose
JSON-HD defines a common **manifest model** for describing a package of metadata + payloads.
Packaging is defined by **Profiles** (e.g., ZIP, HDF5). This Core spec defines:
- the manifest structure,
- payload addressing,
- integrity fields,
- versioning,
- extensibility rules.

## 2. Core object: Manifest
A JSON-HD manifest is a JSON object stored as `manifest.json` (or embedded by profile).
The manifest MUST include:
- `jsonhd` (string): JSON-HD version identifier, e.g. `"0.1"`
- `profile` (string): profile identifier, e.g. `"zip/0.1"`
- `id` (string): stable identifier (UUID/ULID/URI)
- `created` (string): ISO 8601 datetime
- `payloads` (array): payload entries (see §3)
- `integrity` (object): integrity metadata (see §4)

The manifest SHOULD include:
- `about` (object): human-facing description (title, description, keywords)
- `provenance` (object): lineage/events, if relevant
- `extensions` (object): namespaced extension space (see §6)

## 3. Payload entries
Each payload entry MUST be an object with:
- `name` (string): logical name
- `mediaType` (string): IANA media type, e.g. "image/jpeg"
- `ref` (object): how to locate the payload (see below)
- `size` (integer): bytes (if known / applicable)
- `hash` (object): content hash (see §4)

### 3.1 Payload ref types
`ref.type` MUST be one of:
- `"path"`: profile-relative path (e.g., ZIP entry path)
- `"uri"`: external URI
- `"byteRange"`: byte offset + length within a container stream
- `"dataset"`: dataset path (e.g., HDF5 dataset address)
- `"box"`: box identifier (e.g., JUMBF-style)

Each `ref` type has required fields:
- `path`: `{ "type":"path", "path":"payload/hello.txt" }`
- `uri`: `{ "type":"uri", "uri":"https://example.com/file.bin" }`
- `byteRange`: `{ "type":"byteRange", "offset":1234, "length":5678 }`
- `dataset`: `{ "type":"dataset", "path":"/payload/arrays/embedding" }`
- `box`: `{ "type":"box", "id":"com.example.box.payload.1" }`

Profiles MUST specify which ref types they support.

## 4. Integrity
`integrity` MUST include:
- `manifestHash` (object): hash of canonicalized manifest bytes
- `payloadHashMode` (string): how payload hashes are computed (e.g. "sha256")

Hash objects use:
- `alg` (string): e.g. "sha256"
- `value` (string): hex lowercase (recommended)

Example:
`{ "alg":"sha256", "value":"ab12...ff" }`

Profiles MAY define canonicalization rules; Core RECOMMENDS:
- UTF-8 encoding
- stable key ordering for hash-canonicalization (profile-defined)
- no insignificant whitespace assumptions

## 5. Versioning
- `jsonhd` uses semantic-ish versioning: `MAJOR.MINOR`
- Backward compatible changes increment MINOR.
- Breaking changes increment MAJOR.

Profiles use `profile` strings like `"zip/0.1"` and manage their own versioning.

## 6. Extensibility
Forward compatibility rules:
- Parsers MUST ignore unknown top-level fields they do not understand.
- Extensions MUST live under `extensions` and SHOULD use reverse-DNS keys.

Example:
```json
"extensions": {
  "org.json-hd.mytool": { "foo": "bar" }
}
```

## 7. Minimal conformance
A file/package claiming JSON-HD conformance MUST:
- provide a manifest meeting the required fields,
- ensure every payload `ref` resolves under the selected profile rules,
- provide hashes when `integrity.payloadHashMode` is present.
