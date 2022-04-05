# Code for 2019 ACSL Programming Problem #4 by Pahan Dewasurendra
# What it does: Evaluates prefix expressions in a given file with operators +,-,*, and @:
# @ a b c returns b if a is positive; otherwise it returns c.
# --------------------------------------------------------------------------------------------------------


# Main function that evaluates a given prefix expression -------------------------------------------------

def evaluate(e):
   # this keeps modifiying the expression until the expression is a single number
   while len(e) > 1:
     # finds operators starting from the end
     for i in range (len(e)-1,-1,-1):
       # if a normal operator is found, it is used on the numbers next to it and modified in-place
       if e[i] in ['+','-','*']:
         e[i]=eval(str(e[i+1])+str(e[i])+str(e[i+2]))
         del e[i+1:i+3]
         break
       # if an @ operator is found, it is used on the numbers next to it and modified in-place
       if e[i] == '@':
         if int(e[i+1]) > 0:
           ans=e[i+2]
         else:
           ans=e[i+3]

         e[i]=ans
         del e[i+1:i+4]
         break
   # returns the expression (now a single number)
   return e[0]


# Extracts prefix expressions from the input file as lists and removes spaces and newline characters -----

input = []

# opens thte input file
with open('C:\Pahan\python\ACSLCon#4File') as myfile:
  # goes through each line
  for line in myfile:
    # removes spaces and newline characters
    line = line.replace(' ', '').rstrip('\n')
    # appends this as a list to the new input.
    input.append(list(line))


# Uses the main function above on the prefix expressions and prints the output ---------------------------

print('#1.',evaluate(input[0]))
print('#2.',evaluate(input[1]))
print('#3.',evaluate(input[2]))
print('#4.',evaluate(input[3]))
print('#5.',evaluate(input[4]))