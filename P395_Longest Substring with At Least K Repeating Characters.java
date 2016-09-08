public class P395 {
	
	public int longestSubstring(String s, int k) {
		if(s == null || s.length() == 0){
			return 0;
		}
		int[] charCnt = new int[26];
		for(int i=0; i<s.length(); i++){
			charCnt[s.charAt(i)-'a']++;
		}
		boolean flag = true;
		for(int i=0; i<charCnt.length; i++){
			if(charCnt[i] > 0 && charCnt[i] < k){
				flag = false;
			}
		}
		if(flag){
			return s.length();
		}
		int result=0;
		int start = 0;
		int cur = 0;
		while(cur < s.length()){
			if(charCnt[s.charAt(cur)-'a'] < k){
				result = Math.max(result, longestSubstring(s.substring(start,cur), k));
				start = cur + 1;
			}
			cur++;
		}
		result = Math.max(result, longestSubstring(s.substring(start), k));
		return result;
    }

	public static void main(String[] args) {
		P395 solution = new P395();
		System.out.println(solution.longestSubstring("ababbc", 2));
		System.out.println(solution.longestSubstring("aaabb", 3));
		System.out.println(solution.longestSubstring("acbabb", 2));
		System.out.println(solution.longestSubstring("abcdedghijklmnopqrstuvwxyz", 2));

	}

}
