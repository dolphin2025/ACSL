# 20 set var mil per second
# 11 iterate mil per second
# 0.2 char print mil per second
# 11 set list val mil per second
# 5.5 append mil per second
# 13 get list val mil per second
# 18 add/sub/mul/div mil per second


# Increase Recursion Limit. If weird error use queue instead. #########################
# import sys
# sys.setrecursionlimit(10000)


# Sort list by index ##################################################################
# .sort(key = lambda t: t[2])


# String Words ########################################################################
# def words(file):
#     words = []
#     with open(file) as f:
#         lines = f.readlines()
#     for line in lines:
#         words.append(line.split())
#     return words


# Integer Words #######################################################################
# def intwords(file):
#     words = []
#     with open(file) as f:
#         lines = f.readlines()
#     for line in lines:
#         words.append(line.split())
#     for i in range (0,len(words)):
#         for j in range (0,len(words[i])):
#             words[i][j]=int(words[i][j])
#     return words


# pretty_print_2D ####################################################################
# def pretty_print_2D(M):
#   lens = [len(M[0]) for i in range(0,len(M[0]))]
#   fmt = ''.join('{{:{}}}'.format(x) for x in lens)
#   table = [fmt.format(*row) for row in M]
#   print('\n'.join(table))


# Read Write Execute for Code Center ##################################################
# def rwe(fname):
#   c = ''
#   with open(fname+".py") as f:
#     lines = f.readlines()
#     for line in lines :
#       line = '    ' + line
#       c = c + line
#
#   c = "while True:\n  try:\n" + c
#   c = c + "\n    if input('Type exit to return to the Code Center, anything else will rerun the code:')=='exit':\n      break\n" \
#           "  except:\n    print('The code encountered an error and will restart.')"
#
#   exec(c)


# Base Converter (2-36) ###############################################################
# # num1 = input('Number to convert: ')
# # base1 = int(input('Base1(2-36): '))
# # base2 = int(input('Base2(2-36): '))
# #
# # num1 = '258'
# # base1 = 10
# # base2 = 15
#
# digitList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
#              'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# decimal = 0
# for i in range(0,len(num1)):
#   decimal = decimal + int(digitList.index(num1[i]))*(base1**(len(num1)-i-1))
#
# n=''
# i=1
# x=True
# while x:
#   y=(decimal%(base2**i))//(base2**(i-1))
#   # print(digitList[y])
#   if (base2**(i-1))>decimal:
#     x=False
#   else:
#     n+= digitList[y]
#   i+=1
#
# n=n[::-1]
#
# print(n)
# print(num1,'base',base1,'is',n,'base',base2)

