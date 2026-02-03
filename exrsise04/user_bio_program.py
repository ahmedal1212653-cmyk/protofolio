name = input("Enter your name:")                    #name
hometown = input("Enter your hometown:")                #hometown

age = input("Enter you age :")              #age 
if age.isdigit():
    age = int(age)
else:
    print("Age must be a number")
    exit()

bio = {
    "name": name,
    "hometown": hometown,
    "age": age
}


print(bio["name"] , bio["hometown"] , bio["age"], sep="\n")
