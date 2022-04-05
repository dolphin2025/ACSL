def line1(sent):
  chars = ''

  #the for loop adds each new letter as it goes through the list
  for i in sent.lower():
    if i.isalpha() and i not in chars:
      chars += i

  return len(chars)


def line2(sent):
  #counts each vowel seperately and adds them together
  return sent.lower().count('a') + sent.lower().count('e') + sent.lower().count('i') + sent.lower().count('o') + sent.lower().count('u')


def line3(sent):
  count = 0

  #checks how many places the lowercase version of the sentence differs from the normal version (this happens for every uppercase letter)
  for i in range (0,len(sent)-1):
    if sent[i] != sent.lower()[i]:
      count += 1

  return count


def line4(sent):
  count = 0

  #counts each character, the biggest count overwrites the others
  for i in sent:
    if sent.count(i) > count and i.isalpha():
      count = sent.count(i)
      char = i

  return count


def line5(sent):
  #*** explained below
  uwords = sent.split()
  sent = sent.lower()
  words = sent.split()
  bigwords = []

  #finds the length of the biggest word(s)
  maxlen = len(max(words, key= lambda x: len(x)))
  for i in words:
    if len(i)==maxlen:
      bigwords.append(i)

  #alphabetizes the words if there is a tie
  bigwords.sort()

  #*** this, combined with above, gets the uppercase version of the word, which was turned into lowercase above
  ind = words.index(bigwords[0])

  return uwords[ind]


#Main Code-----------------------------------------------------------------------------

sent = input('input sentence:')

#******(used for testing):
# sent = 'The quick brown fox, named Roxanne, jumped over Bruno, a lazy dog.'
# sent = 'a Cb b cy? ? da,,  '

print('Sentence:', sent)

#removes all characters except for letters
newfile = ''
for i in sent:
  if i.isalpha() or i == ' ':
    newfile += i
sent=newfile

#prints output
print('1. ',line1(sent))
print('2. ',line2(sent))
print('3. ',line3(sent))
print('4. ',line4(sent))
print('5. ',line5(sent))