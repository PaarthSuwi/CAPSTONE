class Queue():
    def __init__(self):
        self.values = []
        
    def enqueue(self, value):
        self.values.append(value)
        
    def dequeue(self):
        
        if self.values:
            return self.values.pop(0)

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print("Before dequeue:", q.values)
dequeued_value = q.dequeue()
print("Dequeued value:", dequeued_value)
print("After dequeue:", q.values)

q.enqueue(50)

print("queue after dequeued",q.values)
q.dequeue()
print("queue after dequeued",q.values)