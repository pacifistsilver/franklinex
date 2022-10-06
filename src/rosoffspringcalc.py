from util import expected
"""

Given: Six nonnegative integers, each of which does not exceed 20,000. 
The integers correspond to the number of couples in a population 
possessing each genotype pairing for a given factor.

In order, the six given integers represent the number of couples having the following genotypes:

    AA-AA
    AA-Aa
    AA-aa
    Aa-Aa
    Aa-aa
    aa-aa

Return: The expected number of offspring displaying the dominant phenotype in the next generation, 
under the assumption that every couple has exactly two offspring.
"""
# 1 0 0 1 0 1
# 3.5

lst = [18675, 19165, 18613, 17798, 17067, 19845]
print(expected(lst))