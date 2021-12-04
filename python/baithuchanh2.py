import nltk
#nltk.download('popular')
from urllib import request

text1 = "Rittenhouse attorneys file petition for writ of habeas corpus in bid to halt… Hurricane Delta aims to hit Louisiana as a Category 2 storm, with ferocious… The New York Times logoCampaigns Spar Over Debate Plan After Trump Rejects Virtual Face-Off Next week’s presidential debate was on the verge of cancell"
text2 ="to have the candidates square off from separate locations next Thursday rather than onstage in Miami."
tokens = nltk.word_tokenize(text1)
tokens2 = nltk.word_tokenize(text2)
print(type(tokens2))