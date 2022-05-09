/*
Editors: Malachi Parks
Section: CPEG476-010
Assignment: PCP 24/26
Due Date: 5/6/2022
File Description:   Creating a tcache chain then linking into it and printing it
*/

// Header files to include
#include "tcache.h"

// Defintion of bin funcs
void printBins(struct Bin *headBin){    // print the bins SLL
    // code here
}

void pushBin(struct Bin *headBin, int size, int count){  //https://www.geeksforgeeks.org/linked-list-set-2-inserting-a-node/
    // create new bin
    struct Bin *newBin = malloc(sizeof(struct Bin));
    // data insertion
    newBin->binSize = size;
    newBin->chunkCt = count;
    newBin->chunkList=NULL;
    newBin->nextBin=NULL;
    // inserting at head
    if(headBin == NULL){    // Tcache struct is empty
        headBin = newBin;
    }
    else{
        newBin->nextBin = headBin;
        headBin=newBin;
    }
    //code here
}

// Function definitions - Chunks 
void printChunks(struct Chunk *headChunk){
    // code here
}

int pushChunk(struct Chunk *headChunk){ // https://www.geeksforgeeks.org/linked-list-set-2-inserting-a-node/
    return 0;
    //code here
}

int main(void){
    // generate empty tcache
    struct Tcache *homemadeTcache;
    homemadeTcache = malloc(sizeof(struct Tcache));

    // Set up bins
    int binSize = 32;
    int binCount = 0;
    for(int i=0; i< BIN_LIMIT; i++){    // create serveral bins
        pushBin(homemadeTcache->headBin, binSize, binCount);
        binSize+=16;
        binCount+=1;
    }
    return 0;
}