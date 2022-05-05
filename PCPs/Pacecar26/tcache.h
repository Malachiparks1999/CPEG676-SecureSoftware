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
#define CHUNK_LIMIT=10
#define DATA_LIMIT=100

// Definition of bin struct
struct Bin{
    int bin_size;       // range of sizes from 0x20 - 0x90
    int chunk_ct;       // needs to never exceed 10
    struct Chunk* chunk_list;   // first chunk in the ilist
    struct Bin* next_bin;       // Next bin, should only be 8
};

// Defintion of chunk struct
struct Chunk{
    char data[DATA_LIMIT];
    struct Chunk* next_chunk;
};