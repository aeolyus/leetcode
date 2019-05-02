bool isHappy(int n) {
  int i, j;
  i = j = n;
  do {
    i = process(i);
    j = process(process(j));
  } while (i != j);
  if (i == 1) {
    return 1;
  }
  return 0;
}

int process(int n) {
  int sum = 0, t = 0;
  while (n) {
    t = n%10;
    sum += t*t;
    n /= 10;
  }
  return sum;
}
