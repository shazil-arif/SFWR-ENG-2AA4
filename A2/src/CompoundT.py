## @file CompoundT.py
#  @author Shazil
#  @brief CompoundT is a sub module used to build a chemical equation balancer
#  @date February 1st, 2020


from MoleculeT import *

## @brief CompoundT 
#  @details
class CompoundT(MoleculeT):
    ## @brief constructor for class CompoundT
    #  @param molec_set A MolecSet Object
    def __init__(self, molec_set):
        self._C = molec_set

    ## @brief return the molecules in the compound
    #  @return a Set containing the molecules in the compound
    def get_molec_set(self):
        return self._C

    ## @brief count the number of atoms of a element in the compound
    #  @param e the element to check for in the compound
    #  @return integer indicating the number of atoms of element e in the compound
    def num_atoms(self, e):
        temp_seq = self._C.to_seq()
        count = 0
        for molecule in temp_seq:
            count += molecule.num_atoms(e)
        return count

    ## @brief return an ElmSet of the elements in the molecules that are in the compound
    #  @return ElmSet containing the element
    def constit_elems(self):
        molecs = self._C.to_seq()
        elems = []
        for molecule in molecs:
            elems.append(molecule.get_elm())
        return ElmSet(elems)


    ## @brief check if two compounds are equals
    #  @param d the object to compare against
    #  @return integer indicating the number of atoms of element e in the compound
    def equals(self, d):
        return self.get_molec_set().equals(d.get_molec_set())
        

        

    