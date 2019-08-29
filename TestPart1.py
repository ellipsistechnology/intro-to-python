#!/usr/bin/env python3

import subprocess
import TestFile

TEST_NAME = "Ben"
TEST_NAMES = ['Ben', 'Bob', 'Bill']


def test(script):
    if not script:
        return False, "Error: Script not given."
    else:
        # Test file structure:
        fileResult, fileMessage = TestFile.testFile(script)
        if not fileResult:
            return fileResult, fileMessage

        # Part 1 - Test 1: With no parameters prints "Hello world!:
        result = subprocess.check_output([script])
        output = result.decode("utf-8")
        expected = "Hello world!"
        if output.strip() != expected:
            return False, "Part 1 - Test 1 FAIL: expected '%s', got '%s'" % (expected, output)

        # Part 1 - Test 2: Prints one name:
        result = subprocess.check_output([script, TEST_NAME])
        output = result.decode("utf-8")
        expected = "Hello %s!" % TEST_NAME
        if output.strip() != expected:
            return False, "Part 1 - Test 2 FAIL: expected '%s', got '%s'" % (expected, output)

        # Part 1 - Test 3: Prints multiple names:
        result = subprocess.check_output([script] + TEST_NAMES)
        output = result.decode("utf-8")
        expected = "Hello %s!Hello %s!Hello %s!" % (TEST_NAMES[0], TEST_NAMES[1], TEST_NAMES[2])
        if output.strip().replace("\n", "").replace("\r", "") != expected:
            return False, "Part 1 - Test 3 FAIL: expected '%s', got '%s'" % (expected, output)

        return True, "OK"
