from util import find_protein_mass

path = "./data/rosalind_prtm.txt"

with open(path, "r") as f:
    protein = str(f.readline().strip('< \n'))
    
print(find_protein_mass(protein))

