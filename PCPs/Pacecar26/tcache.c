/*
Editors: Malachi Parks
Section: CPEG476-010
Assignment: PCP 24/26
Due Date: 5/6/2022
File Description:   Creating a tcache chain then linking into it and printing it
*/

// Header files to include
#include "tcache.h"

// tcache funcions
void printTcache(struct Tcache *tcache){    // take in tcache and print the current values
    int binCount = 0;
    int chunkCount = 0;
    bin *headbin = tcache->headBin;
    while(headbin != NULL){
        printf("BIN %d\n",binCount);
        printf("BIN %d CHUNK COUNT: %d\n",binCount, headbin->chunkCount);
        printf("BIN %d BIN SIZE: %d\n",binCount, headbin->binSize);
        printf("\n");

        // print chunk information related to bin
        chunk *headChunk = headbin->headChunk;
        while(headChunk != NULL){
            printf("BIN %d CHUNK %d\n", binCount, chunkCount);
            printf("BIN %d CHUNK %d DATA: %d\n", binCount, chunkCount, headChunk->data);
            chunkCount++;
            headChunk = headChunk->nextChunk;
        }
        chunkCount=0;
        binCount++;
        headbin = headbin->nextBin;
    }
}

// bin functions
void appendBin(struct Tcache *tcache, int size){       // append to end of list
    struct Bin *newBin = malloc(sizeof(struct Bin));
    struct Bin *currentBin = tcache->headBin;

    // data into new bin
    newBin->chunkLimit = CHUNK_LIMIT;
    newBin->chunkCount = 0;
    newBin->binSize = size;
    newBin->headChunk = NULL;
    newBin->nextBin = NULL;

    // check if headref is null
    if(tcache->headBin == NULL){
        tcache->headBin = newBin;
        return;
    }

    // not null appeand to end of list, traverse then add
    while(currentBin->nextBin != NULL){
        currentBin = currentBin->nextBin;
    }

    currentBin->nextBin = newBin;
    return;
}

// chunk functions
void appendChunk(struct Chunk ***headChunk, char *data);    // append chunk to end of list

int main(void){
    // make tcache struct
    struct Tcache *myTcache = malloc(sizeof(struct Tcache));
    
    /*
    // make chunk to see if pritning works
    struct Chunk *firstChunk = malloc(sizeof(struct Chunk));
    firstChunk->data = 1;
    struct Chunk *secondChunk = malloc(sizeof(struct Chunk));
    secondChunk->data = 2;
    firstBin->headChunk = firstChunk;
    firstChunk->nextChunk = secondChunk;
    secondChunk->nextChunk = NULL;
    */
    appendBin(myTcache, 32);
    appendBin(myTcache, 48);
    appendBin(myTcache, 64);
    appendBin(myTcache, 80);

    // test print
    printTcache(myTcache);
    return 0;
}