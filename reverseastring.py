# Reverse a string with out using slice operator.
d = input("Enter a string :")
i = len(d)-1
rev_data = " "
while i>=0:
    rev_data=rev_data+d[i]
    i = i-1
print(rev_data)
print('---------------------------------------------')

a = input("Enter a string :")
b = len(a)-1
c = " "
while b>=0:
    c = c+a[b]
    b=b-1
print(c)

print('----------------------------------------------')

data = input("Enter a data :")
i = len(data)-1
while i>=0:
    print(data[i])
    i = i -1
print('----------------------------------------------')
a = input('Enter a string :')
x = len(a)-1
y = ' '
while x>=0:
    y = y+a[x]
    x = x-1
print(y)