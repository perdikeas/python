N=100
def erato(x):
    rv=[]
    marked_nums=[]
    for p in range(2,x+1):
        if p not in marked_nums:
            rv.append(p)
        for j in range(p**2,x+1,p):#this is a for loop that implements start,stop and step
            marked_nums.append(j)
    return rv
print(erato(N))
