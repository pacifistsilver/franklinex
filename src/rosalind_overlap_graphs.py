# return adjacency list corresponding to O3. any order.
# overlap graph for strings is a directed graph Ok.
# string s connected to string t when k suffix of s == k prefix of t
# so long as s != t

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

def is_k_overlap(s1, s2, k):
    return s1[-k:] == s2[:k]

fasta = read_fasta("./overlap_graph.txt")
# instead of creating two dictionaries outright it probably is better to perform the operation outright and then append to an array? 
head_tail = []
for x in fasta:
    head_tail.append(fasta[x][:3])
    head_tail.append(fasta[x][-3:])
    fasta.update({x:head_tail})
    head_tail = []
# although we know implicitly that there are indexes related to these, there must surely be a better way... 

# i want to look at all the possible matches
all_matches = {}
for x in fasta:
    # this ofc doesnt work because we're looking at the same dictionary key value 
    k = fasta[x][1]
    matches = []
    for key, value in fasta.items():
        if value[0] == k and key != x:
            matches.append(key)
    if matches != []:
        all_matches.update({x: matches})
    
for x in all_matches:
    for y in all_matches[x]:
        print(f"{x} {y}")