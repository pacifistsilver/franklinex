from util import reverse_translate

path = "./data/rosalind_mrna.txt"

with open(path, "r") as f:
    protein = str(f.readline().strip('< \n'))

print(reverse_translate(protein))