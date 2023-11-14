atendees_count=int(input())
atendees=[]
males=[]
females=[]
for i in range(0,atendees_count):
    
    atendees.append(input().split('.'))

for i in range(0,len(atendees)):
        if atendees[i][0]=='m':
            m=('m',str(atendees[i][1]).capitalize(),atendees[i][2])
            males.append(m)
        else:
            f=('f',str(atendees[i][1]).capitalize(),atendees[i][2])
            females.append(f)
            

males=sorted(males,key = lambda x: x[1])
females=sorted(females,key= lambda x: x[1])

for i in range(0,len (females)):
    print(females[i][0],females[i][1],females[i][2])

for i in range(0,len (males)):
    print(males[i][0],males[i][1],males[i][2])    


