N = 6  # number of months
M = 3  # ttl

# 1 1 2 2 3 4

memo = [0 for _ in range(N+1)]
memo[1] = 1
memo[2] = 1

for month in range(3, N+1):
    dead = 0 if month < M else memo[month-M]
    memo[month] = (memo[month-1] + memo[month-2]) - dead

print memo
