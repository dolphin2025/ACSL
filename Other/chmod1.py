
n = input()
octToBin = ['000','001','010','011','100','101','110','111']
binary = octToBin[int(n[0])]+' '+octToBin[int(n[1])]+' '+octToBin[int(n[2])]
rwx = list('rwx rwx rwx')
for i in range(11):
    if binary[i] == '0':
        rwx[i] = '-'
print(binary,'and',''.join(rwx))