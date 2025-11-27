
##lists basics 

#creating  a list 
numbers=[10,20,30,40,50]
names=["puneeth","rahul","adi"]
print("number: ",numbers)
print("names: ",names)

#indexing 
print("first number: ",numbers[0])
print("last name: ",names[-1]) 

#modifying list 
numbers[0]=76 
print("after modifying: ",numbers)

#adding elements 
numbers.append(234) 
print("after appending: ",numbers)

#inserting at specific index 
numbers.insert(3,474) 
print("after inserting at index 3: ",numbers)

#removing elements 
numbers.remove(20)
print("after removing(20): ",numbers) 

#length of list 
print("length of numbers: ",len(numbers))
