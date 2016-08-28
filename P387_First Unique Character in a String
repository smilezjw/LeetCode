//Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

public class Solution {
    public int firstUniqChar(String s) {
        char[] arr = s.toCharArray();
        int[] index = new int[26];
        Arrays.fill(index, -1);
        for(int i=0; i<arr.length; i++){
            int idx = s.charAt(i) - 'a';
            if(index[idx] == -1){
                index[idx] = i;
            }else if(index[idx] >= 0){
                index[idx] = -2;
            }
        }
        int result = arr.length;
        for(int i=0; i<index.length; i++){
            if(index[i] >= 0){
                result = Math.min(result, index[i]);
            }
        }
        if(result == arr.length){
            return -1;
        }
        return result;
    }
}
