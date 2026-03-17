x = list()
print(x)
print(type(x))
print(len(x))
y = list("lokesh")
print(y)
print(type(y))
print(len(y))
z = [10,90,30,20,70]
print(z)
print(type(z))
print(len(z))
p = [100,200,100,200,100,300]
print(p)
q = [100,12.12,True, "Naveen",None]
print(q)
print(q[2])
q[1]="Python"
print(q)
print("---------------------------------------")
# x = [10,20,30,40,50]
# print(x)
# i = 0
# while i<len(x):
#     print(x[i])
#     i = i+1
# for p in x:
#     print(p)
# print("---------------------------------------")
# x = [10,20,30,40,50]
# print(x)
# i = int(input("Enter a search Element:"))
# if i in x:
#     print("Element is found")
# else:
#     print("Element is not found")
# print("---------------------------------------")
# x = [10,20,30,40,50]
# print(x)
# i = int(input("Enter a number:"))
# for q in x:
#     if q==i:
#         print('Element is found')
#         break
# else:
#     print('element is not found')
print('-----------------------------------')
x = [10,20,30,40,50,60]
print(x)
print(len(x))
x.append([60,70,80])
print(x)
x.extend([100,200,300,400,500])
print(x)
z=x.copy()
print(z)
x.reverse()
print(x)

# Unpacking elements of a list
x = [1000, 123.12,True,"Naveen"]
print(x)
p,q,r,s=x
print(p,type(p))
print(q,type(q))
print(r,type(r))
print(s,type(s))

print('--------------------------------')
x = [[10,20,30],[40,50,60],[70,80,90]]
print(x)
print(len(x))
print(x[0])
print(x[0][0])
print(x[0][1])
print(x[0][2])
print('--------------------------------')
x = [[10,20,30],[40,50,60],[70,80,90]]
print(x)
for p in x:
    for q in p:
        print(q,end=" ")
    print()

print('--------------------------------')
x = [[10,20,30],[40,50,60],[70,80,90]]
print(x)
for r,s,t in x:
    print(r,s,t)

print('--------------------------------')
x = [[10,20,30],[40,50,60,90],[70,80,90]]
print(x)
for p in x:
    for q in p:
        print(q,end=" ")
    print()
print("---------------------------------------")
x = [[1001,'mobile',10000.00],[1002,'A.C',50000.00],[1003,'Book',1000.00]]
print(x)
total_cost = 0.0
for p,q,r in x:
    total_cost+=r
print(total_cost)
print("---------------------------------------")
x = [[1001,'mobile',10000.00],[1002,'A.C',50000.00],[1003,'Book',1000.00]]
print(x)
for p,q,r in x:
    print(p,q,r)
x.sort(reverse=True)
for i,j,k in x:
    print(i,j,k)
x.sort(key=lambda C:C[2],reverse=True)
for a,b,c in x:
    print(a,b,c)
print("---------------------------------------")
