#include <limits.h>
int maxProfit(int* prices, int pricesSize) {
    int max = 0, prev = INT_MAX;
    for (int i = 0; i < pricesSize; i++) {
        int curr = *(prices + i);
        if (max < (curr - prev))
            max = curr - prev;
        if (curr < prev)
            prev = curr;
    }
    return max;
}
