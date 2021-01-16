list=["bugatti","ferrari","pagani"]
print("\tMy favorite supercar is "+ list[0].title())
list[1]='rolls-royce'
print(list)
list.remove("pagani")
list.append("bentley")
print(list)
list.insert(1,"ferrari")
print(list)

print("\n\n")

list2=["cambridge","harvard","oxford"]
del list2[1]
print(list2)
popped_item=list2.pop()
list3=[]
list3.append(popped_item)

print("\n\n")

list3=["scarface","godfather","casino"]
print("The first gangster movie i watched was the "+ list3.pop().title())
too_unrealistic="scarface"
list3.remove(too_unrealistic)
print(list3)
print("\t "+too_unrealistic.title()+ " was too unrealistic for me")

print("\n\n")

guests=["tom","steve","bryce","anthony","alex"]
guests.remove("tom")
del guests[2]
guest_of_honour=guests[1]
print("My guest of honour is "+ guest_of_honour)
guests.pop()
print(guests)
guests.append("tony")
guests.insert(0,"harry")
print(guests)

print("\n\n")
names=["zoe","alex","will","robert"]
names.sort()
names.sort(reverse=True)
print(names)

list5=["a","n","v","c"]
list5.reverse()
print(list5)


dream_places=["hawai","maldives","bahamas"]
print(sorted(dream_places))
print(dream_places)
dream_places.reverse()
print("My dream destination is "+ dream_places[0])

random=[1,2,3,5,6,7,str(4)]
print(len(random))
print("My favorite number is "+ random.pop())
print(random[-1])
for i in range(0,len(random)):
    print(random[i])

print("\n\n")
