
d = int(input())
houses = [[i[0], int(i[1:])] for i in input().split(', ')[1:]]
odd = [i for i in houses if i[1] % 2]
even = [i for i in houses if i[1] % 2 == 0]

for delivery in range(d):
    inp = input().split(', ')[1:]
    odd += [[i[0], int(i[1:])] for i in inp[:-2] if int(i[1:]) % 2]
    odd.sort()
    even += [[i[0], int(i[1:])] for i in inp[:-2] if int(i[1:]) % 2 == 0]
    even.sort()
    if int(inp[-1]) <= len(odd):
        for i in range(len(odd)):
            if ord(odd[i][0]) >= ord(inp[-2]):
                print(''.join([str(i) for i in odd[(i + int(inp[-1]) - 1) % len(odd)]]))
                break
    else:
        for i in range(len(even)):
            if ord(even[i][0]) >= ord(inp[-2]):
                print(''.join([str(i) for i in even[(i + int(inp[-1]) - 1 - len(odd)) % len(even)]]))
                break
