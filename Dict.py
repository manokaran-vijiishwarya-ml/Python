dict1={
   "name":"viji",
   "age":21,
}
print(dict1)

dict2=dict(name="ish",age=22)
print(dict2)
print(type(dict2))
print(len(dict2))

x=dict2["name"]
print(x)
y=dict2.get("age")
print(y)
z=dict2.keys()
print(z)
dict2["desig"]="ASE"
print(dict2)
a=dict2.values()
print(a)
dict2["name"]="vijiishwarya"
print(dict2)

b=dict2.items()
dict2["age"]=21
print(b)

dict2.update({"age":22})
print(dict2)

# dict2.popitem()
# print(dict2)

dict2.pop("desig")
print(dict2)

del dict1["age"]
print(dict1)

dict1.clear()
print(dict1)

for x  in dict2:
    # print(x)
    print(dict2[x])


for x in dict2.values():
    print(x)

copydict=dict2.copy()
print(copydict)

copy_dict=dict(dict2)
print(copy_dict)



fruits={
    "fruit1":{
        "name":"apple",
        "color":"red"
    },
    "fruit2":{
        "name":"orange",
        "color":"orange"
    }
}
print(fruits["fruit1"]["name"])
for x, obj in fruits.items():
      print(x)
      for y in obj:
        print(y + ':', obj[y])

print(fruits["fruit1"].pop("color"))