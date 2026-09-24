#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
else:
    result = ""
    for character in sys.argv[1]:
        if character == "z":
            result += character

    if result:
        print(result)
    else:
        print("none")
