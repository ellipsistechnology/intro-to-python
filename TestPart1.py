#!/usr/bin/env python3

import subprocess
import sys
import TestFile

TEST_NAME = "Ben"
TEST_NAMES = ['Ben', 'Bob', 'Bill']

if len(sys.argv) != 2:
    print("Error: Please pass your solution script as a command line argument.")
else:
    # Test file structure:
    TestFile.testFile(sys.argv[1])

    # Part 1 - Test 1: With no parameters prints "Hello world!:
    result = subprocess.check_output([sys.argv[1]])
    output = result.decode("utf-8")
    expected = "Hello world!"
    if output.strip() == expected:
        print("Part 1 - Test 1 PASS")
    else:
        print("Part 1 - Test 1 FAIL: expected '%s', got '%s'" % (expected, output))

    # Part 1 - Test 2: Prints one name:
    result = subprocess.check_output([sys.argv[1], TEST_NAME])
    output = result.decode("utf-8")
    expected = "Hello %s!" % TEST_NAME
    if output.strip() == expected:
        print("Part 1 - Test 2 PASS")
    else:
        print("Part 1 - Test 2 FAIL: expected '%s', got '%s'" % (expected, output))

    # Part 1 - Test 3: Prints multiple names:
    result = subprocess.check_output([sys.argv[1]] + TEST_NAMES)
    output = result.decode("utf-8")
    expected = "Hello %s!\nHello %s!\nHello %s!" % (TEST_NAMES[0], TEST_NAMES[1], TEST_NAMES[2])
    if output.strip() == expected:
        print("Part 1 - Test 3 PASS")
    else:
        print("Part 1 - Test 3 FAIL: expected '%s', got '%s'" % (expected, output))
