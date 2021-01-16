
#prompt="Tell us what pizza topping you want\n Once you're done write quit  "
#while True:
    #topping=input(prompt)
    #if topping!="quit":
        #print("Adding "+ topping)
    #else:
        #break

#while True:
    #age=int(input("\nWhat is your age"))
    #if age<3:
        #print("Price is 0")
    #elif 3<=age<=12:
        #print("Price is 10")
    #elif age>12:
        #print("Price is 15")
    #elif age=="quit":
        #break

#sandwich_orders=["bacon","cheese","butter"]
#sandwiches_prepared=[]
#while sandwich_orders:
    #order=sandwich_orders.pop()
    #print("Preparing your "+ order +" sandwich")
    #sandwiches_prepared.append(order)

#print(" All sandwiches done")

prompt1="What is your name"
prompt2="Tell us your dream trip location"
dict1={}
while True:
    name=input(prompt1)
    dream_location=input(prompt2)
    dict1[name]=dream_location
    repeat=input("Would you like to let someone else answer (yes,no)")
    if repeat!="yes":
        break
for k,v in dict1.items():
    print("The dream trip location of "+ k +" is "+v)
