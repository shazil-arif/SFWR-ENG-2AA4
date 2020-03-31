abstract public class StrategyGameMode implements Strategy {
	protected BoardView v = new BoardView();
	protected BoardController c;
	protected BoardMoves moves;
	public void play(TwoDotsBoard b) {
		c = new BoardController(b,v);
		while(c.isPlayable() && canContinue()) {
			c.updateView();
			moves = c.getInput();
			c.updateBoard(moves);
			updateConditions();
		}
	}
	abstract void updateConditions();
	abstract boolean canContinue();

}
