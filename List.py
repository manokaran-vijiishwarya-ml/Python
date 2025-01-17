list=["apple","Mango","orange"]
print(list)
print(list[1])
list.insert(2,"kiwi")
print(list)
print(list[:2])
print(list[-3:-1])
print(list)
list.remove(list[-2])
print(list)
list.append("watermelon")
print(list)
new_list=["pineapple","cherry"]
list.extend(new_list)
print(list)
tuple=("berry","papaya")
list.extend(tuple)
print(list)
list.append("apple")
print(list)
list.remove("apple")
print(list)
list.pop(2)
print(list)
list.pop()
print(list)
del list[3]
print(list)
print(tuple)
del tuple
print(tuple)
print(list)
# list.clear()
# print(list)
for x in list:
    print(x)
print(len(list))

for i in range(len(list)):
  print(list[i])

i=0
while(i<len(list)):
   print(list[i])
   i+=1

[print(x) for x in list]

newlist=[]
for x in list:
   if "e" in x:
        newlist.append(x)
print(newlist)

#list comprehension
listnew=[x  for  x in list if "a" in x]
print(listnew)
      
list_new=[x.upper() for x in listnew]
print(list_new)

list_new.sort()
print(list_new)

list_new.sort(reverse=True)
print(list_new)

# list.sort()
# print(list)
list.sort(key=str.lower)
print(list)

copylist=list.copy()
print(copylist)

# copy_list=list(copylist)
# print(copy_list)

newlist2=copylist[:]
print(newlist2)


list1=["viji","sharmi","malar"]
list2=[20,21,22]
list3=list1+list2
print(list3)

for x in list2:
   list1.append(x)
print(list1)


list1.extend(list2)
print(list1)
