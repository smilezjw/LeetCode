package Leetcode;

/**
 * Created by Jiawen on 16/10/22.
 */
public class MaximumGap {

    /*
    * Bucket sort
    * https://segmentfault.com/a/1190000002732382
    * */
    public int maximumGap(int[] nums) {
        if(nums == null || nums.length <= 1){
            return 0;
        }
        int maxNum = Integer.MIN_VALUE;
        int minNum = Integer.MAX_VALUE;
        int length = nums.length;
        for(int i=0; i<length; i++){
            maxNum = Math.max(maxNum, nums[i]);
            minNum = Math.min(minNum, nums[i]);
        }
        int buckets = (maxNum - minNum) / (length - 1);
        buckets = buckets == 0 ? 1 : buckets;
        int[] left = new int[(maxNum - minNum) / buckets + 1];
        int[] right = new int[(maxNum - minNum) / buckets + 1];
        for(int i=0; i<length; i++){
            int buck = (nums[i] - minNum) / buckets;
            if(buck == left.length){
                buck--;
            }
            left[buck] = left[buck] == 0 ? nums[i] : Math.min(left[buck], nums[i]);
            right[buck] = right[buck] == 0 ? nums[i] : Math.max(right[buck], nums[i]);
        }
        int leftMax = 0;
        int rightMin = 0;
        int maxGap = 0;
        for(int i=0; i<left.length; i++){
            if(left[i] == 0 && right[i] == 0){
                continue;
            }
            if(leftMax == 0){
                leftMax = right[i];
                continue;
            }
            rightMin = left[i];
            maxGap = Math.max(maxGap, rightMin - leftMax);
            leftMax = right[i];
        }
        return maxGap;
    }



}
