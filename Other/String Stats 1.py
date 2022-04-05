
s = input() # input string

print(len(set(c for c in s.lower() if c.isalpha()))) # number of different letters
print(sum(c in 'aeiou' for c in s.lower())) # number of different vowels
print(sum(c.isupper() for c in s)) # number of uppercase letters
print(max([x for x in s.lower() if x.isalpha()].count(c) for c in s.lower())) # times most frequent letter appears

ws = [[c for c in w if c.isalpha()] for w in s.split()] #  words excluding punctuation
print(''.join(sorted(w for w in ws if len(w)==max(len(w) for w in ws))[0])) # longest word