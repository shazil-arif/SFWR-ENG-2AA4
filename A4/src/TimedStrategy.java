import java.util.Timer;
import java.util.TimerTask;
public class TimedStrategy extends StrategyGameMode{

	private final int TARGET = 5;
	private final int TIME = 60;
	private boolean has_ended = false;
	Timer timer;
	
	@Override
	void updateConditions() {
		
	}

	@Override
	boolean canContinue() {
		return has_ended;
	}

	@Override
	void updateData() {
		if(has_ended) {
			c.printMsg("Time's Up!");
			System.exit(0);
		}
		else {
			c.printMsg("Keep playing");
		}
	}

	@Override
	void introMsg() {
		c.printMsg(String.format("This is the mode with %d seconds",TIME));
		c.printMsg(String.format("You win by eliminating %d dots in one move",TARGET));
		c.printMsg("Enter a sequence of x,y pairs seperate by spaces");
		c.printMsg("Example: 1,2 4,5 5,5");
	}

	@Override
	void startUp() {
		timer = new Timer();
		timer.schedule(new GameEnd(), TIME*1000);	
	}
	
	class GameEnd extends TimerTask {
		public void run() {
			timer.cancel();
			has_ended = true;
		}
		
	}
}
