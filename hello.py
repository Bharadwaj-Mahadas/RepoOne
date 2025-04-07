# print("hello world")
# text = "in small letter"
# print(text.upper())
# k= input("enter any string")
#
# print(len(k))
#
# k= input("enter any string")
#
# print(len(k))
#
# print("the position at which the character is present is " + str(k.index("l")))
#
# #list functions


a = [10,20,30,40,50]
print(a.index(20))

b=a.copy()

a.extend(b)
a.append("bunny")
print(a)

a.pop()
print(a)

a.insert(2,"Hello")
print(a)

b.clear()
print(b)

b= a.copy()
print(b)

print(b.index('Hello'))


