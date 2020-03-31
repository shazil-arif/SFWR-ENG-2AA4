@SuppressWarnings("all")
class MovesStrategy extends StrategyGameMode{

	private int move_count;
	private final int TARGET = 5;
	
	@Override
	boolean canContinue() {
		return move_count > 0;
	}

	@Override
	void checkWin() {
		if(moves.size()==TARGET) {
			c.printMsg(String.format("You won by eliminating %d dots in one move!", TARGET));
			System.exit(0);
			
		}
		else
			move_count--;
	}

	@Override
	void introMsg() {
		c.printMsg(String.format("This is the mode with %d moves",move_count));
		c.printMsg(String.format("You win by eliminating %d dots in one move",TARGET));
		c.printMsg("Enter a sequence of x,y pairs seperate by spaces");
		c.printMsg("Example: 1,2 4,5 5,5");
	}

	@Override
	void updateData() {
		if(move_count == 0) {
			c.printMsg(String.format("The game ended! You ran out of moves"));
			System.exit(0);
		}
		c.printMsg(String.format("Moves left: %d", move_count));
	}

	@Override
	void startUp(TwoDotsBoard b) {
		v = new BoardView();
		c = new BoardController(b,v);
		move_count = 30;
	}

}