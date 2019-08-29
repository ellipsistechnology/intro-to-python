#!/usr/bin/env python3

import sys

# Print Hello <name>! if one name is given:
if len(sys.argv) == 2:
    print("Hello %s" % sys.argv[1])

# Print Hello <name 1> <name 2>! if multiple names are given:
elif len(sys.argv) > 2:
    for i, name in enumerate(sys.argv):
        if i > 0:
            print("Hello %s" % name)

# Print Hello world! if no names are given:
else:
    print("Hello world")
