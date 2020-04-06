/** 
*  @file TimedStrategy.java
*  @author Shazil Arif
*  @brief TimedStrategy is the timed game mode for TwoDots 
*  @date April 2nd 2020
*/

import java.util.Timer;

/**
 * @brief 
 * @details extends StrategyGameMode to implement a customizable game play 
 */
public class TimedStrategy extends StrategyGameMode{

	private final int TARGET = 5;
	private final int TIME = 60; 
	private static final long BILLION = 1000000000;
	GameEnd g;
	Timer timer;
	private long start;
	
	
	@Override
	/*
	 * @brief check winning condition for gaming
	 * @details if 5 or more dots eliminated in one move then the game exits with status code 0
	 */
	void checkWin() {
		if(moves.size()==TARGET) {
			c.printMsg(String.format("You won by eliminating %d dots in one move!", TARGET));
			c.closeViewStream();
			System.exit(0);
		}
	}

	@Override
	/*
	 * @brief check if game can still be continued
	 * @details this always returns true, when the timer runs out the game will end anyways
	 * @return true
	 */
	boolean canContinue() {
		return true;
	}

	@Override
	/*
	 * @brief update view to indicate time elapsed since start of game
	 */
	void updateData() {
		long now = (System.nanoTime() - start)/BILLION;
		c.printMsg(String.format("Time elapsed: %d seconds",now));
	}

	@Override
	/*
	 * @brief display an intro message and brief information on how to play the game mode
	 */
	void introMsg() {
		c.printMsg(String.format("This is the mode with %d seconds",TIME));
		c.printMsg(String.format("You win by eliminating %d dots in one move",TARGET));
		c.printMsg("Enter a sequence of x,y pairs seperate by spaces");
		c.printMsg("Example: 1,2 4,5 5,5");
	}

	@Override
	/*
	 * @brief set up global variables at beginning of game
	 */
	void startUp(TwoDotsBoard b) {
		v = new BoardView();
		c = new BoardController(b,v);
		start = System.nanoTime();
		g = new GameEnd(TIME);
	}
}
