"""
A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, 
GCATGC is a reverse palindrome because its reverse complement is GCATGC.

Given: A DNA string of length at most 1 kbp in FASTA format.
Return: The position and length of every reverse palindrome in the string having length between 4 and 12.
You may return these pairs in any order.
"""

complements = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
inp = 'TCAATGCATGCGGGTCTATATGCAT'
inp_len = len(inp)

def reverse_complement(s):
    return ''.join([complements[c] for c in reversed(s)])

for i in range(inp_len):
    for pal_len in range(4, 12+1):
        if i + pal_len > inp_len:
            break
        candidate = inp[i:i + pal_len]
        complement = reverse_complement(candidate)
        if candidate == complement:
            print i+1, pal_len
