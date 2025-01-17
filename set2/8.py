temperature = float(input("What is the temperature in F     "))
is_rainging = input('raining?(T or F)    ')
if 't' in is_rainging.lower():
    is_rainging = True
else:
    is_rainging = False
is_windy = input(' IS it windy(T OR F )      ')
if 't' in is_windy.lower():
    is_windy = True
else:
    is_windy = False
day_time = input("WHAT TIME of day is it(morning, noon, or night.)")
if 'm' in day_time.lower():
    day_time='morning'
elif 'noon' in day_time.lower():
    day_time = 'afternoon'
else:
    day_time='evening'
if temperature<50:
    if is_rainging:
        print('heavy coat and umbrealla')
    elif is_windy:
        print('windbreaker and gloves')
    else:
        print("jacket and scarf")
elif temperature>70:
    if is_rainging:
        print('raincoat and breathable clothes')
    else:
        print("T-shirt and shorts")
else:
    if day_time=='morning':
        print('light jacket')
    elif day_time=='afternoon':
        print('long-sleeve shirt')
    else:
        print('sweater and scarf')
