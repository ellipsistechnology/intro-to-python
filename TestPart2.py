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
        f = open(script, encoding='utf-8')
        file_string = f.read()
        if "def printThing(x, thing):" not in file_string:
            return False, "Fail: Program does not include the printThing(x, thing) function definition."

        # Part 1 - Test 1: With no parameters prints "Error: Need more arguments.":
        result = subprocess.check_output(['python', script])
        output = result.decode("utf-8")
        expected = "Error: Need more arguments."
        if output.strip() != expected:
            return False, "Part 2 - Test 1 FAIL: expected '%s', got '%s'" % (expected, output)

        # Part 2 - Test 2: With one parameter prints a list of numbers:
        result = subprocess.check_output(['python', script, "5"])
        output = result.decode("utf-8")
        expected = ["1\n2\n3\n4\n5", "1\r\n2\r\n3\r\n4\r\n5", "1\n\r2\n\r3\n\r4\n\r5"]
        if output.strip() != expected[0] and output.strip() != expected[1] and output.strip() != expected[1]:
            return False, "Part 2 - Test 2 FAIL: expected '%s', got '%s'" % (expected, output)

        # Part 2 - Test 3: With two parameter prints a list of numbered things:
        result = subprocess.check_output(['python', script, "5", "carrot"])
        output = result.decode("utf-8")
        expected = ["5 carrots\n4 carrots\n3 carrots\n2 carrots\n1 carrot", "5 carrots\r\n4 carrots\r\n3 carrots\r\n2 carrots\r\n1 carrot", "5 carrots\n\r4 carrots\n\r3 carrots\n\r2 carrots\n\r1 carrot"]
        if output.strip() != expected[0] and output.strip() != expected[1] and output.strip() != expected[2]:
            return False, "Part 2 - Test 3 FAIL: expected '%s', got '%s'" % (expected, output)

        return True, "OK"
