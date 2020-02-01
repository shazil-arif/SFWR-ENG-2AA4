## @file CompoundT.py
#  @author Shazil
#  @brief CompoundT is a sub module used to build a chemical equation balancer
#  @date February 1st, 2020


from ChemEntity import *
from Equality import *
from ElmSet import *
from MolecSet import *
from MoleculeT import *

## @brief CompoundT 
#  @details
class CompoundT(ChemEntity, Equality, ElmSet, MolecSet, MoleculeT):
    ## @brief constructor for class CompoundT
    #  @param molec_set A MolecSet Object
    def __init__(self, molec_set):
        self.C = molec_set

    ## @brief return the molecules in the compound
    #  @return a Set containing the molecules in the compound
    def get_molec_set(self):
        return self.C

    ## @brief count the number of atoms of a element in the compound
    #  @param e the element to check for in the compound
    #  @return integer indicating the number of atoms of element e in the compound
    def num_atoms(self, e):
        temp_seq = self.C.to_seq()
        count = 0
        for molecule in temp_seq:
            count += molecule.num_atoms(e)
        return count

    def constit_elements(self):
        

    def equals(self, r):
        return super().equals(r)
        

        

    