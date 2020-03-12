/** 
*  @file TestPointT.java
*  Author: Shazil Arif
*  Description: TestPointT is used to test the routines in PointT.java
*  Revised: March 12th 2020
*/
import org.junit.*;
public class TestPointT{
    private int row;
    private int col;
    private int delta_r;
    private int delta_c;
    private PointT p;

    @Before
    public void setUp(){
        //set up state variables
        row = 10;
        col = 20;
        p = new PointT(row,col);
    }
    @After
    public void tearDown(){
        //reset state variables
        row = 0;
        col = 0;
        p = null;
        delta_r = 0;
        delta_c = 0;
    }

    @Test
    public void testRow(){
        //test getter method for the row
        assertTrue(p.row() == row);
    }

    @Test
    public void testCol(){
        //test getter method for the column
        assertTrue(p.col() == col);
    }
    public void testTranslate(){
        //test translate method
        int temp_row = row + delta_r;
        int temp_col = col + delta_c;
        PointT new_point = p.translate(delta_r, delta_c);
        assertTrue(new_point.row()==row && new_point.col() == col);
    }
}
