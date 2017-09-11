"""
Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms:
k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.    

Return: The probability that two randomly selected mating organisms will produce an individual
possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
"""

k = 2  # AA  homozygous dominant
m = 2  # Aa  heterozygous
n = 2  # aa  homozygous recessive
population = k + m + n

from itertools import product

all_pop = []
all_pop.extend(['AA']*k)
all_pop.extend(['Aa']*m)
all_pop.extend(['aa']*n)

all_childrens = []
for parent1 in all_pop:
    chosen = all_pop[:]
    chosen.remove(parent1)
    for parent2 in chosen:
        childrens = product(parent1, parent2)
        all_childrens.extend([''.join(c) for c in childrens])

dominants = filter(lambda c: 'A' in c, all_childrens)
print(float(len(list(dominants))) / len(all_childrens))
