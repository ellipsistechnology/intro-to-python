#!/usr/bin/env python3

import subprocess
import TestFile


def test(script):
    if not script:
        return False, "Error: Script not given."
    else:
        # Test file structure:
        fileResult, fileMessage = TestFile.testFile(script)
        if not fileResult:
            return fileResult, fileMessage

        # Test the file includes a the printThing function:
        f = open(script)
        file_string = f.read()
        if "def printThing(x, thing):" not in file_string:
            return False, "Fail: Program does not include the printThing(x, thing) function definition."

        # Part 1 - Test 1: With no parameters prints "Error: Need more arguments.":
        result = subprocess.check_output(['python3', script])
        output = result.decode("utf-8")
        expected = "Error: Need more arguments."
        if output.strip() != expected:
            return False, "Part 2 - Test 1 FAIL: expected '%s', got '%s'" % (expected, output)

        # Part 2 - Test 2: With one parameter prints a list of numbers:
        result = subprocess.check_output(['python3', script, "5"])
        output = result.decode("utf-8")
        expected = "1\n2\n3\n4\n5"
        if output.strip() != expected:
            return False, "Part 2 - Test 2 FAIL: expected '%s', got '%s'" % (expected, output)

        # Part 2 - Test 3: With two parameter prints a list of numbered things:
        result = subprocess.check_output(['python3', script, "5", "carrot"])
        output = result.decode("utf-8")
        expected = "5 carrots\n4 carrots\n3 carrots\n2 carrots\n1 carrot"
        if output.strip() != expected:
            return False, "Part 2 - Test 3 FAIL: expected '%s', got '%s'" % (expected, output)

        return True, "OK"
