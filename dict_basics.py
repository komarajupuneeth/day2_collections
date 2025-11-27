# creating a dictionary 
student={
    "name" : "rajkumar",
    "age" : 20,
    "branch" : "aiml",
    "marks" : 90
} 
print(student) 

#accesing values 
print("name: ",student["name"]) 
print("age: ",student["age"])

#adding a new keyvalue pair 
student["college"]="asdb college"
print("after adding college: ",student)

#updating existing key-value pair 
student["marks"]=99
print("after updating marks: ",student)

#deleting a key_value pair 
del student["branch"]
print("after deleting branch: ",student)

#checking if a key exists 
print("Has 'age'? : ","age" in student)