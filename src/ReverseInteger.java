public class ReverseInteger {
    public static int reverse (int x) {
        int res = 0;
        while (x != 0) {
            if ((res > Integer.MAX_VALUE/10 || (res == Integer.MAX_VALUE/10 && x % 10 > 7))
                || (res < Integer.MIN_VALUE/10 || (res == Integer.MIN_VALUE/10 && x % 10 < - 8)))
                return 0;
            res = res * 10 + x % 10;
            x = x / 10;
        }
        return res;
    }

    public static void main(String[] args) {
        System.out.println(reverse(123));
        System.out.println(reverse(-123));
        System.out.println(reverse(-12));
        System.out.println(reverse(120));
        System.out.println(reverse(1534236469));
        System.out.println(reverse(-2147483412));
    }
}
