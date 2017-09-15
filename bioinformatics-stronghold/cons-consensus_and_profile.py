"""
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist,
then you may return any one of them.)
"""

from collections import defaultdict

profile = {
    'A': [],
    'C': [],
    'G': [],
    'T': []
}

# read FASTA
dataset = defaultdict(str)
with open('/vagrant/input.txt') as f:
    cur_mark = f.readline().strip()[1:]
    for line in f.readlines():
        if line.startswith('>'):
            cur_mark = line.strip()[1:]
        else:
            dataset[cur_mark] += line.strip()
