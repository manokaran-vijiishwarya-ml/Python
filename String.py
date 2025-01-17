a="viji"
d="YES"
print(a[2])
for b in "ish":
    print(b)
print(len(a))
c="this is viji"
# print("is" in c)
print("ish" not in c)

c="I am an associate software engineer"
if "sofart" not in c:
    print("yes")

print(a[1:3])
print(a[1:])
print(a[-2])
print(a[-3:-1])
print(a.upper())
print(d.lower())

e="  viji ish"
print(e)
print(e.strip())
print(e.replace('i','a'))
print(e.replace('a','i'))
f=e.split(",")
print(f)

age=21
j=f"My Age is : {age}"
print(j)


# name="my name is \"viji\" "
# name="my name is \'viji\' "
name="I want to use backslash in this string before the word \\ string"
print(name)



k="my blood grp is {blood}"
print(k.format(blood='O'))


l="my name is {name}".format(name="viji")
print(l)