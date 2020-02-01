## @file MoleculeT.py
#  @author Shazil Arif
#  @brief
#  @date

from ChemTypes import *
from ChemEntity import *
from Equality import *
from ElmSet import *

## @brief MoleculeT is a class that implements a abstract data type containing an element and the number of atoms of that element
#  @details extends from Set, ChemEntity, Equality, ElmSet

class MoleculeT(Set,ChemEntity,Equality,ElmSet):
    ## @brief constructor method 
    #  @param num an integer indicating the number of atoms of element elm
    #  @param elm an element from the periodic table, from ChemTypes
    def __init__(self, num, elm):
        self.__elm = elm
        self.__num = num

    ## @brief get the number of atoms of Element elm in the molecule
    #  return state variable: num, integer indicating the number of atoms
    def get_num(self):
        return self.num

    ## @brief get the Element in the molecule
    #  return state variable: elm, indicating the element from ElementT
    def get_elm(self):
        return self.elm

    ## @brief return the number of atoms of an element in the molecule
    #  @param e an element to check for the number of elements in the molecule
    #  @return integer, number of atoms of e if e is in the molecule. 0 otherwise
    def num_atoms(self,e):
        return self.get_num() if e == self.elm else 0


    ## @brief return a set, specifically ElmSet of the elements in the molecule
    #  @return an ElmSet of the elements in the molecule
    def constit_elements(self):
        return ElmSet(self.get_elm())

    ## @brief check if two molecules are equals
    #  @details two molecules are considered equal if they contain the same element and same number of that element
    #  @param m a MoleculeT object to compare against
    #  @return boolean indicating whether the two molecules are equal 
    def equals(self, m):
        if(m.get_elm() == self.get_elm() and m.get_num() == self.get_num()): return True
        return False
        

    

    

    
