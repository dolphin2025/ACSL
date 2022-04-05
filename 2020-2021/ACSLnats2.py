
def generateSentences(dictionary, sentences):
    dictionary.append('T the')
    dictionary.append('A a')
    dictionary = [i.split() for i in dictionary]
    ind = {}
    w = {}
    for i in dictionary:
        ind[i[0]] = 0
        w[i[0]] = i[1:]
    sentences = sentences.split()
    sentences = [[i[0],i[1:]] for i in sentences]
    ans = []
    for type, struct in sentences:
        sent = []
        for i in struct:
            sent.append(w[i][ind[i]%len(w[i])])
            ind[i] += 1
        for i in range(len(sent)):
            if sent[i]=='a' and i<len(sent)-1 and (sent[i+1][0] in 'aeiou'):
                sent[i] = 'an'
        sent = ' '.join(sent)
        if type in 'DI':
            sent += '.'
        if type == 'E':
            sent += '!'
        if type == 'Q':
            sent = 'What ' + sent
            sent += '?'
        sent = sent[0].upper()+sent[1:]
        ans.append(sent)
    return ' '.join(ans)

print(generateSentences(['N money tree sky', 'C grow fall', 'P on from'], 'ICNPTN ICPTN'))