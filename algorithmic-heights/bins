with open('rosalind_bins.txt') as f:
    n = int(f.readline())
    m = int(f.readline())
    ar = map(int, f.readline().split())
    ixs = map(int, f.readline().split())

def binary(ar, target, left, right):
    if left > right:
        return -1
    mid = (left + right) / 2
    if ar[mid] == target:
        return mid
    elif target < ar[mid]:
        return binary(ar, target, left, mid - 1)
    elif target > ar[mid]:
        return binary(ar, target, mid + 1, right)

res = []
for i in ixs:
    loc = binary(ar, i, 0, len(ar)-1)
    res.append(loc + 1 if loc >= 0 else loc)  # result array should be indexed from 1

with open('out.txt', 'w') as o:
    o.write(' '.join(map(str, res)))
