#include <stdlib.h>
#include <stdio.h>

int add(int num, int num2);

int main(void){
    add(5,2);
    return 0;
}

int add(int num, int num2){
    return(num+num2);
}

// 32 bit assembly creation:  gcc -m32 -S -masm=intel test.c
// 64 bit assembly creation: gcc -S -masm=intel test.c