#!/usr/bin/env python3

import subprocess
import TestFile
import os


def test(script):
    if not script:
        return False, "Error: Script not given."
    else:
        # Test file structure:
        fileResult, fileMessage = TestFile.testFile(script)
        if not fileResult:
            return fileResult, fileMessage

        # Part 3 - Test 1: Creates a file with the count of monkeys:
        subprocess.check_output(['python3', script])
        if not os.path.exists("monkeys.txt"):
            return False, "Part 2 - Test 1 FAIL: File named monkeys.txt not found."
        else:
            data = open("monkeys.txt", encoding="utf-8").read()
            expected = "3 monkeys found."
            if data.strip() != expected:
                return False, "Part 2 - Test 1 FAIL: expected '%s', got '%s'" % (expected, data)
            os.remove("monkeys.txt")

        return True, "OK"
