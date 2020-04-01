
public class Dots {
	public static void main(String[] args) {
		TwoDotsBoard b = new TwoDotsBoard(6,6);
		BoardView v = new BoardView();
		BoardController c = new BoardController(b,v);
		c.printMsg("Welcome to Two Dots!\n");
		c.printMsg("You can choose between the timed mode or the mode that lasts 30 moves");
		Strategy mode = c.modePrompt();
		mode.play(b);
	}

}
