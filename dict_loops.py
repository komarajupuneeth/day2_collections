#dictionary loops 

bike = {
    "brand":"royal enfield",
    "model":"gurella 350",
    "year": 2024,
    "price": 265000
} 

# looping through keys 
print("keys:",end="")
for key in bike:
    print(key,end="  ")

#looping through values 
print("\nvalues: ",end="")
for value in bike.values():
    print(value,end="  ") 

#looping through both key and values 
print("\nkey-value pairs: ")
for key,value in bike.items():
    print(key+":",value)