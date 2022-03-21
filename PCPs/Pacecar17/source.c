/*
For reference here is a compilation with no protections of any kind: 
gcc -m32 -std=c99 -Wall -fno-stack-protector -no-pie -z execstack -Wl,-z,norelro -o pwnme source.c
*/

#include <stdlib.h>
#include <stdio.h>

void vuln(void){
  char buf[256];
  fgets(buf, 256, stdin);
  printf(buf);
  return;
}

int main(void){
  printf("Echo service starting now\n");
  while(1==1){
    vuln();
  }
  printf("Don't expect to see this\n");
  return 0;
}