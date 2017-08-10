N = 5
K = 3

prev_gen, cur_gen = 1, 1

for i in range(2, N):
    next_gen = prev_gen * K + cur_gen
    prev_gen = cur_gen
    cur_gen = next_gen

print cur_gen
