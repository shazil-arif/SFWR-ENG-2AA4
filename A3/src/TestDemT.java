/** 
*  @file TestDemT.java
*  Author: Shazil Arif
*  Description: TestDemT is used to test module DemT
*  Revised: March 10th 2020
*/

import org.junit.*;
import java.util.ArrayList;
import java.util.Arrays;

public class TestDemT{
    private DemT s;
    private double scale;
    private int max;
    ArrayList<ArrayList<Integer>> s_seq;
    private int sum = 90;

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

        s_seq = new  ArrayList<ArrayList<Integer>>();
        ArrayList<Integer> temp = new ArrayList<Integer>(Arrays.asList(2,4,5,9));
        s_seq.add(temp);
        temp = new ArrayList<Integer>(Arrays.asList(9,20,89,10));
        s_seq.add(temp);
        temp = new ArrayList<Integer>(Arrays.asList(9,-1,90,12));
        s_seq.add(temp);
        temp = new ArrayList<Integer>(Arrays.asList(12,1,1099,32));
        s_seq.add(temp);

        //initialize new DemT object
        scale = 2;
        s = new DemT(s_seq,scale);
        
    }
    @After
    public void tearDown(){
       
    }

    @Test
    public void testTotal(){


    }

    @Test
    public void testMax(){

    }

    @Test
    public void testAscendingRows(){

    }
}