import array as arr
a = arr.array('i',[1,2,3])
print(a[2])
a = arr.array('i', [1, 2, 3, 6,9,7,10,8])
print(a[2])  # Output: 3

a.reverse()  
sum = sum(a)
max = max(a)
min = min(a)
ascending = sorted(a)
descending = sorted(a,reverse=True)

print(a)
print(sum)  
print(ascending)
print(descending)

MAX_SIZE = 5 
a = arr.array("i",[0]*MAX_SIZE)
print(a)

a = arr.array('i',[1,2,3,4,5,6])
if len(a)>MAX_SIZE:
    print("overflow")


