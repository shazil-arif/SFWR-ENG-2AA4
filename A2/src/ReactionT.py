## @file ReactionT.py
#  @author Shazil Arif
#  @brief ReactionT is responsible for balancing equations
#  @date Feb 8th, 2020

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
    #  @throws ValueError if the equation cannot be balanceds
    def __init__(self, l, r):
        self._lhs = l
        self._rhs = r
        self._coeff_l = []
        self._coeff_r = []
        self.__balance(l,r)
 
    ## @brief getter method for the Compounds on the left side of reaction
    #  @return a sequence of CompoundT 
    def get_lhs(self): return self._lhs

    ## @brief getter method for the Compounds on the right side reaction
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
    
    ## @brief balanc method for the coefficients on the right side
    def __balance(self):
        left_coeff = []
        right_coeff = []

        #get all elements in reaction
        elm_set = self.__elm_in_chem_eq(self.get_lhs())
        matrix = []
        index = 0       

        #iterate over all elements
        for elm in elm_set.to_seq():
            #append new row
            matrix.append([])

            #iterate over left and right, totalling the count for each element
            for compound in l: matrix[index].append(compound.num_atoms(elm))

            #add the negative of the count on right 
            #can be though of as "subtracting from both sides" 
            for compound in r: matrix[index].append(-compound.num_atoms(elm))

            index +=1

        # Since we are solving the system Ax=B
        # here we construct the B vector by taking the first row of the matrix
        b_vector = []
        for i in range(len(matrix)):
            b_vector.append(-matrix[i][0])

            #remove from matrix after putting in b vector
            matrix[i].pop(0)

        #solve the system using numpy
        coeffs = np.linalg.lstsq(matrix,b_vector,rcond=-1)[0]
        #append 1 to start since first row was set to 1
        coeffs = np.append([1],coeffs) 
        
        #check if coefficients were all positive
        if(self.__pos(coeffs)):
            #take subarrays corresponding to each side of the equation
            self.__set_lhs_coeff(list(coeffs[0:len(self.get_lhs())]))
            self.__set_rhs_coeff(list(coeffs[len(self.get_lhs()):len(coeffs)]))
        else: raise ValueError("Unable to balance")

    ## @brief check if all values in a sequence are positive
    #  @param seq the Sequence to check 
    #  @return boolean indicating the result
    def __pos(self,seq):
        for i in seq: 
            if (i <= 0): return False
        return True

    ## @brief Get all elements in a sequence of compounds
    #  @param Sequence of CompoundT objects
    #  @return Elmset containing the elements
    def __elm_in_chem_eq(self,seq_compounds):
        elms = []
        for i in seq_compounds:
            temp = i.constit_elems().to_seq()
            elms = elms + temp 
        return ElmSet(elms) 



