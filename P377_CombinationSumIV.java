package Leetcode;

/**
 * Created by Jiawen on 16/10/23.
 */
public class CombinationSumIV {

    public int combinationSum4(int[] nums, int target) {
        int[] dp = new int[target+1];
        dp[0] = 1;
        for(int i=1; i <= target; i++){
            for(int n : nums){
                if(i < n){
                    continue;
                }
                dp[i] += dp[i - n];
            }
        }

        return dp[target];
    }

    public static void main(String[] args){
        int[] nums = {3,1,2,4};
        CombinationSumIV solution = new CombinationSumIV();
        System.out.println(solution.combinationSum4(nums, 4));
    }

}
