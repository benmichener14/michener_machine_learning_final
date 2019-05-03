file = open("Youtube01-Psy.csv", "r")
X = open("Psy_X.csv", "w+")
Y = open("Psy_Y.csv", "w+")

#Create dictionary of words and their indexes
i = 0
wordBag = []

for line in file:
    
    if "COMMENT_ID,AUTHOR,DATE,CONTENT,CLASS" not in line: #If not first line
        if "\"" in line:
            tokens = line.split("\"")
            comment = tokens[1].split(" ")
            for word in comment:
                if "http://" in word and "http://" not in wordBag:
                    wordBag.append("http://")
                    i+= 1
                elif word.lower() not in wordBag:
                    wordBag.append(word.lower())
                    i+= 1
        else:
            tokens = line.split(",")
            comment = tokens[3].split(" ")
            for word in comment:
                if "http://" in word and "http://" not in wordBag:
                    wordBag.append("http://")
                    i+= 1
                elif word.lower() not in wordBag:
                    wordBag.append(word.lower())
                    i+= 1
                
file.close()
file = open("Youtube01-Psy.csv", "r")
        
#Write to Files
line = ""
for word in wordBag:
    line += word + ", "
line += "\n"
X.write(line)
for line in file:
    if "COMMENT_ID,AUTHOR,DATE,CONTENT,CLASS" not in line: #If not first line
        if "\"" in line:
            tokens = line.split("\"")
            comment = tokens[1].split(" ")
            line = ""
            Y.write("{}".format(tokens[2].strip(","))) #Designation of Spam or not, Binary
            for word in wordBag:
                if word in (words.lower for words in comment):
                    line += "1, "
                else:
                    line += "0, "
            line += "\n"
            X.write(line)
        else:
            tokens = line.split(",")
            comment = tokens[3].split(" ")
            line = ""
            Y.write("{}".format(tokens[4])) #Designation of Spam or not, Binary
            for word in wordBag:
                if word in (words.lower for words in comment):
                    line += "1, "
                else:
                    line += "0, "
            line += "\n"
            X.write(line)
        
        
        
X.close()
Y.close()
