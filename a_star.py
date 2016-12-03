#!/usr/bin/env python3

import collections
import math

def search(start, goal, neighbors, estimate_cost,
           progress_callback=lambda x: None):
    """Perform A* search. Return None if no path is found.

    start and goal are nodes of some type. neighbors(node) is a generator that
    yields all neighboring nodes of node. estimate_cost(node) is a function
    that returns a heuristic estimation of the cost of getting from node to
    goal.

    The implementation is based on
    https://en.wikipedia.org/wiki/A*_search_algorithm#Pseudocode
    """

    # The set of nodes already evaluated
    closed_set = set()

    # The set of currently discovered nodes still to be evaluated
    open_set = set([start])

    # For each node, which node it can most efficiently be reached from.
    # If a node can be reached from many nodes, came_from will eventually
    # contain the most efficient previous step.
    came_from = {}

    # For each node, the cost of getting from the start node to that node
    g_score = collections.defaultdict(lambda: math.inf)
    g_score[start] = 0

    # For each node, the total cost of getting from the start node to the goal
    # by passing by that node. That value is partly known, partly heuristic.
    f_score = collections.defaultdict(lambda: math.inf)
    f_score[start] = estimate_cost(start)

    while len(open_set) > 0:
        current = min(open_set, key=lambda x: f_score[x])
        progress_callback(estimate_cost(current))

        if current == goal:
            return _reconstruct_path(came_from, current)

        open_set.remove(current)
        closed_set.add(current)

        for neighbor in neighbors(current):
            if neighbor in closed_set:
                # This neighbor is already evaluated
                continue

            # The distance from start to a neighbor
            tentative_g_score = g_score[current] + 1

            if neighbor not in open_set:
                open_set.add(neighbor)
            elif tentative_g_score >= g_score[neighbor]:
                # This is not a better path
                continue

            # This is the best path until now
            came_from[neighbor] = current
            g_score[neighbor] = tentative_g_score
            f_score[neighbor] = g_score[neighbor] + estimate_cost(neighbor)

    return None

def _reconstruct_path(came_from, node):
    path = [node]

    while node in came_from:
        node = came_from[node]
        path.append(node)

    return path
