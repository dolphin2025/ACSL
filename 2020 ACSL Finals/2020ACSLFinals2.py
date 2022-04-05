
line='10 Java Programs'

chars=[0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','G','H','I','J','K']

chars+= ['L','M','N','O','P','Q','R','S','T','U','V','W','X,','Y','Z']

chars+= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

l=[]
sl=[]

for i in line:
    if i in chars:
        l+=i
        sl+=i

sl.sort(key= lambda x: chars.index(x))

coun=0

while l!=sl:
    coun+=1
    print(coun,l,sl)
    mp=[]
    for i in range (0,len(l)):
        if l[i]!=sl[i]:
            for j in range (0,len(l)):
                if l[i]==sl[j] and l[i]!=l[j]:
                    mp.append([l[i],i,j])
                    break
    print(mp)
    if coun%2==1:
        mp.sort(key= lambda x: [chars.index(x[0]),x[1]])
    else:
        mp.sort(key= lambda x: [-chars.index(x[0]),x[1]])

    v=mp[0]

    print(v)

    l[v[1]]=l[v[2]]
    l[v[2]]=v[0]

    print('\n')

print(coun)

import time

