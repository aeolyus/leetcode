#include <limits.h>
int maxProfit(int* prices, int pricesSize) {
    int total = 0, prev = INT_MAX;
    for (int i = 0; i < pricesSize; i++) {
        int curr = *(prices + i);
        if (curr > prev)
            total += curr - prev;
        prev = curr;
    }
    return total;
}
