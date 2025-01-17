class mycls:
    x=5
print(mycls)

p1=mycls()
print(p1.x)

class Person:
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
    def fn(self):
        print(self.name)
p2=Person("viji",22)
p2.fn()
print(p2.name)
print(p2.age)
print(p2)
p2.age=23
print(p2.age)


class Check:
      def __init__(self, name, age):
            self.name = name
            self.age = age
      def __str__(self):
        return f"{self.name} {self.age}"
p4 = Check("viji", 20)
print(p4)



class Dog:
    species = "Canine"
    def __init__(self, name, age):
        self.name = name
        self.age = age
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)
print(dog1.species)
print(dog1.name)    
print(dog2.name)    
dog1.name = "Max"
print(dog1.name)  
Dog.species = "Feline"
print(dog1.species) 
print(dog2.species)