#!/usr/bin/env python3
def match(regexp: str, text: str) -> bool:
    # Добавим признак конца строки
    text += '\0'
    regexp += '\0'
    if regexp[0] == '^':
        return matchhere(regexp[1:], text)
    for i in range(len(text)):
        if matchhere(regexp, text[i:]):
            return True
    return False


def matchhere(regexp: str, text: str) -> bool:
    if regexp[0] == '\0':
        return True
    if regexp[1] == '*':
        return matchstar(regexp[0], regexp[2:], text)
    if regexp[0] == '$' and regexp[1] == '\0':
        return text == '\0'
    if text != '\0' and (regexp[0] == '.' or regexp[0] == text[0]):
        return matchhere(regexp[1:], text[1:])
    return False


def matchstar(c: str, regexp: str, text: str) -> bool:
    i = 0
    # * может быть и для 0 вхождений
    if matchhere(regexp, text[i:]):
        return True
    while text[i] != '\0' and (text == c or c == '.'):
        i += 1
        if matchhere(regexp, text[i:]):
            return True
    return False

import sys
import argparse

parser = argparse.ArgumentParser(prog="grep")
parser.add_argument(
    "regexp",
    metavar="regexp",
    type=str,
    help="Simplified regexp (^/./*/$)",
)
parser.add_argument(
    "fname",
    nargs="*",
    metavar="file",
    type=str,
    help="Path to a file. Read from stdin when there is no file argument"
)


def grep(regexp: str, fd: object, name: str = None) -> bool:
    nmatch = 0
    for idx, line in enumerate(fd.readlines()):
        if match(regexp, line.strip()):
            nmatch += 1
            if name is not None:
                print(f"{name}::{idx+1}: ", end='')
            print(f"{line.strip()}")
    return nmatch


def main() -> int:
    args = parser.parse_args()
    regexp = args.regexp
    fnames = args.fname
    nmatch = 0
    if len(fnames) == 0:
        if grep(regexp, sys.stdin):
            nmatch += 1
    else:
        for fname in fnames:
            try:
                with open(fname, "r") as fd:
                    if grep(regexp, fd, fname):
                        nmatch += 1
            except (IOError, OSError) as e:
                print(e, file=sys.stderr)
                continue
    return nmatch == 0


if __name__ == "__main__":
    main()
