from Queue import Queue

with open ('/vagrant/input.txt') as f:
    v, e = map(int, f.readline().split())
    graph = {k:[] for k in range(1, v+1)}
    for line in f.readlines():
        v1, v2 = map(int, line.split())
        graph[v1].append(v2)

D = {}
for goal in range(1, v+1):
    seen = set()
    queue = Queue()
    queue.put(1)
    dist = 0
    while not queue.empty():
        cur = queue.get()
        if cur == goal:
            D[goal] = dist
            break
        dist += 1
        for neighbor in graph[cur]:
            if neighbor not in seen:
                queue.put(neighbor)
                seen.add(neighbor)
    else:
        D[goal] = -1
print D
