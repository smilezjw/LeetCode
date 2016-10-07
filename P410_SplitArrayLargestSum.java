package Leetcode;

/**
 * Created by Jiawen on 16/10/7.
 */
public class SplitArrayLargestSum {

    public int splitArray(int[] nums, int m) {
        int max = 0;
        int sum = 0;
        for(int num : nums){
            max = Math.max(max, num);
            sum += num;
        }
        //如果m等于1，那么整个数组划分为一个子集，直接返回该数组的和即可
        if(m == 1){
            return sum;
        }
        //如果m和nums个数相同，那么每个元素就是一个子集，直接返回最大的那个元素即可
        if(m == nums.length){
            return max;
        }
        //范围在[max, sum]之间，用二分搜索来做
        return binarySearch(nums, max, sum, m);
    }


    public int binarySearch(int[] nums, int low, int high, int m){
        while(low < high){
            int mid = (low + high) / 2;
            //判断mid这个值是否合法
            if(isValid(nums, m, mid)){
                high = mid;
            }else{
                low = mid + 1;
            }
        }
        return high;
    }


    public boolean isValid(int[] nums, int m, int max){
        int sum = 0;
        //注意这里cnt初始值为1，子数组的个数等于划分次数加1
        int cnt = 1;
        for(int num : nums){
            sum += num;
            //如果划分子数组的和大于max，则num划分到新的子数组中
            if(sum > max){
                sum = num;
                cnt++;
                //判断划分的子数组个数是否超过要求的m个，超过则说明这种划分方法不正确
                if(cnt > m){
                    return false;
                }
            }
        }
        return true;
    }


    public static void main(String[] args){
        SplitArrayLargestSum solution = new SplitArrayLargestSum();
        int[] nums = {7, 2, 5, 10, 8};
        System.out.println(solution.splitArray(nums, 2));
    }


}
