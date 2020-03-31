@SuppressWarnings("all")
class MovesStrategy extends StrategyGameMode{

	private int move_count = 30;
	private final int TARGET = 5;
	
	@Override
	boolean canContinue() {
		return move_count > 0;
	}

	@Override
	void updateConditions() {
		if(moves.size()==TARGET) {
			c.printMsg(String.format("You won by eliminating %d in one move!", TARGET));
			System.exit(1);
		}
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
		c.printMsg(String.format("Moves left: %d", move_count));
	}

}