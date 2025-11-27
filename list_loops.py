# lists loops 

marks=[46,34,56,78,23,95,68] 

print("all marks: ",end="")#without end the numbers are each printed in new line
for m in marks: 
    print(m,end=",") 

#calculating sum 
total_sum = 0 
for m in marks:
    total_sum+=m 
print("total sum: ",total_sum)

#claculating average 
avg=total_sum/len(marks) 
print("average: ",avg) 

#filter:print marks >= 50 
for m in marks:
    if m>=50:
        print(m)