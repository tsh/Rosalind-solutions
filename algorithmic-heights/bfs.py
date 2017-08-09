"""
The task is to use breadth-first search to compute single-source shortest distances in an unweighted directed graph.
Given: A simple directed graph with n≤103 vertices in the edge list format.
Return: An array D[1..n] where D[i] is the length of a shortest path from the vertex 1 to the vertex i (D[1]=0). 
If i is not reachable from 1 set D[i] to −1.
"""
        
from collections import deque

# Prepare graph
with open('/vagrant/input.txt') as f:
    vertices, e = map(int, f.readline().split())
    graph = {k: [] for k in range(1, vertices + 1)}
    for line in f.readlines():
        v1, v2 = map(int, line.split())
        graph[v1].append(v2)

# BFS
depths = {}
for goal in range(1, vertices + 1):
    seen = set()
    queue = deque([1, None])  # None is level separator.
    level = 0
    while queue and not (len(queue) == 1 and queue[0] is None):
        cur = queue.popleft()
        if cur == goal:
            depths[goal] = level
            break
        elif cur is None:
            level += 1
            queue.append(None)
            continue

        for neighbor in graph[cur]:
            if neighbor not in seen:
                queue.append(neighbor)
                seen.add(neighbor)
    else:
        depths[goal] = -1

# Write results
D = []
for v in range(1, vertices + 1):
    D.append(str(depths[v]))

out = open('/vagrant/out.txt', 'w')
out.write(' '.join(D))
out.close()
