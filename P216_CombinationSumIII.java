package Leetcode;

import sun.awt.image.ImageWatched;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

/**
 * Created by Jiawen on 16/10/23.
 */
public class CombinationSumIII {

    private List<List<Integer>> results = new ArrayList<>();

    public List<List<Integer>> combinationSum3(int k, int n) {
        LinkedList<Integer> res = new LinkedList<>();
        backtracing(k, n, res, 1);
        return results;

    }

    public void backtracing(int k, int n, LinkedList<Integer> res, int begin){
        if(n == 0 && k == 0){
            results.add(new LinkedList<>(res));
            return;
        }
        for(int i=begin; i<=9; i++){
            if(i > n){
                break;
            }
            res.add(i);
            backtracing(k-1, n-i, res, i+1);
            res.removeLast();
        }
    }

    public static void main(String[] args){
        CombinationSumIII solution = new CombinationSumIII();
        solution.combinationSum3(3,7);
        System.out.println(solution.results);

        CombinationSumIII solution1 = new CombinationSumIII();
        solution1.combinationSum3(3,9);
        System.out.println(solution1.results);
    }


}
