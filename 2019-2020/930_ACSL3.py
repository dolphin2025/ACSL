# Submission for 2019-2020 ACSL Junior Division Contest #3
# Code by Pahan Dewasurendra
################################################################

# open input and output files
input=open('input.txt').readlines()
output=open('output.txt','w')

# variable for the final answer to output into the output file
finalans=''

# loop through the lines in the input file
for hexa in input:

    # convert input line into list of '0's and '1's to represent Veitch Diagram
    a=('0'*(4-len(bin(int(hexa[0],16))[2:]))+bin(int(hexa[0],16))[2:])\
      +('0'*(4-len(bin(int(hexa[1],16))[2:]))+bin(int(hexa[1],16))[2:])
    a=list(a)

    # string of codes for which group of positions corresponds to which term
    codes='1234 B, 5678 ~B, 1256 A, 2367 C, 3478 ~A, 1548 ~C, ' \
          '12 AB, 23 BC, 34 ~AB, 56 A~B, 67 ~BC, 78 ~A~B, ' \
          '15 A~C, 26 AC, 37 ~AC, 48 ~A~C, 14 B~C, 58 ~B~C, ' \
          '1 AB~C, 2 ABC, 3 ~ABC, 4 ~AB~C, 5 A~B~C, 6 A~BC, 7 ~A~BC, 8 ~A~B~C'

    # variable for answer to given line of input
    ans=''

    # loop through each code (in order) separated by commas
    for i in codes.split(','):

        # loop through positions in the given code to see if all '1's
        j=i.split()
        f=True
        for k in j[0]:
            if a[int(k)-1]=='0':
                f=False

        # if all '1's then make them '0's and add term to answer
        if f:
            for k in j[0]:
                a[int(k) - 1] = '0'
            ans+='+'
            ans+=j[1]

    # add answer to the final answer
    finalans+=ans[1:]
    finalans+='\n'

# write the final answer into the output file
output.write(finalans)
