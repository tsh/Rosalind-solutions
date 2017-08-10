N = 33
K = 3

prev_gen, next_gen = 0, 1

for i in range(1, N):
    prev_gen, next_gen = next_gen, prev_gen * K + next_gen

print next_gen
