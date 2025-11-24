info ={
    "name":"Mohanlal",
    "age": 20,
    "city":"Nandakumar"

}
print(info["name"])
print(info["age"])




ID ={
    1: "Mohanlal",
    2: "Mallika",
    3: "Suresh",
    4: "radha",
    5: "Krishna"
}

print(ID[4])
print(ID.get(2))
print(ID.keys())
print(ID.values())
print(ID.items())
print(len(ID))
print(ID.pop(3))
print(ID)
ID[6] = "Lakshmi"
print(ID)



emp1 ={
    "name": "Mohanlal",
    "age": 20,
    "city": "Nandakumar",
    "salary": 50000
}
emp2 ={
    "name": "Mallika",
    "age": 22,
    "city": "Kolkata",
    "salary": 60000
}

emp1.update(emp2)
print(emp1)
del emp1["city"] #delete key
print(emp1)