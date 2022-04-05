# 2019-2020 ACSL Programming Problem #1
# Code by Pahan Dewasurendra
# --------------------------------------------------------

# Function that returns the contents of a file as integers.
def words(file):
  words = []
  with open(file) as f:
    lines = f.readlines()
    for line in lines:
      words.append(line.split())
  for i in range (0,len(words)):
    for j in range (0,len(words[i])):
      words[i][j]=int(words[i][j])
  return words

# Function that returns the transformed number given N, P, and D.
def transform(N,P,D):
  # If the Pth digit of N from the right is from 0 to 4:
  if int(N[len(N)-P])<5:
    return N[0:len(N)-P] +str(int(N[len(N)-P]) + D)[-1] + '0'*(P-1)
  # If the Pth digit of N from the right is from 5 to 9:
  else:
    return N[0:len(N)-P]+str(abs(int(N[len(N)-P])-D))[0]+'0'*(P-1)

# Read the input using the words() function.
input=words('input.txt')

# Use transform() on the input lines and write the output into output file.
fout = open ('output.txt', 'w')
for i in range (0,5):
  N=str(input[i][0])
  P=input[i][1]
  D=input[i][2]
  fout.write(transform(N,P,D)+'\n')
