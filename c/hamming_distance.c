int hammingDistance (int x, int y) {
    int num = x ^ y, c = 0;
    while (num > 0) {
        if ((num >> 1)<< 1 != num) {
            c++;
        }
        num >>= 1;
    }
    return c;
}
