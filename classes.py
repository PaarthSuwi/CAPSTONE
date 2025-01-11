class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:  # If the list was empty, update tail
            self.tail = self.head

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.tail is None:  # If the list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print("None")


# Example usage
linkedlist = LinkedList()
for _  in range(5):
    data = int(input("Enter the number to be appended: "))
    linkedlist.insert_at_beginning(data)
print ("linkedlist:")
linkedlist.display()
