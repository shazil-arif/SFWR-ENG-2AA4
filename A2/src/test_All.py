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
from MoleculeT import MoleculeT
from ChemTypes import ElementT
from Set import Set
from ElmSet import ElmSet
from CompoundT import CompoundT
from MolecSet import MolecSet

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
    
    def test_equals_with_different_size_sets(self):
        test = Set([1,2])
        assert not self.test_set.equals(test)

    def test_equals_with_same_size_sets(self):
        test = self.test_set
        assert self.test_set.equals(test)

    def test_equals_with_nonequal_sets(self):
        test = Set([])
        length = len(self.test_set.to_seq())
        for i in range(0,length):
            #some arbitrary values not equal to those in test_set
            test.add(i*10)
        assert not self.test_set.equals(test)

## @brief test MoleculeT.py
class TestMoleculeT:
    def setup_method(self,method):
        self.elm_num = 2
        self.elm = ElementT.H
        self.molecule = MoleculeT(self.elm_num,self.elm)
       
    #reset state variables
    def teardown_method(self,method):
        self.elm = None
        self.elm_num = None
        self.molecule = None

    def test_get_num(self):
        assert self.molecule.get_num() == self.elm_num
    
    def test_get_elm(self):
        assert self.molecule.get_elm() == self.elm

    def test_num_atoms(self):
        assert self.molecule.num_atoms(self.elm) == self.elm_num

    def test_num_atom_with_wrong_element(self):
        #add one to self.elm to test with arbitrary element
        #main idea is to use blackbox approach and minimize hardcoding
        assert self.molecule.num_atoms(self.elm+1) == 0

    def test_constit_elems(self):
        assert self.molecule.constit_elems().equals(ElmSet([self.elm]))

    def test_equals_with_same_molecule(self):
        test_molec = MoleculeT(self.elm_num,self.elm)
        assert self.molecule.equals(test_molec)

    def test_equals_with_different_molecule(self):
        test_molec = MoleculeT(self.elm_num+1,self.elm)
        assert not self.molecule.equals(test_molec)

class TestCompoundT:
    #state variables to be used for all tests
    def setup_method(self,method):
        self.elm_num = 2
        self.elm = ElementT.H
        self.molecule = MoleculeT(self.elm_num,self.elm)

        self.molecule_two = MoleculeT(self.elm_num+1,self.elm+1)
        self.molec_set = MolecSet([self.molecule,self.molecule_two])

        self.compound = CompoundT(self.molec_set)
       
    #reset state variables
    def teardown_method(self,method):
        self.elm_num = None
        self.elm = None
        self.molecule = None
        self.molecule_two = None
        self.molec_set = None
        self.compound = None

    def test_get_molec_set(self):
        assert self.compound.get_molec_set().equals(self.molec_set)

    def test_num_atoms(self):
        assert self.compound.num_atoms(self.molecule.get_elm())==self.molecule.get_num()
    
    def test_constit_elems(self):
        print(ElmSet([self.molecule.get_elm(),self.molecule_two.get_elm()]))
        assert self.compound.constit_elems().equals(ElmSet([self.molecule.get_elm(),self.molecule_two.get_elm()]))

    def test_equals(self):
        test_compound = CompoundT(self.molec_set)
        assert self.compound.equals(test_compound)

       











