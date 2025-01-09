import random
e = random.randrange(0,3)
if e == 0:
    a = 'rock'
elif e == 1:
    a = 'sissors'
else:
    a = 'paper'
while True:
    user = input('ROCK PAPER SISSORS. ')
    if user.lower() == 'rock' or user.lower()=='sissors' or user.lower()=='paper':
        break
if a == 'rock':
    if user.lower() == 'rock':
        print('tie')
    elif user.lower() =='paper':
        print("win")
    else:
        print("lose")
if a == 'paper':
    if user.lower() == "paper":
        print("tie")
    elif user.lower() == "rock":
        print('Lose')
    else:
        print('you win')
if a == "sissors":
    if user.lower() == 'sissors':
        print('tie')
    elif user.lower() == "rock":
        print('win')
    else:
        print('you lose')