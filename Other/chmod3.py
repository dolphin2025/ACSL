
inp = input().replace('a','ugo').split()
n, commands = inp[0][:-1], inp[1].split(',')
p = [list(['---','--x','-w-','-we','r--','r-x','rw-','rwx'][int(c)]) for c in n]
print(p)
users, perms = 'ugo', 'rwx'

for command in commands:
    if '+' in command:
        c = command.split('+')
        for user in c[0]:
            for perm in c[1]:
                p[users.index(user)][perms.index(perm)] = perm
    elif '-' in command:
        c = command.split('-')
        for user in c[0]:
            for perm in c[1]:
                p[users.index(user)][perms.index(perm)] = '-'
    else:
        c = command.split('=')
        for user in c[0]:
            permissions = {'r':'r--','w':'-w-','x':'--x','rw':'rw-','rx':'r-x','wx':'-wx','rwx':'rwx'}
            p[users.index(user)] = list(permissions[c[1]])

print(''.join([''.join(i) for i in p]))