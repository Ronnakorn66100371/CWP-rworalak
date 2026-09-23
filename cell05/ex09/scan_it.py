#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("none")
else:
    count = sys.argv[2].count(sys.argv[1])
    if count > 0:
        print(count)
    else:
        print("none")
