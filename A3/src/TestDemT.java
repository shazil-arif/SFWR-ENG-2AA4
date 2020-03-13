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
        ArrayList<Integer> temp_one = new ArrayList<Integer>(Arrays.asList(2,4,5,9));
        temp_seq.add(temp_one);
        ArrayList<Integer> temp_two = new ArrayList<Integer>(Arrays.asList(9,20,89,10));
        temp_seq.add(temp_two);
        ArrayList<Integer> temp_three = new ArrayList<Integer>(Arrays.asList(9,-1,90,12));
        temp_seq.add(temp_three);
        ArrayList<Integer> temp_four = new ArrayList<Integer>(Arrays.asList(12,1,1099,32));
        temp_seq.add(temp_four);

        //initialize new DemT object with a scale of 2
        scale = 2;
        s = new DemT(temp_seq,scale);

        ArrayList<ArrayList<Integer>> all_rows = new ArrayList<ArrayList<Integer>>();
        all_rows.add(temp_one);
        all_rows.add(temp_two);
        all_rows.add(temp_three);
        all_rows.add(temp_four);


        total = 0;
        for(int i = 0; i < all_rows.size(); i++){
            for(int j = 0; j < all_rows.get(i).size(); j++){
                total += all_rows.get(i).get(j);
            }
        }

        max = 1099;
        
    }
    // @After
    // public void tearDown(){
    //     s = null;
    //     scale = 0;
    //     total = 0;
    //     max = 0;
    //     temp_seq = null;
    // }

    @Test
    public void testTotal(){
        assertTrue(s.total() == total);
    }

    @Test
    public void testMax(){
        assertTrue(s.max() == max);

    }

    @Test
    public void testAscendingRows(){
        assertTrue(s.ascending_rows()==false);
    }
}