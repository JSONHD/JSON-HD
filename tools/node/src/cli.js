#!/usr/bin/env node
import fs from "node:fs";

const manifestPath = process.argv[2];
if (!manifestPath) {
  console.error("Usage: node src/cli.js <manifest.json>");
  process.exit(1);
}

const txt = fs.readFileSync(manifestPath, "utf8");
JSON.parse(txt);
console.log("OK: parsed JSON (schema validation not yet implemented)");
