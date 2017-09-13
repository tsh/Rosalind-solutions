"""
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. 
Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated.
"""
from collections import defaultdict

# read FASTA
dataset = defaultdict(str)
with open('/vagrant/input.txt') as f:
    cur_mark = f.readline().strip()[1:]
    for line in f.readlines():
        if line.startswith('>'):
            cur_mark = line.strip()[1:]
        else:
            dataset[cur_mark] += line.strip()
# find max gc
max_mark, max_gc = None, None
for mark, dna in dataset.items():
    gc = float(dna.count('G') + dna.count('C')) / len(dna) * 100
    if gc > max_gc:
        max_mark, max_gc = mark, gc

print max_mark
print max_gc
