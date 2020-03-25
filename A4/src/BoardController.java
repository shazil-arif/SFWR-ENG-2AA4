
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
	
	public boolean validateMoves(BoardMoves moves) {
		return model.validateMoves(moves);
	}
	public void updateBoard(BoardMoves moves) {
		model.updateBoard(moves);
	}
	
	public void updateView() {
		view.printBoard(model);
	}
	

}
