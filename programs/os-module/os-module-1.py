import os
os.chdir("/home/constantine/python/books")
print(os.getcwd())
os.makedirs("Random")
os.rename("Random","Random1")
print(os.stat("Random1").st_size)
os.removedirs("Random1")
print(os.listdir())

for dirpath,dirnames,filenames in os.walk("/home/constantine/python"):
    print(dirpath, dirnames, filenames)
