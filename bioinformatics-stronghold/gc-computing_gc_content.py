"""
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. 
Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated.
"""
dataset = {}
with open('/vagrant/input.txt') as f:
    for line in f.readlines():
        if line.startswith('>'):
            mark = line[1:-1]
            dataset[mark] = ''
    print dataset
