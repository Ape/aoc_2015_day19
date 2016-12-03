#!/usr/bin/env python3

import collections
import re
import sys

rules = collections.defaultdict(lambda: [])
for line in sys.stdin:
    if line == "\n":
        break

    left, right = line.strip().split(" => ")
    rules[left].append(right)

molecule = re.findall("[A-Z][^A-Z]*", sys.stdin.readline().strip())

results = set()

for i in range(len(molecule)):
    for right in rules[molecule[i]]:
        new_molecule = molecule[:i] + [right] + molecule[i+1:]
        results.add("".join(new_molecule))

print(len(results))
