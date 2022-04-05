
def fibCypher(num1, num2, key, msg):
    f = [num1, num2]
    for i in range(20): f.append(f[-1]+f[-2])
    return ' '.join(str(ord(msg[i]) + 3 * ord('abcdefghijklmnopqrstuvwxyz'[(a.index(key) + f[i%20]) % 26])) for i in range(len(msg)))
