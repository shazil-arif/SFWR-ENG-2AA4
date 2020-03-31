import java.util.Timer;
import java.util.TimerTask;

public class TimedStrategy extends StrategyGameMode{

	private final int TARGET = 5;
	private final int TIME = 60; 
	private static final long BILLION = 1000000000;
	GameEnd g;
	Timer timer;
	private long start;
	
	
	@Override
	void checkWin() {
		if(moves.size()==TARGET) {
			c.printMsg(String.format("You won by eliminating %d dots in one move!", TARGET));
			c.closeViewStream();
			System.exit(0);
		}
	}

	@Override
	boolean canContinue() {
		return true;
	}

	@Override
	void updateData() {
		long now = (System.nanoTime() - start)/BILLION;
		c.printMsg(String.format("Time elapsed: %d seconds",now));
	}

	@Override
	void introMsg() {
		c.printMsg(String.format("This is the mode with %d seconds",TIME));
		c.printMsg(String.format("You win by eliminating %d dots in one move",TARGET));
		c.printMsg("Enter a sequence of x,y pairs seperate by spaces");
		c.printMsg("Example: 1,2 4,5 5,5");
	}

	@Override
	void startUp(TwoDotsBoard b) {
		v = new BoardView();
		c = new BoardController(b,v);
		start = System.nanoTime();
		g = new GameEnd(TIME);
	}
}
