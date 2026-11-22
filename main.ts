// Entry for make.fun news-image-20261121: copies the bundled entry.png to the output directory.
// Node 22, standard library only, no network. Deterministic: same bytes every run.
// Local test: mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
import { copyFileSync } from "node:fs";
import { join } from "node:path";

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
copyFileSync(new URL("./entry.png", import.meta.url), join(outDir, "entry.png"));
