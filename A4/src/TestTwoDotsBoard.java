/** 
*  @file TestDemT.java
*  @author Shazil Arif
*  @brief TestDemT is used to test module DemT
*  @date March 16th 2020
*/

import org.junit.*;
import static org.junit.Assert.*;
import java.util.ArrayList;
import java.util.Arrays;

public class TestTwoDotsBoard {
	
	TwoDotsBoard b;
	
	@Before
	public void SetUp() {
		ArrayList<ArrayList<Color>> s = new ArrayList<ArrayList<Color>>();
		
		//note that there is a valid path at the top left with the 3 red dots
		s.add(new ArrayList<Color>(Arrays.asList(Color.R,Color.G,Color.R,Color.G,Color.R,Color.B)));
		s.add(new ArrayList<Color>(Arrays.asList(Color.R,Color.R,Color.G,Color.B,Color.G,Color.P)));
		s.add(new ArrayList<Color>(Arrays.asList(Color.B,Color.O,Color.B,Color.B,Color.O,Color.B)));
		s.add(new ArrayList<Color>(Arrays.asList(Color.O,Color.G,Color.O,Color.B,Color.B,Color.G)));
		s.add(new ArrayList<Color>(Arrays.asList(Color.P,Color.B,Color.P,Color.O,Color.G,Color.O)));
		s.add(new ArrayList<Color>(Arrays.asList(Color.R,Color.P,Color.B,Color.R,Color.P,Color.R)));
		b = new TwoDotsBoard(s);
	}
	
	//test constructor exceptions
	@Test(expected=IllegalArgumentException.class)
	public void testBoardExceptionForZeroRow() {
		new TwoDotsBoard(0,1);
	}
	@Test(expected=IllegalArgumentException.class)
	public void testBoardExceptionForNegativeRow() {
		new TwoDotsBoard(-1,1);
	}
	@Test(expected=IllegalArgumentException.class)
	public void testBoardExceptionForZeroCol() {
		new TwoDotsBoard(1,0);
	}
	@Test(expected=IllegalArgumentException.class)
	public void testBoardExceptionForNegativeCol() {
		new TwoDotsBoard(1,-1);
	}
	
	@Test
	public void testValidateMovesForSequenceSizeLessThanOne() {
		TwoDotsBoard board = new TwoDotsBoard(6,6);
		BoardMoves moves = new BoardMoves();
		assertTrue(!board.validateMoves(moves));	
	}
	
	@Test 
	public void testValidateMovesForSequenceSizeEqualOne() {
		TwoDotsBoard board = new TwoDotsBoard(6,6);
		BoardMoves moves = new BoardMoves();
		moves.add(new PointT(1,1));
		assertTrue(!board.validateMoves(moves));	
	}
	
	@Test 
	public void testValidateMovesWithInvalidPoints() {
		TwoDotsBoard board = new TwoDotsBoard(6,6);
		BoardMoves moves = new BoardMoves();
		moves.add(new PointT(-1,1));
		moves.add(new PointT(100,100));
		assertTrue(!board.validateMoves(moves));
	}
	
	@Test
	public void testValidateMoves() {
		BoardMoves moves = new BoardMoves();
		moves.add(new PointT(0,0));
		moves.add(new PointT(1,0));
		moves.add(new PointT(1,1));
		assertTrue(b.validateMoves(moves));	
	}
	
	@Test
	public void testValidateMovesWithRepeatedMoves() {
		BoardMoves moves = new BoardMoves();
		moves.add(new PointT(2,2));
		moves.add(new PointT(2,3));
		moves.add(new PointT(1,3));
		moves.add(new PointT(2,3));
		moves.add(new PointT(3,3));
		assertTrue(! b.validateMoves(moves));	
	}
	@Test
	public void testValidateMovesWithInvalidMoves() {
		BoardMoves moves = new BoardMoves();
		moves.add(new PointT(0,0));
		moves.add(new PointT(1,0));
		moves.add(new PointT(2,0));
		assertTrue(! b.validateMoves(moves));	
	}
	
}
