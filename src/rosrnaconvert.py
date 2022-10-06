from util import translate_rna

string = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"

path = "./data/rosalind_prot.txt"
with open(path, 'r') as file:
    string = file.readline()

print(translate_rna(string))

"""    for i, v in enumerate(rna, 1):
        codon += v
        if i % 3 == 0 and codon_map[codon] != "STOP":
            protein += codon_map[codon]
            codon = ''""" # original solution