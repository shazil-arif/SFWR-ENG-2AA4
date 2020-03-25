
/** 
*  @file LanduseMapT.java
*  @author Shazil Arif
*  @brief LanduseMapT extends Seq2D and is parameterized with type Colors
*  @date April 1st 2020
*/


/** 
* @brief TwoDotsBoard provides an ADT to represent a TwoDots game board parameterized by the type Colors
* @details extends from Board class
*/
public class TwoDotsBoard extends Board<Color>{

	/**
     * @brief Constructor method for TwoDotsBoard
     * @param row the number of rows desired in the board
     * @param col the number of columns desired in the board
     * @details The board is initialized to random colors
     * @throws IllegalArgumentException if the parameter row or parameter col is less than or equal to 0
     */
	public TwoDotsBoard(int row, int col) {
		super(row, col);
		for(int i = 0; i < n_row; i++) {
			for(int j = 0; j < n_col; j++) {
				Color random_color = Color.randomColor();
				s.get(i).add(random_color);
			}
		}
	}
	
	public boolean validateMoves(BoardMoves moves) {
		//first check if each move is a valid point on the board
		for (PointT move : moves) {
			if(!validPoint(move))
				 return false; 
		 }
		
		//then check if the sequence represents a valid path
		return isValidPath(moves);
    }
	
	/**
	 * @brief setter method to update a sequence of cells on the Board that have been removed
	 * @param moves sequence of BoardMoves containing the cells on the Board to update
	 */
	public void updateBoard(BoardMoves moves) {
		for (PointT move : moves) {
			Color rnd_color = Color.randomColor();
			s.get(move.row()).set(move.col(), rnd_color);
		}
		
	}
	
	public boolean isPlayable() {
		return true;
	}
	
	/**
	 * @brief private helper method to check if a given BoardMoves sequence represents a valid move on the Two Dots Board, i.e check if it is a valid path
	 * @param moves the sequence to validate
	 * @return boolean indicating if the given sequence represents a valid path
	 */
	private boolean isValidPath(BoardMoves moves) {
		
		//allow to move horizontally and vertically
		int[] x = {-1,1,0,0};
		int[] y = {0,0,1,-1};
		
		//iterate over all the moves
		//main idea is to check if we can reach every Point starting from the beginning if we move only horizontally and verically
		for (int curr = 0; curr < moves.size() - 1; curr++) {
			int i = moves.get(curr).row();
			int j = moves.get(curr).col();
			
			PointT neighbor = moves.get(curr+1); //the next move
			Color neighbor_color = s.get(neighbor.row()).get(neighbor.col()); //color of next move
			Color current_color = s.get(i).get(j); 
			
			//check if neighbor is reachable from current cell in Board
			for(int k = 0; k < x.length; k++) {
				
				//first check if neighboring cell indices are within bounds, create a point for this
				PointT temp = new PointT(i+x[k],j+y[k]);
				
				//if not reachable this set of moves is invalid
				if(!(validPoint(temp) && current_color == neighbor_color))
					return false;
			}
			
		 }
		
		return true;
		
	}

}