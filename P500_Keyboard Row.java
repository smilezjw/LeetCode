public class Solution {
    public String[] findWords(String[] words) {
        String[] characters = {"zxcvbnm","asdfghjkl","qwertyuiop"};
        ArrayList<String> res = new ArrayList();
        HashMap<Character, Integer> map = new HashMap();
        for(int i=0; i<characters.length; i++){
            for(int j=0; j<characters[i].length(); j++){
                map.put(characters[i].charAt(j), i);
            }
        }
        
        for(int i=0; i<words.length; i++){
            boolean flag = true;
            String word = words[i].toLowerCase();
            for(int j=1; j<word.length(); j++){
                if(map.get(word.charAt(j)) != map.get(word.charAt(j-1))){
                    flag = false;
                    break;
                }
            }
            if(flag){
                res.add(words[i]);
            }
        }
        return res.toArray(new String[0]);
    }
}
