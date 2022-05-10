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
#define BIN_LIMIT 8

// Chunk struct
typedef struct Chunk{
    int chunkSize; // size of the chunk generated
    int data;      // random data within a chunk
    struct Chunk *nextChunk;    // next chunk in SLL
} chunk;

// Bin struct
typedef struct Bin{
    int chunkLimit;             // how many chunks per bin
    int chunkCount;             // how many bins in bin currently
    int binSize;                // size of the bin 0x20, 0x30, ....
    struct Chunk *headChunk;    // start of chunks in bin
    struct Bin *nextBin;        // next bin in SLL
} bin;

// Tcache struct
typedef struct Tcache{
    int binLimit; // how many bins to limit to
    struct Bin *headBin;    // start of the bins
} tcache;

// tcache funcions
void printTcache(struct Tcache *tcache);    // take in tcache and print the current values

// bin functions
void appendBin(struct Tcache *tcache, int size);     // append to end of list

// chunk functions
void appendChunk(struct Tcache *tcache, int size, int data);    // append chunk to end of list