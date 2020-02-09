## @file Equality.py
#  @author Shazil Arif
#  @date Feb 8th, 2020

from abc import ABC, abstractmethod


## @brief Equality contains a generic equals methods

class Equality(ABC):

    @abstractmethod
    ## @brief a generic method to compare two values/objects
    ## @param T any type
    ## @return boolean indicating results of comparison
    def equals(self,T):
        pass
    

    

