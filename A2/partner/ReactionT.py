## @file ReactionT.py
#  @author Amir Afzali
#  @title ReactionT
#  @date February 8, 2020
from typing import List
from CompoundT import CompoundT
from ChemTypes import ElementT
from ElmSet import ElmSet
from numpy import linalg

## @brief An ADT for representing chemical reactions
#  @details This class is allows for creating and balancing chemical reactions


class ReactionT:

    ## @brief Constructor for ReactionT
    #  @details Constructor accepts two parameters: Sequence of CompoundT for left
    #  and right side of chemical reaction. Constructor will balance the reaction if
    #  possible, otherwise a ValueError is thrown
    #  @param L: CompoundT sequence representing compounds in left side of reaction
    #  @param R: CompoundT sequence representing compounds in right side of reaction
    def __init__(self, L: List[CompoundT], R: List[CompoundT]):
        self.__lhs = L
        self.__rhs = R
        self.__coeffL = []
        self.__coeffR = []

        self.__balance__()

        if not (self.__is_balanced__(L, R, self.get_lhs_coeff(), self.get_rhs_coeff())
                and self.__pos__(self.get_lhs_coeff())
                and self.__pos__(self.get_rhs_coeff())):
            raise ValueError('Cannot balance equation')

    ## @brief Getter method for the reaction left side compounds
    #  @return List of CompoundT
    def get_lhs(self) -> List[CompoundT]:
        return self.__lhs

    ## @brief Getter method for the reaction right side compounds
    #  @return List of CompoundT
    def get_rhs(self) -> List[CompoundT]:
        return self.__rhs

    ## @brief Getter method for the reaction left side coefficients
    #  @return List of float coefficient
    def get_lhs_coeff(self) -> list:
        return self.__coeffL

    ## @brief Getter method for the reaction right side coefficients
    #  @return List of float coefficient
    def get_rhs_coeff(self) -> list:
        return self.__coeffR

    def __balance__(self):
        L, R = self.get_lhs(), self.get_rhs()

        ls = self.__populate__(L[0:1])
        mid = self.__populate__(L[1:], True)
        rs = mid + self.__populate__(R)

        full = self.__elm_in_chem_eq__(L).to_seq()

        coeff1 = self.__get_coeffs__(full, ls)
        coeff2 = self.__get_coeffs__(full, rs)
        coeff1 = [j for sub in coeff1 for j in sub]
        coeffs = linalg.lstsq(coeff2, coeff1, -1)

        final_coeffs = list(map(lambda x: round(x, 4), coeffs[0].tolist()))

        self.__coeffL = [1] + final_coeffs[:len(L) - 1]
        self.__coeffR = final_coeffs[len(L) - 1:]

    def __populate__(self, L: List[CompoundT], neg=False) -> List[dict]:
        ls = []
        for i in range(len(L)):
            ls.append({})
            for molec in L[i].get_molec_set().to_seq():
                ls[i][molec.get_elm()] = molec.get_num() if not neg else molec.get_num() * -1
        return ls

    def __get_coeffs__(self, scope, side) -> list:
        coefficients = []
        for i, elm in enumerate(scope):
            coefficients.append([])
            for compound in side:
                toPush = compound[elm] if elm in compound else 0
                coefficients[i].append(toPush)
        return coefficients

    def __pos__(self, s: list) -> bool:
        print(s)
        return all(x >= 0 for x in s)

    def __n_atoms__(self, C: List[CompoundT], c: list, e: ElementT) -> int:
        sum = 0
        for i in range(len(C)):
            sum = sum + c[i] * C[i].num_atoms(e)
        return sum

    def __elm_in_chem_eq__(self, C: List[CompoundT]):
        elemArr = []
        for c in C:
            elemArr = elemArr + c.constit_elems().to_seq()
        return ElmSet(elemArr)

    def __is_bal_elm__(self, L: List[CompoundT], R: List[CompoundT], cL: list, cR: list, e):
        return self.__n_atoms__(L, cL, e) == self.__n_atoms__(R, cR, e)

    def __is_balanced__(self, L: List[CompoundT], R: List[CompoundT], cL: list, cR: list):
        eInChem = self.__elm_in_chem_eq__
        isBal = self.__is_bal_elm__

        firstCond = eInChem(L).equals(eInChem(R))
        secondCond = all([isBal(L, R, cL, cR, e) for e in eInChem(L).to_seq()])
        return firstCond and secondCond
