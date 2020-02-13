## @file Set.py
#  @author Amir Afzali
#  @title Set
#  @date February 8, 2020
from Equality import *

## @brief An ADT for holding sets of generic elements
#  @details This class implements the equality abstract class.


class Set(Equality):

    ## @brief Constructor for Set
    #  @details Constructor accepts one parameter, a list of any data type
    #  If the passed objects data type is not a list, an empty array is initialized
    #  @param s: Intial list of values
    def __init__(self, s: list):
        if type(s) == list:
            self.__S = list(set(s))
        else:
            self.__S = []

    def __eq__(self, R: 'Set'):
        return self.equals(R)

    ## @brief Adds some passed element to the set
    #  @details If the element is already in the set, do nothing
    #  @param e: Any passed item
    def add(self, e) -> None:
        if not self.member(e):
            self.__S.append(e)

    ## @brief Removes some passed element to the set
    #  @details If the element is not in the set, a ValueError exception is raised
    #  @param e: Any passed item
    def rm(self, e) -> None:
        self.__S.remove(e)

    ## @brief Returns if some passed element is in the set
    #  @param e: Any passed item
    #  @return bool True if element is in set
    def member(self, e) -> bool:
        return e in self.__S

    ## @brief Returns the size of the set
    #  @return int length of set
    def size(self) -> int:
        return len(self.__S)

    ## @brief Returns if some passed Set is 'equal' to the current set
    #  @details Two sets are considered equal if they are of equal length
    #  and all elements in the current set exist in the passed set
    #  @param R: Set object
    #  @return bool True if the two sets are equal
    def equals(self, R: 'Set') -> bool:
        if(R.size() != self.size()):
            return False
        return all([x in R.to_seq() for x in self.__S])

    ## @brief Returns the set as a list sequence
    #  @return list representation of object's set
    def to_seq(self) -> list:
        return self.__S
