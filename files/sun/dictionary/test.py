def addWorld(w,wcDict):
    if w in wcDict:
        wcDict[w] += 1
    else:
        wcDict[w] = 1

import string
def processLine(line,wcDict):
    line = line.strip()
    wordList = line.split()
    for word in wordList:
        if word != "--":
            word = word.lower()
            word = word.strip()
            word = word.strip(string.punctuation)
            addWorld(word, wcDict)

def prettyPrint(wcDict):
    valKeyList=[]
    for key,val in wcDict.items():
        valKeyList.append((val,key))
    valKeyList.sort(reverse=True)
    print ("%-10s%10s"%("Word","Count"))
    print ("_"*21)
    for val,key in valKeyList:
        print ("%-12s    %3d"%(key,val))

def main():
    wcDict = {}
    fobj = open("Harry Potter 1.txt","r")
    for line in fobj:
        processLine(line,wcDict)
    print ("length of the dictionary:",len(wcDict))
    prettyPrint(wcDict)

main()
