public class ReverseString {
    public String reverseString(String s) {
        char[] chars = s.toCharArray();
        int i = 0, j = chars.length - 1;
        while (i < j) {
            char temp = chars[i];
            chars[i++] = chars[j];
            chars[j--] = temp;
        }
        return new String(chars);
    }
}
