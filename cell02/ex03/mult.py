z= int(input("Enter the second number: "))
y=int(input("Enter the first number: "))
print(z,"x",y,'=',z*y)
if z*y == 0:
    print("The result is positive and negative.")
elif z*y > 0:
    print("The result is positive.")
else:
    print("The result is negative.")