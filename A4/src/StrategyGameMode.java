abstract public class StrategyGameMode implements Strategy {
	protected BoardView v;
	protected BoardController c;
	protected BoardMoves moves;
	public void play(TwoDotsBoard b) {
		c = new BoardController(b,v);
		startUp();
		introMsg();
		while(c.isPlayable() && canContinue()) {
			c.updateView();
			moves = c.getInput();
			c.updateBoard(moves);
			checkWin();
			updateData();
		}
	}
	
	abstract void startUp();
	abstract void checkWin();
	abstract boolean canContinue();
	abstract void updateData();
	abstract void introMsg();

}

