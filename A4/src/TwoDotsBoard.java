
/** 
*  @file LanduseMapT.java
*  @author Shazil Arif
*  @brief LanduseMapT extends Seq2D and is parameterized with type Colors
*  @date April 1st 2020
*/

import java.util.ArrayList;
import java.util.Arrays;

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
		//ArrayList<ArrayList<Color>> p = new ArrayList<ArrayList<Color>>();
		s = new ArrayList<ArrayList<Color>>();

		s.add(new ArrayList<Color>(Arrays.asList(Color.R,Color.G,Color.R,Color.G,Color.R,Color.B)));
		s.add(new ArrayList<Color>(Arrays.asList(Color.G,Color.R,Color.G,Color.B,Color.G,Color.P)));
		s.add(new ArrayList<Color>(Arrays.asList(Color.B,Color.O,Color.B,Color.R,Color.O,Color.B)));
		s.add(new ArrayList<Color>(Arrays.asList(Color.O,Color.G,Color.O,Color.P,Color.B,Color.G)));
		s.add(new ArrayList<Color>(Arrays.asList(Color.P,Color.B,Color.P,Color.O,Color.G,Color.O)));
		s.add(new ArrayList<Color>(Arrays.asList(Color.R,Color.P,Color.B,Color.R,Color.P,Color.R)));

		
//		for(int i = 0; i < n_row; i++) {
//			for(int j = 0; j < n_col; j++) {
//				Color random_color = Color.randomColor();
//				s.get(i).add(random_color);
//			}
//		}
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
	
	public void isPlayable() {
		//BoardMoves all_points = getAllPoints();
		boolean[][] visited = new boolean[n_row][n_col];
		DFS(visited,new PointT(0,0), s.get(0).get(0));
		//return isValidPath(all_points);
	}
	
	private boolean DFS(boolean[][] visited, PointT p, Color target) {
		if(visited[p.row()][p.col()]==false) return;
		if(s.get(p.row()).get(p.col()) == target) return true;
		
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
				System.out.println("testing");
				//first check if neighboring cell indices are within bounds, create a point for this
				PointT temp = new PointT(i+x[k],j+y[k]);
				
				//if not reachable this set of moves is invalid
				if(!(validPoint(temp) && current_color == neighbor_color))
					return false;
			}
			
		 }
		
		return true;
		
	}
	public static void main(String[] args) {
		TwoDotsBoard b = new TwoDotsBoard(6,6);
		BoardView v = new BoardView();
		BoardController c = new BoardController(b,v);
		c.updateView();
		c.isPlayable();
	}
}
