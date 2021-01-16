list1=list(range(1000))

def is_mul_of(x,y):
    return True if x%y==0 else False
sum=0
for i in list1:
    if is_mul_of(i,3):
        sum+=i
    elif is_mul_of(i,5):
        sum+=i
    else:
        pass
print("The sum is "+str(sum))
