## @file ChemEntity.py
#  @author Shazil Arif
#  @brief ChemEntity is a sub module used to build equation balancer 
#  @date Feb 8th 2020
#  


from abc import ABC,abstractmethod

class ChemEntity(ABC):
    @abstractmethod
    def num_atoms(elm):
        pass

    @abstractmethod
    def constit_elems():
        pass

        

