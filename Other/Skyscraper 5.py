from itertools import permutations

def rightvis(ar):
    return len([i for i in range(1, 5) if ar[i] > max(ar[:i])]) + 1

l, r = [int(i) for i in input().split(',')]
ans = 0
for ar in permutations(range(5)):
    if rightvis(ar) == r and rightvis(ar[::-1]) == l: ans += 1
print(ans)
