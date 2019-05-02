import java.util.HashSet;

public class PalindromeNumber {
    public static boolean isPalindrome (int x) {
        if (x < 0) return false;
        char[] c = (x + "").toCharArray();
        for (int i = 0; i < c.length / 2; i++){
            if (c[i] != c[c.length - i - 1]) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(isPalindrome(121));
        System.out.println(isPalindrome(-121));
        System.out.println(isPalindrome(10));
    }
}
