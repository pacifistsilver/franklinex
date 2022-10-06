f = open("rosalind_ini5.txt")
nf = open("ros1.txt", "w")

for num, lines in enumerate(f, 1):
    if num % 2 == 0:
        nf.write(lines)
    num+=1

f.close(), nf.close()