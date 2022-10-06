from util import reverse_complement

newf = open("./data/ros1.txt", "w")
f = open("./data/rosalind_revc.txt", "r")
dna = list(f.readline())

newf.write(reverse_complement(dna))
    