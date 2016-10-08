package Leetcode;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;

/**
 * Created by Jiawen on 16/10/8.
 */
public class FrogJump {

    public boolean canCross(int[] stones) {
        int m = stones.length;
        if(m == 0){
            return true;
        }
        //key是stone[i]，value是从这快石头出发可以跳的步数
        HashMap<Integer, HashSet<Integer>> map = new HashMap<>();
        map.put(0, new HashSet<>());
        //从第0块石头出发，只能跳1步
        map.get(0).add(1);

        for(int i=1; i<m; i++){
            map.put(stones[i], new HashSet<>());
        }

        for(int i=0; i<m; i++){
            HashSet<Integer> steps = map.get(stones[i]);
            //计算从这快石头出发，能够到达的所有距离，如果该距离正好是一块石头的位置，
            //则更新下一块石头可以跳的步数
            for(int step : steps){
                int reach = stones[i] + step;
                if(reach == stones[m-1]){
                    return true;
                }
                HashSet<Integer> set = map.get(reach);
                if(set != null){
                    set.add(step);
                    set.add(step+1);
                    if(step-1 >0){
                        set.add(step-1);
                    }
                }
            }
        }
        return false;
    }


    public static void main(String args[]){
        FrogJump solution = new FrogJump();
        int[] stones0 = {0, 1, 3, 5, 6, 8, 12, 17};
        System.out.println(solution.canCross(stones0));

        int[] stones1 = {0,1,2,3,4,8,9,11};
        System.out.println(solution.canCross(stones1));
    }

}
