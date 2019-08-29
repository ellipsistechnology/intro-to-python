#!/usr/bin/env python3

import sys


# Function to print one numbered thing:
def printThing(x, thing):
    if(x > 1):
        print("%d %ss" % (x, thing))
    else:
        print("%d %s" % (x, thing))


# If no arguments then print an error:
if len(sys.argv) == 1:
    print("Error: Need more arguments.")
# If one argument then it's a number so print a list of numbers:
elif len(sys.argv) == 2:
    count = int(sys.argv[1])
    i = 1
    while i <= count:
        print(i)
        i = i + 1
# If it's two arguments then it's a count and a thing; print a list of numberd things:
else:
    count = int(sys.argv[1])
    thing = sys.argv[2]
    for x in range(count, 0, -1):
        printThing(x, thing)
