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
            printf("BIN %d CHUNK %d SIZE: %d\n", binCount, chunkCount, headChunk->chunkSize);
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
void appendChunk(struct Tcache *tcache, int size, int data){    // append chunk to end of list of bins
    // Bins for traversing
    struct Bin *currentBin = tcache->headBin;
    
    // Generate new chunk
    struct Chunk *newChunk = malloc(sizeof(struct Chunk));
    newChunk->chunkSize = size;
    newChunk->data = data;
    newChunk->nextChunk = NULL;

    // traverse to find new bin of right size
    while(currentBin->binSize < size && currentBin->nextBin != NULL){
        currentBin = currentBin->nextBin;
    }

    // Don't insert if chunk limit reached
    if(currentBin->chunkLimit <= currentBin->chunkCount){
        printf("CANNOT ADD CHUNK: CURRENT TCACHE BIN IS FULL\n");
        return;
    }

    // Generate traversal chunk
    struct Chunk *currentChunk = currentBin->headChunk;

    // null head ie empty list
    if(currentChunk == NULL){
        currentChunk = newChunk;
        currentBin->chunkCount++;
        return;
    }

    // append in the chunk after traversal
    while(currentChunk->nextChunk != NULL){
        currentChunk = currentChunk->nextChunk;
    }

    currentChunk->nextChunk = newChunk;
    currentBin->chunkCount++;
    return;

}

int main(void){
    // make tcache struct
    struct Tcache *myTcache = malloc(sizeof(struct Tcache));

    appendBin(myTcache, 32);
    appendBin(myTcache, 48);
    appendBin(myTcache, 64);
    appendBin(myTcache, 80);

    appendChunk(myTcache, 33, 1);
    appendChunk(myTcache, 79, 1);

    // test print
    printTcache(myTcache);
    return 0;
}