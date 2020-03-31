
public class MovesStrategy extends StrategyGameMode{

	private int moves = 30;
	@Override
	public void play() {
		// TODO Auto-generated method stub
	}

	@Override
	boolean canContinue() {
		return moves > 0;
	}

	@Override
	void updateConditions() {
		moves--;
	}

}
