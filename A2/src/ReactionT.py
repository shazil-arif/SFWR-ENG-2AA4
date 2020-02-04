## @file ReactionT.py
#  @author Shazil Arif
#  @brief ReactionT is responsible for balancing equations
#  @date Feb 1st, 2020

from CompoundT import *

## @brief ReactionT is responsible for balancing equations 
#  @details extends from CompoundT
class ReactionT(CompoundT):
    ## @brief constructor method for ReactionT
    #  @param l
    #  @param r
    def __init__(self, l, r):
        self._lhs = l
        self._rhs = r
        self._coeff_l = self.get_lhs_coeff()
        self._coeff_r = self.get_rhs_coeff()
        

    def get_lhs(self):
        return self._lhs

    def get_rhs(self):
        return self._rhs

    def get_lhs_coeff(self):
        pass


    def get_rhs_coeff():



    def __pos(self,seq):
        for i in seq:
            if (i <= 0): return False
        return True

    def __n_atoms(self,compound,c,e):
        count = 0
        for i in range(len(c)):
            count += c[i]*compound[i].num_atoms(e)
        return


    def __elm_in_chem_eq():
        pass

    def __is_bal_elm():
        pass

    def __is_balanced():
        pass
