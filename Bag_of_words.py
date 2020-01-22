#Compute the top 10 words in the entire document

import pandas as pd

file = input("Enter file name:")
fh=open(file,"r")
file_content=fh.read()
BOW = file_content.split()
wordDict = {}

for word in BOW:
    if(word.lower() in wordDict):
        wordDict[word.lower()]+=1
    else:
        wordDict[word.lower()]=1

df = pd.DataFrame(wordDict.items(), columns = ['Word', 'Count'])
df = df.sort_values(ascending=False, by = ["Count"])
print(df[:10][:10])

