score = int(input("GRADE:    "))
participation = input("Participation?       ")
if 'exe' in participation.lower():
    participation = 'excellent'
elif 'oo' in participation.lower():
    participation = 'poor'
elif 'above' in participation.lower():
    participation="above average"
else:
    participation="average"
homework = input('Homework done? Y/N     ')
if 'y' in homework:
    homework=True
else:
    homework=False
if score >=90:
    if participation=="excellent":
        print('A+')
    else:
        print("A")
elif score>=80:
    if participation =="above average":
        print("B+")
    else:
        print("B")
elif score>=70:
    if homework==True:
        print("C+")
    else:
        print("C")
else:
    if participation=="poor":
        print("F")
    else:
        print('D')
    