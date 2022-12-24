#!/usr/bin/env python3

import argparse
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path_to_file", nargs="*")

    args = parser.parse_args()

    all_lines = []

    if len(args.path_to_file) == 0:
        #exit() # why must we do something when we can do nothing?
        for fle in sys.stdin:
            all_lines.append(fle)
    else:
        for fle in args.path_to_file:
            with open(fle, "r") as inn:
                for line in inn:
                    all_lines.append(line.strip())

    if not sys.stdin.isatty():
        for line in sorted(sorted(all_lines), key=lambda x: x.lower()):
            out_line = line
            sys.stdout.write(out_line)
    else:
        for line in sorted(sorted(all_lines), key=lambda x: x.lower()):
            out_line = f"{line}\n"
            sys.stdout.write(out_line)