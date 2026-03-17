data = "Naveen"
for p in data:
    print(p*3)
print('--------------------------------------------------')
# data=1234 #TypeError: 'int' object is not iterable
# for p in data:
#     print(p*3)

x = range(5)
print(x)
for p in x:
    print(p)
y = range(5,15,2)
print(y)
for q in y:
    print(q)
z = range(15,25,-2)
print(z)
for r in z:
    print(r)

print('--------------------------------------')
x = range(20,30,-2)
print(x)
for p in x:
    print(p)
y = range(50,15,-5)
print(y)
for q in y:
    print(q)
for r in range(10,20,2):
    print(r)

print('---------------------------------------------')
p = 1000
print(p)
print(bin(p))
x= p.bit_count()
print(x)
y = p.bit_length()
print(y)

x = "Naveen python"
print(x)
a = x.capitalize()
print(a)
print(x)
b  = x.title()
print(b)
c=x.upper()
print(c)
d=x.lower()
print(d)
e=x.isupper()
print(e)
f=x.islower()
print(f)
g = x.isalpha()
print(g)
k = x.isdigit()
print(k)

print('---------------------------------------------')
x = "NavEEn PyThOn"
print(x)
a=x.swapcase()
print(a)
y = "1234"
a = y.isdigit()
print(a)
b = y.isupper()
c = y.islower()
print(c)

print('------------------------------------------------')
x = "Naveen"
print(x)
a = x.join(["python ","Java ","Hadoop"])
print(a)
b = a.join(['Django ','flask ','fastapi'])
print(b)
