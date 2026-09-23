#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
    print("none")
else:
    for parameter in sys.argv[1:]:
        if not parameter.endswith("ism"):
            print(parameter + "ism")
