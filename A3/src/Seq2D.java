/**
*  @file Seq2D.java
*  Author: Shazil Arif
*  Description: Seq2D is a module used to represent a generic 2D sequence 
*  Revised: March 10th 2020
*/

import java.util.ArrayList;
/** 
* @brief Seq2D represents a generic 2D sequence parametrized over any type
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
    * @throws IllegalArgumentException if the scale is less than 0, the input sequence is empty, the length of th
    * first sequence is 0 or the length of any row is not equal to the length of the first row
    */
    public Seq2D(ArrayList<ArrayList<T>> S, double scl){
        //check exceptions
        if(scl <= 0 || S.size()==0 || S.get(0).size()==0){
            throw new IllegalArgumentException("Illegal Argument to Seq2D");
        }

        //check remaining exceptions
        for(int i = 1; i < S.size(); i++){
            if(S.get(i).size()!=S.size()){
                throw new IllegalArgumentException("Illegal Argument to Seq2D");
            }
        }

        for(int i = 0; i < S.size(); i++){
            ArrayList<T> temp = new ArrayList<T>();
            s.add(temp);
            for(int j = 0; j < S.get(i).size(); j++){
                s.get(i).add(S.get(i).get(j));
            }
        }
        scl = scale;
        n_row = S.size();
        n_col = S.get(0).size();
    }

    /**
    * @brief setter method for Seq2D, set a value at a given point
    * @param p the point to set the value at
    * @param v the value to set
    * @throws IllegalArgumentException if the point lies outside of the map, i.e the row and column of the point are out of bounds
    */
    public void set(PointT p, T v){
        if(valid_point(p)){
            s.get(p.row()).set(p.col(), v);
        }
        else{
            throw new IndexOutOfBoundsException("The given point lies outside of the 2D sequence");
        }
    }

    /**
    * @brief setter method for Seq2D, set a value at a given point
    * @param p the point to set the value at
    * @throws IllegalArgumentException if the point lies outside of the map, i.e the row and column of the point are out of bounds
    */
    public T get(PointT p){
        if(valid_point(p)){
            return s.get(p.row()).get(p.col());
        }
        else{
            throw new IndexOutOfBoundsException("The given point lies outside of the 2D sequence");
        }

    }

    /**
    * @brief getter method for the number of rows in an instance of Seq2D
    */
    public int getNumRow(){
        return n_row;
    }

    /**
    * @brief getter method for the number of columns in an instance of Seq2D
    */
    public int getNumCol(){
        return n_col;
    }

    /**
    * @brief getter method for the scale in an instance of Seq2D
    */
    public double getScale(){
        return scale;
    }

    /**
    * @brief count the occurences of a value in the current 2D sequence
    * @param t the value to count the occurences for
    * @return the number of occurences of t in the current 2D sequence
    */
    public int count(T t){
        int count = 0;
        for(int i = 0; i < s.size(); i++){
            count += countRow(t, i);
        }
        return count;
    }

    /**
    * @brief count the occurences of a value in the current 2D sequence in a particular row
    * @param t the value to search for
    * @param i the row index to search t 
    * @return the count of the occurences of parameter t in row i
    * @throws IllegalArgumentException if the row index i is out of bounds
    */
    public int countRow(T t, int i){
        if(!valid_row(i)) throw new IndexOutOfBoundsException("Invalid row index");

        int count = 0;
        for(int j = 0; j < s.get(i).size(); j++){
            if(s.get(i).get(j) == t) count++;
        }
        return count;
    }

    /**
    * @brief return the area taken up by a particular value t
    * @param t the value to calculate the area taken up for
    * @throws IllegalArgumentException if the row index i is out of bounds
    */
    public double area(T t){
        return count(t)*scale;
    }

    /**
     * @brief private helper method to validate a row numer
     * @param row the row number to validate
     * @return boolean indicating if the row number is valid
     */
    private boolean valid_row(int row){
        return row >= 0 && row < n_row;
    }

     /** 
     * @brief private helper method to valid a column number
     * @param col the column number to validate
     * @return boolean indicating if the column number is valid (i.e lies in the 2D sequences bounds)
     */
    private boolean valid_col(int col){
        return col >= 0 && col < n_col;
    }

     /** 
     * @brief private helper method to valid a PointT object
     * @param p the PointT object to validate
     * @return boolean indicating if the column number is valid (i.e lies in the 2D sequences bounds)
     */
    private boolean valid_point(PointT p){
        return valid_row(p.row()) && valid_col(p.col());
    }

}