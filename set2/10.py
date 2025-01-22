income = float(input("ANnual income:    "))
credit_score = int(input('What is your credit score?    '))
has_collateral = input("do you have collateral(yes or no)?    ")
if 'y' in has_collateral:
    has_collateral=True
else:
    has_collateral=False
loan_amount = float(input("How much money do you want?"))
if credit_score>750:
    if income>50000:
        print("Okay it will have a 5% intrest rate")
    else:
        print("okay it will have a 7% intrest rate")
elif credit_score<600:
    print('no')
else:
    if has_collateral:
        print("Okay it will have a 10% intrest rate")
    else:
        print("No")