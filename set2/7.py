age = int(input("AGE:     "))
fitness_level = input("WHAT is your fitness level?      ")
if 'b' in fitness_level.lower():
    fitness_level = 'beginner'
elif 'i' in fitness_level.lower():
    fitness_level = 'intermediate'
else:
    fitness_level = 'advanced'
goal = input("Goal:     ")
if 'st' in goal.lower():
    goal = 'strength'
elif 'car' in goal.lower():
    goal = 'cardio'
else:
    goal = 'weight loss'
health_concerns = input("do you have health concerns? (YES OR NO)    ")
if 'y' in health_concerns:
    health_concerns=True
else:
    health_concerns=False

if age<18:
    if goal=="strength":
        print("Youth strength program")
    elif goal =="cardio":
        print("Youth cardio plan")
elif age <=50:
    if fitness_level == 'beginner':
        print("Beginner Strength and Cardio")
    else:
        if goal=='weight loss':
            print("HIIT and Strength plan.  ")
        elif goal == 'strength':
            print('advanced strength program')
else:
    if health_concerns:
        print("Gentle mobility Program")
    else:
        print("Active aging plan")

        

