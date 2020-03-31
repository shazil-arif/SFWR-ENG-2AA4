abstract public class StrategyGameMode implements Strategy {
	
	public void play(TwoDotsBoard b) {
		BoardView v = new BoardView();
		BoardController c = new BoardController(b,v);
		BoardMoves moves;
		while(c.isPlayable() && canContinue()) {
			c.updateView();
			moves = c.getInput();
			updateConditions();
			c.updateBoard(moves);
		}
	}
	abstract void updateConditions();
	abstract boolean canContinue();

}
