/** 
*  @file TestLanduseMapT.java
*  @author: Shazil Arif
*  @brief: TestLanduseMapT is used to test module LanduseMapT
*  @date: March 16th 2020
*/

import org.junit.*;
import java.util.ArrayList;
import java.util.Arrays;
import static org.junit.Assert.*;

public class TestLanduseMapT{
    private ArrayList<ArrayList<LuT>> test_seq; //global variable that can used multiple times to create instances of LanduseMapT
    private int count_T; //represents number of occurrences of value T, will be used in several tests
    
    @Before
    public void setUp() {
    	ArrayList<LuT> temp = new ArrayList<LuT>(Arrays.asList(LuT.A,LuT.C,LuT.R,LuT.T));
    	ArrayList<LuT> temp_two = new ArrayList<LuT>(Arrays.asList(LuT.A,LuT.T,LuT.A,LuT.C));
    	count_T = 2;
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
    	LanduseMapT test = new LanduseMapT(test_seq,scale); //this should throw an error in the constructor since the scale is negative
  
    }
    @Test (expected=IllegalArgumentException.class)
    public void testConstructorExceptionForScaleEqualZero(){
    	LanduseMapT test = new LanduseMapT(test_seq,0); //this should throw an error in the constructor since the scale is 0
    }
    
    @Test (expected=IllegalArgumentException.class)
    public void testConstructorExceptionForEmptyInput(){
    	test_seq.clear(); //empty the sequence for this test
    	LanduseMapT test = new LanduseMapT(test_seq,10); //this should throw an error in the constructor since the input sequence is empty
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
    
    @Test
    public void testGet() {
    	PointT point = new PointT(0,0); //first entry in the test sequences
    	LanduseMapT test = new LanduseMapT(test_seq,20);
    	assertEquals(test.get(point),test_seq.get(0).get(0)); //compare to test sequence
    }
    
    @Test(expected=IndexOutOfBoundsException.class)
    public void testGetExceptionWithNegativeCoordinates() {
    	PointT point = new PointT(-1,-1); //create a point object with negative values that are not valid
    	LanduseMapT test = new LanduseMapT(test_seq,20);
    	test.get(point); //this should throw in error since the row and column values are negative
    }
    
    @Test(expected=IndexOutOfBoundsException.class)
    public void testGetExceptionWithCoordinatesOutofBounds() {
    	PointT point = new PointT(test_seq.size(),test_seq.get(0).size()); //first entry in the test sequences
    	LanduseMapT test = new LanduseMapT(test_seq,20);
    	test.get(point); //this should throw an error since the row and column indices are equal to the lengths respectively
    }
    
    
    @Test
    public void testSet() {
    	PointT point = new PointT(0,0); //first entry in the test sequences
    	LanduseMapT test = new LanduseMapT(test_seq,20);
    	test.set(point, LuT.T);
    	assertEquals(test.get(point),LuT.T); //compare to test sequence
    }
    
    @Test(expected=IndexOutOfBoundsException.class)
    public void tesSetExceptionWithNegativeCoordinates() {
    	PointT point = new PointT(-1,-1); //create a point object with negative values that are not valid
    	LanduseMapT test = new LanduseMapT(test_seq,20);
    	test.set(point, LuT.T); //this should throw in error since the row and column values are negative
    }
    
    @Test(expected=IndexOutOfBoundsException.class)
    public void testSetExceptionWithCoordinatesOutofBounds() {
    	PointT point = new PointT(test_seq.size(),test_seq.get(0).size()); //first entry in the test sequences
    	LanduseMapT test = new LanduseMapT(test_seq,20);
    	test.set(point, LuT.T); //this should throw in error since the row and column values are to the lengths respectively
    }
    
    @Test
    public void testGetNumRow() {
    	LanduseMapT test = new LanduseMapT(test_seq,20);
    	assertEquals(test.getNumRow(),test_seq.size());
    }
    @Test
    public void testGetNumCol() {
    	LanduseMapT test = new LanduseMapT(test_seq,20);
    	assertEquals(test.getNumCol(),test_seq.get(0).size());
    }
    
    @Test
    public void testGetScale() {
    	double scale = 20;
    	LanduseMapT test = new LanduseMapT(test_seq,scale);
    	assertTrue(test.getScale()==scale);
    }
    
    @Test
    public void testCount() {
    	LuT test_landtype = LuT.T;
    	LanduseMapT test = new LanduseMapT(test_seq,20);
    	assertEquals(test.count(test_landtype),count_T);
    }
    
    @Test
    public void testCountRow() {
    	//count the number of occurrences of T in second row
    	int row = 1;
    	LuT test_landtype = LuT.T;
    	LanduseMapT test = new LanduseMapT(test_seq,20); //create the instance
    	assertEquals(test.countRow(test_landtype, row),count_T-1);
    }
    
    
    @Test(expected=IndexOutOfBoundsException.class)
    public void testCountRowExceptionWithNegativeNumber() {
    	//test count row with a invalid row number
    	int row = -1;
    	LuT test_landtype = LuT.T;
    	LanduseMapT test = new LanduseMapT(test_seq,20); //create the instance
    	assertEquals(test.countRow(test_landtype, row),count_T-1); //this should throw an error
    }
    
    @Test(expected=IndexOutOfBoundsException.class)
    public void testCountRowExceptionWithNumberGreaterThanSequenceSize() {
    	//test count row with a invalid row number
    	int row = test_seq.size();
    	LuT test_landtype = LuT.T;
    	LanduseMapT test = new LanduseMapT(test_seq,20); //create the instance
    	assertEquals(test.countRow(test_landtype, row),count_T-1); //this should throw an error since 'row' parameter is invalid row number to countrow()
    }
    
    @Test
    public void testArea() {
    	LuT test_landtype = LuT.T;
    	double scale = 20;
    	LanduseMapT test = new LanduseMapT(test_seq,scale); //create the instance
    	double area = scale*scale*count_T; //represents area taken up by cell values containing enumerated type T from LuT
    	assertTrue(test.area(test_landtype)==area);
    	
    	//to add, tolerance for decimal point areas
    }
    
}