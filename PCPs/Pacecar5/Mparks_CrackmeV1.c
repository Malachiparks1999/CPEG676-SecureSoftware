/*
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     Pacecar Problem 5
File Description:  Creating a problem which takes in random junk and produces a flag
*/
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#define MAX 20

int main(){
    // set up variables
    int term1 = 0, term2 = 1, term3 = term1 + term2;
    int flagLen = MAX;
    char userInput[MAX] = "UDFLAG{F1b!_@nd_R3v}";
    char encryptUser[MAX];
    char secret[MAX] = "\x55\x45\x47\x4e\x42\x42\x73\x4b\x24\x40\x16\x06\x51\x04\x1f\x39\x30\x7a\x5a\x08";

    // ask for user input
    printf("Enter the secret:\n");
    //scanf("%s",userInput);
    
    //encryptString
    for(int i=0; i < MAX; i++){
      char encrypted = userInput[i]^(term1%127);
      encryptUser[i] = encrypted;
      term1=term2;
      term2=term3;
      term3=term1+term2;
    }
    
    if(strcmp(encryptUser, secret)){
      printf("That's the secret!");
    } else {
      printf("That's not the secret!");
    }
    return 0;
}