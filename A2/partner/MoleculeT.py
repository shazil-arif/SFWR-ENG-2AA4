## @file MoleculeT.py
#  @author Amir Afzali
#  @title MoleculeT
#  @date February 8, 2020
from ElmSet import ElmSet
from ChemTypes import ElementT
from ChemEntity import ChemEntity
from Equality import Equality

## @brief An ADT for representing chemical molecules
#  @details This class is allows for creating and accessing properties on
#  chemical molecules. This class implements the ChemEntity and Equality abstract classes.


class MoleculeT(ChemEntity, Equality):

    ## @brief Constructor for MoleculeT
    #  @details Constructor accepts two parameters: int n and ElementT e
    #  @param n: int representing amount of the element
    #  @param e: ElementT representing the element of which the molecule consists of
    def __init__(self, n: int, e: ElementT):
        self.__num = n
        self.__elm = e

    ## @brief Getter method for the molecule num property
    #  @return int n for the object's num property
    def get_num(self) -> int:
        return self.__num

    ## @brief Getter method for the molecule elm property
    #  @return ElementT m for the object's elm property
    def get_elm(self) -> ElementT:
        return self.__elm

    ## @brief Returns the number of atoms of some ElementT contained in the molecule
    #  @details This methods takes some ElementT and determines the number of atoms
    #  of that element within the MoleculeT. In other words, if e is the object's elm,
    #  return the num property. Otherwise return 0.
    #  @return int number of atoms
    def num_atoms(self, e) -> int:
        return self.get_num() if e == self.get_elm() else 0

    ## @brief Returns an ElmSet of consisting of the object's elm.
    #  @return ElmSet of current Molecule's element
    def constit_elems(self) -> ElmSet:
        return ElmSet([self.get_elm()])

    ## @brief Returns if the current MoleculeT object is equal to the passed MoleculeT
    #  @details Equality is determined if the two object's have the same elm property
    #  and the same num property. That is to say, they are the same number of the same elm.
    #  @param m: MoleculeT to be compared
    #  @return bool with True if both molecules are equal
    def equals(self, m) -> bool:
        return m.get_elm() == self.get_elm() and m.get_num() == self.get_num()
