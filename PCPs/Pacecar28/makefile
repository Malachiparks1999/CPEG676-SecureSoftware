# Editors: Malachi Parks
# Section: CPEG476-010
# Assignment: PCP 24/26
# Due Date: 5/13/2022
# File Description:   Compile playground without any issues

# Variables for ease
CC=gcc	# Compiler type
OUTPUTNAME=playground

# Make all entries listed here
all: $(OUTPUTNAME)

$(OUTPUTNAME): $(OUTPUTNAME).c makefile
	$(CC) -o $(OUTPUTNAME) $(OUTPUTNAME).c

# Launch executable 
test:
	./$(OUTPUTNAME)

clean: 	
	rm $(OUTPUTNAME)

