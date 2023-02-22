#include <stdio.h>
#include <stdlib.h>

#define N 16 /* buffer size */

int main(void) {
  char name[N]; /* buffer */

  /* prompt user for name */
  printf("What's your name? ");
  scanf("%s", name);

  printf("Hi there, %s!\n", name); /* greet the user */

  return EXIT_SUCCESS;
}