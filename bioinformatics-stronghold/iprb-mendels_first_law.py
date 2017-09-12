"""
Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms:
k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.    

Return: The probability that two randomly selected mating organisms will produce an individual
possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
"""

from itertools import product

k = 2  # AA  homozygous dominant
m = 2  # Aa  heterozygous
n = 2  # aa  homozygous recessive

population = (['AA'] * k) + (['Aa'] * m) + (['aa'] * n)

all_children = []
for parent1 in population:
    # remove selected parent from population.
    chosen = population[:]
    chosen.remove(parent1)
    for parent2 in chosen:
        # get all possible children from 2 parents. Punnet square
        children = product(parent1, parent2)
        all_children.extend([''.join(c) for c in children])

dominants = filter(lambda c: 'A' in c, all_children)
# float for python2
print(float(len(list(dominants))) / len(all_children))
