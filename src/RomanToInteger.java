public class RomanToInteger {
    public static int romanToInt(String s) {
        int sum = 0;
        char[] c = s.toCharArray();
        for (int i = 0; i < s.length(); i++) {
            int num = val(c[i]);
            if (i + 1 < s.length()) {
                int next = val(c[i + 1]);
                if (num < next) {
                    sum += next - num;
                    i++;
                } else {
                    sum += num;
                }
            } else {
                sum += num;
            }
        }
        return sum;
    }

    private static int val(char c) {
        switch(c) {
            case 'I': return 1;
            case 'V': return 5;
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            case 'M': return 1000;
            default: return -1;
        }
    }

    public static void main(String[] args) {
        System.out.println(romanToInt("MCMIV"));
    }
}
