info={}
s=int(input("enter the no of students: "))
for i in range(s):
    name=input("enter the name of the students: ")
    id=input("enter the id of the students: ")

    mark={}
    sum_mark=0
    sub=int(input("enter the no of subjects: "))
    for x in range(sub):
        subject=input("enter the subject name: ")
        score=int(input("enter the marks: "))
        mark[subject]=score
        sum_mark=sum_mark+score
    avg=sum_mark/sub
    if avg>=90:
        grade="A"
    elif avg>=80:
        grade="B"
    elif avg>=70:
        grade="C"
    elif avg>=60:
        grade="D"
    elif avg>=50:
        grade="E"
    else:
        grade="FAIl"
    info[name] = {"id": id,"marks": mark,"avg_score": avg,"grade":grade}
print("the info of the student: ", info)


    
