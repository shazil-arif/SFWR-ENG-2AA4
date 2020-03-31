import java.util.Timer;
import java.util.TimerTask;


public class GameEnd{
	//special thanks to: http://www.iitk.ac.in/esc101/05Aug/tutorial/essential/threads/timer.html
	 Timer timer;
	 End task;
	 public GameEnd(int time) {
		 timer = new Timer();
		 task = new End();
		 timer.schedule(new End(), time*1000);	
	 }		
	class End extends TimerTask {
		public void run() {
			timer.cancel();
			System.out.println("Times up!");
			System.exit(0);
		}
	}
}