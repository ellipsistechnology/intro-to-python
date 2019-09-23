import re
import os


def testByRegex(regex, test_str):
    # print("testing %s: found %d" % (regex, len(re.findall(regex, test_str, re.MULTILINE))))
    return re.findall(regex, test_str, re.MULTILINE)


def testFile(fileName):
    if not os.path.exists(fileName):
        return False, "FAIL: Script %s does not exist." % fileName

    f = open(fileName, encoding="utf-8")
    file_string = f.read()
    if len(testByRegex("((?<!\\s)^(#!/usr/bin/env python3)$)", file_string)) == 0:
        return False, "FAIL: File %s does not start with #!/usr/bin/env python3" % fileName

    if len(testByRegex("^[\\s[^!]]*#.*\\w.+$", file_string)) < 2:
        return False, "FAIL: File %s does not include enough comments" % fileName

    return True, "OK"
