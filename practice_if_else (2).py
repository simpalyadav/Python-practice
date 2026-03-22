# Write a program to find the greatest of 3 numbers entered by the user.

a = int(input("Enter first num="))
b = int(input("Enter second num="))
c = int(input("Enter third num="))
if a>b and a>c:

    print("Greatest ammong all is",a)
elif b>a and b>c:
     
    print("Greatest among all is",b)
else:
    print("Greatest among all is",c)
