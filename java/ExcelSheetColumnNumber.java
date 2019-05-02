public class ExcelSheetColumnNumber {
    public int titleToNumber(String s) {
        char[] chars = s.toCharArray();
        int value = 0;
        for (int i = 0; i < s.length(); i++) {
            value += Math.pow(26, i) * (chars[s.length() - 1 - i] - 'A' + 1);
        }
        return value;
    }
}
