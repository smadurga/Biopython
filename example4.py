#! /usr/bin/python3
#
# Simple program to print ARG residues
# iteration over residues

from Bio.PDB.PDBParser import PDBParser


parser = PDBParser()

st = parser.get_structure('estructura', '1ubq.pdb')

selec=[]
aa=["ARG"]

for res in st.get_residues():
    if res.get_resname() in aa:
        selec.append(res)
        print(res.get_resname(),res.id)	

print("Coordinates:")
for res in selec:
    for atom in res.get_atoms():   # Replace get_atoms with get_atom if you get an Error!
        print(res.get_resname(),res.id,
        atom.get_name(),atom.get_coord())
