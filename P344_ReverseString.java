package Leetcode;

/**
 * Created by Jiawen on 16/10/7.
 */
public class ReverseString {

    public String reverseString(String s) {
        StringBuffer sb = new StringBuffer(s);
        int i = 0, j = sb.length() - 1;
        while(i < j){
            char temp = sb.charAt(i);
            sb.setCharAt(i, sb.charAt(j));
            sb.setCharAt(j, temp);
            i++;
            j--;
        }
        return sb.toString();
    }

    public static void main(String[] args){
        ReverseString solution = new ReverseString();
        System.out.println(solution.reverseString("Hello"));
    }


}
