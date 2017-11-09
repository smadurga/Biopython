#! /usr/bin/python3
#
# Simple program to calculate ResidueDepth

from Bio.PDB.PDBParser import PDBParser
import Bio.PDB.ResidueDepth as ResidueDepth
import numpy as np


parser = PDBParser()

st = parser.get_structure('estructura', '1ubq.pdb')

print("\nResidue.     (Avg. Depth, CA Depth)")
resdepth=ResidueDepth(st)
for resInfo , depth in resdepth:
    print(resInfo,depth)

