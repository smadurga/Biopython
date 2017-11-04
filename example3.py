#! /usr/bin/python3
#
# Simple program to print ARG residues

from Bio.PDB.NeighborSearch import NeighborSearch
from Bio.PDB.PDBParser import PDBParser



HBLNK=3.5

parser = PDBParser(PERMISSIVE=1)

st = parser.get_structure('estructura', '1ubq.pdb')

selec=[]
aa=["ARG"]

for at in st.get_atoms():
    if at.get_parent().get_resname() in aa:
        selec.append(at)
        print(at)	

print("Coordinates:")
for atom in selec:
    print(atom.get_parent().get_resname(),atom.get_parent().id,
    atom.get_name(),atom.get_coord())
