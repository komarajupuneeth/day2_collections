#first question-take 5 numbers from user and store in a list,
#then print max and min numbers

nums=[]

for i in range(5):
    n=int(input("enter number: "))
    nums.append(n)

print("numbers : ",nums) 
print("max is : ",max(nums)) 
print("min is : ",min(nums)) 

#second question-create a lists of fruits and print them with
#their index 

fruits=["banana","pineapple","kiwi","custard apple","pomogranate"] 
l=len(fruits)
for i in range(l): 
    print(i," : ",fruits[i])