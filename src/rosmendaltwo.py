from util import find_binomial
from os.path import dirname

path = "./data/rosalind_lia/txt"
dataset = open(dirname(__file__) + '/rosalind_lia.txt').read().strip().split()
k, n = map(int, dataset)
print(round(find_binomial(k, n), 3))