import nltk
#nltk.download('popular')
from urllib import request
url = 'http://www.gutenberg.org/files/2554/2554-0.txt'
response = request.urlopen(url)
raw = response.read().decode('utf8')
tokens = nltk.word_tokenize(raw)
#print(tokens[1:10])

dir = {} #chi tu dien
for word in tokens:
	if word in dir.keys():
		dir[word] += 1
	else :
		dir[word] = 1

#dir.keys()
#words = list(dir.keys())

s = 'DAI hoc thuy loi'
print(s.lower())
