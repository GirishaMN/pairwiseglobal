from Bio import Entrez
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
Entrez.email ="eigtw59tyjrt403@gmail.com"
GID=[1207832173,1207832173]
seq = []
records=[]
for ids in (GID):
    handle = Entrez.efetch(db="protein", id=ids, retmode="xml")
    records = Entrez.read(handle)
    seq.append(records[0]["GBSeq_sequence"])
    print (seq)
alignments = pairwise2.align.globalxx(seq[0], seq[1])
print(format_alignment(*alignments[0]))
