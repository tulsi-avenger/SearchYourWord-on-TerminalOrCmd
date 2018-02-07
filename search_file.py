import json

from difflib import get_close_matches

data=json.load(open("data.json","r"))

def translate_word(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
        
    else:
        get_similar=get_close_matches(word,data.keys(),n=1,cutoff=0.8)
        if len(get_similar)>0:
            yn=input("Did you mean %s instead? Enter Y if yes, or N if no. " % get_similar[0])
            if yn=='Y' or yn=='y':
                return data[get_similar[0]]
            elif yn=='N' or yn=='n':
                return "The Word doesn't exist! Please double check it. ~tpj"
            else:
                return "i didn't get your query."
        else:
            return "The Word doesn't exist! Please double check it! ~tpj"

word=input("Enter word: ")
output=translate_word(word)
if type(output)== list:
    for i in output:
        print(i)
else:
    print(output)


#import difflib
#SequenceMatcher(None,"raiinn","rain").ratio()
