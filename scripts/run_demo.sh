#!/bin/sh
ROOT=$(cd "$(dirname "$0")/.." && pwd)
cd "$ROOT" || exit 1
python3 main.py --vfs "$ROOT/vfs/default" --script demo.txt
