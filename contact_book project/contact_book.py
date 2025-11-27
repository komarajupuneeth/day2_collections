contacts=[]

def add_contact():
    name=input("enter name: ")
    phone=input("enter phone number: ") 
    email=input("enter email: ") 

    contact = {
        "name":name,
        "phone":phone,
        "email":email
    }
    contacts.append(contact)
    print("contact added successfully\n")

def view_contacts():
    if not contacts:
        print("no contacts found\n")
        return 
    print("all contacts found\n")
    for c in contacts:
        print("name:",c["name"])
        print("phone:",c["phone"])
        print("email:",c["email"]) 
        print("--------------") 
    print()

def search_contact():
    name=input("enter name to search: ") 
    found=False 
    for c in contacts:
        if c["name"].lower()==name.lower():
            print("contact found:")
            print("name:",c["name"])
            print("phone:",c["phone"])
            print("email:",c["email"]) 
            found=True
            break 
    if not found:
        print("no contact found wtih taht name.\n") 

def delete_contact():
    name=input("enter name to delete: ")
    global contacts 

    updated=[c for c in contacts if c["name"].lower()==name.lower()]
    if len(updated)!= len(contacts): 
        contacts=updated 
        print("contacts deleted successfully\n")
    else:
        print("no contact found with that name.\n") 

while True:
    print("Contact Book")
    print("1. add contact")
    print("2. view contacts")
    print("3. search contact")
    print("4. delete contact")
    print("5. exit") 

    choice=input("enter your choice(1 to 5): ")
    if choice=="1":
        add_contact()
    if choice=="2":
        view_contacts()
    if choice=="3":
        search_contact()
    if choice=="4":
        delete_contact()
    if choice=="5":
        print("exiting program")
    else :
        print("invalid choice,try again")