## @file MolecSet.py
#  @author Shazil Arif
#  @brief
#  @date

from Set import *

class MolecSet(Set):
    def equals(self, other):
        if(self.size()!=other.size()):return False
        self_obj = self.to_seq()
        other_obj = other.to_seq()
        for i in range(len(other_obj)):
            if(not other_obj[i].__dict__ == self_obj[i].__dict__):
                return False
        return True
  

    

    

    
