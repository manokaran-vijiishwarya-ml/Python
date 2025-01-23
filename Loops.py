# a=10
# b=100
# if(a>b):
#     print("A is big")
# elif(a==b): print("Equal")
# else: print("b is large")

# print("A is large") if(a>b) else print("B is large")

# c=5
# d=5
# print("C") if(c>d) else print("D") if(d>c) else print("=")

# e=100
# if(e>10):
#     print("number is more than 10")
#     if(e>50):
#         print("num  is greater than 50")
#     else:
#         print("less than 50")


# i=1
# while(i<=5):
#     print(i)
#     i+=1



# fruits=["apple","banana","cherry"]
# for x in fruits:
#     print(x)

# for y in "hello":
#     print(y)

# for z in range(5):
#     print(z)
# for g in range(3,7):
#     print(g)
# for k in range(3,15,3):
#     print(k)

# for h  in range(7):
#     print(h)
# else:
#     print("Over")

# for s in range(9):
#     if(s==8): break
#     print(s)  
# else:
#     print("Completed")


# fruit=["apple","cherry"]
# msg=["hi","hlo"]
# for x in fruit:
#     for y in msg:
#         print(x,y)



# fruitss=('apple','banana','kiwi')
# myiter=iter(fruitss)
# print(next(myiter))
# print(next(myiter))


# str="kiwi"
# my=iter(str)
# print(next(my))
# print(next(my))

# class num:
#     def __init__(self):
#         self.a=1    
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         x=self.a
#         self.a=self.a+1
#         return x
    
# n1=num()
# item=iter(n1)
# print(next(item))
# print(next(item))
# print(next(item))


class num:
    def __init__(self):
        self.a=1    
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.a<20:
            x=self.a
            self.a=self.a+1
            return x
        else:
            raise Exception(StopIteration)
    
n1=num()
item=iter(n1)
# print(next(item))
# print(next(item))
# print(next(item))
for x in item:
    print(x)