#!/usr/bin/env python3

import os
import sys
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--all", action="store_true", required=False)
    parser.add_argument("path_to_dir", type=str, nargs="*", default=os.getcwd())

    args = parser.parse_args()

    path = args.path_to_dir

    try:
        if args.all:
            current_files = [".", ".."]
            current_files += list(sorted(os.listdir(path)))
        else:
            current_files = sorted(os.listdir(path))
        sys.stdout.write(' '.join(current_files) + "\n")
    except FileNotFoundError:
        sys.stderr.write(f"ls: cannot access '{path}': No such file or directory\n")