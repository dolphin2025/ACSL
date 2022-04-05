
n,h = input().split(', ')
n = int(n)
h = bin(int(h,16))[2:]
if len(h)%4: h = '0'*(4-(len(h)%4))+h
edges = [[] for i in range(n)]

for u in range(n):
    for v in range(u+1,n):
        if int(h[v-u-1]):
            edges[u].append(v)
            edges[v].append(u)
    h = h[n-u-1:]

seen = set()
def dfs(u):
    if u not in seen:
        seen.add(u)
        for v in edges[u]: dfs(v)
dfs(0)
ans = ''.join([chr(ord('A')+i) for i in seen])

cc = 1
for i in range(n):
    if i not in seen:
        dfs(i)
        cc += 1
print(cc,'',ans)