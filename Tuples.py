x=("viji","malar","sharmi")
print(x)
y=list(x)
print(y)
y[1]="nivetha"
print(y)
print(tuple(y))
y.append("ish")
print(y)
z=("nithi",)
y+=z
print(y)
b=list(y)
b.remove("viji")
print(tuple(b))

fruit=("apple","mango","orange","pineapple","berry")
# (blue,red,*green)=fruit
(blue,*green,red)=fruit
print(red)
print(green)
print(red)
print(blue)



for x in fruit:
    print(x)

for i in range(len(fruit)):
    print(fruit[i])

i=0
while(i<len(fruit)):
    print(fruit[i])
    i+=1

fruit2=("kiwi","papaya")
print(fruit+fruit2)

fruit3=fruit2*2
print(fruit3)