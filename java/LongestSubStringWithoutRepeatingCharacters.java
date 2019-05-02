import java.util.HashSet;

public class LongestSubStringWithoutRepeatingCharacters {
    public static int lengthOfLongestSubstring(String s) {
        int max = 0;
        HashSet<Character> seen = new HashSet<Character>();
        int j = 0;
        for (int i = 0; i < s.length(); i++) {
            if (!seen.contains(s.charAt(i))) {
                seen.add(s.charAt(i));
                max = Math.max(max, seen.size());
            } else {
                seen.remove(s.charAt(j++));
                i--;
            }
        }
        return max;
    }

    public static void main(String[] args) {
        System.out.println(lengthOfLongestSubstring(" "));
    }
}
