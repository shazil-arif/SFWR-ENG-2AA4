/** 
*  @file Colors.java
*  @author Shazil Arif
*  @brief Colors contains an enumeration for different colors on a two dots game board
*  @date April 1st 2020
*/

import java.util.Random;

public enum Color{
    R,G,B,P,O;
	
	public static Color randomColor(){
		Random rnd = new Random();
	    int index = rnd.nextInt(Color.values().length);
	    return Color.values()[index];
	}
}


