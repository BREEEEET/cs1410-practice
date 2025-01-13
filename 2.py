num1 = int(input("NUMBER:    "))
num2 = int(input("NUMBER:    "))
num3 = int(input("NUMBER:    "))
if num1 == num2 and num1 == num3:
    print("ALL ARE EQUAL")
elif num1 == num2 or num1==num3 or num2 == num3:
    print("2 are equal")
elif num1 < num2 and num2 < num3:
    print("ascending order?")
elif num1>num2 and num2>num3:
    print("Descending order")
else:
    print("No specific pattern found.")