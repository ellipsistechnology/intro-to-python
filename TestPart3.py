#!/usr/bin/env python3

import subprocess
import sys
import TestFile
import os

if len(sys.argv) != 2:
    print("Error: Please pass your solution script as a command line argument.")
else:
    # Test file structure:
    TestFile.testFile(sys.argv[1])

    # Part 3 - Test 1: Creates a file with the count of monkeys:
    subprocess.check_output([sys.argv[1]])
    if not os.path.exists("monkeys.txt"):
        print("Part 2 - Test 1 FAIL: File named monkeys.txt not found.")
    else:
        data = open("monkeys.txt").read()
        expected = "3 monkeys found."
        if data.strip() == expected:
            print("Part 2 - Test 1 PASS")
        else:
            print("Part 2 - Test 1 FAIL: expected '%s', got '%s'" % (expected, data))
        os.remove("monkeys.txt")
