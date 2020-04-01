import java.util.Dictionary;
import java.util.Hashtable;
import java.util.Scanner;

public class BoardView {
	//source: https://stackoverflow.com/questions/5762491/how-to-print-color-in-console-using-system-out-println
	private static final String ANSI_RESET = "\u001B[0m";
	private static final String ANSI_RED = "\u001B[31m";
	private static final String ANSI_GREEN = "\u001B[32m";
	private static final String ANSI_BLUE = "\u001B[34m";
	private static final String ANSI_PURPLE = "\u001B[35m";
	private static final String ANSI_YELLOW = "\u001B[33m";
	private static final Dictionary<Color,String> colors = new Hashtable<Color,String>(); 
	Scanner s;
    
         
	public void printBoard(TwoDotsBoard board) {
		//create a mapping between Colors enums and corresponding string value for printing colored text in terminal
		colors.put(Color.R, ANSI_RED);
		colors.put(Color.G,ANSI_GREEN);
		colors.put(Color.B,ANSI_BLUE);
		colors.put(Color.P,ANSI_PURPLE);
		colors.put(Color.O,ANSI_YELLOW); //using yellow for orange for now

		
		System.out.print(" | 0 |");
		for(int i = 0; i < board.getNumRow(); i++) {
			String line = String.format(" | %d |",i+1);  
			System.out.print(line);			
		}
		
		System.out.println();
		
		for(int i = 0; i < board.getNumRow(); i++) {
			String line = String.format(" | %d |",i+1);  
			System.out.print(line);
			for(int j = 0; j < board.getNumCol(); j++) {
				Color out = board.get(new PointT(i,j));
				String out_line = String.format("   %s  ",out);
				//out_line = colors.get(out) + out_line + ANSI_RESET;
				System.out.print(out_line);

			}
			System.out.println();
			
		}	
	}
	public Strategy modePrompt() {
		s = new Scanner(System.in);
		printMsg("Enter T for timed Mode or M for moves mode.");
		String input = s.nextLine();
		input = input.toUpperCase();
		while(!(input.equals("T") || input.equals("M"))) {
			printMsg("Only T and M are valid game modes");
			input = s.nextLine();
			input = input.toUpperCase();
		} 
		if(input.equals("T")) {
			TimedStrategy t = new TimedStrategy();
			return t;
		}
		else {
			MovesStrategy m = new MovesStrategy();
			return m;
		}
	}
	
	public BoardMoves getInput() {
		s = new Scanner(System.in);
		String input;
		BoardMoves bmoves = new BoardMoves();
		boolean retry = true;
		while(retry) {
			input = s.nextLine();
			String[] moves = input.split(" ");
			for(String move : moves) {
				if(tryParseString(move)) {
					String[] temp = move.split(",");
					if(tryParse(temp[0]) && tryParse(temp[1])) {
						int row = Integer.parseInt(temp[0]);
						int col = Integer.parseInt(temp[1]);
						PointT point = new PointT(row-1,col-1);
						retry = false;
						bmoves.add(point);
					}		
					else {
						printMsg("Invalid input");
						break;
					}
				}
				else {
					printMsg("Invalid input");
					break;
				}
				
			}
		}
		return bmoves;
	}
	
	
	public void closeStream() {
		s.close();
	}
	public void printMsg(String msg) { 
		System.out.println(msg); 
	}
	
	public static void main(String[] args) {
		TwoDotsBoard b = new TwoDotsBoard(6,6);
		BoardView v = new BoardView();
		v.printBoard(b);
	}
	
	private boolean tryParse(String a) {
		try {
			Integer.parseInt(a);
			return true;
		}
		catch(NumberFormatException e) {
			return false;
		}
	}
	private boolean tryParseString(String a) {
		try {
			String[] tmp = a.split(",");
			String s= tmp[0];
			String c = tmp[1];
			return true;
		}
		catch(RuntimeException e) {
			return false;
		}
		
	}
}

