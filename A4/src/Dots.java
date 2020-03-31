
public class Dots {
	public static void main(String[] args) {
		MovesStrategy m = new MovesStrategy();
		TwoDotsBoard b = new TwoDotsBoard(6,6);
		BoardView v = new BoardView();
		v.printMsg("Welcome to Two Dots!");
		v.printMsg("You can choose between the timed mode or the mode that lasts 30 moves");
		m.play(b);
	}

}
