#!/usr/bin/env python3

import os
import TestPart1
import TestPart2
import TestPart3
import importlib.util

REPORT_FILE = "marks.csv"


def test(dir):

    if dir.endswith("__pycache__"):
        return

    print("Testing %s" % dir)

    # Check that all required files exist and run tests:
    idPath = os.path.join(dir, "id.py")
    if not os.path.exists(idPath):
        print("Error: File %s not found" % idPath)
        return

    spec = importlib.util.spec_from_file_location("module.name", idPath)
    idModule = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(idModule)

    id, name, cohort = idModule.id()
    if not id or not name or cohort not in ["Electrical", "Communications"]:
        print("Error: Invalid (id, name, cohort) = (%s, %s, %s)" % id, name, cohort)
        return

    part1Path = os.path.join(dir, "Part1.py")
    if not os.path.exists(part1Path):
        result1, message1 = False, "Error: File %s not found" % part1Path
    else:
        result1, message1 = TestPart1.test(part1Path)

    part2Path = os.path.join(dir, "Part2.py")
    if not os.path.exists(part2Path):
        result2, message2 = False, "Error: File %s not found" % part2Path
    else:
        result2, message2 = TestPart2.test(part2Path)

    part3Path = os.path.join(dir, "Part3.py")
    if not os.path.exists(part3Path):
        result3, message3 = False, "Error: File %s not found" % part3Path
    else:
        result3, message3 = TestPart3.test(part3Path)

    # Update report:
    report = open(REPORT_FILE, "a")
    report.write( "%s, 1,%s,%s\n" % (id, "PASS" if result1 else "FAIL", message1.replace("\n", "")) )
    report.write( "%s, 2,%s,%s\n" % (id, "PASS" if result2 else "FAIL", message2.replace("\n", "")) )
    report.write( "%s, 3,%s,%s\n" % (id, "PASS" if result3 else "FAIL", message3.replace("\n", "")) )
    report.close()


# Enpty report file fisrt:
report = open(REPORT_FILE, "w")
report.write("ID, Part, Result, Message\n")
report.close()


# Test all scripts in all subdirs of assignments:
# r=root, d=directories, f = files
for r, d, f in os.walk("assignments"):
    for dir in d:
        test(os.path.join(r, dir))
