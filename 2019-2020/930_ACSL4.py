# 2019-2020 ACSL Programming Problem #4
# Code by Pahan Dewasurendra
# --------------------------------------------------------

import math

# function to read input and convert to a 2D array of integers
def intwords(file):
  words = []
  with open(file) as f:
    lines = f.readlines()
    for line in lines:
      words.append(line.split())
  for i in range (0,len(words)):
    for j in range (0,len(words[i])):
      words[i][j]=int(words[i][j])
  return words

# function to check if a number is prime
def isprime(x):
    prime=True
    for i in range (2,int(math.sqrt(x)+1)):
        if x%i==0:
            prime=False
            break
    return prime

# function to check if a number is a perfect square greater than 4
def isperfectsquare(x):
    return x>4 and math.sqrt(x)==int(math.sqrt(x))

# function to check if a given path made a horizontal move followed by a vertical move
def HthenV(start,end):
    for i in [7,12,17,22,27,35,40,45,50]:
        if start<i<end:
            return True
    return False

# clear the output
open('output.txt','w').write('')

# read the input and loop through each input line
for input in intwords('input.txt'):

    # get the positions of the opponent's markers, your marker, and the die rolls
    opp,pos,d=input[0:3],input[3],input[5:]

    # loop through the die rolls, updating the player marker value each time
    for i in d:
        # create a variable for the location the player would land on if no rule applies
        end=pos+i

        # if the end position is already taken or is not on the game board, skip turn and go to next die roll
        if end in opp or end>52:
            continue

        # if the end position is the last square, set the position/output to "GAME OVER" and break the loop
        if end==52:
            pos='GAME OVER'
            break

        # if the end position is prime, advance the player marker 6 squares or until an opponent marker is hit
        if isprime(end):
            for i in range (end+1,end+7):
                if i in opp:
                    pos=i-1
                    break
                pos=i
            continue

        # if the end position is perfect square, retreat the player marker up to 6 squares
        if isperfectsquare(end):
            for i in range(end - 1, end - 7, -1):
                if i in opp:
                    pos = i + 1
                    break
                pos = i
            continue

        # if the player marker's path moves HthenV move to the position that is a multiple of the die roll
        if HthenV(pos,end):
            if end-(end%i) not in opp:
                pos=end-(end%i)
            continue

        # if none of the specific rules apply, update the player marker to the normal end position
        pos=end

    # output the ending position to the output file
    open('output.txt', 'a+').write(str(pos)+'\n')
