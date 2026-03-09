str=input("enter a sentence: ")
count=0
s=str.split()
for i in s:
    if i.isalpha():
        count=count+1
print(count)
