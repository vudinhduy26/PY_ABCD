import re
import re
def get_count(sentence):
    pattern = "[a,e,i,o,u]"
    result = re.findall(pattern,sentence)
    return len(result)

print(get_count("abracadabra"))