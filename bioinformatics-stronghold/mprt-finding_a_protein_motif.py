"""       
Given: At most 15 UniProt Protein Database access IDs.
Return: For each protein possessing the N-glycosylation motif, output its given access ID
followed by a list of locations in the protein string where the motif can be found.
"""

import requests


url = 'http://www.uniprot.org/uniprot/{}.fasta'
dataset_raw = """
A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST
"""
dataset = dataset_raw.split()

for access_id in dataset:
    rsp = requests.get(url.format(access_id))
    # remove info line from fasta
    prot = ''.join(rsp.content.split('\n')[1:])
    motifs = []
    # find motif N{P}[ST]{P}. Could use regex, but what fun in that? :)
    for i in range(len(prot)):
        if i+3 > len(prot)-1:
            continue
        if prot[i] != 'N':
            continue
        if prot[i+1] == 'P':
            continue
        if prot[i+2] not in ['S', 'T']:
            continue
        if prot[i+3] == 'P':
            continue
        motifs.append(str(i+1))
    if motifs:
        print access_id
        print ' '.join(motifs)
