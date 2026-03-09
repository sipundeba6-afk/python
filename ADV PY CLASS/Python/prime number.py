#find the prime number:
num=int(input("enter a number: "))
count=0
for i in range (1,num+1):
    if num%2==0:
        count=count+1
if(count==2):
    print("it is a prime number")
else:
    print("it is not a prime number")
