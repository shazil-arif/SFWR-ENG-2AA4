## @file MolecSet.py
#  @author Shazil Arif
#  @brief MolecSet is a sub module used to build a Equation balancer
#  @date Feb 8th, 2020

from Set import *

## @brief MolecSet is a set of MoleculeT objects
#  @details extends from Set.py
class MolecSet(Set):
    
    ## @brief compare two MolecSets
    #  @details Overrides equals defined in Set.py
    #  @param other The other MolecSet to compare against
    #  @return Boolean indicating if two sets are equal
    def equals(self, other):
        if(self.size()!=other.size()):
            return False

        self_obj = self.to_seq()
        other_obj = other.to_seq()

        for i in range(len(other_obj)):
            if(not other_obj[i].__dict__ == self_obj[i].__dict__):
                return False
        return True
  

    

    

    
