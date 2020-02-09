## @file ReactionT.py
#  @author Shazil Arif
#  @brief ReactionT is responsible for balancing equations
#  @date Feb 1st, 2020

from CompoundT import *
from MolecSet import MolecSet
from MoleculeT import MoleculeT
from ChemTypes import ElementT
from ElmSet import ElmSet
import numpy as np


## @brief ReactionT is responsible for balancing equations 
#  @details extends from CompoundT
class ReactionT(CompoundT):
    ## @brief constructor method for ReactionT
    #  @details the chemical equation is balanced in the constructor
    #  @param l a sequence of compounds on the left side of the equation
    #  @param r a sequence of compounds on the right side of the equation
    def __init__(self, l, r):
        self._lhs = l
        self._rhs = r
        self._coeff_l = []
        self._coeff_r = []
        self.__balance(l,r)
 
    ## @brief getter method for the Compounds on the left side
    #  @return a sequence of CompoundT 
    def get_lhs(self): return self._lhs

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
    def get_rhs_coeff(self): return self._coeff_r

    ## @brief setter method for the coefficients on the left side
    #  @details private method, coefficients are not to be modified by a client
    #  @param coeff The list of coefficient values to assign
    def __set_lhs_coeff(self,coeff): self._coeff_l = coeff
    
    ## @brief setter method for the coefficients on the right side
    #  @details private method, coefficients are not to be modified by a client
    #  @param coeff The list of coefficient values to assign
    def __set_rhs_coeff(self,coeff): self._coeff_r = coeff
    
    def __balance(self,l,r):
        left_coeff = []
        right_coeff = []

        elm_set = self.__elm_in_chem_eq(l)
        matrix = []
        index = 0       
        for elm in elm_set.to_seq():
            matrix.append([])
            for compound in l: matrix[index].append(compound.num_atoms(elm))
            for compound in r: matrix[index].append(-compound.num_atoms(elm))
            index +=1

        b_vector = []
        for i in range(len(matrix)):
            b_vector.append(-matrix[i][0])
            matrix[i].pop(0)

        coeffs = np.linalg.lstsq(matrix,b_vector,rcond=-1)[0]
        coeffs = np.append([1],coeffs)
        
        #take subarrays corresponding to each side of the equation
        if(self.__pos(coeffs)):
            self.__set_lhs_coeff(list(coeffs[0:len(l)]))
            self.__set_rhs_coeff(list(coeffs[len(l):len(coeffs)]))
        else: raise ValueError("Unable to balance")

    def __pos(self,seq):
        for i in seq: 
            if (i <= 0): return False
        return True

    def __n_atoms(self,compound,c,e):
        count = 0
        for i in range(len(c)):
            count += c[i]*compound[i].num_atoms(e)
        return

    def __elm_in_chem_eq(self,seq_compounds):
        elms = []
        for i in seq_compounds:
            temp = i.constit_elems().to_seq()
            elms = elms + temp 
        return ElmSet(elms) 


# left = [CompoundT(MolecSet([MoleculeT(2,ElementT.H)])),CompoundT(MolecSet([MoleculeT(2,ElementT.O)]))]
# M2 = MoleculeT(1,ElementT.O)
# M1 = MoleculeT(2,ElementT.H)
# molecule = MolecSet([M1,M2])
# compound = CompoundT(molecule)
# right = [compound]
# test_reac = ReactionT(left,right)



