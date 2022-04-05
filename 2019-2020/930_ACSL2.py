def words(file):
  words = []
  with open(file) as f:
    lines = f.readlines()
    for line in lines:
      words.append(line.split())
  return words
input=words('input.txt')
def e(a,b):
  a,b=list(a),list(b)
  v=['A','E','I','O','U']
  x,y=[a[0]],[b[0]]
  for i in range (1,len(a)):
    if (a[i-1]!=a[i]) or (a[i] in v):
      x.append(a[i])
  for i in range (1,len(b)):
    if (b[i-1]!=b[i]) or (b[i] in v):
      y.append(b[i])
  a,b=x,y
  x,y=[a[0]],[b[0]]
  for i in a[1:]:
    if i not in v:
      x.append(i)
  for i in b[1:]:
    if i not in v:
      y.append(i)
  a,b=x,y
  x,y=[],[]
  for i in range (0,max(len(a),len(b))):
    if i<min(len(a),len(b)):
      if a[i]!=b[i]:
        x.append(a[i])
        y.append(b[i])
    else:
      if i<len(a):
        x.append(a[i])
      if i<len(b):
        y.append(b[i])
  a,b=x,y
  x,y=[],[]
  for i in range (0,max(len(a),len(b))):
    if i<min(len(a),len(b)):
      if a[::-1][i]!=b[::-1][i]:
        x.append(a[::-1][i])
        y.append(b[::-1][i])
    else:
      if i<len(a):
        x.append(a[::-1][i])
      if i<len(b):
        y.append(b[::-1][i])
  x.reverse()
  y.reverse()
  a,b=x,y
  if len(a)<len(b):
    return ''.join(a)
  if len(a)>len(b):
    return ''.join(b)
  if len(a)==len(b):
    l=[a,b]
    l.sort()
    return ''.join(l[0])
output=''
for i in input:
  output+=(e(i[0],i[1]) + '\n')
with open('output.txt', 'w') as f:
  f.write(output)