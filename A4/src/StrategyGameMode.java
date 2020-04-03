/** 
*  @file StrategyGameMode.java
*  @author Shazil Arif
*  @brief StrategyGameMode defines a generic algorithm for playing a Strategy/game mode for TwoDots
*  @date April 2nd 2020
*/


/** 
* @brief Strategy is an interface for defining a family of game modes for Two Dots
* @details implements the Strategy interface
*/
abstract public class StrategyGameMode implements Strategy {
	
	//state variables
	protected BoardView v;
	protected BoardController c;
	protected BoardMoves moves;
	
	/*
	 * @brief implements the play method in the Strategy interface. represents a generic process for playing different modes with 
	 * the help of abstract template methods
	 * @param the TwoDotsBoard to play the game on
	 */
	public void play(TwoDotsBoard b) {
		startUp(b);
		introMsg();
		while(canContinue()) {
			c.updateView();
			moves = c.getInput();
			c.updateBoard(moves);
			checkWin();
			updateData();
		}
	}
	
	/*
	 * @brief abstract method to be overriden. model a customizable startup process at the beginning of each game mode
     * @param b a TwoDotsBoard
	 */
	abstract void startUp(TwoDotsBoard b);
	
	/*
	 * @brief generic method to check winning condition. customizable by child class/each differet game mode has its own conditions
	 */
	abstract void checkWin();
	
	/*
	 * @brief generic template method to check if the game can be continued based on some constraints
	 */
	abstract boolean canContinue();
	
	/*
	 * @brief generic template method to update/output some data/info about the current game to a user. examples may include but not limited to
	 * score, moves left, time left, number of dots eliminated for a specific color etc. Again a customizable method 
	 */
	abstract void updateData();
	
	/*
	 * @brief generic template method to give the user a brief intro to the current game mode. customizable as per game mode and can be overriden
	 * by child classes
	 */
	abstract void introMsg();

}

