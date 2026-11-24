#!/usr/bin/env python3
"""news-image-20261124 entry: copy the pre-rendered front page to the
output directory. Standard library only; deterministic byte-for-byte copy.

Usage:  MAKEFUN_OUTPUT_DIR=out python3 main.py
        (defaults to /output when the variable is unset)
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("copied", src, "->", dst)


if __name__ == "__main__":
    main()
