
public class BoardController {
	private TwoDotsBoard model;
	private BoardView view;
	
	public BoardController(TwoDotsBoard model, BoardView view) {
		this.model = model;
		this.view = view;
	}
	
	public Color get(PointT p) {
		return model.get(p);
	}
	
	public void set(PointT p, Color c) {
		model.set(p, c);
	}
	
	public boolean isPlayable() {
		return model.isPlayable();
	}
	public boolean validateMoves(BoardMoves moves) {
		return model.validateMoves(moves);
	}
	public void updateBoard(BoardMoves moves) {
		model.updateBoard(moves);
	}
	
	public void updateView() {
		view.printBoard(model);
	}
	
	public BoardMoves getInput() {
		BoardMoves b = view.getInput();
		while(!model.validateMoves(b)) {
			view.printMsg();
			b = view.getInput();
		}
		return b;
	}
	

}
