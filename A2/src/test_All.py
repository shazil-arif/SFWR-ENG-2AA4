## @file test_All.py
#  @author Spencer Smith, Shazil Arif 
#  @brief Tests implementation of python files for balancing chemical reactions.
#  @date 02/21/2020
#  @details Written to test student code.
#           Avoids interacting with state variables to enforce information hiding.

from Set import *
from MoleculeT import *
from CompoundT import *
from ReactionT import *
from ChemTypes import ElementT
from MolecSet import MolecSet

from pytest import *

class TestSetADT:

    # initialize an instance of Set for each test
    def setup_method(self, method):
        self.test_list = [1, 2, 3, 4, 5, 6, 7]
        self.test_set = Set(self.test_list)

    # reset state variables
    def teardown_method(self, method):
        self.test_set = None
        self.test_list = None

    # test to_seq() method
    def test_to_seq(self):
        assert self.test_set.to_seq() == self.test_list

    # test add method
    def test_add_with_new_element(self):
        self.test_set.add(8)
        assert 8 in self.test_set.to_seq()

    # test add method with existing element
    def test_add_with_existing_element(self):
        self.test_set.add(2)

        # check if 2 in set and it should occur only once
        assert 2 in self.test_set.to_seq() and self.test_set.to_seq().count(2) == 1

    # test member method, it should return True
    def test_member_with_existing_element(self):
        assert self.test_set.member(1)

    def test_member_with_non_existing_element(self):
        assert not self.test_set.member(0)

    def test_remove_method_exception(self):
        with raises(ValueError):
            self.test_set.rm(max(self.test_list) + 1)

    def test_remove_method(self):
        # assume we are blackbox testing, remove arbitrary values
        removed_element = max(self.test_list)
        self.test_set.rm(removed_element)
        assert removed_element not in self.test_set.to_seq()

    def test_size(self):
        assert self.test_set.size() == len(self.test_list)

    # test size method with a zero size
    def test_size_zero(self):
        test = Set([])
        assert test.size() == 0

    def test_equals_with_different_size_sets(self):
        test = Set([1, 2])
        assert not self.test_set.equals(test)

    def test_equals_with_same_size_sets(self):
        test = self.test_set
        assert self.test_set.equals(test)

    def test_equals_with_nonequal_sets(self):
        test = Set([])
        length = len(self.test_set.to_seq())
        for i in range(0, length):
            # some arbitrary values not equal to those in test_set
            test.add(i * -1)
        assert not self.test_set.equals(test)

# @brief test MoleculeT.py


class TestMoleculeT:
    def setup_method(self, method):
        self.elm_num = 2
        self.elm = ElementT.H
        self.molecule = MoleculeT(self.elm_num, self.elm)

    # reset state variables
    def teardown_method(self, method):
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
        assert self.molecule.num_atoms(ElementT.O) == 0

    def test_constit_elems(self):
        assert self.molecule.constit_elems().equals(ElmSet([self.elm]))

    def test_equals_with_same_molecule(self):
        test_molec = MoleculeT(self.elm_num, self.elm)
        assert self.molecule.equals(test_molec)

    def test_equals_with_different_molecule(self):
        test_molec = MoleculeT(self.elm_num + 1, self.elm)
        assert not self.molecule.equals(test_molec)
        
# @brief Test CompoundT


class TestCompoundT:
    # state variables to be used for all tests
    def setup_method(self, method):
        self.elm_num = 2
        self.elm = ElementT.H
        self.molecule = MoleculeT(self.elm_num, self.elm)
        self.molecule_two = MoleculeT(1, ElementT.O)
        self.molec_set = MolecSet([self.molecule, self.molecule_two])
        self.compound = CompoundT(self.molec_set)

    # reset state variables
    def teardown_method(self, method):
        self.elm_num = None
        self.elm = None
        self.molecule = None
        self.molecule_two = None
        self.molec_set = None
        self.compound = None

    def test_get_molec_set(self):
        assert self.compound.get_molec_set().equals(self.molec_set)

    def test_num_atoms(self):
        assert self.compound.num_atoms(self.molecule.get_elm()) == self.molecule.get_num()

    def test_constit_elems(self):
        assert self.compound.constit_elems().equals(
            ElmSet([self.molecule.get_elm(), self.molecule_two.get_elm()]))

    def test_equals(self):
        test_compound = CompoundT(self.molec_set)
        assert self.compound.equals(test_compound)

 # @brief Test ReactionT


class TestReactionT:
    def setup_method(self):
        #Example C_4 H_10 + O_2 = C O_2 + H_2 O

        # create left side
        c4 = MoleculeT(4, ElementT.C)
        h10 = MoleculeT(10, ElementT.H)
        o2 = MoleculeT(2, ElementT.O)
        L1 = CompoundT(MolecSet([c4, h10]))
        L2 = CompoundT(MolecSet([o2]))
        self.left = [L1, L2]
        
        # create right side
        c1 = MoleculeT(1, ElementT.C)
        h2 = MoleculeT(2, ElementT.H)
        o1 = MoleculeT(1, ElementT.O)
        R1 = CompoundT(MolecSet([c1, o2]))
        R2 = CompoundT(MolecSet([h2, o1]))
        self.right = [R1, R2]
        
        # create Reaction
        self.reaction = ReactionT(self.left, self.right)

    def teardown_method(self):
        self.left = None
        self.right = None
        self.reaction = None

    def tet_get_lhs(self):
        assert self.is_equal_array(self.reaction.get_lhs(), self.left)

    def test_get_rhs(self):
        assert self.is_equal_array(self.reaction.get_rhs(), self.right)

    def test_balanced(self):
        assert self.is_balanced(self.reaction)

    # utility function
    def is_equal_array(self, one, two):
        for i in range(len(one)):
            if(not one[i].equals(two[i])):
                return False
        return True

    # utility function
    # admit a tolerance of 0.1
    def is_equal_numbers_array(self, one, two):
        for i in range(len(one)):
            if(abs(one[i] - two[i]) > 0.1):
                return False
        return True
       
    def is_balanced(self, reaction):
        elms = ElmSet([])
        for compound in reaction.get_lhs():
            for e in compound.constit_elems().to_seq():
                elms.add(e)
        for e in elms.to_seq():
            totL = 0
            totR = 0
            L = reaction.get_lhs()
            R = reaction.get_rhs()
            coeff_L = reaction.get_lhs_coeff()
            coeff_R = reaction.get_rhs_coeff()            
            for i in range(len(reaction.get_lhs())):
                totL = totL + coeff_L[i]*L[i].num_atoms(e)
            for i in range(len(reaction.get_rhs())):
                totR = totR + coeff_R[i]*R[i].num_atoms(e)
        if not((totL - totR)/totL <= 0.01): # relative error less than 1%
            return False
        return True
