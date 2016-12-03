#!/usr/bin/env python3

import collections
import sys

import a_star

rules = collections.defaultdict(lambda: [])
for line in sys.stdin:
    if line == "\n":
        break

    left, right = line.strip().split(" => ")
    rules[right].append(left)

molecule = sys.stdin.readline().strip()

def neighbors(node):
    for i in range(len(node)):
        for k, vs in rules.items():
            if node[i:i+len(k)] == k:
                for v in vs:
                    yield node[:i] + v + node[i+len(k):]

def estimate_cost(node):
    return len(node)

# Perform A* search from the final molecule to "e" using the length of string
# as the heuristic.
path = a_star.search(molecule, "e", neighbors, estimate_cost,
                     progress_callback=lambda x: print(x))
print(len(path) - 1)
