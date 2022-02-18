# Variables
junkString="nhlie~q4dj:fiRz?Oc!e'{qj"
i=0
answerString=""
# Original Junk String
print("Original Junk String: nhlie~q4dj:fiRz?Oc!e'{qj")

'''
# XORing junk string piece by piece
for letter in junkString:
    letterNum = int(letter)
    flagLetter =  letterNum ^ i
    answerString += flagLetter
'''    
print("Flag: " + answerString)