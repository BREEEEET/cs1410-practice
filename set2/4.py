income = float(input("Total Yearly income:     "))
is_marrired = input('ARE YOU MARRIED?(yes or no)   ')
has_dependents = input(' HAS DEPENDENTS :y/n    ')
owns_business = input("DO YOU OWN A BUISSNESS      ")
if 'y' in is_marrired:
    is_marrired = True
else:
    is_marrired = False
if 'y' in has_dependents:
    has_dependents = True
else:
    has_dependents = False
if 'y' in owns_business:
    owns_business = True
else:
    owns_business = False


if income < 30000:
    if is_marrired:
        tax =10
    else:
        tax = 8
elif income >=30000 and income<=100000:
    if has_dependents:
        if is_marrired:
            tax = 12
        else:
            tax=15
    else:
        tax = 18
else:
    if owns_business:
        tax = 25
    else:
        tax = 28
print(income * ((100-tax)/100))