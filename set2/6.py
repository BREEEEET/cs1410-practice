distance = float(input("DISTANCE :        "))
is_sunny = input("IS IT SUNNY(YES OR NO).    ")
if 'y' in is_sunny.lower():
    is_sunny=True
else:
    is_sunny=False
has_bike = input("DO YOU HAVE A BIKE?(YES OR NO)      ")
if 'y' in has_bike.lower():
    has_bike=True
else:
    has_bike=False
rush_hour = input("IS IT RUSH HOUR(YES OR NO)      ")
if 'y' in rush_hour.lower():
    rush_hour =True
else:
    rush_hour=False
if distance<5:
    if is_sunny:
        print('walking')
    else:
        print('driving')
elif distance>=5 and distance<=20:
    if has_bike:
        print('cycling')
    else:
        print('bus')
else:
    if rush_hour:
        print('Train')
    else:
        print('Driving')