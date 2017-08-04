with open('input.txt') as f:
    n = int(f.readline())
    ar = map(int, f.readline().split())
swaps = 0
for i in range(n):
    j = i
    while j > 0 and ar[j] < ar[j-1]:
        ar[j], ar[j-1] = ar[j-1], ar[j]
        swaps += 1
        j -= 1
print swaps
