//apt-get update
//apt-get install gcc-multilib
//gcc -m32 -std=c99 -Wall -fno-stack-protector -z execstack -o pwnme sv.c
//temporarily live at: nc 165.22.46.243 1337 
//hosted with: socat TCP-LISTEN:1337,reuseaddr,fork EXEC:"./pwnme"
//after `ufw allow 1337`
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void win(){
	system("cat flag.txt");
}
int myFunc(int a, int b, int c){
	int d;
	int e;
	int f;
	char buf[15];
	d = 5;
	e = 6;
	f = 7;
	fgets(buf, 0x150, stdin);
        printf("%s\n", buf);

	if(f == 0x61626364){
		win();
	}
	printf("a = %d, b = %d, c = %d\n", a, b, c);
        printf("d = %d; e = %d; f = %d\n", d, e, f);

	return (a*d + b*e + c*f);
}
int main(){
	myFunc(1, 2, 3);
}