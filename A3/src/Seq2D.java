/**
*  @file Seq2D.java
*  @author: Shazil Arif
*  @brief: Seq2D is a module used to represent a generic 2D sequence 
*  @date: March 16th 2020
*/

import java.util.ArrayList;

/** 
* @brief Seq2D provides an ADT to represent a generic 2D sequence parameterized over any type
*/

public class Seq2D<T>{

    //state variables
    protected ArrayList<ArrayList<T>> s;
    protected double scale;
    protected int n_row;
    protected int n_col;


    /**
    * @brief Constructor method for Seq2D
    * @param S the input sequence of rows
    * @param scl the scale/dimension of a side of each cell
    * @throws IllegalArgumentException if the scale is less than or equal to 0, the input sequence is empty, the length of the
    * first row in the sequence is 0 or the length of any row is not equal to the length of the first row
    */
    public Seq2D(ArrayList<ArrayList<T>> S, double scl){
        //check exceptions
        if(scl <= 0 || S.size()==0 || S.get(0).size()==0){
            throw new IllegalArgumentException("Illegal Argument to Seq2D");
        }

        //check remaining exceptions
        int length = S.get(0).size();
        for(int i = 1; i < S.size(); i++){
            if(S.get(i).size()!=length){
                throw new IllegalArgumentException("Illegal Argument to Seq2D");
            }
        }

        s = new ArrayList<ArrayList<T>>();

        //copy input sequence to state variable s
        for(int i = 0; i < S.size(); i++){
            ArrayList<T> temp = new ArrayList<T>();
            for(int j = 0; j < S.get(i).size(); j++){
                temp.add(S.get(i).get(j));
            }
            s.add(temp);
        }

        //set remaining state variables
        scale = scl;
        n_row = S.size();
        n_col = S.get(0).size();
    }

    /**
    * @brief getter method for Seq2D, get a value at a given point
    * @param p A PointT object representing the point to get the value at
    * @return the value at point p
    * @throws IndexOutBoundsException if the point lies outside of the map, i.e the row and column of the point are out of bounds
    */
    public T get(PointT p){
        if(valid_point(p))
            return s.get(p.row()).get(p.col());
        else
            throw new IndexOutOfBoundsException("The given point lies outside of the 2D sequence!");
    }
    
    /**
     * @brief setter method for Seq2D, set a value at a given point
     * @param p A PointT object representing the point to set the value at
     * @param v the value to set
     * @throws IndexOutOfBoundsException if the point lies outside of the map, i.e the row and column of the point are out of bounds
     */
     public void set(PointT p, T v){
         if(valid_point(p))
            s.get(p.row()).set(p.col(), v);
         else
            throw new IndexOutOfBoundsException("The given point lies outside of the 2D sequence!");
     }

    /**
    * @brief getter method for the number of rows in the current Seq2D object
    * @return the number of rows in the current Seq2D object
    */
    public int getNumRow(){ return n_row; }

    /**
    * @brief getter method for the number of columns in the current Seq2D object
    * @return the number of columns in the current Seq2D object
    */
    public int getNumCol(){ return n_col; }

    /**
    * @brief getter method for scale of the current Seq2D object
    * @return the scale of the current Seq2D object
    */
    public double getScale(){ return scale; }

    /**
    * @brief count the number of occurrences of a value in the current 2D sequence
    * @param t the value to count the occurrences for
    * @return the number of occurrences of t in the current 2D sequence
    */
    public int count(T t){
        int count = 0;
        for(int i = 0; i < s.size(); i++){
            count += countRow(t, i);
        }
        return count;
    }

    /**
    * @brief count the occurrences of a value in the current 2D sequence in a particular row
    * @param t the value to search for
    * @param i the index of the row to search t in
    * @return the count of the occurrences of parameter t in row i
    * @throws IndexOutOfBoundsException if the row index i is out of bounds
    */
    public int countRow(T t, int i){
        if(!valid_row(i)) 
            throw new IndexOutOfBoundsException("Invalid row index");

        int count = 0;
        for(int j = 0; j < s.get(i).size(); j++){
            if(s.get(i).get(j) == t) count++;
        }
        return count;
    }

    /**
    * @brief return the area taken up by a particular value t
    * @details assumes each cell is a square
    * @param t the value to calculate the area taken up by
    * @return the total area taken up by value t
    */
    public double area(T t){ return count(t)*scale*scale; }

    /**
     * @brief private helper method to validate a row number
     * @param row the row index to validate
     * @return boolean indicating if the row number is valid
     */
    private boolean valid_row(int row) { return row >= 0 && row < n_row; }

     /** 
     * @brief private helper method to validate a column number
     * @param col the column index to validate
     * @return boolean indicating if the column number is valid (i.e lies in the 2D sequence bounds)
     */
    private boolean valid_col(int col){ return col >= 0 && col < n_col; }

     /** 
     * @brief private helper method to validate a PointT object
     * @param p the PointT object to validate
     * @return boolean indicating if the column number is valid (i.e lies in the 2D sequence bounds)
     */
    private boolean valid_point(PointT p){ 
        return valid_row(p.row()) && valid_col(p.col()); 
    }

}