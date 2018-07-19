with open('input.txt') as f:
    f.readline()
    arrs = []
    for line in f:
        arrs.append(list(map(int, line.split())))

def solve(arr):
    h = {}
    for i, el in enumerate(arr):
        if -el in h:
            return str(h[-el]+1) + ' ' + str(i+1)
        else:
            h[el] = i
    return '-1'

print('\n'.join(map(solve, arrs)))