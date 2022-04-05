
l = [input()[0] for i in range(5)]

def sm(s): return sum([1, 1, 2, 3, 5][i] for i in range(5) if l[i] in s)

print("%02d:%02d" % ((sm('RB') + (sm('GB') == 12)) % 12, 5 * sm('GB') % 60))