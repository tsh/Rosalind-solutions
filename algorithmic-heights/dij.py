with open('input.txt') as f:
    num_nodes, num_edges = map(int, f.readline().split())

    matrix = [[0] * (num_nodes + 1) for _ in range(num_nodes + 1)]

    for line in f.readlines():
        frm, to, w = map(int, line.split())
        matrix[frm][to] = w
