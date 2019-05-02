import java.util.HashMap;
class Fibonacci {
    HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
    public int fib(int N) {
        if (N <= 1) {
            return N;
        }
        if (map.containsKey(N)) {
            return map.get(N);
        } else {
            int v = fib(N - 1) + fib(N - 2);
            map.put(N, v);
            return v;
        }
    }
}
