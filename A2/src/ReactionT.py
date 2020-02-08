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
        left_coeff = []
        right_coeff = []

        mapping = {
            11:"Na",
            8:"O",
            1:"H",
            16:"S"
        }

        elm_set = self.__elm_in_chem_eq(l)
        print(elm_set.to_seq())
        matrix = []
        index = 0
        flag = elm_set.to_seq()[0]
       
        for elm in elm_set.to_seq():
            matrix.append([])
            for compound in l:
                matrix[index].append(compound.num_atoms(elm))
            for compound in r:
                #can be thought of as subtracting terms from both
                #sides of a linear equation, thus add the negative
                matrix[index].append(-compound.num_atoms(elm))
            index +=1

        b_vector = []
        for i in range(len(matrix)):
            b_vector.append(-matrix[i][0])
            matrix[i].pop(0)

        print(matrix)
        print(b_vector)

        coeffs = np.linalg.lstsq(matrix,b_vector)[0]
        # for compound in l:
        #     elm_set = compound.constit_elems().to_seq()
        #     for elm in elm_set:
        #         left_coeff.append({"elm":mapping[elm],"num":compound.num_atoms(elm)})

        # right_coeff = []
        # for compound in r:
        #     elm_set = compound.constit_elems().to_seq()
        #     for elm in elm_set:
        #         right_coeff.append({"elm":mapping[elm],"num":compound.num_atoms(elm)})

        # count = len(left_coeff)-1
        # matrix = np.array([3])
        # matrix = np.append(matrix,[1,2])
        # print(matrix)
        
        for i in left_coeff:
            print(i)
        print("-----------")
        for i in right_coeff:
            print(i)

        # self._coeff_l = self.get_lhs_coeff()
        # self._coeff_r = self.get_rhs_coeff()
        
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

    def __elm_in_chem_eq(self,seq_compounds):
        elms = []
        for i in seq_compounds:
            temp = i.constit_elems().to_seq()
            elms = elms + temp #concatenate/union two lists
        return ElmSet(elms) #return an elmset

    
    def __is_bal_elm():
        pass

    def __is_balanced():
        pass

# left = [CompoundT(MolecSet([MoleculeT(2,ElementT.H)])),CompoundT(MolecSet([MoleculeT(2,ElementT.O)]))]
# M2 = MoleculeT(1,ElementT.O)
# M1 = MoleculeT(2,ElementT.H)
# molecule = MolecSet([M1,M2])
# compound = CompoundT(molecule)
# right = [compound]
# test_reac = ReactionT(left,right)

left_h = MoleculeT(1,ElementT.H)
left_na = MoleculeT(1,ElementT.Na)
left_o = MoleculeT(1,ElementT.O)
sodium_hydroxide = CompoundT(MolecSet([left_na,left_o,left_h]))

left_h2 = MoleculeT(2,ElementT.H)
left_sulfur = MoleculeT(1,ElementT.S)
left_o4 = MoleculeT(4,ElementT.O)

sulfuric_acid = CompoundT(MolecSet([left_h2,left_sulfur,left_o4]))

right_na2 = MoleculeT(2,ElementT.Na)
right_sulfur = MoleculeT(1,ElementT.S)
right_o4 = MoleculeT(4,ElementT.O)

sodium_sulfate = CompoundT(MolecSet([right_na2,right_sulfur,right_o4]))

right_h2 = MoleculeT(2,ElementT.H)
right_o = MoleculeT(1,ElementT.O)

water = CompoundT(MolecSet([right_h2,right_o]))

left = [sodium_hydroxide,sulfuric_acid]
right = [sodium_sulfate,water]

reaction = ReactionT(left,right)

