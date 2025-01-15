age = int(input("AGE:   "))
weekend = input("IS IT THE WEEKEND(yes or no)?    ")
is_student = input("STUDENT(yes or no)?  ")
if age<12:
    price = 8
elif age >=12 and age<=17:
    if weekend.lower() == 'yes':
        price = 12
    else: 
        price = 10
elif age >=18 and age<=64:
    if is_student.lower()=='yes' and weekend.lower()=='no':
        price = 12
    else:
        price = 15
else:
    price = 10
print("$" + str(price))