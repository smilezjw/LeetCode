package Leetcode;

import java.util.HashSet;

/**
 * Created by Jiawen on 16/10/8.
 */
public class ReverseVowelsOfString {

    public String reverseVowels(String s) {
        HashSet<String> set = new HashSet<>();
        set.add("a");
        set.add("e");
        set.add("i");
        set.add("o");
        set.add("u");

        StringBuffer sb = new StringBuffer(s);
        int i = 0, j = sb.length()-1;
        while(i < j){
            String is = String.valueOf(s.charAt(i)).toLowerCase();
            String js = String.valueOf(s.charAt(j)).toLowerCase();
            if(set.contains(is) && set.contains(js)){
                char temp = s.charAt(i);
                sb.setCharAt(i++, s.charAt(j));
                sb.setCharAt(j--, temp);
            }else if(set.contains(is)){
                j--;
            }else if(set.contains(js)){
                i++;
            }else{
                i++;
                j--;
            }
        }
        return sb.toString();
    }

    public static void main(String[] args){
        ReverseVowelsOfString solution = new ReverseVowelsOfString();
        System.out.println(solution.reverseVowels("hello"));
    }


}
