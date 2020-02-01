## @file ReactionT.py
#  @author Shazil Arif
#  @brief
#  @date Feb 1st, 2020

from CompoundT import *

## @brief
#  @details
class ReactionT(CompoundT):
    ## @brief constructor method for ReactionT
    #  @param l
    #  @param r
    def __init__(self, l, r):
        self._lhs = l
        self._rhs = r
        

    def get_lhs():
        return self._lhs

    def get_rhs():
        return self._rhs

    def get_lhs_coeff():

    def get_rhs_coeff():



    @staticmethod
    def pos(self,seq):
        for i in seq:
            if (i <= 0): return False
        return True

    @staticmethod
    def n_atoms():
        pass

    @staticmethod
    def elm_in_chem_eq():
        pass

    @staticmethod
    def is_bal_elm():
        pass

    @staticmethod
    def is_balanced():
        pass
