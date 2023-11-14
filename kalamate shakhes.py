phrase=input()
sentences=phrase.split('.')
words=[]# تمام کلمات همه ی جمله ها کنار هم 
Firstwords=[]
count=0
allwords=[] # کلمه های هر جمله رو کنار هم بدون اسپسیس میچینه  
for i in range(0, len(sentences)-1):
    allwords.append((sentences[i].split()))

for i in  range (0,len(allwords)):
    for j in range(0,len(allwords[i])):
        if j==0:
            Firstwords.append(allwords[i][j])
            words.append(allwords[i][j])
        else:
            words.append(allwords[i][j])

for index , word in enumerate(words):
    if word not in Firstwords and word.capitalize()==words[index]:
        count+=1
        print(index+1,':',word)
if count==0:
    print("None")    
                    