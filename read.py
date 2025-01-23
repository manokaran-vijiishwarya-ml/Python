# import os
# f=open("demo.txt","r")
# print(f.read())
# print(f.read(5))
# print(f.readline())
# print(f.readline())
# for x in f:
#     print(x)
# f.close()
# print(f.read(5))
# f=open("demo.txt","w")
# f.write("I am overwritting existingg file")
# f=open("demo.txt","r")
# print(f.read())
# f.close()
# f=open("demo.txt","a")
# f.write("I am overwritting existingg file")
# f=open("demo.txt","r")
# print(f.read())
# f=open("new.txt","x")
# f=open("new.txt","w")
# f.write("new content")
# f=open("new.txt","r")
# print(f.read())
# os.remove("new.txt")
# f=open("check.txt","x")
# f=open("checck.txt","w")
# f.write("Checking how del works")
# f=open("checck.txt","r")
# print(f.read())
# f.close()

# if os.path.exists("checkk.txt"):
#     os.remove("checck.txt")
# else:
#     print("No file exist")


# if os.path.exists("checck.txt"):
#     os.remove("checck.txt")
# else:
#     print("No file exist")

# f=open("checkk.txt","r")
# print(f.read())

# f=open("check.txt","w")
# f.write("Writing to check with how it works in diff modes simultaneously")
# f=open("check.txt","rb")
# print(f.read())

# with open("check.txt") as file:
#     m=file.read()
#     print(m)

# try:
#     file=open("check.txt","rb+")
#     print(file.readlines())
# finally:
#     print("The file is readed")

# position=file.tell()
# print(position)

# f=open("check.txt","w")
# lst=[]
# for i in range(3):
#     name=input("Enter names:")
#     lst.append(name)
# f.writelines(lst)
#f.writelines("Continue to see about how writelines work anyways the data will be overwridden and then now you can check about how things work")
# f=open("check.txt","r")
# print(f.read())

# f=open("checcck.txt","x")
# f=open("checcck.txt","w+")
# f.write("Working on  with read and write modes using r+")
# f=open("checcck.txt","r")
# print(f.read())


# f=open("twofile","x")
# f=open("twofiles","x")
# with open("twofile","r") as file_in:
#     with open("twofiles","w") as file_out:
#         for line in file_in:
#             p=file_out.write(line)
#             print(p.read())
