set={"viji","sharmi","malar"}
print(set)
set2=(("hi","hlo","welcome","viji"))
print(set2)
set3={"apple","banana","mango","apple"}
print(set3)
set4={"apple",1,"banana",True,0,False}
print(set4)

for x in set:
    print(x)

# for i in range(len(set)):
#     print(set[i])

# i=0
# while(i<len(set)):
#     print(set[i])
#     i+=1
# print(i)

print("viji" in set)

set.add("nivetha")
print(set)

# set5={"ish","nithi"}
set5=["ish","nithi"]
set.update(set5)
print(set)

set.remove("ish")
print(set)

set.discard("viji")
print(set)
print(set.pop())
print(set)
# set.clear()
# print(set)
# del set
# print(set)

# set7=set.union(set2)
# print(set7)

set8=set.intersection(set2)
print(set8)
