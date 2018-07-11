public class MinimumMovesToEqualArrayElements {
    public int minMoves (int[] nums) {
        int minNum = nums[0];
        for(int n : nums) {
            minNum = min(n,minNum);
        }

        int steps = 0;
        for(int n : nums) {
            steps += n - minNum;
        }
        return steps;
    }

}

