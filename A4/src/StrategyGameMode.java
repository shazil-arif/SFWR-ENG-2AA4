import java.util.Timer;
import java.util.TimerTask;
abstract public class StrategyGameMode implements Strategy {
	
	public void play(TwoDotsBoard b) {
		BoardView v = new BoardView();
		BoardController c = new BoardController(b,v);
		while(b.isPlayable() && canContinue()) {
			c.updateView();
			c.getInput();
			
			
		}
	}
	abstract boolean canContinue();

}
