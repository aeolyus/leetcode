import java.util.Arrays;
import java.util.List;

public class FizzBuzz {
    public List<String> fizzBuzz(int n) {
        String[] list = new String[n];
        for (int i = 1; i <= n; i++) {
            if (i % 15 == 0) {
                list[i - 1] = "FizzBuzz";
            } else if (i % 3 == 0) {
                list[i - 1] = "Fizz";
            } else if (i % 5 == 0) {
                list[i - 1] = "Buzz";
            } else{
                list[i - 1] = "" + i;
            }
        }
        return Arrays.asList(list);
    }
}
