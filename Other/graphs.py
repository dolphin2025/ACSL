
def findCharacteristic(choice, edges):
    e = [[int(i[0]),int(i[1])] for i in edges.split()]
    d = {i[0]:{j[1] for j in e if j[0]==i[0]} for i in e}
    if choice == 1: return len([i for i in e if i[0]==i[1] or i[0]<i[1] and i[::-1] in e])
    if choice == 2: return [sum(d[i])+10*i*len(d[i]) for i in range (10) if i in d and len(d[i])==max([len(d[i]) for i in d])][0]
    if choice == 3: return sum(sum(len(d[j]) for j in d[i]) for i in d)