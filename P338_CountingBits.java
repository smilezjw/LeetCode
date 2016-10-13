package Leetcode;

/**
 * Created by Jiawen on 16/10/14.
 */
public class CoutingBits {

    public int[] countBits(int num) {
        int[] res = new int[num+1];
        if(num < 0){
            return res;
        }
        res[0] = 0;
        //动归
        for(int n=1; n<=num; n++){
            res[n] = res[n>>1] + (n & 1);
        }
        return res;
    }

    public static void main(String[] args){
        CoutingBits solution = new CoutingBits();
        int[] res = solution.countBits(5);
        for(int i=0; i<res.length; i++){
            System.out.println(res[i]);
        }
    }


}
