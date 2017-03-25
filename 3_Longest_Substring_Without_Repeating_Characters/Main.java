import java.util.Map;
import java.util.HashMap;

/** 
    Given a string, find the length of the longest substring without repeating characters.

    Examples:

    Given "abcabcbb", the answer is "abc", which the length is 3.

    Given "bbbbb", the answer is "b", with the length of 1.
    
    Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
**/

public class Main {
    public static int lengthOfLongestSubstring(String s) {
	Map<Character, Integer> map = new HashMap<Character, Integer>();
	int maxlen = 0;
	for(int j = 0, i = -1; j < s.length(); j++) {
	    char c = s.charAt(j);
	    if(map.containsKey(c)) {
		i = Math.max(map.get(c), i);
	    }
	    maxlen = Math.max(maxlen, j - i);
	    map.put(c, j);
	}
	return maxlen;
    }

    public static void main(String[] args) {
	String s = "abcabcbb"; // Expected 3
	System.out.println(lengthOfLongestSubstring(s));
	s = "aab"; // Expected 2
	System.out.println(lengthOfLongestSubstring(s));
	s = "c"; // Expected 1
	System.out.println(lengthOfLongestSubstring(s));
	s = "pwwkew"; // Expected 3
	System.out.println(lengthOfLongestSubstring(s));
	s = "dvdf"; // Expected 3
	System.out.println(lengthOfLongestSubstring(s));
	s = "tmmzuxt"; // Expected 5
	System.out.println(lengthOfLongestSubstring(s));
    }
}
