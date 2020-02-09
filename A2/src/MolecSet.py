## @file MolecSet.py
#  @author Shazil Arif
#  @brief MolecSet is a sub module used to build a Equation balancer
#  @date Feb 8th, 2020

from Set import *

## @brief MolecSet
## @
class MolecSet(Set):
    def equals(self, other):
        if(self.size()!=other.size()):
            return False

        self_obj = self.to_seq()
        other_obj = other.to_seq()

        for i in range(len(other_obj)):
            if(not other_obj[i].__dict__ == self_obj[i].__dict__):
                return False
        return True
  

    

    

    
