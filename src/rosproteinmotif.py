"""
Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output its given access ID followed 
by a list of locations in the protein string where the motif can be found.
"""

# A motif is an interval of nucleotides (in nucleic acids) or of amino acids (in proteins) that has biological importance
# 5 AA LONG xcept. P. middle aa must be S or T.
# N

import requests

BASE = "http://www.uniprot.org"
KB_ENDPOINT = "/uniprot/"
TOOL_ENDPOINT = "/uploadlists/"

fullURL = "http://www.uniprot.org/uniprot/?query=name%3A%22polymerase+alpha%22+AND+taxonomy%3Amus+AND+reviewed%3Ayes&format=list"   
result = requests.get(fullURL)

payload = {"query": "name:'polymerase alpha' AND taxonomy:mus AND reviewed:yes", 
        "format": "list"}

"""if result.ok:
    print(result.text)
else:
    print("Something went wrong ", result.status_code)"""

"""for key, value in result.headers.items():
    print("{}: {}".format(key, value))"""

result2 = requests.get(BASE + KB_ENDPOINT, params=payload)

if result2.ok:
    print(result2.text)
else:
    print("Something went wrong", result.status_code)