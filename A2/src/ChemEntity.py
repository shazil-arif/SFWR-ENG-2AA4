## @file ChemEntity.py
#  @author 
from abc import ABC,abstractmethod

class ChemEntity(ABC):
    @abstractmethod
    def num_atoms(elm):
        pass

    @abstractmethod
    def constit_elems():
        pass

        

