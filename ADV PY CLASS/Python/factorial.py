#factorial:

num=int(input("enter a number: "))
fact=1
for i in range(1,num+1):
    if(num>0):
        if(num%i==0):
            fact=fact*i
print(fact)

        
