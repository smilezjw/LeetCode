package com.smilezjw.mvnbook.hello_world;

import java.util.function.IntPredicate;

public class GasStation {
    
    public static int canCompleteCircuit(int[] gas, int[] cost){
        int totalGas = 0;
        int totalCost = 0;
        for(int i = 0; i < gas.length; i++){
            totalGas += gas[i];
            totalCost += cost[i];
        }
        if(totalGas < totalCost){
            return -1;
        }
        int startIndex = 0, remain = 0;
        for(int i=0; i<cost.length; i++){
            if(gas[i] + remain < cost[i]){
                startIndex = i+1;
            }else{
                remain += gas[i] - cost[i];
            }
        }
        return startIndex;
        
    }

    public static void main(String[] args) {
        int[] gas = {2,4};
        int[] cost = {3,4};
        System.out.println(canCompleteCircuit(gas, cost));
    }
}
