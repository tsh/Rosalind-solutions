"""
Given: An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 'U'
 and the same number of occurrences of 'C' as 'G'.
Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s.
"""

from collections import defaultdict
from math import factorial

# read FASTA
dataset = defaultdict(str)
with open('rosalind_pmch.txt') as f:
    mark = f.readline().strip()[1:]
    for line in f.readlines():
        if line.startswith('>'):
            mark = line.strip()[1:]
        else:
            dataset[mark] += line.strip()

string = list(dataset.values())[0]
cg = string.count('C')
au = string.count('A')

print(factorial(cg) * factorial(au))
