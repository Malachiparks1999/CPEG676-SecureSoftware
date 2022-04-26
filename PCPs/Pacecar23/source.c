#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int vuln(char* target){
  unsigned long sizechunk = 0;
  void* ptr = 0;
  int attempts = 0;
  while(attempts < 5){
    printf("Attempt number: %d\n", attempts+1);
    puts("calling malloc(\"%d\"), what size?:\n");
    fflush(stdout);
    scanf("%ld",&sizechunk);
    getchar();
    printf("Asking for chunk of size %ld\n",sizechunk);
    fflush(stdout);
    ptr = malloc(sizechunk);
    printf("Your chunk m'lady: %p\n", ptr);
    fflush(stdout);
    printf("What would you like to store in this fine chunk?:\n");
    fflush(stdout);
    fgets(ptr, sizechunk+16, stdin);
    printf("And now for system(%p)\n", target);
    fflush(stdout);
    system(target);
    printf("\nWhat? You're still here?  Try again\n");
    attempts += 1;
    fflush(stdout);
  }
  return 0;
}

int main(void){
  char buff[64];
  printf("What is your name? (I'm only asking to have full-green canary protection, no exploit here. No, really.)\n");
  fflush(stdout);
  fgets(buff, 63, stdin);
  char target[32]="ls -ltr";
  vuln(target);
  return 0;
}