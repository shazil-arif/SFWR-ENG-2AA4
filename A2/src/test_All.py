## @file test_All.py
#  @author Shazil
#  @brief test_All.py is used to test several modules used to model and balance chemical equations
#  @date Feb 6th 2020

import pytest
# import ChemEntity
# import CompoundT
# import ChemTypes
# import ElmSet
# import Equality
# import MolecSet
# import MoleculeT
# import ReactionT
from Set import Set

## @brief Test methods from Set.py
class TestSetADT:

    #initialize an instance of Set for each test
    def setup_method(self,method):
        self.test_list = [1,2,3,4,5,6,7]
        self.test_set = Set(self.test_list)        

    #reset state variables
    def teardown_method(self,method):
        self.test_set = None
        self.test_list = None

    #test to_seq() method
    def test_to_seq(self):
        assert self.test_set.to_seq() == self.test_list

    #test add method
    def test_add_with_new_element(self):
        self.test_set.add(8)
        assert 8 in self.test_set.to_seq()

    #test add method with existing element
    def test_add_with_existing_element(self):
        self.test_set.add(2)
        
        #check if 2 in set and it should occur only once 
        assert 2 in self.test_set.to_seq() and self.test_set.to_seq().count(2) == 1

    #test member method, it should return True
    def test_member_with_existing_element(self):
        assert self.test_set.member(1) == True

    def test_member_with_non_existing_element(self):
        assert self.test_set.member(0) == False

    def test_remove_method_exception(self):
        with pytest.raises(ValueError):
            self.test_set.rm(max(self.test_list)+1)

    def test_remove_method(self):
        #assume we are blackbox testing, remove arbitrary values
        removed_element = max(self.test_list)
        self.test_set.rm(removed_element)
        assert not removed_element in self.test_set.to_seq()

    def test_size(self):
        assert self.test_set.size() == len(self.test_list)

    #test size method with a zero size
    def test_size_zero(self):
        test = Set([])
        assert test.size() == 0
    
    def test_equals(self):



