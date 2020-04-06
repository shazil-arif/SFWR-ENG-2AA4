/** 
*  @file GameEnd.java
*  @author Shazil Arif
*  @brief GameEnd contains routines to create a count down timer and execute a function when this timer is out of time
*  @date April 1st 2020
*/
import java.util.Timer;
import java.util.TimerTask;



/*  @brief GameEnd contains routines to create a count down timer and execute a function when this timer is out of time 
 */
public class CountDownTimer{
	//special thanks to: http://www.iitk.ac.in/esc101/05Aug/tutorial/essential/threads/timer.html
	 private Timer timer;
	 private End task;
	 private boolean cancelled;
	 
	 /*
	  * @brief constructor for GameEnd
	  * @param time the time in milli seconds to set for the timer
	  */
	 public CountDownTimer(int time) {
		 timer = new Timer();
		 task = new End();
		 cancelled = false;
		 timer.schedule(new End(), time*1000);	
	 }		
	 
	 public boolean isCancelled() {
		 return !this.cancelled;
	 }
	 
	 /*
	  * @brief class End extends TimerTask and provides a method to cancel the timer
	  */
	private class End extends TimerTask {
		
		/*
		 * @brief this method is executed when the timer's allocated time has run out
		 * @details exists the system with status code 0 once the timer cancels	
		 */
		public void run() {
			timer.cancel();
			cancelled = true;
			//System.out.println("Times up!");
			//System.exit(0);
		}
	}
}