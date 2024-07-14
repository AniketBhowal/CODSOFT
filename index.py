A = int(input("Num 1:"))
B = int(input("Num 2:"))
C = input("Operator:")
if (C=="+"):
    print("Sum is: " , (A+B))
elif (C=="-"):
    print("Sum1 is: " , (A-B))
elif (C=="*"):
    print("Sum1 is: " , (A*B))
elif (C=="/"):
    print("Sum1 is: " , (A/B))
else:
    print("Error! Enter a valid operator")