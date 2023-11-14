person_count=int(input())
each_vote=[]

for i in range(0,person_count):
    x=input().capitalize()
    each_vote.append(x.split())
votes=[]
persons=[]
new_votes=[]
for i in range(0,len(each_vote)):
    for j in range(0,len(each_vote[i])):
        if j==0:
            persons.append(each_vote[i][0])
        else:
            votes.append(str(each_vote[i][j]).capitalize())

romance=('Romance',votes.count('Romance'))
horror=('Horror',votes.count('Horror'))
comedy=('Comedy',votes.count('Comedy'))
action=('Action',votes.count('Action'))
history=('History',votes.count('History'))
adventure=('Adventure',votes.count('Adventure'))


new_votes.append(action)
new_votes.append(adventure)
new_votes.append(comedy)
new_votes.append(history)
new_votes.append(horror)
new_votes.append(romance)
sort_votes=sorted(new_votes,key=lambda x:x[1],reverse=True)

for i in range(0,len(sort_votes)):
        print(sort_votes[i][0],':',sort_votes[i][1])

