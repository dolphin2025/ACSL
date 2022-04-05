def words(file):
  words = []
  with open(file) as f:
    lines = f.readlines()
    for line in lines:
      words.append(line.split())
  return words

def sum(pile):
  sum = 0
  for c in pile:
    sum += c[0]
  return sum

# input = [['4H','AC','8H','5D','6S','3D','4C','2D'],
#          ['2C','3D','AH','3H','AC','4H','3C','2S','AS','AD','2H','4C','3S','2D'],
#          ['6S','7H','8C','4C','5C','6D','3D','4D','5H','2C','3H','4S','AC']]

input = words('text.txt')

values = ['-','A','2','3','4','5','6','7','8','9','T','J','Q','K']
suits = ['-','D','C','H','S']

for inputl in input:
  piles = []
  cards = []
  for card in inputl:
    c=[values.index(card[0]),suits.index(card[1])]
    cards.append(c)

  for i in range (52):
    piles.append([])

  for c in cards:
    pilenum = 0
    while True:
      pile=piles[pilenum]
      if pile==[]:
        pile.append(c)
        break
      top = pile[len(pile)-1]
      if top[1]!=c[1]:
        if (top[0]>c[0]) or (top[0]==1 and c[0]==13):
          pile.append(c)
          break
      pilenum += 1

  lpiles = []
  for pile in piles:
    if len(pile)==len(max((piles), key=len)):
      lpiles.append(sum(pile))
  print(str(input.index(inputl)+1)+'. '+str(min(lpiles)))