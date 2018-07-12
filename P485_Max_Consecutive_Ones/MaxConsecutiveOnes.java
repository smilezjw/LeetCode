public class MaxConsecutiveOnes {
    public int findMaxConsecutiveOnes(int[] nums) {
        int cnt = 0;
        int res = 0;
        for(int n : nums) {
            if (n == 1) {
                cnt++;
                res = Math.max(res, cnt);
            } else {
                cnt = 0;
            }
        }
        return res;
    }

}