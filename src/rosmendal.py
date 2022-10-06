from util import mendels_first

path = "./data/rosalind_iprb.txt"
with open(path, 'r') as file:
    lines = file.readlines()
k, m, n = [int(i) for i in lines[0].split(' ')]
print(mendels_first(k, m, n))