public class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        if(nums.length == 0){
            return 0;
        }
        int cnt = 0;
        int res = 0;
        for(int i=0; i<nums.length; i++){
            if(nums[i] == 1){
                cnt++;
                res = Math.max(res, cnt);
            }else{
                cnt = 0;
            }
        }
        return res;
    }
}
