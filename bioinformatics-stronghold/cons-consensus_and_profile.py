"""
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist,
then you may return any one of them.)
"""

from collections import defaultdict, Counter


# read FASTA
dataset = defaultdict(str)
with open('/vagrant/input.txt') as f:
    cur_mark = f.readline().strip()[1:]
    for line in f.readlines():
        if line.startswith('>'):
            cur_mark = line.strip()[1:]
        else:
            dataset[cur_mark] += line.strip()

# create matrix
matrix = [dna_ for dna_ in dataset.values()]

profile = {
    'A': [],
    'C': [],
    'G': [],
    'T': []
}
consensus = ''
for i in range(len(matrix[0])):
    c = Counter()
    for dna in matrix:
        c[dna[i]] += 1
    consensus += c.most_common(1)[0][0]
    profile['A'].append(str(c['A']))
    profile['C'].append(c['C'])
    profile['G'].append(c['G'])
    profile['T'].append(c['T'])

print consensus
print 'A: ', ' '.join(profile['A'])
