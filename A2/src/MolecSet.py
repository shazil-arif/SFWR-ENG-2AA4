## @file MolecSet.py
#  @author Shazil Arif
#  @brief
#  @date

from ChemTypes import *
from ChemEntity import *
from Equality import *
from ElmSet import *

class MolecSet(Set):
    ## @brief constructor method 
    #  @param num an integer indicating the number of atoms of element elm
    #  @param elm an element from the periodic table, from ChemTypes
    def __init__(self, num, elm):
        self.elm = elm
        self.num = num

    ## @brief get the number of atoms of Element elm in the molecule
    #  return state variable: num, integer indicating the number of atoms
    def get_num(self):
        return self.num

    ## @brief get the Element in the molecule
    #  return state variable: elm, indicating the element from ElementT
    def get_elm(self):
        return self.elm

    

    
