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
        lhs_elms = l.consit_elements()
        self._coeff_l = self.get_lhs_coeff()
        self._coeff_r = self.get_rhs_coeff()
        
    ## @brief getter method for the Compounds on the left side
    #  @return a sequence of CompoundT 
    def get_lhs(self):
        return self._lhs

    ## @brief getter method for the Compounds on the right side
    #  @return a sequence of CompoundT 
    def get_rhs(self): return self._rhs

    ## @brief getter method for the coefficients of compounds on the left side
    #  @details indicates the coefficient of the compounds retrieved from get_lhs()
    #  @return a sequence of real numbers indicating the coefficents  
    def get_lhs_coeff(self): return self._coeff_l

    ## @brief getter method for the coefficients of compounds on the right side
    #  @details indicates the coefficient of the compounds retrieved from get_rhs()
    #  @return a sequence of real numbers indicating the coefficents  
    def get_rhs_coeff(): return self._coeff_r

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
