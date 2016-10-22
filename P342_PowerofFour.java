package Leetcode;

/**
 * Created by Jiawen on 16/10/14.
 */
public class PowerofFour {

    public boolean isPowerOfFour(int num) {
        while(num >= 4){
            if(num % 4 != 0){
                return false;
            }
            num >>= 2;
        }
        return num == 1;
    }

    public static void main(String[] args){
        PowerofFour solution = new PowerofFour();
        System.out.println(solution.isPowerOfFour(16));
        System.out.println(solution.isPowerOfFour(5));
        System.out.println(solution.isPowerOfFour(8));
        System.out.println(solution.isPowerOfFour(20));
    }

}
