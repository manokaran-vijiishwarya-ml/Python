x="viji"
# def fun():
#     y="ish"
#     print(y)
#     print(x)
# # print(y)
# print(x)
# fun()

# def fn():
#     global b
#     b="ishwarya"
# fn()
# print(b)
# print(x)


# def funct():
#     global x
#     x="ishwarya"
# funct()
# print(x)


def function():
    return True
if function():
    print("yes")
else:
    print("no")
function()


# def function():
#     return False

# if function():
#     print("yes")
# else:
#     print("no")
# function()



class functions():
    def __len__(self):
        return 0
obj=functions()
print(bool(obj))

b=isinstance(x,str);
print(b)

# b=isinstance(x,int);
# print(b)


def fn(name):
    print(name+"ish")
fn("viji")


def fun(f,l):
    print(f+l)
fun("viji","ishwarya")


# def age(*a):
#     print("My age is:" + a[2])
# age("21","25","22")

def age(viji,malar,sharmi):
    print("my age is : "+viji)
age(malar="22",sharmi="21",viji="20")


def my_function(country = "Norway"):
      print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(**name):
      print("His last name is " + name["lname"])
my_function(fname = "viji", lname = "ish")

