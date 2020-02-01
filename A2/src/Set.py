# @file Set.py
#  @author Shazil Arif
#  @brief Set.py contains a class that implements a set data type
#  @date Feb 1st, 2020

from Equality import *


class Set(Equality):

    ## @brief constructor method for class Set, intializes a Set from a given sequence t
    #  @param t a sequence of values that will be converted a set
    def __init__(self, t):
        self.S = set(t)

    # @brief add a new element to the set
    #  @param e The element to add to the set
    def add(self, e):
        self.S.add(e)

    # @brief remove a element from the set
    #  @param e The element to remove from the set
    #  @throws ValueError if e is not a member of the set
    def rm(self, e):
        if (e in self.S):
            self.S.remove(e)
        else:
            raise ValueError("{e} is not a member".format(e=e))

    # @brief check if an element is in the set
    #  @param e The element to add to the set
    #  @return boolean value indicating whether parameter e was # found in the set
    def member(self, e):
        return self.S.__contains__(e)

    # @brief return size of the set
    #  @return integer representing the size of the set
    def size(self):
        return len(self.S)

    # @brief check if two sets are equal
    #  @param r the set to compare against
    #  @return boolean indicating if the sets are equal
    def equals(self, r):
        if(R.size() != self.size()):
            return False
        temp_set = r.to_seq()
        for element in self.S:
            if (element not in temp_set):
                return False
        return True

    # @brief convert the set to a sequence
    #  @return a sequence containing all elements of the set
    def to_seq(self):
        return list(self.S)