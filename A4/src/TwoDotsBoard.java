import java.util.ArrayList;

/** 
*  @file TwoDotsBoard.java
*  @author Shazil Arif
*  @brief TwoDotsBoard extends Board and is parameterized with type Colors
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
		
		while(!isPlayable()) {
			for(int i = 0; i < n_row; i++) {
				for(int j = 0; j < n_col; j++) {
					Color random_color = Color.randomColor();
					s.get(i).add(random_color);
				}
			}
		}
	}
	
	 /**
     * @brief second constructor for TwoDotsBoard, this constructor should be used when a initially randomized board is not desired
     * @details this is usually helpful for testing the board
     * @param s input sequence of rows representing the board to instantiate
     */
	public TwoDotsBoard(ArrayList<ArrayList<Color>> s) {
		super(s);
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
	 * @brief setter method to update the board after 
	 * @param moves sequence of BoardMoves containing the cells on the Board to remove
	 */	
	public void updateBoard(BoardMoves moves) {
		for(PointT move: moves) {
			int row = move.row();
			int col = move.col();
			for(int i = row; i >= 1; i--) {
				//exchange board[row][col] with board[row-1][col]
				Color temp = s.get(i-1).get(col);
				set(new PointT(row,col), temp);
				row--;
			}
			setRandom(new PointT(row,col));
		}
	}
	public boolean isPlayable() {
		int[] x = {-1,1,0,0};
		int[] y = {0,0,1,-1};
		for(int i = 0; i < s.size(); i++) {
			for(int j = 0; j < s.get(i).size(); j++) {
				for(int k = 0; k < x.length; k++) {
					PointT neighbor = new PointT(i+x[k],j+y[k]);
					if(validPoint(neighbor)) {
						Color neighbor_color = s.get(neighbor.row()).get(neighbor.col()); //color of neighboring cell
						Color current_color = s.get(i).get(j);
						if(neighbor_color == current_color) return true;
						
					}
				}
			}
		}
		return false;
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
		boolean[][] visited = new boolean[getNumRow()][getNumCol()];
		for(int i = 0; i < getNumRow(); i++)
			for(int j = 0; j < getNumCol(); j++) 
				visited[i][j] = false;
		
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
				if(validPoint(temp)) {
					if(temp.row() == neighbor.row() && temp.col() == neighbor.col()) {
						//if neighboring cell is not same color this path cannot be valid
						
						//this cell was already visited on path, this means the line connecting the dots attempts to turn back which is not allowed
						if(visited[neighbor.row()][neighbor.col()]) return false;

						visited[neighbor.row()][neighbor.col()] = true;
						if(current_color != neighbor_color) 
							return false;						
					}
				}
			}
			if(!visited[neighbor.row()][neighbor.col()]) return false;
		 }
		
		return true;	
	}
	
	private void setRandom(PointT p) {
		Color rnd_color = Color.randomColor();
		set(p,rnd_color);
		if(!isPlayable()) setRandom(p);
	}
}
