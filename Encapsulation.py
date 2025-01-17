class Dog:
    def __init__(self, name, breed, age):
        self.name = name  
        self._breed = breed  
        self.__age = age  

   
    def get_info(self):
        return f"Name: {self.name}, Breed: {self._breed}, Age: {self.__age}"

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")

dog = Dog("Scooby", "Labrador", 3)
print(dog.name)  

print(dog._breed)  

print(dog.get_age())

dog.set_age(5)
print(dog.get_age())
print(dog.get_info())