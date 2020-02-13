## @file CompoundT.py
#  @author Amir Afzali
#  @title CompoundT
#  @date February 8, 2020
from Equality import Equality
from ChemEntity import ChemEntity
from ElmSet import ElmSet
from MolecSet import MolecSet

## @brief An ADT for representing chemical compounds
#  @details This class is allows for creating and accessing properties on
#  chemical compounds. This class implements the ChemEntity and Equality abstract classes.


class CompoundT(ChemEntity, Equality):

    ## @brief Constructor for CompoundT
    #  @details Constructor accepts one parameter, a MolecSet
    #  @param M: MolecSet representing the compound molecules
    def __init__(self, M: MolecSet):
        self.__C = M

    ## @brief Getter method for the compound MolecSet
    #  @return MolecSet for the object's MolecSet property
    def get_molec_set(self) -> MolecSet:
        return self.__C

    ## @brief Returns the number of atoms of some ElementT contained in the compound
    #  @details This methods takes some ElementT and determines the number of atoms
    #  of that element within the CompoundT MolecSet.
    #  @return int number of atoms
    def num_atoms(self, e) -> int:
        sum = 0
        for molec in self.get_molec_set().to_seq():
            if molec.get_elm() == e:
                sum += molec.get_num()
        return sum

    ## @brief Returns an ElmSet of all ElementT's contained in the CompoundT MolecSet
    #  @return ElmSet of unique ElementT in MolecSet
    def constit_elems(self) -> ElmSet:
        return ElmSet([x.get_elm() for x in self.get_molec_set().to_seq()])

    ## @brief Returns if the current CompoundT object is equal to the passed CompoundT
    #  @details Equality is determined if the two object's MolecSets are equal
    #  @param D: CompoundT to be compared
    #  @return bool with True if both compounds are equal
    def equals(self, D: 'CompoundT') -> bool:
        c_set = self.get_molec_set()
        d_set = D.get_molec_set()
        return c_set.equals(d_set)
