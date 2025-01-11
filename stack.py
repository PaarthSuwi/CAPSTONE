class stack:
    def __init__(self):
        self.value = []
        
    def push(self,x):
        self.value = [x] + self.value
    
    def pop(self):
        return self.value.pop(0)
    
s = stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)

print(s.value)
print(s.pop())
print(s.value)

s.push(50)
print(s.pop())
print(s.value)