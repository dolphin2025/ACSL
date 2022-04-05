
s,n = input(),[]
s = [i.lower() for i in s if i.isalpha()]
while len(s) != 0:
    letters = sorted([s[i] for i in range (len(s)) if s[i] not in s[i+1:]])
    n += letters
    for i in letters: s.remove(i)
print(''.join(n[i] for i in range (len(n)-1) if n[i] != n[i+1])+n[-1])

