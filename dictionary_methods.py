student ={
    "name":"ali",
    "age": 20,
    "gender": "male"
    }

print(student.get("age"))

# mobile model

mobile = {
    "brand" : "samsung",
    "model":  "A15",
    "price" : 35000
}
print(mobile.keys())

# values

mobile2={ 
    "name": "Iphone",
    "brand": "Iphone12 pro",
    "price": 50000
}

print(mobile2.values())

# update

stud = {
    "name": "usman",
    "marks": 80,
    "city": "lahore"
}

stud.update({"marks": 90})
print(stud)


#pop() method

citizen = {
    "name": "ahmed",
    "age": 23,
    "city": "ISB"
}
my_city = citizen.pop("city")
print(my_city)
print(citizen)

#pop ka dusra task 
stud1 = {
    "name": "khan",
    "age": 25,
    "gender": "male"
}

stud2= stud1.pop("gender")
print(stud2)
print(stud1)

# setdeault method

person = {
    "name" : "nomi",
    "age": 26
}
person.setdefault("country", "pak")
print(person)

# copy method

car = {
    "brand": "honda",
    "model": "civic",
    "price": "550000"
}

cars = car.copy()
print(cars)

# get() se brand nikalo.
# update() se RAM ko 16 karo.
# pop() se color remove karo.
# keys() se saari keys display karo.
# Aakhir mein puri dictionary print karo.

laptop = {
    "brand": "Dell",
    "RAM": 8,
    "price": 50000,
    "color": "Black"   
}

laptop.update({"RAM": 16})
print(laptop)
