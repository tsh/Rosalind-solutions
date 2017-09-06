"""
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t),
is the number of corresponding symbols that differ in s and t. 

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t).
"""

s1 = 'GAGCCTACTAACGGGAT'
s2 = 'CATCGTAATGACGGCCT'
dh = 0

for i in range(len(s1)):
    if s1[i] != s2[i]:
        dh += 1

print dh
