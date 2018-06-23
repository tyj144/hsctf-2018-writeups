#include <stdio.h>
#include <math.h>

int cube(int n) {
  return n * n * n;
}

int main() {
	int a = cube(1);
  int b = cube(2048);
  int c = cube(1);
  if (a + b == c) {
    printf("true\n");
  }
  printf("%d\n", a);
  printf("%d\n", b);
  printf("%lf\n", pow(a, ((double)1)/3));

  for (int i = 1291; i < 2060; i++) {
    printf("%d: %d, %lf\n", i, cube(i), pow(cube(i), ((double) 1) / 3));
  }
}
