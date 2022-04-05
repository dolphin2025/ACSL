Lines = []

with open('AcslCon#1File') as myfile:
  for line in myfile:
    Lines.append(line.rstrip('\n'))

def LineOne(num):
  return len(num)

def LineTwo(num):
  sum = 0
  for i in range (0,len(num)):
    sum = sum + int(num[i])
  return sum

def LineThree(num):
  sum = 0
  for i in range(0, len(num)):
    if i%2 == 0:
      sum = sum + int(num[i])
  return sum

def LineFour(num):
  counter = 0
  for i in range(0, len(num)):
    if num[i]=='4':
      counter = counter + 1
  return counter

def LineFive(num):
  if len(num) % 2 == 0:
    return num[int(len(num)/2-1)]
  if len(num) % 2 == 1:
    return num[int(len(num)/2)]

print(LineOne(Lines[0]))
print(LineTwo(Lines[1]))
print(LineThree(Lines[2]))
print(LineFour(Lines[3]))
print(LineFive(Lines[4]))