#! /usr/bin/python3
#
# Simple program to search contacts

from Bio.PDB.NeighborSearch import NeighborSearch
from Bio.PDB.PDBParser import PDBParser


HBLNK=3.5  # Define distance for a contact

parser = PDBParser(PERMISSIVE=1)

st = parser.get_structure('estructura', '1ubq.pdb')

selecc=[]

for at in st.get_atoms():
    selecc.append(at)
    print("ATOM:",at)	

#Selecting all atoms.
nbsearch=NeighborSearch(selecc)

print("NBSEARCH:")
#Searching for contacts under HBLNK
ncontact=1
for at1,at2 in nbsearch.search_all(HBLNK):
    print("Contact: ",ncontact)
    print("at1",at1,at1.get_serial_number(),at1.get_parent().get_resname())
    print("at2",at2,at2.get_serial_number(),at2.get_parent().get_resname())
    print()
    ncontact+=1
