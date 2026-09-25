#!/usr/bin/env bash
set -euo pipefail

# Rebuild the demo environment and render lcpy-preview.gif deterministically.
# Usage: ./setup.sh [output-dir]

DIR="${1:-lcpy-demo-render}"
SRC="$(cd "$(dirname "$0")" && pwd)"

for cmd in vhs uv lcpy; do
    command -v "$cmd" >/dev/null || { echo "error: $cmd not on PATH" >&2; exit 1; }
done

VHS_VER="$(vhs --version | awk '{print $NF}')"
if [ "$VHS_VER" = "0.12.0" ] || [ "$VHS_VER" = "v0.12.0" ]; then
    echo "error: vhs 0.12.0 writes no output, install 0.12.1 or later" >&2
    exit 1
fi

rm -rf "$DIR"
mkdir -p "$DIR"
cd "$DIR"

# The tape expects an activated venv with pytest + the sdk. Build it before
# rendering: inside the tape, environment setup would race the Sleep
# durations and cascade typed commands into each other. The tape's hidden
# warm-up block then absorbs the lcpy cold start (see README.md).
uv venv -q .venv
uv pip install -q --python .venv/bin/python pytest leetcode-py-sdk

cp "$SRC/lcpy.tape" .
vhs lcpy.tape

echo "done: $DIR/lcpy-preview.gif"
echo "re-render: cd $DIR && vhs lcpy.tape"
