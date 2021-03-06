## @file MoleculeT.py
#  @author Shazil Arif
#  @brief MoleculeT is used to model a chemical Molecule
#  @date Feb 8th , 2020

from ChemTypes import ElementT
from ChemEntity import *
from ElmSet import *

## @brief MoleculeT is a class that implements an ADT for chemical Molecules
#  @details the ADT contains en element and its number of atoms


class MoleculeT(ElementT, ChemEntity, ElmSet):

    ## @brief constructor method
    #  @param num an integer indicating the number of atoms of element elm
    #  @param elm an element from the periodic table, from ChemTypes

    def __init__(self, num, elm):
        self.__elm = elm
        self.__num = num

    ## @brief get the number of atoms of Element elm in the molecule
    #  @return integer indicating the number of atoms
    def get_num(self):
        return self.__num

    ## @brief get the Element in the molecule
    #  @return Enumerated ElementT indicating the element from periodic table
    def get_elm(self):
        return self.__elm

    ## @brief return the number of atoms of an element in the molecule
    #  @param e an element to check for the number of elements in the molecule
    #  @return an integer, number of atoms of e if e is in the molecule. 0 otherwise
    def num_atoms(self, e):
        return self.get_num() if e == self.get_elm() else 0

    ## @brief return a set, specifically ElmSet of the elements in the molecule
    #  @return an ElmSet of the elements in the molecule
    def constit_elems(self):
        return ElmSet([self.get_elm()])

    ## @brief check if two molecules are equals
    #  @details two molecules are equal if they have the same element and count
    #  @param m a MoleculeT object to compare against
    #  @return boolean indicating whether the two molecules are equal
    def equals(self, m):
        if(m.get_elm() == self.get_elm() and m.get_num() == self.get_num()):
            return True
        return False
