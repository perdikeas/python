pizzas=["peperonni","special","margarita"]
for pizza in pizzas:
    print("I really like "+pizza.title()+ " pizza!")
print("All these pizzas were wonderful")

print("\n")

even_numbers=list(range(0,11,2))
odd_numbers=[]

for i in range(1,10):
    if i in even_numbers:
        print(i)
    else:
        odd_numbers.append(i)

def square(x):
    return x**2

print(list((map(square,odd_numbers))))

list=[3,4,5,6]
print(sum(list))

def mean(list):
    rv=(list[0]+list[-1])
    return rv/2

print(mean(list))

players=["martina","zoe","michael","zach","dylan"]
print(players[0:4])

print(players[:2])

print(players[2:])

for player in players[2:]:
    print(len(player))

    print("\n\n")
    
