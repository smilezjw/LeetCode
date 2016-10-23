package Leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

/**
 * Created by Jiawen on 16/10/23.
 */
public class CombinationSum {
    private List<List<Integer>> results = new ArrayList<>();

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        LinkedList<Integer> res = new LinkedList<>();
        backtracing(candidates,target, res, 0);
        return results;

    }

    public void backtracing(int[] candidates, int target, LinkedList<Integer> res, int begin){
        if(target == 0){
            results.add(new LinkedList<>(res));
            return;
        }
        for(int i=begin; i<candidates.length; i++){
            if(candidates[i] > target){
                break;
            }
            if(i>begin && candidates[i] == candidates[i-1]){
                continue;
            }
            res.add(candidates[i]);
            // 同一个元素是否可以重复计算，区别就在于这里传入参数i 还是 i+1
            backtracing(candidates, target-candidates[i], res, i);
            res.removeLast();
        }
    }

    public static void main(String[] args){
        int[] nums = {2, 3, 6, 7};
        CombinationSum solution = new CombinationSum();
        solution.combinationSum(nums, 7);
        System.out.println(solution.results);

    }


}
