/** 
*  @file LanduseMapT.java
*  Author: Shazil Arif
*  Description: LanduseMapT extends Seq2D and is parameterized with type LuT
*  Revised: March 12th 2020
*/

import java.util.ArrayList;

/** 
* @brief LanduseMapT provides an ADT to represents a generic 2D sequence parameterized over any type LuT
* @details extends from Seq	2D
*/

public class LanduseMapT extends Seq2D<LuT>{
	
	/**
    * @brief Constructor method for LanduseMapT
    * @param S the input sequence of rows
    * @param scl the scale/dimension of a side of each cell
    * @throws IllegalArgumentException if the scale is less than or equal to 0, the input sequence is empty, the length of the
    * first sequence is 0 or the length of any row is not equal to the length of the first row
    */
    public LanduseMapT(ArrayList<ArrayList<LuT>> S, double scl){
        super(S,scl);
    }
}
