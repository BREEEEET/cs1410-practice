password = "Yippeebugs"
e= " "
while e != password:
    e = input("What is the password?   ")
    if e == 'stop' or e =="end":
        break
    if e != password:
        print("WRONMG")
print("CORRECT")