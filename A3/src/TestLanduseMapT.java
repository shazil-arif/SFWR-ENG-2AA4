/** 
*  @file TestLanduseMapT.java
*  Author: Shazil Arif
*  Description: TestLanduseMapT is used to test module LanduseMapT
*  Revised: March 10th 2020
*/

import org.junit.*;
import java.util.ArrayList;
import java.util.Arrays;
import static org.junit.Assert.*;

public class TestLanduseMapT{
    private ArrayList<ArrayList<LuT>> test_seq; //global variable that can used multiple times to create instances of LanduseMapT
  
    @Before
    public void setUp() {
    	ArrayList<LuT> temp = new ArrayList<LuT>(Arrays.asList(LuT.A,LuT.C,LuT.R,LuT.T));
    	ArrayList<LuT> temp_two = new ArrayList<LuT>(Arrays.asList(LuT.A,LuT.T,LuT.A,LuT.C));
    	test_seq = new ArrayList<ArrayList<LuT>>();
    	test_seq.add(temp);
    	test_seq.add(temp_two);
    }
    @After
    public void tearDown() {
    	test_seq = new ArrayList<ArrayList<LuT>>();
    }
    
    @Test (expected=IllegalArgumentException.class)
    public void testConstructorExceptionForScaleLessThanZero(){	
    	double scale = -5;
    	LanduseMapT test = new LanduseMapT(test_seq,scale); //this should throw an error in the constructor since the scale is less than 0
  
    }
    @Test (expected=IllegalArgumentException.class)
    public void testConstructorExceptionForScaleEqualZero(){
    	LanduseMapT test = new LanduseMapT(test_seq,0); //this should throw an error in the constructor since the scale is less than 0
    }
    
    @Test (expected=IllegalArgumentException.class)
    public void testConstructorExceptionForEmptyInput(){
    	test_seq.clear(); //empty the sequence for this test
    	LanduseMapT test = new LanduseMapT(test_seq,10); //this should throw an error in the constructor since the scale is less than 0
    }
    
    @Test(expected=IllegalArgumentException.class)
    public void testConstructExceptionForEmptyFirstRow() {
    	test_seq.clear(); //clear sequence
    	ArrayList<LuT> temp = new ArrayList<LuT>(); //add nothing so row is empty
    	ArrayList<LuT> temp_two = new ArrayList<LuT>(Arrays.asList(LuT.A,LuT.T,LuT.A,LuT.C));
    	test_seq = new ArrayList<ArrayList<LuT>>();
    	test_seq.add(temp);
    	test_seq.add(temp_two);
    	LanduseMapT test = new LanduseMapT(test_seq,10); //this should throw an error since the first row is empty
    }
    
    @Test(expected=IllegalArgumentException.class)
    public void testConstructExceptionForMisMatchedRowSizes() {
    	ArrayList<LuT> temp = new ArrayList<LuT>(Arrays.asList(LuT.A)); //add nothing so row is empty
    	test_seq.add(temp);
    	LanduseMapT test = new LanduseMapT(test_seq,10); //this should throw an error since the last row just added is not the same size as first row
    }
    
}