

# Code for ACSL Programming Problem #3 by Pahan Dewasurendra

# --- This code has been divided into 3 parts:
        # 1. Small functions
        # 2. Deciphering the input
        # 3. Main function and output

# --- -1 means piece A, -2 means piece B, -3 means piece C

# --- Some prints have been commented, they are used for debugging

#######################################################################################################################



# 1. Small functions

# These variables are used to mark the matrix where there is blocked spot, where piece A is placed, etc.
blocked = -1000
start = -1000000
connector = 0
spotA = -1
spotB = -2
spotC = -3

# This function prints a matrix neatly, we learned it in class
def pretty_print_2D(M):
  lens = [len(M[0]) for i in range(0,len(M[0]))]
  fmt = ''.join('{{:{}}}'.format(x) for x in lens)
  table = [fmt.format(*row) for row in M]
  print('\n'.join(table))

# This function finds the next piece to place
def next(P):
  if P == -1:
    return -2
  if P == -2:
    return -3
  if P == -3:
    return -1

# This function finds if a place [r,c] is valid (in the matrix and not blocked)
def isinvalid(m,r,c):
  invalid = False

  try:
    if m[r][c] == blocked:
      invalid = True

  except:
    invalid = True

  return invalid

# This function converts piece numbers to pieces
def letter(n):
  if n == -1:
    return 'A'
  if n == -2:
    return 'B'
  if n == -3:
    return 'C'


# The pieces are defined here
def piece(P,r,c):
  if P == -1:
    return [[r,c],[r,c+1],[r,c+2]]
  if P == -2:
    return [[r, c], [r + 1, c], [r + 1, c + 1]]
  if P == -3:
    return [[r, c], [r, c + 1], [r + 1, c + 1], [r + 2, c + 1]]

# This function places pieces into the matrix
def place(P,m,r,c):
  if P == -1:
    m[r][c] = connector
    m[r][c+1] = spotA
    m[r][c+2] = connector

  if P == -2:
    m[r][c] = connector
    m[r + 1][c] = spotB
    m[r + 1][c + 1] = connector

  if P == -3:
    m[r][c] = connector
    m[r][c + 1] = spotC
    m[r + 1][c + 1] = spotC
    m[r + 2][c + 1] = connector


# This function finds where to place the next piece
def piecePos(m):
  posfound = False
  c = len(m[0])
  while not posfound and c > -1:
    c = c - 1
    for r in range(len(m) - 1, -1, -1):
      if m[r][c] == start:
        spot = [r, c]
        posfound = True
      if m[r][c] == connector:
        spot = [r, c + 1]
        posfound = True

  return spot

# This function finds if a certain piece can be placed in a given position
def canPlace(m,P,r,c):
  possible = True
  for s in piece(P,r,c):
    if isinvalid(m,s[0],s[1]):
      possible = False
  return possible

# 2. Deciphering the input
# The 5 matrices are created and stored in a 3d array using the input with the starting point and blocked cells marked

input = [[6, 10, 11, 1,37],
     [4, 9, 1, 1, 16],
     [4, 10, 1, 0],
     [6, 11, 1, 1, 42],
     [4, 8, 17, 1, 21]]

M = []

for i in input:
  # Creates the matrices without the starting point and blocked cells marked
  matrix = []
  for r in range (0,i[0]):
    row = []
    for c in range (0,i[1]):
      row.append( r * i[1]  + c + 1)
    matrix.append(row)

  # Makes a list of the blocked cells
  blockedList = []
  for b in range (0,i[3]):
    blockedList.append(i[b+4])

  # Marks the starting point and blocked cells
  for r in range (0,len(matrix)):
    for c in range (0,len(matrix[0])):
      if i[3] != 0:
        if matrix[r][c] in blockedList:
          matrix[r][c] = blocked
      if matrix[r][c] == i[2]:
        matrix[r][c] = start


  # pretty_print_2D(matrix)
  # print('\n')
  M.append(matrix)

# print('3dArray=',M)

# 3. Main funciton and output

# The main function is defined here, it finds the path in a given matrix
def findPath(m):
  end = False
  P=-1
  path = ''

  while not end:
    # If a piece can be placed, it is placed and added to the path
    if canPlace(m,P,piecePos(m)[0],piecePos(m)[1]):
      place(P,m,piecePos(m)[0],piecePos(m)[1])
      path += letter(P)
    P=next(P)

    # Checks if the end has been reached
    for i in m:
      if i[len(i)-1] == connector:
        end = True

  pretty_print_2D(m)
  return path


# The output is printed

print('1.',findPath(M[0]))
print('2.',findPath(M[1]))
print('3.',findPath(M[2]))
print('4.',findPath(M[3]))
print('5.',findPath(M[4]))

