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
    #  @param elm an element from the periodic table, from ChemTypes
    #  @param num an integer indicating the number of atoms of element elm
    def __init__(self, elm, num):
        self.elm = elm
        self.num = num
