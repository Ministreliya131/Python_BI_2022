#!/usr/bin/env python3

import argparse
import sys
import os
import shutil

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_or_dir", nargs="*")
    parser.add_argument("-r", "-R", "--recursive", action="store_true", required=False)
    args = parser.parse_args()

    for fd in args.file_or_dir:
        if not os.path.exists(fd):
            sys.stdout.write(f"rm.py: cannot remove '{fd}': No such file or directory\n")
        else:
            is_dir = os.path.isdir(fd)
            is_file = os.path.isfile(fd)

            if is_dir and not args.recursive:
                sys.stdout.write(f"rm.py: cannot remove '{fd}': Is a directory\n")

            elif is_dir:
                shutil.rmtree(fd)

            elif is_file:
                os.remove(fd)
