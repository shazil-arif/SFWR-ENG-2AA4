
public class BoardView {
	public static final String ANSI_RESET = "\u001B[0m";
	public static final String ANSI_BLACK = "\u001B[30m";
	public static final String ANSI_RED = "\u001B[31m";
	public static final String ANSI_GREEN = "\u001B[32m";
	public static final String ANSI_YELLOW = "\u001B[33m";
	public static final String ANSI_BLUE = "\u001B[34m";
	public static final String ANSI_PURPLE = "\u001B[35m";
	public static final String ANSI_CYAN = "\u001B[36m";
	public static final String ANSI_WHITE = "\u001B[37m";
	public void printBoard(TwoDotsBoard board) {
		for(int i = 0; i < board.getNumRow(); i++) {
			String line = String.format(" | %d | ",i+1);  
			System.out.print(line);			
		}
		System.out.println();
		for(int i = 0; i < board.getNumRow(); i++) {
			String line = String.format(" | %d |  ",i+1);  
			System.out.print(line);
			for(int j = 0; j < board.getNumCol(); j++) {
				Color out = board.get(new PointT(i,j));
				String out_line = String.format("  %s   ",out);  
				System.out.println(ANSI_RED + out_line + ANSI_RESET);
			}
			System.out.println();
			
		}
		
	}
	
	public static void main(String[] args) {
		TwoDotsBoard b = new TwoDotsBoard(6,6);
		BoardView v = new BoardView();
		v.printBoard(b);
		
	}

}
