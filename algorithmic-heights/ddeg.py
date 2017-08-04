finp = open('input.txt')
vert, edges = map(int, finp.readline().split())
graph = {k: [] for k in range(1, vert+1)}
for line in finp.readlines():
    n1, n2 = map(int, line.split())
    graph[n1].append(n2)
    graph[n2].append(n1)
finp.close()

dda = {k: [] for k in range(1, vert + 1)}
for v in range(1, vert+1):
    nodes = graph[v]
    for n in nodes:
        dda[v].extend(graph[n])
res = ' '.join(map(str, [len(dda[v]) for v in range(1, vert +1)]))
with open('out.txt', 'w') as out:
    out.write(res)
