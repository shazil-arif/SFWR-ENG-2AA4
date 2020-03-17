/** 
*  @file PointT.java
*  @author Shazil Arif
*  @brief PointT is a a module used to represent a point in 2D space
*  @date March 16th 2020
*/

/**
* @brief PointT represents a single point in 2 dimensional space
*/

public class PointT{
    private int r;
    private int c;

    /**
    * @brief constructor method for PointT
    * @param row the row number to create the point at
    * @param col the column number to create the point at
    */
    public PointT(int row, int col){
        r = row;
        c = col;
    }

    /** 
    * @brief getter method for the row value the point is on
    * @return the row the point is on
    */
    public int row(){ return r; }
    /**
    * @brief getter method for the column value the point is on
    * @return the column the point is on
    */
    public int col(){ return c; }

    /**
    * @brief Translate the current PointT object
    * @param delta_r the amount to translate the row value by
    * @param delta_c the amount to translate the col value by
    * @return a new PointT object with the translated/shifted over coordinates
    */
    public PointT translate(int delta_r, int delta_c) { 
        return new PointT(r + delta_r, c + delta_c); 
    }
}