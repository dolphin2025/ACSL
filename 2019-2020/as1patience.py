
# I will try to attach this file during the zoom meeting


# During the contest, you CANNOT use ovcc grader, but you CAN use the following functions to read the input
# I highly recommend you use these during the contest, it will save you time


# This function returns a matrix of the words in the input file name given (as strings)
# i.e., first index of the returned matrix is the line number and the second index is the word
# (word meaning separated by spaces, such as cards in this case)

# String Words ########################################################################
def words(file):
    words = []
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        words.append(line.split())
    return words


# This function does the above, but converts the words into integers

# Integer Words #######################################################################
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


# During the finals use
# open('output.txt','w').write('')
# to clear the output and
# open('output.txt','a+').write(str(line)+'\n')
# to append a line to the output



#################################################################################################################

# The code I wrote when timed (35 min)
# Notice that it doesn't have comments or good variable names, and is not organized
# During the finals that is okay since you have 3 hours to solve 4 problems
# Also, when debugging, there is no need to delete debug print statements, just comment them


def intwords(file):
    words = []
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        words.append(line.split())
    for i in range (0,len(words)):
        for j in range (0,len(words[i])):
            word = words[i][j]
            words[i][j]=[[0, 'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'].index(word[0]), word[1]]
    return words

open('output.txt','w').write('')

for l in intwords('as1-test.txt'):
    p=[[]]
    p[0].append(l[0])
    for i in l[1:]:
        placed=False
        for s in range (0,len(p)):
            z=p[s][-1]
            if i[1]==z[1]:
                continue
            if i[0]==13 or z[0]==1:
                if i[0]==13 and z[0]==1:
                    p[s].append(i)
                    placed=True
                    break
                else:
                    continue
            if i[0]<z[0]:
                p[s].append(i)
                placed=True
                break
        if not placed:
            p.append([i])
    # print(p)
    sums=[]
    for pile in p:
        if len(pile)==len(max(p, key=lambda x: len(x))):
            sum=0
            for i in pile:
                sum+=i[0]
            sums.append(sum)
    open('output.txt','a+').write(str(min(sums))+'\n')



# More readable code #######################################################################################


# Reads the file as a matrix of cards, and converts each card into [value (int),suit (str)]
def readfile(file):
    words = []
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        words.append(line.split())
    for i in range (0,len(words)):
        for j in range (0,len(words[i])):
            card = words[i][j]
            words[i][j]=[[0, 'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'].index(card[0]), card[1]]
    return words

# Clears the output
open('output.txt','w').write('')

# Loop through each converted line of input
for line in readfile('as1-test.txt'):

    # Create a variable for the piles, starts of with the first card
    piles=[[line[0]]]

    # Loop through the other cards to be played
    for pcard in line[1:]:

        # The card is currently not played
        played=False

        # Loop through each pile in piles
        for pile in range (0,len(piles)):

            # Get the last card in the pile
            lcard=piles[pile][-1]

            # If the card to be played is of the same suit as the last card, do not play it and continue to next pile
            if pcard[1]==lcard[1]:
                continue

            # If either the card to be played is a King or the last card is an Ace
            if pcard[0]==13 or lcard[0]==1:

                # Play the card if and only if the card to be played is a King AND the last card is an Ace
                if pcard[0]==13 and lcard[0]==1:
                    piles[pile].append(pcard)
                    played=True
                    break
                else:
                    continue

            # If the card to be played has a lesser value than the last card, play it
            if pcard[0]<lcard[0]:
                piles[pile].append(pcard)
                played=True
                break

        # If the card did not get played, start a new pile for the card
        if not played:
            piles.append([pcard])

    # Get the minimum sum of the pile with the most cards
    sums=[]
    for pile in piles:

        # Lambda is very useful for finding minimums and maximums
        # Basically, it creates a function that you can to use when calculating the minimum
        # In this case I use the len() function to get the pile with maximum length
        if len(pile)==len(max(piles, key=lambda x: len(x))):
            sum=0
            for card in pile:
                sum+=card[0]
            sums.append(sum)

    # Output the minimum sum to the output file
    open('output.txt','a+').write(str(min(sums))+'\n')

