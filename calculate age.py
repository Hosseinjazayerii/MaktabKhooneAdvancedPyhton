from datetime import datetime, timedelta
date=[]
now = datetime.now()
dob_input = input()
date=dob_input.split('/')
if int(date[1])>12 or int(date[1])<1:
    print("WRONG")
elif(int(date[2])>31) or int (date[2])<1:
    print("WRONG")
elif int(date[0])<0:
    print('WRONG')
else:        
    birthday = datetime.strptime(dob_input, "%Y/%m/%d")
    difference = now - birthday
    age_in_years = difference.days // 365
    print(age_in_years)