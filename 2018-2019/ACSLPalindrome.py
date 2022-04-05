#function that checks if a number is a palindrome---------------------------
def checkpal(num):
  num = str(num)
  if num == num[::-1]:
    return False
  else:
    return True

#function that adds reverse of a number to itself
def addrev(num):
  num = str(num)
  y = int(num) + int(num[::-1])
  return y

#Main Code
while True:
  counter = 0
  num = int(input("Enter a number:"))
  while checkpal(num) and counter < 10:
    num = addrev(num)
    counter += 1
  if counter == 10:
    print("NONE",",",num)
  else:
    print(num)