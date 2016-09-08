public class P392 {

	public boolean isSubsequence(String s, String t) {
		if(s == null || s.length() == 0){
			return true;
		}
		int i=0, j=0;
		while(i<s.length() && j<t.length()){
			if(s.charAt(i) == t.charAt(j)){
				i++;
				j++;
			}else{
				j++;
			}
		}
		return i==s.length();
    }
	
	public static void main(String[] args) {
		P392 solution = new P392();
		System.out.println(solution.isSubsequence("abc", "ahbgdc"));
		System.out.println(solution.isSubsequence("axc", "ahbgdc"));
	}
}
