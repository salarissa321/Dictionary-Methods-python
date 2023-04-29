


#--------------------------------
#----Dictionary Methods-----
#--------------------------------


# clear()


user = {
    "name" : "Salar"
}
print(user) # {'name': 'Salar'}
user.clear() 
print(user) # {}


print("-" * 40) # ----------------------------------------


# update()

number= {
    "name" : "Issa"
}

print(number) # {'name': 'Issa'}
number.update({"country" : "Deutschland"}) 
print(number) # {'name': 'Issa', 'country': 'Deutschland'}
number["age"] = 36
print(number) # {'name': 'Issa', 'age': 36}


print("-" * 50) # --------------------------------------------------


# copy()

book = {
    "name" : "Verrat"
}

b = book.copy()
print(b) # {'name': 'Verrat'}
book.update({"Skills" : "Killing"})
print(book) # {'name': 'Verrat', 'Skills': 'Killing'}
print(b) # {'name': 'Verrat'}

print("-" * 50) # --------------------------------------------------


# Keys() + Values()


print(book.keys()) # dict_keys(['name', 'Skills'])
print(book.values()) # dict_values(['Verrat', 'Killing'])


print("-" * 50) # --------------------------------------------------


# setdefault()

user = {
    "name" : "Salar"
}


print(user) # {'name': 'Salar'}
print(user.setdefault("name", "Issa")) # Salar
print(user) # {'name': 'Salar'}
print(user.setdefault("age", 27)) # 27
print(user) # {'name': 'Salar', 'age': 27}


print("-" * 50) # --------------------------------------------------

# popitem()

user = {
    "name" : "salar",
    "Skills" : "flying"
}

print(user) # {'name': 'salar', 'Skills': 'flying'}
user.update({"age" : 27}) # {'name': 'salar', 'Skills': 'flying', 'age': 27}
print(user.popitem()) # ('age', 27)

print("-" * 50) # --------------------------------------------------


# items()

anblick = {
    "name" : "salar" ,
    "Skills" : "swimming"
}

allItems = anblick.items()
print(anblick) # {'name': 'salar', 'Skills': 'swimming'}
anblick["age"] = 27
print(allItems) # dict_items([('name', 'salar'), ('Skills', 'swimming'), ('age', 27)])


print("-" * 50) # --------------------------------------------------

# formkeys()


a = ("myKeyOne" , "myKeyTwo" , "myKeyThree")
b = "X"

print(dict.fromkeys(a,b)) # {'myKeyOne': 'X', 'myKeyTwo': 'X', 'myKeyThree': 'X'}