/*
Editors: Malachi Parks
Section: CPEG476-010
Assignment: PCP 24/26
Due Date: 5/6/2022
File Description:   Header file for tache implementation which includes standard headers
*/

// Headers to include
#include <stdlib.h>
#include <stdio.h>

// Defintions for vars
#define CHUNK_LIMIT 10
#define DATA_LIMIT 100
#define BIN_LIMIT 8

// Definition of bin struct
typedef struct Bin{
    int binSize;       // range of sizes from 0x20 - 0x90
    int chunkCt;       // needs to never exceed 10
    struct Chunk* chunkList;   // first chunk in the ilist
    struct Bin* nextBin;       // Next bin, should only be 8
};

// Defintion of chunk struct
typedef struct Chunk{
    char data[DATA_LIMIT];
    struct Chunk* nextChunk;
};

// Defintion of tcache struct
typedef struct Tcache{
    struct Bin* headBin;
};

// Function definitions - Bins
void printBins(struct Bin *headBin);
void pushBin(struct Bin *headBin, int binSize, int count);   // return negative # if something is wrong

// Function definitions - Chunks 
void printChunks(struct Chunk *headChunk);
int pushChunk(struct Chunk *headChunk); // return negative # if something is wrong