from itertools import permutations
import os
"""n = 3
array = [x for x in range(1,n+1)]
lst = list(permutations(array))

print(len(lst))
with open("geneorder.txt", "w") as f:
    for i, v in enumerate(lst):
        string = ' '.join(map(str, (v)))
        f.write(string + '\n')""" # og solution

"""p = list(permutations(range(1,n+1)))
print(len(p))
for l in p:
    print (' '.join(map(str,l)))""" # top solution found

n = 3
#array = [x for x in range(1,n+1)] not needed. can just do this in range smh
lst = list(permutations(range(1, n+1)))
path = "./data"
file = "geneorder"
completeName = os.path.join(path, file+".txt")         
print(len(lst))
with open(completeName, "w") as f:
    for i, v in enumerate(lst):
        string = ' '.join(map(str, (v)))
        f.write(string + '\n')