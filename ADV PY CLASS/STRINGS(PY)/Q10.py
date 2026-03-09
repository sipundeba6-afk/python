str=input("enter the sentence: ")
a=str.split()
for i in a:
    if i[0]==i[-1]:
        print("the words are: ",i)
