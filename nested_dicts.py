<<<<<<< HEAD
#nested dictonary 

students={
    1:{"name":"ali","age":20,"marks":78},
    2:{"name":"sai","age":21,"marks":83},
    3:{"name":"sri","age":20,"marks":89},
} 

#print each students details 
for roll, info in students.items():
    print("roll:",roll)
    print("name:",info.get("name")) #we can use get method also for accesing values
    print("age:",info["age"])
    print("marks:",info["marks"]) 
    print()


#example question  
roll=int(input("enter roll: "))
name=input("enter name: ")
age=int(input("enter age: "))
marks=int(input("enter marks: ")) 

students[roll]={
    "name":name,
    "age":age,
    "marks":marks
}

print("\nupadated students list: ")
for r,roll in students.items():
=======
#nested dictonary 

students={
    1:{"name":"ali","age":20,"marks":78},
    2:{"name":"sai","age":21,"marks":83},
    3:{"name":"sri","age":20,"marks":89},
} 

#print each students details 
for roll, info in students.items():
    print("roll:",roll)
    print("name:",info.get("name")) #we can use get method also for accesing values
    print("age:",info["age"])
    print("marks:",info["marks"]) 
    print()


#example question  
roll=int(input("enter roll: "))
name=input("enter name: ")
age=int(input("enter age: "))
marks=int(input("enter marks: ")) 

students[roll]={
    "name":name,
    "age":age,
    "marks":marks
}

print("\nupadated students list: ")
for r,roll in students.items():
>>>>>>> d559aba40a5b4953448e674677c9156b27d7d652
    print("roll:",r,info)