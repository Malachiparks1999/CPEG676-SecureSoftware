# Editors: Malachi Parks
# Section: CPEG476-010
# Assignment: PCP 24/26
# Due Date: 5/6/2022
# File Description:   Makefile for generating tcache executable

# Variables for ease
CC=gcc	# Compiler type
OUTPUTNAME=tcache

# Make all entries listed here
all: $(OUTPUTNAME)

$(OUTPUTNAME): $(OUTPUTNAME).c makefile
	$(CC) -o $(OUTPUTNAME) $(OUTPUTNAME).c

# Launch executable 
test:
	./$(OUTPUTNAME)

clean: 	
	rm $(OUTPUTNAME)