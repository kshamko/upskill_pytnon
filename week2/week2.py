#STRING
#print("§")

"""
s = "abcd"
print(hex(id(s)))
print(s, s[0])
#s[2] = "f"
s = s + "sdf"
print(hex(id(s)))
print(s)
"""

# TUPLE
a = ("a", 1, "b")
print(a)
print(type(a))
a = a * 2
a = a + a
print(a)

b = tuple("hello world")
print(b)

#b[1] = 2
print(b[1:4])
print(b[-3:], b[8:])

person = ("name", 15, True)
person1 = ("name1", 25, False)

name, age, loveCats = person
print(name, age, loveCats)

if age < 16 and loveCats:
    print("child who loves cats")

#persons = [person, person1]
#for p in persons:
#    name, age, loveCats = p


#LIST
a = [1,2,3,4,5]
print(a, hex(id(a)))
a[1] = 10
print(a, hex(id(a)))

a.append(90)
a.insert(7, 8)
print(a)

head, *tail = a
print(head, tail)

first, *rest, prelast, last = a
print(first, rest, prelast, last)

i = 0
while i < len(a):
    print(a[i])
    i = i + 1
    

#DICT
d = dict({"name": "Name", "age": 16, "loveCats": True, 12.5:1})

#cards = [1,2,3,4,5,6]
#cards = dict({"1": "0987", "2": xxxx})

for key, val in d.items():
    print(key, val)

d.update(dict({"x": 56, "name": "XXX"}))
print(d)

if not d.get("key"):
    print("do smth")