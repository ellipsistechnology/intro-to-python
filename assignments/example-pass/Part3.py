#!/usr/bin/env python3

# Read the input text:
text = open("file.txt").read()

# Count the number of times monkey is found:
count = text.count("monkey")

# Write the result to monkeys.txt:
out = open("monkeys.txt", "w")
out.write("%d monkeys found." % count)
