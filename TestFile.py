import re


def testByRegex(regex, test_str):
    # print("testing %s: found %d" % (regex, len(re.findall(regex, test_str, re.MULTILINE))))
    return re.findall(regex, test_str, re.MULTILINE)


def testFile(fileName):
    f = open(fileName)
    file_string = f.read()
    if len(testByRegex("((?<!\\s)^(#!/usr/bin/env python3)$)", file_string)) == 0:
        print("FAIL: File %s does not start with #!/usr/bin/env python3" % fileName)

    if len(testByRegex("^[\\s[^!]]*#.*\\w.+$", file_string)) < 2:
        print("FAIL: File %s does not include enough comments" % fileName)
