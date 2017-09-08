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
