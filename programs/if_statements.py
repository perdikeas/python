# right to vote
age=18
if age>=21:
    print("you can vote")
else:
    print("You are too young to vote")
print("\n")
#car to buy
car="mercedes"
if car=="bmw":
    print("I will buy this car")
elif car=="audi":
    print("I might buy this car")
else:
    print("I do not want this car")

print("\n")
#fun park fare
age=6
if age<=4:
    cost=0
elif age<=15:
    cost=5
else:
    cost=10
print("The cost is "+ str(cost) +" dollars\n")

print("\n")
#alien_game
alien_color="green"
if alien_color=="green":
    points_earned=3
elif alien_color=="yellow":
    points_earned=5
else:
    points_earned=10
print("You earned "+ str(points_earned)+" points\n")



#if statements with list comprehension
requested_toppings=["cheese","mushrooms","mozarella","tomato_sauce"]
for requested_topping in requested_toppings:
    if requested_topping!="mushrooms":
        print("Adding "+ requested_topping+" to your pizza")
    else:
        print("Sorry, we are out of "+ requested_topping)
print("Your pizza is ready\n")

#username_choice
taken_usernames=["bob","admin","joe","alex"]
new_usernames=["tom","cat","alex","joe"]
removed_usernames=["joe"]

for new_username in new_usernames:
    if new_username not in taken_usernames:
        print("Welcome "+ new_username)
    elif new_username in taken_usernames and new_username in removed_usernames:
        print("Welcome "+ new_username)
    else:
        print("Sorry, this username is taken")
