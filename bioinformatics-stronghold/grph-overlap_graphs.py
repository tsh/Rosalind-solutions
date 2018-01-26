"""
Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
Return: The adjacency list corresponding to O3. You may return edges in any order.
"""

from collections import defaultdict

# read FASTA
dataset = defaultdict(str)
with open('rosalind_grph.txt') as f:
    mark = f.readline().strip()[1:]
    for line in f.readlines():
        if line.startswith('>'):
            mark = line.strip()[1:]
        else:
            dataset[mark] += line.strip()

with open('result.txt', 'w') as f:
    for head, string1 in dataset.items():
        for tail, string2 in dataset.items():
            if head == tail:
                continue
            elif string1[-3:] == string2[0:3]:
                f.write('{} {}\n'.format(head, tail))
