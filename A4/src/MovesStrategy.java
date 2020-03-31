
public class MovesStrategy extends StrategyGameMode{

	private int move_count = 30;
	private final int TARGET = 5;
	@Override
	public void play() {
		// TODO Auto-generated method stub
	}

	@Override
	boolean canContinue() {
		return move_count > 0;
	}

	@Override
	void updateConditions() {
		if(moves.size()==TARGET) {
			c.printMsg(String.format("You won by eliminating %d %s in one move!", TARGET));
			System.exit(1);
		}
		move_count--;
	}

}
