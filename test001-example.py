#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
    print("Hello %s!" % sys.argv[1])
elif len(sys.argv) > 2:
    for i, name in enumerate(sys.argv):
        if i > 0:
            print("Hello %s!" % name)
else:
    print("Hello world!")
