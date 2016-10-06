package Leetcode;

import java.util.LinkedList;
import java.util.List;

/**
 * Created by Jiawen on 16/10/6.
 */
public class BinaryWatch {

    public List<String> readBinaryWatch(int num) {
        LinkedList<String> result = new LinkedList<>();
        for(int hour=0; hour<12; hour++){
            for(int min=0; min<60; min++){
                if(numOfDigit1(hour) + numOfDigit1(min) == num){
                    if(min == 0){
                        result.add(hour + ":00");
                    }else if(min < 10){
                        result.add(hour + ":0" + min);
                    }else{
                        result.add(hour + ":" + min);
                    }
                }
            }
        }
        return result;
    }

    public int numOfDigit1(int n){
        int res = 0;
        while(n > 0){
            res += n & 1;
            n >>= 1;
        }
        return res;
    }

    public static void main(String[] args){
        BinaryWatch solution = new BinaryWatch();
        System.out.println(solution.readBinaryWatch(1));
        System.out.println(solution.readBinaryWatch(3));
    }

}
