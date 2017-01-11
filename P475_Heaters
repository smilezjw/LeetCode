public class Solution {
    public int findRadius(int[] houses, int[] heaters) {
        if(houses.length <= 0 || heaters.length <= 0){
            return -1;
        }
        Arrays.sort(houses);
        Arrays.sort(heaters);
        int minRadius = Integer.MIN_VALUE;
        int left = 0;
        int right = 0;
        for(int i=0; i<houses.length; i++){
            while(right < heaters.length && houses[i] > heaters[right]){
                left = right++;
            }
            if(right == heaters.length){
                right--;
            }
            minRadius = Math.max(minRadius,Math.min(Math.abs(houses[i] - heaters[left]), Math.abs(heaters[right] - houses[i])));
        }
        return minRadius;
    }
}
