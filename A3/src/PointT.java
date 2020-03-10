/*
*  @file PointT.java
*  Author: Shazil Arif
*  Description: PointT is a a module used to represent a single point in 2d grid
*  Revised: March 10th 2020
**/

/*
* @brief PointT represents a single point in a 2d grid
*/

public class PointT{
    private int r;
    private int c;

    /*
    * @brief constructor method for PointT, intialize a point
    * @param row the row number to create the point on
    * @param col the column number to create the point on
    **/
    public PointT(int row, int col){
        r = row;
        c = col;
    }

    /*
    * @brief getter method for the row value the point is on
    * @return the row the point is on
    **/
    public int row(){
        return r;
    }

    /*
    * @brief getter method for the column value the point is on
    * @return the column the point is on
    **/
    public int col(){
        return c;
    }

    /*
    * @brief Translate the current 
    * @param delta_r the amount to translate the row value by
    * @param delta_c the amount to translate the col value by
    * @return a new PointT with the translated/shifted over coordinates
    **/
    public PointT translate(int delta_r, int delta_c){
        return new PointT(r + delta_r, c + delta_c);
    }
}