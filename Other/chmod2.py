
n = input()
octToBin = ['000','001','010','011','100','101','110','111']
binary = octToBin[int(n[1])]+' '+octToBin[int(n[2])]+' '+octToBin[int(n[3])]
rwx = list('rwx rwx rwx')
for i in range(11):
    if binary[i] == '0':
        rwx[i] = '-'

if n[0] == '1' and rwx[2] == 'x': rwx[2] = 's'
if n[0] == '2' and rwx[6] == 'x': rwx[6] = 's'
if n[0] == '4' and rwx[10] == 'x': rwx[10] = 't'

print(binary,'and',''.join(rwx))