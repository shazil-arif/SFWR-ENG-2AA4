abstract public class StrategyGameMode implements Strategy {
	protected BoardView v;
	protected BoardController c;
	protected BoardMoves moves;
	public void play(TwoDotsBoard b) {
		startUp(b);
		introMsg();
		while(c.isPlayable() && canContinue()) {
			c.updateView();
			moves = c.getInput();
			c.updateBoard(moves);
			checkWin();
			updateData();
		}
	}
	
	abstract void startUp(TwoDotsBoard b);
	abstract void checkWin();
	abstract boolean canContinue();
	abstract void updateData();
	abstract void introMsg();

}

