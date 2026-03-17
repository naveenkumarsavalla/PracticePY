s = 0
for p in range(1,101):
    s=s+1
print(s)
es = 0
for q in range (2,101,2):
    es = es+q
print(es)
os = 0
for r in range(1,101,2):
    os = os+r
print(os)
# While loop
i =1
es=0
os = 0
while i<=100:
    if i%2 == 0:
        es=es+i
    else:
        od=os+i
    i = i+1
print("Sum of even num:", es)
print("Sum of odd num",es)

