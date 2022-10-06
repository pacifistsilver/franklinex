import itertools
from collections import Counter
import re

f = open("rosalind_ini6.txt")
nf = open("ros1.txt", "w")

line = f.readlines()

for word in line:
    x = re.split(" ", word) # list
    result = Counter(itertools.chain(x))

def print_inventory(data):
    for item, amount in data.items(): 
        print("{} {}".format(item, amount))
        nf.write("{} {} \n".format(item, amount))

print_inventory(result)
f.close(), nf.close()