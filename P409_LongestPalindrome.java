package leetcode;

import java.util.HashMap;

/**
 * Created by Jiawen on 16/10/6.
 */
public class LongestPalindrome {

    public int longestPalindrome(String s) {
        HashMap<Character, Integer> map = new HashMap<>();
        for(int i=0; i<s.length(); i++){
            if(map.containsKey(s.charAt(i))){
                map.put(s.charAt(i), map.get(s.charAt(i))+1);
            }else{
                map.put(s.charAt(i),1);
            }
        }
        int result = 0;
        boolean oneChar = false;
        for(Integer val : map.values()){
            if(val % 2 == 0){
                result += val;
            }else{
                result += --val;
                oneChar = true;
            }
        }
        return oneChar ? result + 1 : result;
    }


    public static void main(String[] args){
        LongestPalindrome solution = new LongestPalindrome();
        System.out.println(solution.longestPalindrome("abccccdd"));
        System.out.println(solution.longestPalindrome("ccc"));
    }

}
