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
	
	@Before
	public void SetUp() {
		ArrayList<ArrayList<Color>> s = new ArrayList<ArrayList<Color>>();
		s.add(new ArrayList<Color>(Arrays.asList(Color.R,Color.G,Color.R,Color.G,Color.R,Color.B)));
		s.add(new ArrayList<Color>(Arrays.asList(Color.G,Color.R,Color.G,Color.B,Color.G,Color.P)));
		s.add(new ArrayList<Color>(Arrays.asList(Color.B,Color.O,Color.B,Color.R,Color.O,Color.B)));
		s.add(new ArrayList<Color>(Arrays.asList(Color.O,Color.G,Color.O,Color.P,Color.B,Color.G)));
		s.add(new ArrayList<Color>(Arrays.asList(Color.P,Color.B,Color.P,Color.O,Color.G,Color.O)));
		s.add(new ArrayList<Color>(Arrays.asList(Color.R,Color.P,Color.B,Color.R,Color.P,Color.R)));
	}
	

}
