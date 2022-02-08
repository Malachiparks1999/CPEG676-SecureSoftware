/*
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     Pacecar Problem 1
File Description:

PACECAR 1: 

OK so write, compile, and execute a C program that does the following:

Create a character array to hold your flag

Loop through this array of values: [110, 1, 105, 110, 1, 106, 2, 97, 123, 100, 3, 117, 53, 5, 116, 95, 48, 102, 8, 102, 95, 121, 48, 117, 114, 95, 67, 125]

If a value is <= 10 skip it
Otherwise append the letter whose ascii value matches the given value to your flag

Print the flag

*/

/*
IDEADS

go through array once, find #'s greater then 10
use amount of #'s greater than 10 to malloc character array
append to character array
print string
*/

#include <stdio.h>
#include <stdlib.h>

int main(void){
	// constant values to loop through to find flag
	int challengeArr[28] = {110, 1, 105, 110, 1, 106, 2, 97, 123, 100, 3, 117, 53, 5, 116, 95, 48, 102, 8, 102, 95, 121, 48, 117, 114, 95, 67, 125};
	char alphaString[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\n";
	int trueLength = 0;

	// traverse challenge array to find out how many # > 10
	for(int i=0; i<27; i++){
		if(challengeArr[i] > 10){
			trueLength++;
		}
	}//for

	// dynamically created array to hold the flag
	printf("trueLength: %d\n", trueLength);
	char flag[] = (int*) malloc(trueLength * sizeof(int));
	

	//prints the flag
	printf("%s", alphaString);
	return 0;
}//main
