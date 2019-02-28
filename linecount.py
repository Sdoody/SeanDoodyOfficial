wordlist = [] 
with open('most_security.txt') as infile:
    for line in infile:
        wordlist.append(line)

print len(wordlist)