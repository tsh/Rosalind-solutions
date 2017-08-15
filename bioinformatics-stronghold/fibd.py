"""
Given: Positive integers n≤100 and m≤20.
Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
"""

N = 6  # number of months
M = 3  # ttl

memo = [None for _ in range(N)]
memo[0] = 1
memo[1] = 1

for month in range(2, N):
    if month < M:
        dead = 0
    elif month == M:
        dead = 1  #  month - (M+1) < 0; first pair of rabbit is dead
    else:
        dead = memo[month - (M+1)]
    memo[month] = (memo[month - 1] + memo[month - 2]) - dead

print memo[-1]
