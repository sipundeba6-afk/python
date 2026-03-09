n=input("enter the string: ")      #weather is 
s=n.split()                        # weather   is
t=" "                              #len(t)=0 ,,,len(t)=7
for i in s:
    if len(i)>len(t):             #len(weather)=7>0...len(is)=2<7
        t=i                       #t=7
    print(t)
    
