from util import boyer_moore_search, find_dnamotif

s = "ACGTACGTACGTACGT"
t = "GTA"

"""path = "./data/rosalind_subs.txt"
with open(path, 'r') as file:
    s = file.readline(0)
    t = file.readline(1)
"""

print(boyer_moore_search(s, t))
# Alu repeats are very frequently found in DNA repeats. even in coding regions. frequently causes genetic discorders and may be parasitic almost

"""
def find_dnamotif(s,t):
    indexes = ''
    for i in range(0, len(s)):
        if s[i:i+len(t)] == t:
            indexes += str(i+1) + " "
    return indexes
"""
# original solution

"""The Boyer Moore algorithm uses a shift table.
 When it starts scanning characters, if a character isnt matching the current character of the pattern, the pattern is shifted until:
The mismatch becomes a match.
The pattern moves past the mismatched character
This is done by using the shift table. Here is how the shift table is created:

Formula -> Value = Max(1,Length of Pattern - Index -1) """