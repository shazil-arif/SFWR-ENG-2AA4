
/** 
*  @file LanduseMapT.java
*  @author Shazil Arif
*  @brief LanduseMapT extends Seq2D and is parameterized with type Colors
*  @date April 1st 2020
*/


/** 
* @brief LanduseMapT provides an ADT to a 2D TwoDots game board parametrized by the type Colors
* @details extends from Board
*/
public class TwoDotsBoard extends Board<Colors>{

	public TwoDotsBoard(int row, int col) {
		super(row, col);
	}
	
	public boolean validateMoves(BoardMoves moves) {
   	 for (PointT move : moves) {
   		 if(!validPoint(move))
   			 return false;
   		 if()
   		 
   	 }
   	 return true;
    }
	
	private boolean hasPath(PointT source, PointT dest) {
		return true;
	}

}
