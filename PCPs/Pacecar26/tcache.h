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

// Tcache struct
typedef struct Tcache{
    int binLimit; // how many bins to limit to
    struct Bin *headBin;    // start of the bins
} tcache;

// Bin struct
typedef struct Bin{
    int chunkLimit;             // how many chunks per bin
    int chunkCount;             // how many bins in bin currently
    int binSize;                // size of the bin 0x20, 0x30, ....
    struct Chunk *headChunk;    // start of chunks in bin
    struct Bin *nextBin;        // next bin in SLL
} bin;

// Chunk struct
typedef struct Chunk{
    char data[DATA_LIMIT];      // random data within a chunk
    struct Chunk *nextChunk;    // next chunk in SLL
} chunk;