/** 
*  @file TestDemT.java
*  @author: Shazil Arif
*  @brief: TestDemT is used to test module DemT
*  @date: March 16th 2020
*/

import org.junit.*;
import static org.junit.Assert.*;
import java.util.ArrayList;
import java.util.Arrays;

public class TestDemT{
    private DemT s;
    private double scale;
    private int max;
    ArrayList<ArrayList<Integer>> temp_seq;
    private int total;

    @Before
    public void setUp(){
        //set up state variables

        /*
        map looks like
        | 2 4 5 9 |
        | 9 20 89 10 |
        | 9 -1 90 12 |
        | 12 1 1099 32 |
        */

        //set up arrays for each row 
        temp_seq = new  ArrayList<ArrayList<Integer>>();
        ArrayList<Integer> temp_one = new ArrayList<Integer>(Arrays.asList(new Integer(2),new Integer(4),new Integer(5),new Integer(9)));
        temp_seq.add(temp_one);
        ArrayList<Integer> temp_two = new ArrayList<Integer>(Arrays.asList(new Integer(9),new Integer(20),new Integer(89),new Integer(10)));
        temp_seq.add(temp_two);
        ArrayList<Integer> temp_three = new ArrayList<Integer>(Arrays.asList(new Integer(9),new Integer(-1),new Integer(90),new Integer(12)));
        temp_seq.add(temp_three);
        ArrayList<Integer> temp_four = new ArrayList<Integer>(Arrays.asList(new Integer(12),new Integer(1),new Integer(1099),new Integer(32)));
        temp_seq.add(temp_four);

        //initialize new DemT object with a scale of 2
        scale = 2;
        s = new DemT(temp_seq,scale);

        ArrayList<ArrayList<Integer>> all_rows = new ArrayList<ArrayList<Integer>>();
        all_rows.add(temp_one);
        all_rows.add(temp_two);
        all_rows.add(temp_three);
        all_rows.add(temp_four);


        //get and set total
        total = 0;
        for(int i = 0; i < all_rows.size(); i++){
            for(int j = 0; j < all_rows.get(i).size(); j++){
                total += all_rows.get(i).get(j);
            }
        }

        //set max to largest value in 2D sequence
        max = 1099;
      
    }
   
    /**
     * brief: Test total method
     */
    @Test
    public void testTotal(){ 
        assertTrue(s.total() == total); 
    }

    /**
     * brief: Test max method
     */
    @Test
    public void testMax(){ 
        assertTrue(s.max() == max); 
    }

    /**
     * brief: Test ascending rows method when return value should be false
     */
    @Test
    public void testAscendingRowsFalse(){ 
    	assertTrue(!s.ascendingRows());
    }
    
    /**
     * brief: Test ascending rows method when return value should be true
     */
    @Test
    public void testAscendingRowsTrue(){
    	/*
        map looks like
        | 2 4 5 9 |
        | 9 20 89 10 |
        | 9 20 100 45 |
        | 12 1 1099 32 |
        */

        //set up arrays for each row 
        temp_seq = new ArrayList<ArrayList<Integer>>();
        ArrayList<Integer> temp_one = new ArrayList<Integer>(Arrays.asList(new Integer(2),new Integer(4),new Integer(5),new Integer(9)));
        temp_seq.add(temp_one);
        ArrayList<Integer> temp_two = new ArrayList<Integer>(Arrays.asList(new Integer(9),new Integer(20),new Integer(89),new Integer(10)));
        temp_seq.add(temp_two);
        ArrayList<Integer> temp_three = new ArrayList<Integer>(Arrays.asList(new Integer(9),new Integer(20),new Integer(100),new Integer(45)));
        temp_seq.add(temp_three);
        ArrayList<Integer> temp_four = new ArrayList<Integer>(Arrays.asList(new Integer(12),new Integer(1),new Integer(1099),new Integer(32)));
        temp_seq.add(temp_four);
        
        DemT p = new DemT(temp_seq,scale);
        assertTrue(p.ascendingRows());
    }
    
    /**
     * brief: Test ascending rows method when return value should be false when there is only one row
     */
    @Test
    public void testAscendingRowsWithOneRow() {
    	//create a single row and instantiate a DemT object with it
    	ArrayList<ArrayList<Integer>> temp = new ArrayList<ArrayList<Integer>>();
    	ArrayList<Integer> temp_two = new ArrayList<Integer>(Arrays.asList(new Integer(1), new Integer(2), new Integer(3)));
    	temp.add(temp_two);
    	DemT test = new DemT(temp,scale);
    	assertTrue(!test.ascendingRows());
    }
}