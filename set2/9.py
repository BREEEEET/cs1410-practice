nights = int(input("How many nights?  "))
is_weekend = input("Is it the weekend?(yes or no)  ")
if 'y' in is_weekend:
    is_weekend=True
else:
    is_weekend=False
room_type = input('do you want a stardard, deluxe or suite room?   ')
if 'x' in room_type:
    room_type='deluxe'
elif 'stan' in room_type:
    room_type='standard'
else:
    room_type='suite'
has_membership = input("Has membership card?(yes or no)  ")
if 'y' in has_membership:
    has_membership=True
else:
    has_membership=False
if room_type=='standard':
    price = 100*nights
    if is_weekend:
        price += 20*nights
elif room_type=='deluxe':
    price=150*nights
    if is_weekend:
        price += 20*nights
else:
    price = 250*nights
    if is_weekend:
        price +=50*nights
if has_membership:
    price=price*.9
if nights>5:
    price *= .95

print(price)