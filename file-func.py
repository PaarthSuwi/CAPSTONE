file =  open("C://Users//paart//OneDrive//Desktop//codes//seminar//add.py",'r')
data = file.read()
print(data)
lines = file.readline()
print(lines)
file.close()

file2 =  open("C://Users//paart//OneDrive//Desktop//codes//seminar//add.py",'w')
file2.write("hell yeah!!")

import os.path
if os.path.exists():
    print("file exists")
else:
    print("doesnt exist")
    

