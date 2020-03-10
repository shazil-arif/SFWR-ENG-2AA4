//package src;
import java.util.ArrayList;
public class DemT extends Seq2D<Integer>{
    public DemT(ArrayList<ArrayList<Integer>> S, double scl){
        super(S,scl);
    }

    /**
    * @brief sum up the total of all values in the current DemT object
    * @return the sum of all the values
    */
    public int total(){
        int count = 0;
        for(int i = 0; i < s.size(); i++){
            for(int j = 0; j < s.get(i).size(); j++){
                count += s.get(i).get(j);
            }
        }
        return count;
    }

    /**
    * @brief find the maximum value in the DemT object
    * @return the max value
    */
    public int max(){
        int max = s.get(0).get(0);
        for(int i = 0; i < s.size(); i++){
            for(int j = 0; j < s.get(i).size(); j++){
                if(s.get(i).get(j) >= max){
                    max = s.get(i).get(j);
                }
            }
        }
        return max;
    }

    /**
    * @brief find the maximum value in the DemT object
    * @return the max value
    */
    public boolean ascending_rows(){
        for(int i = 0; i < s.size()-1; i++){
            if(row_sum(i+1) <= row_sum(i)) return false;
        }
        return true;
    }


    /**
    * @brief jelper method to find the sum of values in a given row
    * @param r the row to sum up the values of
    * @return the sum of the values in the row r
    */
    private int row_sum(int r){
        int count = 0;
        for(int i = 0; i < s.get(r).size(); i++){
            count += s.get(r).get(i);
        }
        return count;
    }


}
