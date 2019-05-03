import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')

file = open("Psy-X_unsorted.csv", mode="r", encoding='utf-8-sig')
X = open("Psy_X.csv", "w+")
wordFile = open("words.csv", "w+")


#Create dictionary of words and their indexes
wordBag = []

print("Tokenizing Lines")
for line in file:
    tokens = word_tokenize(line)                    #Splits comment into words
    for word in tokens:
        if len(word) > 3:
            if "\ufeff" in word:                        #Removes nasty little unicode character that messes up data
                word = word.replace("\ufeff", "")
            if ".com" in word or ".ru" in word or "//" in word:
                word = "https"
            if word.lower() not in wordBag:             #Add new words to the word bag.
                wordBag.append(word.lower())            #Side note, have you ever played Warhammer 40k? Do you know anything about it?
                                                        #If you don't, then this is going to sound strange, but...
                                                    #       MORE WORDS FOR THE WORD GOD
print("Words found: ")
print(len(wordBag))


file.close()
file = open("Psy-X_unsorted.csv", mode="r", encoding='utf-8-sig')

entry = ""
for word in wordBag:
    entry += word + ", "
    wordFile.write(word + "\n")
X.write(entry)
wordFile.close()

for line in file:
    entry = ""                                    #FUN FACT HERE! I didn't have this line at first, so the number of entries in line n that got written to the file was ~1300^n
                                                  #By the time the file was done writing, it was 250MB. Which is over 5 times the size of the first 4 pokemon games put together
    temp = word_tokenize(line)                    #Same old song, this time turning them all to lowercase
    tokens = []
    for token in temp:
        token = token.lower()
        tokens.append(token)
        
    for word in wordBag:
        if word in tokens:
            entry += "1"
        else:
            entry += "0"
        
        if word != wordBag[-1]:
            entry += ", "
    X.write(entry + "\n")
            
        
X.close()
file.close()
#Y.close()
