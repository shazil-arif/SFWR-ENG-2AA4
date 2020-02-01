## @file ChemEntity.py
#  @author 
import ChemTypes
import ElmSet
from abc import ABC,abstractmethod

class ChemEntity(ABC):
    @abstractmethod
    def num_atoms(elm):
        pass

    @abstractmethod
    def constit_elements():
        pass

        

