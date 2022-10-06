from collections import Counter
import math as m

def fib(n, k):
    cache = {0:0, 1:1}
    if n in cache: return cache[n]
    cache[n] = fib(n - 1, k) + k * fib(n - 2, k)
    return cache[n]


def newfib(n, k=1):
    ages = [1] + [0]*(k-1) 
    # ages array maintains a count of the rabbit pairs of different age
    # The first element is count of rabbits that are one month old, second element two months old and so on. 
    # There are k elements in that array, corresponding to the maximum number of months the rabbits can live.
    for i in range(n-1):
        ages = [sum(ages[1:])] + ages[:-1]
        print(ages)
        # The line from the for loop will calculate the number of newborns
        # sum(ages[1:]) - each rabbit pair will have a newborn except the ones that are newborns themselves, 
        # that's why the first element in excluded from the sum: ages[1:]. 
        # The result will become the first element in the list and the rest of the list will be the 
        # rabbits advancing in age with one month (the oldest ones dieing, hence the ages[:-1] which excludes the last entry).
    return sum(ages)

def reverse_complement(dna_file):
    dna_inverse = {
        "A": "T",
        "C": "G",
        "T": "A",
        "G": "C"
    }
    complement_dna = ''
    for base in dna_file:
        try:
            complement_dna += str(dna_inverse[base])
        except Exception:
            pass
    
    return complement_dna[::-1]

def read_fasta(path):

    sequences = {}

    current_id = None
    current_seq = None

    with open(path) as f:

        data = f.readline()
        while data:

            if data.startswith('>'):
                if current_id:
                    sequences[current_id] = current_seq

                current_id = data[1:].rstrip()
                current_seq = ''
            else:
                current_seq += data.rstrip()

            data = f.readline()

    # Add any left over sequence data
    if current_id:
        sequences[current_id] = current_seq

    return sequences


def gc_content(sequence):
    count = Counter(sequence)

    return (count['G'] + count['C']) / float(len(sequence))

def hamming_distance(s, t):
    point_mutations = 0

    for c, v in enumerate(s):
        if s[c] != t[c]:
            point_mutations += 1
            
    return point_mutations

def mendels_first(k, m, n): # k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
    total_pop = k + m + n
    # organize a list with allele one * allele two (possibles) * dominant probability
    # multiplications by one were ignored
    # remember to substract the haplotype from the total when they're the same for the second haplotype choosed
    couples = [
            k*(k-1),  # AA x AA
            k*m,  # AA x Aa
            k*n,  # AA x aa
            m*k,  # Aa x AA
            m*(m-1)*0.75,  # Aa x Aa
            m*n*0.5,  # Aa x aa
            n*k,  # aa x AA
            n*m*0.5,  # aa x Aa
            n*(n-1)*0  # aa x aa
            ]
    # (t-1) indicate that the first haplotype was select
    return round(sum(couples)/total_pop/(total_pop-1), 5)

def translate_rna(rna):
    """
    Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

    Return: The protein string encoded by s. """

    codon_map = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}
    protein = ''

    for i in range(0, len(rna)-3, 3): #
        if codon_map[rna[i:i+3]] == "STOP" : break
        else:
            protein += codon_map[rna[i:i+3]]

    return protein

def find_dnamotif(s,t):
    indexes = ''
    for i in range(0, len(s)):
        if s[i:i+len(t)] == t:
            indexes += str(i+1) + " "
    return indexes

def generate_shift_table(pattern): # table for boyer-moore algorithm
    skip_list ={}
    for i in range(0, len(pattern)):
        skip_list[pattern[i]] = max(1, len(pattern) - i - 1)
    # key will be the character, value will be the number of shifts.
    return skip_list

def boyer_moore_search(source, pattern): 
    bad_char = generate_shift_table(pattern)
    #print(bad_char)
    i = len(pattern) - 1
    answer = []
    while i <= len(source) - 1: # i will be the current right most index from source where the comparison will begin
        j = 0 # index for character from pattern
        while j < len(pattern) and pattern[len(pattern) - j - 1] == source[i - j]:
            j += 1
        if j == len(pattern):
            # pattern has been found in source return index
            answer.append(i-len(pattern)+2)
            i += 1
            continue
        else:
            shift = bad_char.get(source[i+j], len(pattern))
            # get value of shift for corresponding character form shift table, if character doesnt exist return length of pattern
            if shift == 0:
                shift = len(pattern) - 1

            skips = shift - j

            i += skips
    return answer # returns list of index where pattern is found

def expected(a):
    sum = (a[0] * 1 + a[1] * 1 + a[2] * 1 + a[3] *0.75 + a[4] *0.5 + a[5] * 0) * 2
    return sum

def reverse_translate(protein):
    req = {
    'A': 4, 'C': 2, 'D': 2, 'E': 2,
    'F': 2, 'G': 4, 'H': 2, 'I': 3,
    'K': 2, 'L': 6, 'M': 1, 'N': 2,
    'P': 4, 'Q': 2, 'R': 6, 'S': 6,
    'T': 4, 'V': 4, 'W': 1, 'Y': 2,
    'STOP': 3
    } # no need for rna codons. not doing anything iwth that, just need occurences. 
    prior_val = 1
    for i, v in enumerate(protein):
        prior_val *= req[v]
    return (prior_val*3) % 1000000

def find_binomial(k, n): #k : gen number; n: number of AaBb individuals in k-th generation
    """
    given: two positive integers 
    return: probability that at least N AaBb orgs belong to k-th gen    
    """
    q = 2**k # number of offspring overall 
    f = m.factorial
    p = []
    binomial = lambda n, r: f(n)/ f(r) / f(n - r) 
    # returns binomial coefficient(
    # the number of ways of picking unordered outcomes from possibilities, 
    # also known as a combination or combinatorial number)
    # of n and r.
    for i in range(n, (q+1)):
        probability = binomial(q, i) * (0.25**i) * (0.75**(q-i))
        p.append(probability)
    return sum(p)

def find_protein_mass(protein):
    mass_table = {'A':   71.03711, 'C':   103.00919, 'D':   115.02694,
                'E':   129.04259, 'F':   147.06841, 'G':   57.02146,
                'H':   137.05891, 'I':   113.08406, 'K':   128.09496,
                'L':   113.08406, 'M':   131.04049, 'N':   114.04293,
                'P':   97.05276,'Q':   128.05858, 'R':   156.10111,
                'S':   87.03203, 'T':   101.04768, 'V':   99.06841,
                'W':   186.07931,'Y':   163.06333 }
    return "%.2f"%(sum(map(lambda x:mass_table[x],protein))+18.01528) # answer found on rosalind forum
"""    protein_mass = 0.0
    for k, v in enumerate(protein):
        protein_mass += mass_table[v]
    return round(protein_mass, 3)"""

    
