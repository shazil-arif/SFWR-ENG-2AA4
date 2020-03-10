import java.beans.Transient;

import org.junit.*;
public class TestPointT{
    private final int row;
    private final int col;
    private final int delta_r;
    private final int delta_c;
    private final PointT p;

    @Before
    public void setUp(){
        row = 10;
        col = 20;
        p = new PointT(row,col);
    }
    @After
    public void tearDown(){
        row = 0;
        col = 0;
        p = null;
        delta_r = 0;
        delta_c = 0;
    }
    @Test
    public void testRow(){
        assertTrue(p.row() == row);
    }
    public void testCol(){
        assertTrue(p.col() == col);
    }
    public void testTranslate(){
        int temp_row = row + delta_r;
        int temp_col = col + delta_c;
        PointT new_point = p.translate(delta_r, delta_c);
        assertTrue(new_point.row()==row && new_point.col() == col);
    }
}
