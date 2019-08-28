#!/usr/bin/env python3

import subprocess
import sys
import TestFile


if len(sys.argv) != 2:
    print("Error: Please pass your solution script as a command line argument.")
else:
    # Test file structure:
    TestFile.testFile(sys.argv[1])

    # Test the file includes a the printThing function:
    f = open(sys.argv[1])
    file_string = f.read()
    if not ("def printThing(x, thing):" in file_string):
        print("Fail: Program does not include the printThing(x, thing) function definition.")

    # Part 1 - Test 1: With no parameters prints "Error: Need more arguments.":
    result = subprocess.check_output([sys.argv[1]])
    output = result.decode("utf-8")
    expected = "Error: Need more arguments."
    if output.strip() == expected:
        print("Part 2 - Test 1 PASS")
    else:
        print("Part 2 - Test 1 FAIL: expected '%s', got '%s'" % (expected, output))

    # Part 2 - Test 2: With one parameter prints a list of numbers:
    result = subprocess.check_output([sys.argv[1], "5"])
    output = result.decode("utf-8")
    expected = "1\n2\n3\n4\n5"
    if output.strip() == expected:
        print("Part 2 - Test 2 PASS")
    else:
        print("Part 2 - Test 2 FAIL: expected '%s', got '%s'" % (expected, output))

    # Part 2 - Test 3: With two parameter prints a list of numbered things:
    result = subprocess.check_output([sys.argv[1], "5", "carrot"])
    output = result.decode("utf-8")
    expected = "5 carrots\n4 carrots\n3 carrots\n2 carrots\n1 carrot"
    if output.strip() == expected:
        print("Part 2 - Test 3 PASS")
    else:
        print("Part 2 - Test 3 FAIL: expected '%s', got '%s'" % (expected, output))
