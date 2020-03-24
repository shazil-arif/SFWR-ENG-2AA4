/**
*  @file Seq2D.java
*  @author Shazil Arif
*  @brief Board is a module used to represent a generic playable game board
*  @date March 16th 2020
*/

import java.util.ArrayList;

/** 
* @brief Board provides an ADT to represent a generic 2D board parameterized over any type
*/

public class Board<T>{

    //state variables
    protected ArrayList<ArrayList<T>> s;
    protected int n_row;
    protected int n_col;
    
    
    /**
     * @brief Constructor method for Board
     * @param row the number of rows desired in the board
     * @param col the number of columns desired in the board
     * @throws IllegalArgumentException if the parameter row or parameter col is less than or equal to 0
     */
    public Board(int row, int col)
    	if(row <= 0 || col <= 0) {
    		throw new IllegalArgumentException("Number of rows and columns have to be positive!");
    	n_row = row;
    	n_col = col;
    	s = new ArrayList<ArrayList<T>>();
    	for(int i = 0; i < n_row; i++) {
    		s.add(new ArrayList<T>());
    	}
    }
    
    public void set(int row, int col, T v) {
    	if(validPoint(row,col)) {
    		s.get(row).get(col);
    	}
    	
    	
    }
    
    /**
     * @brief getter method for Board, get a value at a given point
     * @param row row index to access
     * @param col column index to access
     * @return the value at point p
     * @throws IndexOutBoundsException if the point lies outside of the map, i.e the row and column of the point are out of bounds
     */
     public T get(int row, int col){
         if(!validPoint(row,col))
             return s.get(row).get(col);
         else
             throw new IndexOutOfBoundsException("The given point lies outside of the Board!");
     }
    
    public int getRow() {return n_row;}
    public int getCol() {return n_col; }
    
    private boolean validPoint(int row, int col) {
    	if(row < n_row && row >=0 && col < n_col && col >=0) return true;
    	return false;
    }
    
}
