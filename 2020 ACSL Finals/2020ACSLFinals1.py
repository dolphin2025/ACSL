import sys

def pretty_print_2D(M):
  lens = [len(M[0]) for i in range(0,len(M[0]))]
  fmt = ''.join('{{:{}}}'.format(x) for x in lens)
  table = [fmt.format(*row) for row in M]
  print('\n'.join(table))

def isY(n,m,p):
    for r in range (1,n-1):
        for c in range (1,n-1):
            if m[r][c]==p and m[r+1][c]==p and m[r-1][c-1]==p and m[r-1][c+1]==p:
                return [True,[[r,c],[r+1,c],[r-1,c-1],[r-1,c+1]]]

            if m[r][c]==p and m[r-1][c]==p and m[r+1][c-1]==p and m[r+1][c+1]==p:
                return [True,[[r,c],[r-1,c],[r+1,c-1],[r+1,c+1]]]

            if m[r][c]==p and m[r][c+1]==p and m[r-1][c-1]==p and m[r+1][c-1]==p:
                return [True,[[r,c],[r,c+1],[r-1,c-1],[r+1,c-1]]]

            if m[r][c]==p and m[r][c-1]==p and m[r-1][c+1]==p and m[r+1][c+1]==p:
                return [True,[[r,c],[r,c-1],[r-1,c+1],[r,c+1]]]

    return [False,0]

n=5
line='1 14 24 20 12 18 3 15 12 20 17 8'
l=line.split()
for i in range (0,len(l)):
    l[i]=int(l[i])

m=[]
for i in range (n):
    templist=[]
    for j in range (n):
        templist.append(2)
    m.append(templist)

pretty_print_2D(m)

player=0

for i in l:
    if m[(i-1)//n][(i-1)%n]==player:
        m[(i - 1) // n][(i - 1) % n]=2
    else:
        m[(i - 1) // n][(i - 1) % n] = player
    if isY(n,m,player)[0]:
        print('\n', i, l, player, isY(n, m, player))
        pretty_print_2D(m)
        sum=0
        for j in isY(n,m,player)[1]:
            sum+=(n*j[0]+j[1]+1)
        print('hi',sum)
        sys.exit()
    print('\n', i, l, player, isY(n, m, player))
    pretty_print_2D(m)
    player=not(player)

print(0)