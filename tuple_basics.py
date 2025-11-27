# tuple basics 

#tuples are like lists but immutable(cant be changed)  

coordinates=(10,20)
print("coordinates: ",coordinates)  
print("x :",coordinates[0])  
print("y :",coordinates[1])  

#tuple packing and unpacking 
person=("raj",20,"student") 
name,age ,role = person 

print("name: ",name)
print("age: ",age)
print("role: ",role) 

coordinates[0]=233