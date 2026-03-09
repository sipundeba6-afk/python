str=input("enter the sentence: ")
s=" "
for i in str:
    if i not in s:
        count=0
for x in str:
    if x in s:
        count=count+1
print("no of similar letters: ",count)
