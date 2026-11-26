#!/usr/bin/env python3
"""news-image-20261125 entrypoint.

Drops the finished news picture into the grader's output folder. The
picture itself ships in this repo as entry.png, painted by make_image.py;
this script only moves those exact bytes to the output directory, so two
runs always produce the same file. Nothing is downloaded and nothing else
is needed beyond the standard library. Because the copy is byte for byte,
the entry is deterministic: run it twice, get the same PNG both times.

Local check (outside the grader's container):

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys
from pathlib import Path

PICTURE_NAME = "entry.png"
DEFAULT_OUTPUT = "/output"


def output_path() -> Path:
    """Where the grader expects the picture, creating the folder first."""
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT)
    folder = Path(wanted)
    folder.mkdir(parents=True, exist_ok=True)
    return folder / PICTURE_NAME


def main() -> None:
    picture = Path(__file__).resolve().parent / PICTURE_NAME
    if not picture.is_file():
        print(f"entry image not found: {picture}", file=sys.stderr)
        raise SystemExit(1)
    shutil.copyfile(picture, output_path())


if __name__ == "__main__":
    main()
