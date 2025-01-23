#fun is higher order fn so that we are calling another fn sq
def fun(f,x):
    return f(x)

def sq(x):
    return(x*x)

res=fun(sq,3)
print(res)

def mul(f):
    def make_mul(x):
        return f*x
    return make_mul

d=mul(5)
print(d(2))


def welcome(n):
    return("HI",n)
p=welcome("viji")
print(p)

def function(f,v):
    return f(v)
d=welcome("ishwarya")
print(d)


def decorators(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper
@decorators
def hi():
    print("hello")
hi()

def greet():
    print("hi")
greet()


def sampledec(func):
    def wrapper(self,*args,**kwargs):
        print("previous")
        res=func(self,*args,**kwargs)
        print("After")
        return res
    return wrapper

class myclass:
    @sampledec
    def hello(self):
        print("welcome")
obj=myclass()
obj.hello()




def fun(cls):
    cls.class_name = cls.__name__
    return cls
@fun
class Person:
    pass
print(Person.class_name)



