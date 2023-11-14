dictionary_count=int(input())
all_words=[]
english=[]
deustuch=[]
persian=[]
francise=[]

for i in range(0, dictionary_count):
    all_words.append(input().split())

for i in range(0,len(all_words)):
    persian.append(all_words[i][0])
    english.append(all_words[i][1]) 
    francise.append(all_words[i][2])    
    deustuch.append(all_words[i][3])


sentence=input().split()

if sentence[0] in persian:
    for sentence in range()
print(all_words)    