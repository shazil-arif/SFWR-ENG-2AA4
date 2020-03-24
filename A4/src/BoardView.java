
public class BoardView {
	public void printBoard(TwoDotsBoard board) {
		for(int i = 0; i < board.getNumRow(); i++) {
			String line = String.format(" | %d | ",i);  
			System.out.print(line);			
		}
		System.out.println();
		for(int i = 0; i < board.getNumRow(); i++) {
			String line = String.format(" | %d |  ",i);  
			System.out.print(line);
			for(int j = 0; j < board.getNumCol(); j++) {
				System.out.print(board.get(new PointT(board.getNumRow(),board.getNumCol())));
			}
			
		}
		
	}
	
	public void main(String[] args) {
		
	}

}
