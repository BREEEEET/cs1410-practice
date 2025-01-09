side1 = int(input('enter a side lenght:   '))
side2 = int(input('enter a side lenght:   '))
side3 = int(input('enter a side lenght:   '))
if side1 + side2 <= side3:
    print("not good triangle")
elif side2+side3<=side1:
    print("not good triangle")
elif side1 + side3<= side2:
    print('bad triangle')
else:
    print("good triangle")