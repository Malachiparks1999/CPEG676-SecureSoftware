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
To refactor can realloc when finding inital true length?
*/

#include <stdio.h>
#include <stdlib.h>

int main(void){
	// constant values to loop through to find flag
	int challengeArr[] = {110, 1, 105, 110, 1, 106, 2, 97, 123, 100, 3, 117, 53, 5, 116, 95, 48, 102, 8, 102, 95, 121, 48, 117, 114, 95, 67, 125};
	int trueLength = 0;
	char *flag; // empty flag pointer

	// traverse challenge array to find out how many # > 10
	// Also dynamically reallocates the size
	for(int i=0; i<28; i++){
		if(challengeArr[i] > 10){
			trueLength++;
			if(trueLength){
				flag = (char*) malloc(trueLength * sizeof(char)); // malloc flag upon first hit
			} else {
				flag = (char *) realloc(flag, trueLength); // realloc based upon size of flag
			}
		}//if
	}//for

	// dynamically created array to hold the flag
	int j=0; // used for flag array traversal
	for(int i=0; i<28; i++){
		if(challengeArr[i] > 10){
			flag[j] = challengeArr[i];
			j++;
		}
	}//for

	//prints the flag
	printf("%s\n", flag);
	return 0;
}//main
