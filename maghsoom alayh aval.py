def IsPrime(number):
    prime=True
    if number==1:
        prime=False
    elif number==2:
        prime=True
    elif number==3:
        prime=True
    else:
        for i in range(2,int(number**0.5)+1):
            if number%i==0:
             prime=False
             break
    return prime    

    
def divisor(number):
    count=0
    for i in range(1,number):
        if number%i==0 and IsPrime(i):
            count+=1
    return count        


numbers={}
for i in range(0,10):
    x=int(input())
    numbers[x]=divisor(x)
x=max(numbers.values())

numbers_with_max_divisor=[]
for keys in numbers:
    if numbers[keys]==x:
        numbers_with_max_divisor.append(keys)
print(max(numbers_with_max_divisor),x)
