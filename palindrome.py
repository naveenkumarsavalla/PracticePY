# To check palindeome without using slice operator
data = input("Enter a string:")
i = len(data)-1
rev_data = "" # Don't give the space in quotes what if give the space the compailer take that as a integer then we will get error in code
while i>=0:
    rev_data=rev_data+data[i]
    i = i-1
if data == rev_data:
    print(data,"is a palindrome")
else:
    print(data,"is not a palindrome")

print('-----------------------------------------------')
# To check palindrome without using slice operator

# data = input("Enter a string: ")
# i = len(data) - 1
# rev_data = ""
#
# while i >= 0:
#     rev_data = rev_data + data[i]
#     i = i - 1
#
# if data == rev_data:
#     print(data, "is a palindrome")
# else:
#     print(data, "is not a palindrome")

print('----------------------------------')
data = input("Enter a string:")
i = len(data)-1
rev = ""
while i>=0:
    rev = rev+data[i]
    i = i-1
if rev == data:
    print(data,"is a palindrome")
else:
    print(data ,"is not a palindrome1")