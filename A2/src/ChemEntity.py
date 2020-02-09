## @file ChemEntity.py
#  @author Shazil Arif
#  @brief ChemEntity is a sub module used to build equation balancer 
#  @date Feb 8th 2020


from abc import ABC,abstractmethod

## @brief ChemEntity is a class with abstract methods
## @details these methods are meant to be overriden by other modules
class ChemEntity(ABC):

    @abstractmethod
    ## @brief a generic method for counting the number of atoms
    #  @param elm the element to count the number of atoms for
    #  @return an integer indicating the number of atoms
    def num_atoms(elm):
        pass

    @abstractmethod
    ## @brief a generic method for getting the elements
    #  @details can be inherited and overriden to specific modules
    #  @return an ElmSet of elements
    def constit_elems():
        pass

        

