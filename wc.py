#!/usr/bin/env python3

import argparse
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path_to_file", nargs="*")
    parser.add_argument("-l", "--lines", action="store_true", required=False)
    parser.add_argument("-w", "--words", action="store_true", required=False)
    parser.add_argument("-c", "--bytes", action="store_true", required=False)

    args = parser.parse_args()

    options = [False, False, False]
    if args.lines == args.words == args.bytes == False:
        options = [True, True, True]
    else:
        options = [args.lines, args.words, args.bytes]

    all_fles = []

    if len(args.path_to_file) == 0:
        #exit() # why must we do something when we can do nothing?
        l, w, c = 0, 0, 0
        for inn in sys.stdin:
            all_fles.append(inn)
            l += 1
            w += len(inn.split())
            c += len(inn.encode("utf-8"))
    else:
        all_fles = args.path_to_file
        for fle in all_fles:
            l, w, c, fle_name = 0, 0, 0, ""
            with open(fle) as f:
                fle_name += fle
                for line in f:
                    l += 1
                    w += len(line.split())
                    c += len(line.encode("utf-8"))

    out = []
    if options[0]:
        out.append(l)
    if options[1]:
        out.append(w)
    if options[2]:
        out.append(c)

    if sys.stdin.isatty():
        print(" ".join(map(str, out)) + " " + fle_name)
    else:
        print(f"      {'      '.join(map(str, out))}")